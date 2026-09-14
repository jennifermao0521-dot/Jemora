#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Jemora 中文小說章節字數檢查器。

參考來源：PenglongHuang/chinese-novelist-skill
原始專案：MIT License
"""
import re
import sys
from pathlib import Path


def count_chinese_chars(text: str) -> int:
    text = re.sub(r'#{1,6}\s*', '', text)
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    text = re.sub(r'\*(.*?)\*', r'\1', text)
    text = re.sub(r'~~(.*?)~~', r'\1', text)
    text = re.sub(r'`(.*?)`', r'\1', text)
    text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)
    return len(re.findall(r'[\u4e00-\u9fff]', text))


def check_file(path: Path, minimum: int = 3000):
    if not path.exists():
        return path, 0, False, '檔案不存在'
    text = path.read_text(encoding='utf-8')
    count = count_chinese_chars(text)
    return path, count, count >= minimum, ('達標' if count >= minimum else f'不足 {minimum} 字')


def main():
    if len(sys.argv) < 2:
        print('用法：python check_chapter_wordcount.py <檔案> [最低字數]')
        print('或：python check_chapter_wordcount.py --all <目錄> [最低字數]')
        return
    minimum = 3000
    if sys.argv[1] == '--all':
        directory = Path(sys.argv[2])
        if len(sys.argv) > 3:
            minimum = int(sys.argv[3])
        files = sorted(directory.glob('第*.md'))
    else:
        files = [Path(sys.argv[1])]
        if len(sys.argv) > 2:
            minimum = int(sys.argv[2])

    total = passed = 0
    print('=' * 60)
    print('Jemora 章節字數檢查')
    print('=' * 60)
    for path in files:
        _, count, ok, message = check_file(path, minimum)
        total += count
        passed += int(ok)
        icon = 'OK' if ok else 'WARN'
        print(f'{icon} {path.name}: {count:,} 字 — {message}')
    print('-' * 60)
    print(f'共 {len(files)} 章，達標 {passed} 章，總中文字數 {total:,}')


if __name__ == '__main__':
    main()
