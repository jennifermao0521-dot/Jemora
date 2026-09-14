# Jemora

**Jemora｜原創故事 IP 資產庫**

- **定位**：原創故事 IP 資產管理、多通路發行，以及 AI Agent 協作寫作與內容製作知識庫。
- **作者／IP 創作**：知遙
- **發行通路**：Kobo、Readmoo、Apple Books、Pubu、Amazon（非獨家 Wide Distribution）、喜馬拉雅（Himalaya）
- **內容延伸**：小說 → 有聲小說 → 影片 → 字幕 → 音樂 → 多平台出版
- **AI 影片工具**：Google Flow（Veo／Gemini 工作流）已納入 Novel-to-Media Pipeline
- **資產治理**：讓各 Agent 能依照作品設定讀取資料、維持角色與世界觀一致性，並支援續寫、改編、配音與影音製作。

---

## 目錄架構

```text
Jemora/
├── 小說/
│   ├── 局中玫瑰四部曲/
│   │   ├── 01_局中玫瑰/
│   │   ├── 02_權局之下/
│   │   ├── 03_生死有你/
│   │   └── 04_謎底之外/
│   ├── 渡神/
│   ├── 神諭之下_獸王只愛她/
│   ├── 他的例外/
│   └── 長生燼/
│
├── 童書/
│   └── 小小心靈研究所/
├── 有聲小說/
├── 影片/
├── 字幕/
├── 音樂/
├── 封面與視覺/
├── metadata/
├── agents/
└── docs/
    └── google-flow/              # Google Flow 影像製作指南
```

> 實際大型影音檔案、原始音檔與出版檔案可依 Git LFS／外部儲存策略管理；GitHub 主要保存可版本控制的文字、設定、metadata、腳本與必要的小型資產。

---

## 內容生產 Pipeline

Jemora 的核心是 **Novel-to-Media IP Pipeline**：

```text
小說原稿
   ↓
章節／場景解析
   ↓
角色、世界觀、情緒與對白資料
   ↓
Character Bible + World Bible + Visual Bible
   ↓
Scene Sheet／Storyboard／Prompt
   ↓
Google Flow（Veo／Gemini）
   ├─ References / Ingredients
   ├─ Frames to Video
   ├─ Text to Video
   ├─ Camera Controls
   ├─ Extend
   ├─ Video Edit
   └─ Scenebuilder
   ↓
場景影片素材
   ↓
旁白／角色語音
   ↓
同步字幕（SRT／VTT）
   ↓
音樂／音效
   ↓
完整影片／劇集
   ↓
多平台發行
```

### Google Flow 工作原則

**Jemora 管理故事 Canon；Google Flow 負責視覺化與影片創作。**

Google Flow 的生成結果不得反過來決定小說劇情、角色設定或時間線。每個影片素材都應保留來源作品、篇章、章節、Scene、Shot 與版本資訊。

詳細指南：`docs/google-flow/README.md`

### 影音輸出目標

針對小說指定章節，系統逐步支援：

1. 讀取指定小說內容
2. 分析章節與場景
3. 產生影片腳本／分鏡資料
4. 產生影像或影片素材
5. 產生旁白／角色語音
6. 產生同步字幕（SRT／VTT）
7. 配置背景音樂
8. 合成完整影片
9. 同時保留 **影片、字幕、音樂、音訊** 等獨立檔案

目標形式：**每章可製作成約 1 小時的電視劇式內容**。

---

## AI Agent 協作規則

所有 Agent 應優先遵循：

- 角色姓名、年齡、生日、關係不可任意修改。
- 世界觀、時間線、重要事件需以作品 Bible 為準。
- 已完成章節不得在未授權情況下改寫核心劇情。
- 續寫前先讀取該作品的角色與世界觀資料。
- 改編成影片、音訊或字幕時，原著內容為最高優先級來源。
- 產出新資產時，保留來源作品、章節與版本資訊。
- Google Flow 生成前先使用 Scene Sheet、Character Bible、Visual Bible。
- 重要角色與場景優先使用固定 reference／ingredients，以降低跨鏡頭視覺漂移。
- 每個場景拆成多個 Shot，再於 Scenebuilder 或後製階段組接。

---

## 版本與資產命名原則

```text
作品名_資產類型_章節或範圍_版本
```

影片素材例如：

```text
作品_篇章_章節_Scene01_Shot01_flow_v01.mp4
作品_篇章_章節_Scene01_Shot01_final.mp4
作品_角色_VisualRef_v01.png
作品_章節_Scene01_Shot01_flow_prompt_v01.md
```

其他資產：

```text
渡神_第001章_旁白_v1.mp3
渡神_第001章_字幕_v1.srt
渡神_第001章_影片_v1.mp4
渡神_第001章_配樂_v1.mp3
```

---

## Roadmap

- [x] 建立 Jemora IP 資產庫
- [x] 建立 Git 忽略規則
- [x] 建立小說／童書資產分類
- [x] 規劃有聲小說、影片、字幕、音樂資產層
- [x] 規劃 Novel-to-Media Pipeline
- [x] 納入 Google Flow 影像製作工作流
- [x] 建立 Google Flow 使用指南
- [ ] 建立各作品 Character Bible
- [ ] 建立各作品 World Bible
- [ ] 建立小說章節 metadata
- [ ] 接入有聲小說產製流程
- [ ] 接入小說 → 影片流程
- [ ] 建立字幕自動產生流程
- [ ] 建立音樂與影片同步流程
- [ ] 建立一章約 1 小時的電視劇式自動化製作流程
- [ ] 建立出版 metadata 自動整理流程

---

## License / Rights

Jemora 收錄之故事、角色、世界觀、文字內容與原創 IP 資產，除另有標示外，均屬原創創作資產。未經授權不得擅自複製、改編、重新出版或商業使用。
