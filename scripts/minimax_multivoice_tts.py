#!/usr/bin/env python3
"""Jemora multi-character audiobook generator for MiniMax Speech 2.8.

Reads a simple dialogue script (TXT) and generates one MP3 per speaker plus a
mixed chapter MP3. API credentials are read from MINIMAX_API_KEY and are never
stored in the repository.

Script format:
  [旁白] 婚禮結束後的第三個月。
  [樓慕妍] 你今天不用上班？
  [白景深] 要。

A line without [speaker] is treated as narration.
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

import requests

API_BASE = os.getenv("MINIMAX_BASE_URL", "https://api.minimax.io")
MODEL = os.getenv("MINIMAX_TTS_MODEL", "speech-2.8-hd")
DEFAULT_SPEED = float(os.getenv("MINIMAX_TTS_SPEED", "1.0"))
DEFAULT_VOLUME = float(os.getenv("MINIMAX_TTS_VOLUME", "1.0"))
DEFAULT_PITCH = int(os.getenv("MINIMAX_TTS_PITCH", "0"))

# Replace these with the actual MiniMax voice IDs chosen for the project.
VOICE_MAP = {
    "旁白": os.getenv("JEMORA_VOICE_NARRATOR", ""),
    "樓慕妍": os.getenv("JEMORA_VOICE_LOU_MUYAN", ""),
    "白景深": os.getenv("JEMORA_VOICE_BAI_JINGSHEN", ""),
    "宋昭言": os.getenv("JEMORA_VOICE_SONG_ZHAOYAN", ""),
    "駱晚晴": os.getenv("JEMORA_VOICE_LUO_WANQING", ""),
    "顏書瑤": os.getenv("JEMORA_VOICE_YAN_SHUYAO", ""),
    "梁修遠": os.getenv("JEMORA_VOICE_LIANG_XIUYUAN", ""),
}

LINE_RE = re.compile(r"^\s*\[([^\]]+)\]\s*(.+?)\s*$")


def parse_script(path: Path) -> list[tuple[str, str]]:
    items: list[tuple[str, str]] = []
    for raw in path.read_text(encoding="utf-8-sig").splitlines():
        line = raw.strip()
        if not line:
            continue
        match = LINE_RE.match(line)
        if match:
            speaker, text = match.group(1).strip(), match.group(2).strip()
        else:
            speaker, text = "旁白", line
        items.append((speaker, text))
    if not items:
        raise ValueError(f"No dialogue lines found in {path}")
    return items


def tts(text: str, voice_id: str) -> bytes:
    if not voice_id:
        raise RuntimeError("Voice ID is empty. Set the appropriate JEMORA_VOICE_* environment variable.")
    api_key = os.getenv("MINIMAX_API_KEY")
    if not api_key:
        raise RuntimeError("MINIMAX_API_KEY is not set. Keep the key local; never commit it to GitHub.")

    payload = {
        "model": MODEL,
        "text": text,
        "stream": False,
        "language_boost": "Chinese",
        "output_format": "hex",
        "voice_setting": {
            "voice_id": voice_id,
            "speed": DEFAULT_SPEED,
            "vol": DEFAULT_VOLUME,
            "pitch": DEFAULT_PITCH,
        },
        "audio_setting": {
            "sample_rate": 32000,
            "bitrate": 128000,
            "format": "mp3",
            "channel": 1,
        },
    }
    response = requests.post(
        f"{API_BASE}/v1/t2a_v2",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=180,
    )
    response.raise_for_status()
    data = response.json()
    base = data.get("base_resp", {})
    if base.get("status_code", 0) != 0:
        raise RuntimeError(f"MiniMax error: {base.get('status_msg', data)}")
    import binascii
    return binascii.unhexlify(data["data"]["audio"])


def ensure_ffmpeg() -> None:
    if subprocess.call(["ffmpeg", "-version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) != 0:
        raise RuntimeError("ffmpeg is required for mixing. Install ffmpeg and make sure it is on PATH.")


def mix(files: list[Path], output: Path) -> None:
    # Concatenating generated segments preserves the script order and avoids
    # re-generating voices. ffmpeg's concat demuxer handles MP3 segments.
    list_file = output.with_suffix(".concat.txt")
    list_file.write_text("\n".join(f"file '{p.resolve().as_posix().replace("'", "'\\''")}'" for p in files), encoding="utf-8")
    try:
        subprocess.run(
            ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(list_file), "-c", "copy", str(output)],
            check=True,
        )
    finally:
        list_file.unlink(missing_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a Jemora multi-character audiobook with MiniMax Speech 2.8")
    parser.add_argument("script", type=Path, help="TXT script using [speaker] text lines")
    parser.add_argument("--out", type=Path, default=Path("outputs/audiobook"))
    args = parser.parse_args()

    items = parse_script(args.script)
    args.out.mkdir(parents=True, exist_ok=True)
    segment_files: list[Path] = []

    for index, (speaker, text) in enumerate(items, start=1):
        voice_id = VOICE_MAP.get(speaker, "")
        if not voice_id:
            raise RuntimeError(
                f"No voice configured for '{speaker}'. Add JEMORA_VOICE_* for this character before running."
            )
        audio = tts(text, voice_id)
        path = args.out / f"{index:04d}_{speaker}.mp3"
        path.write_bytes(audio)
        segment_files.append(path)
        print(f"Generated {path}")

    ensure_ffmpeg()
    final = args.out / f"{args.script.stem}_multi_voice.mp3"
    mix(segment_files, final)
    print(f"Final audiobook: {final}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
