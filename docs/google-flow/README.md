# Google Flow｜Jemora 影像製作工作流指南

> 目的：把 Google Flow 納入 Jemora 的 Novel-to-Media IP Pipeline，作為小說場景 → 角色／素材一致性 → AI 影片 → 場景組接 → 後製素材的重要製作工具。
>
> 官方入口：https://flow.google.com/
>
> 本文件依 Google Flow 官方說明與 Google 官方產品資料整理；功能、模型、地區限制與點數可能持續變動，實際製作前應以 Flow 介面顯示為準。

## 1. Google Flow 是什麼

Google Flow 是 Google 的 AI filmmaking 工具，核心使用 Veo、Gemini 與影像模型建立影片、場景與故事。它不只是「文字生影片」，而是把角色／物件／風格素材、鏡頭控制、場景組接與影片編修放在同一個創作工作區。

對 Jemora 最有價值的能力是：

- Text to Video：文字描述直接建立影片片段。
- Frames to Video：使用起始／結束影格控制轉場與敘事連續性。
- Ingredients / References：使用角色、物件、場景等參考素材維持視覺一致性。
- Camera Controls：控制鏡位、角度與運動。
- Scenebuilder：排列、修剪與組接多個影片片段成場景。
- Extend：延伸既有 Veo 影片，使動作與鏡頭繼續發展。
- Video Editing：以提示詞修改既有影片，保留版本歷史。
- Flow Agent：以自然語言協助構思、分鏡、提示詞、批次變體與素材整理。
- Audio：目前部分 Veo／Omni 工作流支援生成聲音、環境音與角色對話；實際可用功能依模型與地區而異。

## 2. 與 Jemora 的關係

Jemora 的既有核心 Pipeline：

```text
小說
 ↓
章節解析
 ↓
場景拆解
 ↓
角色／世界觀／視覺 Bible
 ↓
分鏡與 Prompt
 ↓
AI 影像／影片
 ↓
旁白／角色聲音
 ↓
字幕 SRT／VTT
 ↓
音樂／音效
 ↓
場景組接
 ↓
完整影片／劇集
```

Google Flow 應放在「分鏡與 Prompt」之後、「完整影片合成」之前：

```text
小說章節
  ↓
場景表 Scene Sheet
  ↓
Character Bible + Visual Bible
  ↓
場景參考圖／角色素材
  ↓
Google Flow
  ├─ Ingredients / References
  ├─ Frames to Video
  ├─ Text to Video
  ├─ Camera Controls
  ├─ Extend
  ├─ Video Edit
  └─ Scenebuilder
  ↓
場景影片素材
  ↓
字幕／配音／音樂
  ↓
最終影片
```

## 3. Jemora 的標準製作方法

### Step A｜先從小說拆場景，不直接把整章丟進 Flow

每章先建立 Scene Sheet：

- 作品
- 篇／章
- 場景編號
- 場景地點
- 時間
- 出場人物
- 人物情緒
- 動作
- 對白／旁白
- 場景目的
- 前一鏡狀態
- 下一鏡狀態
- 視覺素材需求
- 鏡頭需求
- 音效／音樂需求
- 來源章節

原則：一個生成片段只處理清楚的一個視覺事件，不把大量劇情塞進單一 Prompt。

### Step B｜建立角色與場景素材

先準備可重複使用的角色、服裝、道具、場景與風格參考圖，再在 Flow 中作為 Ingredients / References 使用。

四姊妹系列尤其要維持：

- 樓慕妍
- 宋昭言
- 駱晚晴
- 顏書瑤

四人的臉部、髮型、服裝邏輯與人物氣質必須依作品 Bible 固定，不因單一鏡頭重新生成而任意變更。

### Step C｜先做關鍵影格，再做影片

對重要敘事鏡頭，優先使用：

```text
角色／場景參考圖
        ↓
Start Frame
        ↓
動作／鏡頭 Prompt
        ↓
Video
        ↓
必要時加入 End Frame
```

這比每次完全從文字重新生成更適合長篇小說改編，因為可以控制角色與場景的視覺連續性。

### Step D｜使用 Camera Controls 建立「電視劇感」

場景 Prompt 不只寫人物做什麼，也要寫鏡頭怎麼拍，例如：

- wide establishing shot
- medium shot
- close-up
- over-the-shoulder shot
- slow dolly in
- lateral tracking shot
- static locked camera
- shallow depth of field

每一個鏡頭只指定一個主要鏡頭語言，避免同一段同時要求過多複雜運鏡。

### Step E｜Extend 用於需要連續動作的鏡頭

需要角色走路、轉身、進門、對話後離開等連續動作時，可以從上一個影片片段延伸，而不是每次重新生成。

注意：Extend 是否可用取決於所選模型與影片來源；目前 Google Flow 官方說明對不同 Veo／Omni 模型有不同限制。

### Step F｜Scenebuilder 組成完整場景

一個「小說場景」通常不是一支影片，而是多個短鏡頭：

```text
Shot 01 建立環境
↓
Shot 02 人物出現
↓
Shot 03 人物反應
↓
Shot 04 對話／動作
↓
Shot 05 情緒特寫
↓
Shot 06 離開／轉場
```

使用 Scenebuilder 排列、修剪與預覽，再輸出場景。

## 4. Flow Agent 的使用方式

Flow Agent 可作為「導演助理／提示詞協作者」，而不是取代 Jemora 的小說 Canon。

建議工作方式：

```text
Jemora 提供：
原著章節 + Scene Sheet + Character Bible + Visual Bible
        ↓
Flow Agent
        ↓
分鏡構想／Prompt 變體／素材整理
        ↓
人工選定 Canon 版本
        ↓
生成影片
```

可讓 Agent：

- 將場景轉成 storyboard。
- 產生多個鏡頭版本。
- 修改既有素材。
- 批次生成變體。
- 協助整理與命名素材。

重要規則：Flow Agent 的創意建議不得覆寫小說 Canon、角色設定、時間線或既定事件。

## 5. Prompt 標準格式

Jemora 建議將 Flow Prompt 統一成：

```text
[CHARACTERS]
角色、年齡感、服裝、外觀、關係

[LOCATION]
地點、時間、環境、天氣

[ACTION]
人物正在做什麼

[EMOTION]
情緒與潛台詞

[CAMERA]
景別、角度、鏡頭運動

[LIGHTING]
光線、色溫、時間感

[STYLE]
寫實／電影感／電視劇感等

[CONTINUITY]
必須延續的角色、道具、場景元素

[AUDIO]
環境聲、對白、需要的聲音元素
```

### Prompt 原則

1. 先寫「誰、在哪裡、做什麼」。
2. 再寫情緒與鏡頭。
3. 最後補光線、風格與連續性。
4. 重要角色使用固定 reference ingredient。
5. 不要讓同一 Prompt 同時要求太多事件。
6. 需要對白時，先確認當前模型是否支援所需音訊功能。

## 6. 四姊妹小說的實際改編策略

以《局中玫瑰》為例，不直接做「第一章 → 一支影片」，而是：

```text
第一章
 ↓
Scene 01：白景深深夜辦公室
Scene 02：異常資金出現
Scene 03：樓慕妍夜間查資料
Scene 04：四姊妹資料出現
Scene 05：黑色信封
Scene 06：兩封信指向彼此
 ↓
每個 Scene 再拆成 Shot
 ↓
每 Shot 生成數個候選
 ↓
挑選 Canon Shot
 ↓
Scenebuilder 組場
 ↓
加入角色聲音／旁白／字幕／音樂
```

這種做法最適合後續製作「一章約 1 小時的電視劇式內容」，因為小說文字、鏡頭、聲音與字幕可以分開管理，再進行最後合成。

## 7. 與有聲劇、字幕、音樂的分工

Google Flow 不應取代 Jemora 的完整媒體 Pipeline。

建議分工：

| 資產 | Jemora 管理 | Google Flow |
|---|---|---|
| 原著小說 | Canon | 不修改 Canon |
| 角色 Bible | Canon | 作為視覺參考 |
| 場景表 | Canon | 作為生成依據 |
| 角色／場景圖 | 管理 | 生成／編輯 |
| AI 影片 | 保存版本與來源 | 生成／編輯／組場 |
| 有聲小說 | 管理 | 可配合部分生成音訊能力 |
| 有聲劇 | 管理多角色音軌 | 可提供部分影音聲音素材 |
| 字幕 | SRT/VTT Canon | 不作為唯一字幕來源 |
| 音樂 | 獨立音樂資產 | 可作為影片創作的一部分，但最終音樂仍獨立保存 |
| 最終影片 | 發行資產 | 提供場景／片段 |

## 8. 版本與檔名

建議延續 Jemora 命名規則：

```text
作品_篇章_章節_Scene01_Shot01_flow_v01.mp4
作品_篇章_章節_Scene01_Shot01_flow_v02.mp4
作品_篇章_章節_Scene01_Shot01_final.mp4
```

參考圖：

```text
作品_角色_VisualRef_v01.png
作品_場景_VisualRef_v01.png
```

Prompt：

```text
作品_章節_Scene01_Shot01_flow_prompt_v01.md
```

## 9. 品質控制

每個鏡頭在進入 Final 前檢查：

- [ ] 角色外觀符合 Character Bible
- [ ] 年齡感正確
- [ ] 服裝符合時間線
- [ ] 場景符合 World Bible
- [ ] 道具前後一致
- [ ] 人物左右位置沒有無意義跳變
- [ ] 光線與時間一致
- [ ] 動作符合小說描述
- [ ] 對白沒有改變原著意思
- [ ] 鏡頭接續自然
- [ ] 音訊與字幕可分離保存
- [ ] 有來源章節／Scene／Shot metadata

## 10. 目前值得注意的官方功能狀態

Google Flow 的模型能力會持續更新。官方目前列出的能力包括不同 Veo 版本、Gemini Omni，以及 Nano Banana 系列影像模型；不同模型支援的影片長度、影格、素材參考、Extend、影片編輯與解析度不同。

2026 年 8 月的官方更新已加入更強的起始／結束影格控制，以及 1080p／4K 輸出能力；同時也提供 360p 草稿生成後再升級到較高解析度的工作方式。實際可用功能仍以帳號、地區、模型與當前 Flow 介面為準。

## 11. Jemora 的標準原則

> **Jemora 管理故事 Canon；Google Flow 負責視覺化與影片創作。**

不可反過來讓生成結果決定小說劇情。

最終來源優先順序：

```text
作品 Canon / 最終小說
        ↓
Character Bible / World Bible
        ↓
Scene Sheet
        ↓
Visual Bible
        ↓
Google Flow Prompt
        ↓
AI Generation
        ↓
人工 QC
        ↓
Final Media Asset
```

## 官方資料

- Google Flow：https://flow.google.com/
- Google Flow Help：https://support.google.com/flow/
- Google Flow：Create videos：https://support.google.com/flow/answer/16353334
- Google Flow：Edit videos & build scenes：https://support.google.com/flow/answer/16935718
- Google Flow Agent：https://support.google.com/flow/answer/17093911
- Google Flow models & supported features：https://support.google.com/flow/answer/16352836
- Google Blog：Introducing Flow：https://blog.google/innovation-and-ai/products/google-flow-veo-ai-filmmaking-tool/
- Google Blog：Veo 3.1 in Flow：https://blog.google/innovation-and-ai/products/veo-updates-flow/
- Google Blog：2026 Flow creative controls：https://blog.google/innovation-and-ai/models-and-research/google-labs/new-creative-controls-google-flow/
