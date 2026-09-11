# Jemora IP Production Workflow

> 小說 → 有聲小說 → 喜馬拉雅 → 字幕 → 音樂 → 影片

## 0. 核心原則

Jemora 以「小說原稿」作為 IP Source of Truth。小說只需解析一次，後續媒體產品全部由結構化資料產生。

```text
小說原稿
  ↓
IP Asset Extraction
  ↓
Character Bible + World Bible + Style Guide
  ↓
Chapter Metadata
  ↓
┌────────────┬────────────┬────────────┐
│ 有聲小說   │ 字幕       │ 音樂       │
└────────────┴────────────┴────────────┘
             ↓
          影片製作
             ↓
      約 1 小時／章 TV Drama
```

## 1. Stage A — 小說 IP 解析

輸入：DOCX / TXT / 其他可解析小說格式。

工作：
1. 清理文字與章節結構。
2. 辨識章名、段落、旁白、對白。
3. 建立角色清單。
4. 建立世界觀、地點、勢力與時間線。
5. 建立每章 Chapter Metadata。
6. 記錄來源小說版本。

輸出：Character Bible、World Bible、Style Guide、Chapter Metadata。

## 2. Stage B — 有聲小說

```text
Chapter Metadata
 ↓
旁白／對白分段
 ↓
Voice Mapping
 ↓
TTS
 ↓
音訊清理與音量標準化
 ↓
Chapter MP3
 ↓
QC
```

初期可使用免費／低成本 TTS，例如 edge-tts；聲音必須依 Voice Mapping 固定，避免同一角色每章聲音改變。

輸出至少包含：
- 旁白音檔
- 角色聲音音檔（若採角色分軌）
- 最終章節音檔

## 3. Stage C — 喜馬拉雅

喜馬拉雅視為「發行渠道」，不是另一套內容生產系統。

從作品 metadata 自動整理：
- 專輯名稱
- 作者：知遙
- 專輯簡介
- 分類
- 關鍵字
- 封面
- 集數名稱
- 集數排序
- 音檔
- 發布版本

平台資料保存於 `metadata/喜馬拉雅/`。

## 4. Stage D — 字幕

```text
Chapter Metadata
 ↓
旁白／對白文字
 ↓
時間軸對齊
 ↓
SRT
```

預設產出：
- Traditional Chinese SRT
- Simplified Chinese SRT
- English SRT（需要時）

字幕必須能獨立於影片保存，亦可產生燒錄字幕版本。

## 5. Stage E — 音樂

建立作品級 IP Music Library，而非每章臨時選曲。

標準分類：
- Main Theme
- Love Theme
- Mystery Theme
- Tension Theme
- Action Theme
- Sad Theme
- Ending Theme

每個場景由 Chapter Metadata 指定 music_theme、進入點、淡入與淡出。

音樂檔案必須保持獨立輸出，不能只存在於影片裡。

## 6. Stage F — 影片

目標：每章製作成約 1 小時的 TV Drama 形式。

```text
Chapter Metadata
 ↓
Scene Breakdown
 ↓
Storyboard
 ↓
Shot List / AI Video Prompts
 ↓
角色／世界一致性檢查
 ↓
影像生成
 ↓
旁白／角色聲音
 ↓
音樂
 ↓
字幕
 ↓
FFmpeg Render
 ↓
QC
 ↓
MP4
```

每章建議保存：
- `storyboard.json`
- `旁白.mp3`
- `配樂.mp3`
- `字幕.srt`
- `影片.mp4`

## 7. Stage G — JEHA Media Engine

Jemora 負責 IP 資產、設定、metadata 與製作規格；JEHA Media Engine 負責媒體生成與渲染。

目標接口：

```text
Jemora Chapter Metadata
        ↓
JEHA Media Engine
        ↓
video + subtitle + music + narration
        ↓
final MP4
```

現階段先固定資料標準，再將 JEHA 的 FFmpeg render pipeline 接入。

## 8. QC — 品質檢查

每章完成前檢查：

### 小說
- 章節完整
- 角色名稱一致
- 世界觀無衝突

### 有聲
- 無漏讀
- 無重複
- 聲音角色正確
- 音量一致

### 字幕
- 文字正確
- 時間軸正確
- 無字幕重疊

### 音樂
- 不遮蓋人聲
- 場景情緒正確
- 淡入淡出自然

### 影片
- 角色外觀一致
- 場景一致
- 畫面無明顯生成錯誤
- 聲音與畫面同步
- 字幕同步
- 成片時長符合章節目標

## 9. Version Control

所有成品都必須能追溯：

```text
作品版本
 → Chapter Metadata 版本
 → 生成設定
 → 媒體版本
 → 最終發布版本
```

不得直接覆蓋已發布成品；修改後建立新版本。

## 10. 標準章節成品

```text
影片/
└── 作品/
    └── 第001章/
        ├── storyboard.json
        ├── narration.mp3
        ├── music.mp3
        ├── subtitles_zh-TW.srt
        ├── subtitles_zh-CN.srt
        └── video.mp4
```

這套結構是 Jemora 後續自動化的標準輸出格式。
