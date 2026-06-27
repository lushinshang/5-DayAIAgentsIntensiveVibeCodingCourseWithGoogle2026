# Day 3 — Agent Skills（Agent 技能）

## 摘要

本目錄目前已將 Google「5-Day AI Agents Intensive Course」Day 3 白皮書 PDF
歸檔至 `source/Agent Skills_Day_3.pdf`。

依照 Day 2 `README.md` 的交接建議，Day 3 建議採用相同主流程：

**PDF 解析 → Markdown + 圖片擷取 → 確認真正 Figure → 整理正式圖 → 多代理人翻譯
→ 中文化圖片 → HTML 排版 → 對照 PDF double check → Podcast / 學習頻道導讀整合
→ 根目錄入口更新**。

本檔案先作為 Day 3 的執行規劃與交接紀錄。尚未完成的產物會明確標示為「預計」，
避免把規劃誤認為已完成。

**目前狀態**：已完成 task1-task22。

- task1：已建立 `source/`、`pipeline/`，並將 PDF 移入 `source/`。
- task2：已用 docling 以 `images_scale=5.0` 產出英文 Markdown。
- task3：已確認 Day 3 有 11 張正式 Figure。
- task4：已整理 11 張正式 Figure 到 `source/Agent Skills_Day_3_images/`。
- task5：已產出繁體中文 Markdown 與 normalized 版本。
- task6：已建立中文圖目錄並複製 11 張正式 Figure，檔名與原圖一致。
- task7：已建立 `index.html`，完成 HTML 語法驗證與桌機/手機截圖 QA。
- task8：已完成 PDF / 英文 MD / 繁中 MD / HTML double check，並補回缺漏內容。
- task9：已重繪 11 張中文化 Figure，檔名與尺寸維持與原圖一致，並重產截圖 QA。
- task10：已完成 Podcast 深度導讀頁，整合影片、英文 SRT 與兩個學習頻道 Codelab。
- task11：已更新上一層根目錄入口，Day3 卡片改為可點擊完成狀態，並更新根目錄 README。
- task12：已對齊 Day1 / Day2 學習頻道規格，移除 Markdown 卡片、Podcast 逐字稿改為分講者呈現，並補 Codelab 導讀資訊圖。
- task13：已補上兩個 Codelab 導讀頁的官方步驟對照表。
- task14：已整理 Day3 目錄，將根目錄散落 SRT 歸檔到 `source/podcast/`，並同步 README 目錄結構。
- task15：已在 `index.html` 學習頻道新增「推薦頻道」群組，加入阿魁 Notion 卡片（外部連結）。
- task16：已移除 `index.html` 中的「推薦頻道」群組（含阿魁卡片）。原因：task15 加入的連結實為 Day 2 直展導讀，已移至 Day 2 頁面；Day 3 阿魁分享連結尚未公開，暫時隱藏，待阿魁提供 Day 3 連結後再行補入。（2026-06-17）
- task17：已建立 `source/livestream/` 目錄並將當前目錄的 Day 3 英文與繁中字幕歸檔。
- task18：已撰寫直播深度導讀腳本 `pipeline/build_day3_transcript.py`，完成中英字幕時間戳對齊，並產生純文字逐字稿 `day3-transcript.txt` 與逐字稿 HTML 片段 `transcript_fragment.html`。
- task19：已排除資訊圖繪製，僅以逐字稿與深度導讀本文作為直播導讀主體。
- task20：已建立 `day3-deep-guide/index.html` 網頁，整合直播影片播放器、導讀本文與 7 位講者識別之雙語摺疊逐字稿（402 輪發言），並通過 HTML 語法驗證。
- task21：已在 `index.html` 學習頻道中插入「🎬 Day 3 直播深度導讀」卡片進行雙向串聯，並清理臨時測試腳本。
- task22：在推薦頻道中補齊快半拍AI實驗室的 Day 3 學習筆記卡片。（2026-06-28）
- task17：已建立 `source/livestream/` 目錄並將當前目錄的 Day 3 英文與繁中字幕歸檔。
- task18：已撰寫直播深度導讀腳本 `pipeline/build_day3_transcript.py`，完成中英字幕時間戳對齊，並產生純文字逐字稿 `day3-transcript.txt` 與逐字稿 HTML 片段 `transcript_fragment.html`。
- task19：已排除資訊圖繪製，僅以逐字稿與深度導讀本文作為直播導讀主體。
- task20：已建立 `day3-deep-guide/index.html` 網頁，整合直播影片播放器、導讀本文與 7 位講者識別之雙語摺疊逐字稿（402 輪發言），並通過 HTML 語法驗證。
- task21：已在 `index.html` 學習頻道中插入「🎬 Day 3 直播深度導讀」卡片進行雙向串聯，並清理臨時測試腳本。�文化 Figure，檔名與尺寸維持與原圖一致，並重產截圖 QA。
- task10：已完成 Podcast 深度導讀頁，整合影片、英文 SRT 與兩個學習頻道 Codelab。
- task11：已更新上一層根目錄入口，Day3 卡片改為可點擊完成狀態，並更新根目錄 README。
- task12：已對齊 Day1 / Day2 學習頻道規格，移除 Markdown 卡片、Podcast 逐字稿改為分講者呈現，並補 Codelab 導讀資訊圖。
- task13：已補上兩個 Codelab 導讀頁的官方步驟對照表。
- task14：已整理 Day3 目錄，將根目錄散落 SRT 歸檔到 `source/podcast/`，並同步 README 目錄結構。
- task15：已在 `index.html` 學習頻道新增「推薦頻道」群組，加入阿魁 Notion 卡片（外部連結）。
- task16：已移除 `index.html` 中的「推薦頻道」群組（含阿魁卡片）。原因：task15 加入的連結實為 Day 2 直播導讀，已移至 Day 2 頁面；Day 3 阿魁分享連結尚未公開，暫時隱藏，待阿魁提供 Day 3 連結後再行補入。（2026-06-17）

注意：這份 PDF 與 Day 2 不同，docling 成功產出 Markdown，但沒有抽出任何
picture image。因此 Day 3 圖表改用 `pdfimages` 從 PDF 內嵌圖片直接抽出，
再依 PDF 文字 caption 對應正式 Figure。

---

## PDF 基本資訊

| 項目 | 內容 |
|------|------|
| 檔案 | `Agent Skills_Day_3.pdf` |
| 標題 | Agent Skills |
| 作者 | Tanvi Singhal、Gabriela Hernandez Larios、Debanshu Dus、Lavi Nigam、Smitha Kolan |
| 頁數 | 62 頁 |
| 檔案大小 | 10,125,978 bytes |
| 建立時間 | 2026-06-10 22:14:16 CST |
| PDF 版本 | 1.7 |

---

## 目前目錄結構

```
Day3/
├── README.md                                      ← 本檔案：Day3 規劃與執行紀錄
├── index.html                                     ← Day3 繁中主頁
├── desktop.png                                    ← 桌機截圖 QA
├── mobile.png                                     ← 手機截圖 QA
├── images_cht/                                    ← HTML 正式引用的 11 張中文化 Figure
├── antigravity-skills-guide/
│   ├── antigravity-skills-guide.html              ← Antigravity Skills Codelab 白話導讀
│   ├── images/                                    ← 16:9 / 9:16 導讀資訊圖
│   ├── desktop.png                                ← 導讀頁桌機截圖 QA
│   └── mobile.png                                 ← 導讀頁手機截圖 QA
├── agents-cli-adk-guide/
│   ├── agents-cli-adk-guide.html                  ← Agents CLI + ADK Lifecycle Codelab 導讀
│   ├── images/                                    ← 16:9 / 9:16 導讀資訊圖
│   ├── desktop.png                                ← 導讀頁桌機截圖 QA
│   └── mobile.png                                 ← 導讀頁手機截圖 QA
├── day3-deep-guide/
│   └── index.html                                 ← Day3 直播深度導讀網頁（最終產出）
├── podcast-deep-guide/
│   ├── podcast-deep-guide.html                    ← Podcast 繁中深度導讀頁
│   ├── podcast-deep-guide.md                      ← Podcast 繁中深度導讀 Markdown
│   ├── Whitepaper Companion Podcast Agent Skills.en-orig.srt
│   ├── desktop.png                                ← Podcast 頁桌機截圖 QA
│   └── mobile.png                                 ← Podcast 頁手機截圖 QA
├── pipeline/
│   ├── convert_day3.py                            ← 600 DPI docling 解析：PDF → Markdown
│   ├── extract_day3_figures.py                    ← 從 raw 圖挑出正式 Figure 並重新命名
│   ├── localize_day3_figures.py                   ← 重繪 11 張中文化 Figure
│   ├── build_day3_podcast.py                      ← SRT → Podcast 導讀 Markdown / HTML
│   └── generate_codelab_guide_images.py           ← 產生 Codelab 導讀資訊圖
└── source/
    ├── Agent Skills_Day_3.pdf                     ← 原文 PDF
    ├── Agent Skills_Day_3.md                      ← docling 解析出的英文 Markdown（570 行）
    ├── Agent Skills_Day_3_zh.md                   ← 繁體中文稿
    ├── Agent Skills_Day_3_zh.normalized.md        ← 正規化繁體中文稿
    ├── Agent Skills_Day_3_images_raw/             ← pdfimages 抽出的 34 個 raw 圖檔（含 smask）
    ├── Agent Skills_Day_3_images/                 ← 11 張英文正式 Figure
    ├── Agent Skills_Day_3_images_cht/             ← 11 張中文化 Figure
    ├── codelabs/                                  ← 官方 Codelab HTML 來源快照
    └── podcast/                                   ← Podcast 原始 SRT 來源歸檔
```

## PDF 內容初步概要

依 PDF 目錄頁，Day 3 主題聚焦於「Agent Skills」：如何把任務知識、流程、工具使用方式
封裝成可重用的技能，並進一步評估、部署、組合與演化。

| 章節 | 主題 |
|------|------|
| 1. Introduction | Agent Skills 的背景與定位 |
| 2. What is an Agent Skill | Skill anatomy、progressive disclosure、建立第一個 skill |
| 3. Why did Agent Skills become popular | Skills 在 chatbot、coding agent、enterprise multi-agent 場景的價值 |
| 4. Evaluating Skills | 評估 toolkit、trigger、output quality、tool trajectory、token budget |
| 5. From Prototype to Production | Agent runtime、skills 作為改進單位、context overflow |
| 6. Meta-Skills and Self-Improving Skills | Meta-skill、自我改進 skill 的限制與方向 |
| 7. Composing and Packaging Skills | DAG orchestration、capability profiles、skill taxonomy、context debt |
| 8. How to Decide Among Skills | 如何在大量 skills 中選擇 |
| 9. Conclusion | 結論 |
| Appendix A | Practical cheatsheet、minimal SKILL.md、命名、description、rules、checklists |

---

## 建議完整流程（Pipeline）

### 1. 建立 `source/` 與 `pipeline/`（已完成）

已建立：

- `source/`
- `pipeline/`

並已將 `Agent Skills_Day_3.pdf` 移入 `source/`。

可重用來源：

| 來源 | 用途 |
|------|------|
| `../Day1/pipeline/convert_pdf.py` | 初版 docling 解析 PDF、快速取得 Markdown 與圖片 |
| `../Day1/pipeline/match_figures.py` | 輔助核對圖表與 Markdown 佔位符 |
| `../Day2/pipeline/reprocess_600dpi.py` | Day2 可重取指定 Figure；Day3 因 docling 未抽出 picture，改用 `pdfimages` |

### 2. 600 DPI 初版 docling 轉換（已完成）

已建立 `pipeline/convert_day3.py`，第一次解析就設定：

- `images_scale=5.0`
- `do_ocr=True`
- `do_table_structure=True`
- `generate_picture_images=True`

產出：

- `source/Agent Skills_Day_3.md`（570 行）
- `source/Agent Skills_Day_3_images_raw/`（docling 先建立目錄，但未抽出圖）

執行問題：

- macOS `ocrmac` OCR 多次回報 `NoneType` error，但 docling 最終仍完成 Markdown 輸出。
- `result.document.pictures` 為空，docling 未抽出任何 picture image。
- Markdown 沒有 `<!-- image -->` 或 `{{Figure N}}` 圖片佔位符。

因此 Day3 圖片處理改用 `pdfimages`：

```bash
pdfimages -png source/Agent\ Skills_Day_3.pdf source/Agent\ Skills_Day_3_images_raw/picture
```

### 3. 確認真正 Figure（已完成）

用 `pdftotext` 搜尋 caption，確認 Day3 PDF 共有 11 張正式 Figure：

| Figure | 頁面 | raw 圖檔 | 正式檔名 |
|--------|------|----------|----------|
| 1 | 19 | `picture-012.png` | `Figure 1 Skill Failure Modes.png` |
| 2 | 21 | `picture-014.png` | `Figure 2 Skill Trigger Gatekeeping.png` |
| 3 | 23 | `picture-016.png` | `Figure 3 Evaluation-Driven Development Loop.png` |
| 4 | 26 | `picture-018.png` | `Figure 4 Co-loaded Skills Performance Gap.png` |
| 5 | 29 | `picture-020.png` | `Figure 5 Agents CLI Install Flow.png` |
| 6 | 31 | `picture-022.png` | `Figure 6 Demo-to-Deploy Gap.png` |
| 7 | 33 | `picture-024.png` | `Figure 7 Context Rot in Practice.png` |
| 8 | 34 | `picture-026.png` | `Figure 8 Token Economics Skill Library.png` |
| 9 | 36 | `picture-028.png` | `Figure 9 Production Histories to Procedural Memories.png` |
| 10 | 37 | `picture-030.png` | `Figure 10 Meta-Skill Evaluation Gating.png` |
| 11 | 54 | `picture-032.png` | `Figure 11 Skills-First Retail Architecture.png` |

說明：`pdfimages` 同時輸出 image 與 smask；正式 Figure 使用偶數主圖檔，後面的奇數檔為遮罩，不作正文圖。

### 4. 整理正式 Figure 圖檔（已完成）

已建立並執行 `pipeline/extract_day3_figures.py`，將 11 張正式 Figure 複製到：

- `source/Agent Skills_Day_3_images/`

驗證結果：

- 正式 Figure：11 張
- 圖片寬度：約 1434-1960 px
- 圖片高度：約 596-1632 px
- raw 目錄保留 34 個檔案備查（含封面、TOC、正式圖與 smask）

### 5. 多代理人並行翻譯

建議依 Markdown 行數切成 4 個 chunk：

- Agent 1：標題、摘要、Introduction、What is an Agent Skill
- Agent 2：Popularity、Evaluating Skills 前半
- Agent 3：Evaluating Skills 後半、Prototype to Production、Meta-Skills
- Agent 4：Composing/Packaging、Choosing Skills、Conclusion、Appendix

翻譯規則沿用 Day 2：

- 技術術語保留英文縮寫並補中文說明
- 程式碼區塊不翻譯
- URL、人名、產品名稱保留英文
- 圖片佔位符原樣保留
- 不在翻譯階段自行改寫原意；潤飾與修正留到 double check 階段

預計產出：

- `source/Agent Skills_Day_3_zh.md`
- `source/Agent Skills_Day_3_zh.normalized.md`

目前已完成：

- `source/Agent Skills_Day_3_zh.md`
- `source/Agent Skills_Day_3_zh.normalized.md`

說明：本次未使用子代理，因為使用者此輪沒有明確要求多代理人並行；由主流程直接完成繁中稿。

### 6. 中文化圖表（已完成）

流程建議：

1. 先確認 Day 3 真正 Figure 數量。
2. 將原文圖輸出到 `source/Agent Skills_Day_3_images/`。
3. 中文化後放入 `source/Agent Skills_Day_3_images_cht/`。
4. 中文化圖檔檔名需與原圖一致。
5. 複製正式使用版本到 `images_cht/`，供 `index.html` 相對路徑引用。

目前已建立：

- `source/Agent Skills_Day_3_images_cht/`：11 張圖
- `images_cht/`：11 張圖

task9 已建立並執行 `pipeline/localize_day3_figures.py`，用 PIL 重新繪製 11 張 Figure：

- 中文化後的圖檔檔名與原圖完全一致。
- 圖片尺寸維持與原圖一致，避免 HTML 版面跳動。
- 同步輸出到 `source/Agent Skills_Day_3_images_cht/` 與 `images_cht/`。
- 圖中文字已改為繁體中文；`SKILL.md`、`ADK`、`MCP`、CLI 指令、API / SDK 等技術名稱保留英文。

驗證：

- `images_cht/`：11 張 PNG。
- `source/Agent Skills_Day_3_images_cht/`：11 張 PNG。
- HTML 11 張圖片引用缺檔 0。
- `python3 -m html.parser index.html` 通過。
- 已重新產出 `desktop.png` 與 `mobile.png`。

### 7. 建立 `index.html`（已完成第一版）

建議比照 Day 2 手工建立白皮書主頁，而不是完全依賴自動 Markdown 轉換：

- Hero：Day 3 標題與主題摘要
- Sticky nav：主要章節錨點 + Podcast + 學習頻道
- 正文：依白皮書章節拆成可讀的繁中長文
- 圖表：使用 `<figure class="section-figure">`
- 程式碼：保留 `SKILL.md`、資料夾結構、範例設定等 code block
- 表格：用於 skill vs MCP vs AGENTS.md、eval checklist、deployment checklist
- Lightbox：圖片放大時使用 `img.currentSrc || img.src`
- 響應式 QA：桌機與手機都要截圖檢查

驗證：

```bash
python3 -m html.parser index.html
```

若需要本機伺服器：

```bash
python3 -m http.server 8765
```

目前已完成：

- 建立 `index.html`
- 引用 `images_cht/` 中 11 張 Figure
- 包含 hero、sticky nav、白皮書主線正文、表格、code block、checklist、Appendix A、Appendix B、learning channels
- `python3 -m html.parser index.html` 驗證通過
- Playwright 截圖 QA：
  - `desktop.png`（1440x1000）
  - `mobile.png`（390x844）

### 8. 對照 PDF double check（已完成）

完成 `index.html` 後，逐節比對：

- 英文 Markdown
- 繁中 Markdown
- HTML 實際內容
- 原始 PDF

Day 2 曾在此階段補回 Applied Tip、Toolkit 條列、x402 micropayments 段落。Day 3 同樣要特別檢查：

- Appendix A 的 checklist 是否完整
- Minimal `SKILL.md` 範例是否保留
- Do's and Don'ts 是否完整
- Skill smells 是否完整
- Eval coverage checklist / Deployment checklist 是否完整
- 圖表 caption 與圖片順序是否一致

本次 double check 發現並修正：

1. `index.html` 缺少第 9 章 Conclusion，已補入。
2. `zh.md` 與 `index.html` 未完整呈現 Table 1 Evaluation Toolkit，已補入 5 種測試模式。
3. trigger gate 段落細節不足，已補入 Vercel non-invocation rate、`AGENTS.md` 對照與 4 項 description 檢查。
4. token budget 段落缺少 3 個 practical implications，已補入。
5. 零售案例 HTML 缺 Table 5 ownership model，已補入。
6. Endnotes 原本只有摘要，已在 `zh.md` 與 HTML 補回 36 條來源。
7. HTML footnotes 長 URL 已補 `word-break` / `overflow-wrap`，避免手機版溢出。

驗證：

- `python3 -m html.parser index.html` 通過。
- HTML 11 張圖片引用缺檔 0。
- HTML h2 結構含 1-9 章、Appendix A、Appendix B、學習頻道、附註。
- HTML 附註共 36 條。
- 已重新產出 `desktop.png` 與 `mobile.png`。

### 9. Podcast 與學習頻道（已完成）

已取得並整合：

- 英文 SRT：`/Users/lanss/projects/2_Practice/readpaper/mvmake/subtitles/Whitepaper Companion Podcast Agent Skills.en-orig.srt`
- Antigravity Skills Codelab：`https://codelabs.developers.google.com/getting-started-with-antigravity-skills`
- Agents CLI + ADK Lifecycle Codelab：`https://codelabs.developers.google.com/agents-cli-adk-lifecycle`

已建立 `pipeline/build_day3_podcast.py`，輸出：

- `podcast-deep-guide/podcast-deep-guide.md`
- `podcast-deep-guide/podcast-deep-guide.html`
- `podcast-deep-guide/Whitepaper Companion Podcast Agent Skills.en-orig.srt`
- `podcast-deep-guide/desktop.png`
- `podcast-deep-guide/mobile.png`

導讀內容使用 `ai-mentor` 與 `deep-guide` 的要求處理：以繁體中文台灣用語重寫 Podcast 主線，
聚焦 context rot、progressive disclosure、skill evaluation、production governance、
meta-skill 風險、DAG / file message bus 與企業知識資產。

`podcast-deep-guide.html` 包含：

- Podcast 影片播放器。
- 兩個 Codelab 實作入口。
- 折疊式英文原始逐字稿，共 324 段 cue，依 SRT `>>` 換 speaker 記號分為「主持人」與「專家」。
- 返回 Day 3 主頁連結。

`index.html` 學習頻道已新增：

- Antigravity Skills 白話導讀：`antigravity-skills-guide/antigravity-skills-guide.html`。
- Agents CLI + ADK Lifecycle 導讀：`agents-cli-adk-guide/agents-cli-adk-guide.html`。
- Podcast 深度導讀。

後續依 Day2 版位修正：

- `index.html` 的學習頻道已移到 hero 後、正文前，與 Day2 一致。
- 兩個 Codelab 不再由主頁直接外連，改為先進本地導讀頁，導讀頁末尾保留官方 Codelab 來源。
- 主頁學習頻道不放 Markdown 來源卡片，與 Day1 / Day2 一致。
- 兩個官方 Codelab 已用 `curl -L` 保存到 `source/codelabs/`，並依來源 step 審查導讀內容：
  - Antigravity Skills 導讀補入「官方 Codelab 步驟對照」，完整列出 9 個官方 step，並補入 `npx skills` / open agent skills ecosystem。
  - Agents CLI + ADK 導讀補入「官方 Codelab 步驟對照」，完整列出 10 個官方 step，並補入 cleanup 與 next steps。
- 兩個 Codelab 導讀頁已補 16:9 與 9:16 資訊圖，使用 `pipeline/generate_codelab_guide_images.py` 產生，避免圖片中文字錯誤。

驗證：

- `python3 -m html.parser antigravity-skills-guide/antigravity-skills-guide.html` 通過。
- `python3 -m html.parser agents-cli-adk-guide/agents-cli-adk-guide.html` 通過。
- `python3 -m html.parser podcast-deep-guide/podcast-deep-guide.html` 通過。
- `python3 -m html.parser index.html` 通過。
- `index.html` 本地圖片引用缺檔 0。
- Podcast HTML 含 324 個 transcript turn、主持人 167 段、專家 157 段，並保留影片播放器。
- 已重新產出 Day3 主頁、兩個 Codelab 導讀頁與 Podcast 頁的桌機 / 手機截圖。

### 10. 更新根目錄入口（已完成）

Day 3 `index.html` 完成並驗證後，已更新上一層：

- `../index.html`：Day 3 卡片由 `is-soon` 改為 `is-live`，連結到 `./Day3/index.html`。
- `../README.md`：目前狀態改為 Day1、Day2、Day3 已完成，並補入 Day3 目錄結構。

驗證：

- `python3 -m html.parser ../index.html` 通過。
- 根目錄 `index.html` live 卡片連結為 Day1、Day2、Day3。
- Day1、Day2、Day3 live 連結對應檔案皆存在。

---

## README 維護守則

每次更新本 README 都必須包含：

1. 執行歷程：做了什麼、結果如何、遇到什麼問題。
2. 原始提示詞：逐字紀錄使用者下的指令。
3. 已完成與未完成狀態：避免將規劃寫成已完成。

目的：讓 Day 4、Day 5 及未來專案可以直接複用這份紀錄，不需重新推導流程。

---

## 對話需求紀錄（依時間順序）

1. **建立 Day 3 README 規劃**：「read day2/readme.md 規劃day3/readme.md」
   → 已閱讀 `../Day2/readme.md`，確認 Day 2 README 的結構、pipeline、維護守則與 Day 3 建議。
   → 已讀取 Day 3 PDF 基本資訊與目錄頁。
   → 建立本檔案，將 Day 2 的 SOP 轉換為 Day 3 可執行規劃。

2. **先提供工作流程**：「請先提供工作流程」
   → 先以文字提供 Day3 由 PDF 解析到根目錄入口更新的完整工作流程。

3. **調整策略：第一次就 600 DPI**：「初版 PDF 解析的時候就可以600dpi正式圖了吧」
   → 確認 Day3 PDF 頁數與大小不高，第一次 docling 解析即可用 `images_scale=5.0`。
   → 重新規劃為「第一次解析即 600 DPI raw 圖」，不再先 300 DPI 再重跑。

4. **重新規劃工作流程**：「重新規劃工作流程」
   → 將流程改為 12 步，前四步為：整理目錄、600 DPI 初版 PDF 解析、確認真正 Figure、整理正式 Figure。

5. **執行 task1-task4**：「do task1 - task4」
   → 建立 `source/`、`pipeline/`。
   → 將 `Agent Skills_Day_3.pdf` 移入 `source/`。
   → 建立並執行 `pipeline/convert_day3.py`，以 docling `images_scale=5.0` 產出 `source/Agent Skills_Day_3.md`。
   → 發現 docling 沒有抽出 picture image，改用 `pdfimages` 抽出 34 個 raw 圖檔。
   → 用 `pdftotext` caption 與 `pdfimages -list` 頁碼確認 11 張正式 Figure。
   → 建立並執行 `pipeline/extract_day3_figures.py`，產出 `source/Agent Skills_Day_3_images/` 內 11 張正式 Figure。

6. **執行 task5-task7**：「do task5 - task7」
   → 產出 `source/Agent Skills_Day_3_zh.md`，涵蓋主文、11 張 Figure、表格、Appendix A、Appendix B 與速查表。
   → 複製為 `source/Agent Skills_Day_3_zh.normalized.md`，作為後續 HTML / 校對流程使用。
   → 建立 `source/Agent Skills_Day_3_images_cht/` 與 `images_cht/`，各放入 11 張正式 Figure，檔名與原圖一致。
   → 建立 `index.html`：hero、sticky nav、白皮書正文、表格、code block、checklist、lightbox、學習頻道。
   → `python3 -m html.parser index.html` 驗證通過。
   → Playwright 產出 `desktop.png` 與 `mobile.png` 截圖 QA，首屏渲染正常。
   → 限制：圖表目前是英文原圖複製到中文圖目錄，尚未完成圖內英文標籤重繪。

7. **執行 task8**：「do task8」
   → 比對 PDF 文字、英文 Markdown、繁中 Markdown 與 HTML 的章節、圖表、表格與附註。
   → 發現 HTML 缺第 9 章結論，已補入。
   → 發現 Table 1 Evaluation Toolkit、trigger gate 細節、token budget practical implications、Table 5 ownership model 不完整，已補入 `zh.md` 與 / 或 `index.html`。
   → 發現 Endnotes 只有摘要，已補回 36 條來源。
   → HTML parser、圖片引用、h2 結構與附註數量檢查通過，並重產桌機 / 手機截圖。

8. **執行 task9**：「do task9」
   → 建立 `pipeline/localize_day3_figures.py`，用 PIL 重新繪製 Day3 11 張 Figure。
   → 將圖內主要英文標籤改為繁體中文，並保留必要技術名稱如 `SKILL.md`、`ADK`、`MCP`、CLI 指令與 API / SDK。
   → 中文化 Figure 以相同檔名、相同尺寸輸出到 `source/Agent Skills_Day_3_images_cht/` 與 `images_cht/`。
   → 驗證 HTML parser 通過、HTML 11 張圖片引用缺檔 0，並重新產出 `desktop.png` 與 `mobile.png`。

9. **執行 task10**：「podcast 逐字稿...影片...還有兩個學習頻道...導讀的時候，要用到ai-mentor and deepguide skill --- do task10」
   → 依要求讀取 `ai-mentor` 與 `deep-guide` skill 指引，並讀取 `ai-mentor` 相關專家參考檔。
   → 建立 `pipeline/build_day3_podcast.py`，讀取使用者提供的英文 SRT，產出 Podcast 繁中深度導讀 Markdown / HTML。
   → `podcast-deep-guide/podcast-deep-guide.html` 已整合兩個 Codelab、返回 Day3 主頁連結與折疊式英文逐字稿。
   → `index.html` 學習頻道已加入 Podcast 深度導讀與兩個 Codelab 導讀入口。
   → HTML parser 通過，並重產 Day3 主頁與 Podcast 頁桌機 / 手機截圖。

10. **執行 task11**：「do task11」
    → 更新上一層 `../index.html`，將 Day3 卡片從 `is-soon` 改為 `is-live`，並連到 `./Day3/index.html`。
    → 更新上一層 `../README.md`，將專案狀態改為 Day1、Day2、Day3 已完成，並補入 Day3 目錄結構與參考入口。
    → 驗證 `../index.html` HTML parser 通過，且 Day1、Day2、Day3 live 連結檔案皆存在。

11. **補齊 Day3 學習頻道導讀**：「day3/index.html的學習頻道怎麼和day2/index.html不一樣位置？」與「ok,and https://codelabs.developers.google.com/agents-cli-adk-lifecycle 和 https://codelabs.developers.google.com/getting-started-with-antigravity-skills，應該要做導讀，請觀察day2」
    → 比對 Day2 與 Day3 `index.html`，確認 Day2 的學習頻道位於 hero 後、正文前，Day3 原本位於文章末尾。
    → 將 Day3 `index.html` 的學習頻道移到 hero 後方，並改成 Day2 式的「學習頻道 / 原始素材」分組卡片。
    → 依官方 Codelab 內容新增 `antigravity-skills-guide/antigravity-skills-guide.html` 與 `agents-cli-adk-guide/agents-cli-adk-guide.html` 兩個繁中導讀頁。
    → 驗證三個 HTML 檔案 parser 通過、本地連結缺檔 0，並重產主頁與兩個導讀頁桌機 / 手機截圖。

12. **審查學習頻道與 Podcast 規格**：「1.markdown，day2沒有，day3也應該沒有 2.podcast的逐字稿，應該參考day1,day2的podcast，最好還可以分不同講者 3.學習頻道的導讀，和來源內容是否一致請審查，而且應該需要生圖，請參考day1/day2的方式」
    → 移除 Day3 `index.html` 學習頻道中的繁中 / 英文 Markdown 卡片，與 Day1 / Day2 一致。
    → 修改 `pipeline/build_day3_podcast.py`，將 Podcast 逐字稿改成獨立 transcript section，並依 SRT `>>` 記號分為「主持人」與「專家」兩種 speaker badge。
    → 用 `curl -L` 保存兩個官方 Codelab HTML 到 `source/codelabs/`，抽出 step 標題與關鍵內容，審查並修正兩個導讀頁。
    → 新增 `pipeline/generate_codelab_guide_images.py`，為兩個 Codelab 導讀產生 16:9 / 9:16 資訊圖，並插入導讀頁。
    → 驗證 HTML parser、本地連結、Podcast speaker turn 數量與截圖 QA。

13. **確認 Codelab 是否逐步整理**：「審查兩個 Codelab 導讀與官方來源一致性==>所有步驟都有整理出來了？」
    → 回答並修正：原本是深度導讀覆蓋主線，尚未逐條列出官方 step。
    → 依 `source/codelabs/` 官方 HTML 補入「官方 Codelab 步驟對照」區塊。
    → `antigravity-skills-guide.html` 已列出官方 9 個 step；`agents-cli-adk-guide.html` 已列出官方 10 個 step。
    → 重新驗證兩個導讀頁 HTML parser、本地連結缺檔 0，並重產桌機 / 手機截圖。

15. **新增阿魁推薦頻道卡片**：「阿魁的url：https://meta-ghost.notion.site/Agent-3827b792315a817b9ce3c8b24046021f」
    → channels section 新增第二個 group「推薦頻道」，加入阿魁 Notion 卡片（外部連結）。
    → URL：`https://meta-ghost.notion.site/Agent-3827b792315a817b9ce3c8b24046021f`
    → 描述文字：阿魁的 Agent Skills 學習筆記，涵蓋 Day 3 Skill anatomy、評估、production governance 深度解析。

14. **整理 Day3 目錄**：「整理目錄」
    → 盤點 Day3 檔案樹，確認根目錄有一份散落的 Podcast SRT，且與 `podcast-deep-guide/` 中的 SRT checksum 相同。
    → 建立 `source/podcast/`，將根目錄 `Whitepaper Companion Podcast Agent Skills.en-orig.srt` 移入作為來源歸檔。
    → `podcast-deep-guide/` 保留 SRT 副本，供 HTML 頁面相對連結下載。
    → 更新 README 目前狀態與目錄結構。`.DS_Store` 屬於 macOS 系統暫存，未在未明示刪除的情況下移除。

16. **建立 Day 3 直播深度導讀**：「規劃執行 Task 17 - Task 21（但是不生圖，只要準備逐字稿） 「DAY 3 ... 」原文和中文逐字稿已經準備好 ... 影片連結 ...」
    → 歸檔原始字幕至 `source/livestream/` 中。
    → 建立 `pipeline/build_day3_transcript.py`，合併中英字幕並 stateful 追蹤 7 位講者，產生純文字 `day3-transcript.txt` 與 HTML 片段。
    → 建立 `day3-deep-guide/build_html.py` 產出 `index.html` 導讀頁，內嵌直播影片播放器（指向 github releases 連結）、5 節深度導讀與 402 輪折疊式中英雙語逐字稿。
    → 修改 `index.html` 學習頻道插入卡片完成雙向串聯，清理測試腳本並通過 `html.parser` 語法驗證。

---

## 附錄：原始 Prompt 逐句紀錄

```
1. read day2/readme.md 規劃day3/readme.md
2. 請先提供工作流程
3. 初版 PDF 解析的時候就可以600dpi正式圖了吧
4. 重新規劃工作流程
5. do task1 - task4
6. do task5 - task7
7. do task8
8. do task9
9. podcast 逐字稿「/Users/lanss/projects/2_Practice/readpaper/mvmake/subtitles/Whitepaper\ Companion\ Podcast\ Agent\ Skills.en-orig.srt」
   影片「https://github.com/lushinshang/5-DayAIAgentsIntensiveVibeCodingCourseWithGoogle2026/releases/download/DAY_1_Livestream/Whitepaper.Companion.Podcast.Agent.Skills_compressed.mp4」
   還有兩個學習頻道：
   1.https://codelabs.developers.google.com/getting-started-with-antigravity-skills
   2.https://codelabs.developers.google.com/agents-cli-adk-lifecycle
   導讀的時候，要用到ai-mentor and deepguide skill
   ---
   do task10
10. do task11
11. day3/index.html的學習頻道怎麼和day2/index.html不一樣位置？
12. ok,and https://codelabs.developers.google.com/agents-cli-adk-lifecycle和https://codelabs.developers.google.com/getting-started-with-antigravity-skills，應該要做導讀，請觀察day2
13. 1.markdown，day2沒有，day3也應該沒有
    2.podcast的逐字稿，應該參考day1,day2的podcast，最好還可以分不同講者
    3.學習頻道的導讀，和來源內容是否一致請審查，而且應該需要生圖，請參考day1/day2的方式
14. 審查兩個 Codelab 導讀與官方來源一致性==>所有步驟都有整理出來了？
15. 整理目錄
16. read readme.md now, 説what's next
17. read 每一天的readme.md，day3可以規劃直播導讀嗎？
18. 規劃執行 Task 17 - Task 21（但是不生圖，只要準備逐字稿） 「DAY 3 Livestream - 5-Days of AI Agents Intensive Vibe Coding Course With Google」原文和中文逐字稿已經準備好，影片連結「https://github.com/lushinshang/5-DayAIAgentsIntensiveVibeCodingCourseWithGoogle2026/releases/download/DAY_1_Livestream/DAY.3.Livestream.-.5-Days.of.AI.Agents.Intensive.Vibe.Coding.Course.With.Google_compressed.mp4」也準備好
```

---

## 給 Day 4 的預先提醒

Day 3 的主題是「如何建立與評估 Agent Skills」，很適合作為後續 Day 4/Day 5 的工作流基礎。
在 Day 3 完成後，建議額外整理：

1. Day 3 實際使用到的 prompt pattern。
2. 哪些流程應該固化成專案專用 skill。
3. 哪些檢查清單可以直接放進 Day 4 的 README 範本。
4. `SKILL.md` minimal template 與本專案 pipeline 的對應關係。
5. **阿魁推薦頻道**：Day 4 `index.html` 學習頻道須新增「推薦頻道」群組，加入阿魁 Notion 卡片（外部連結）。
   URL 格式參考 Day2 / Day3，描述文字請對應 Day 4 主題更新。

---

## 更新紀錄

### 阿魁頻道卡片修正（2026-06-17）

**問題說明**：Day3 的阿魁卡片原本指向 Day2 直播導讀 URL（錯位），且類型標示不清。
**修正內容**：
- `index.html` 阿魁卡片標題改為「阿魁｜直播導讀」，圖示改為 🎥。
- 因該連結為 Day 2 內容，已將其移至 Day 2 頁面。
- 由於 Day 3 阿魁直播導讀正確 URL 尚未公開，已於 task16 暫時移除整個「推薦頻道」群組。
- **待辦**：未來阿魁若提供 Day 3 連結，再行將該區塊與卡片補回。

## 異動紀錄

### 2026-06-19 目錄架構標準化調整
* **推薦資源新增**：於 `index.html` 恢復推薦頻道群組，並補入「阿魁｜直播導讀」Notion 卡片。
* **檔案位置整理**：將原本放在 `podcast-deep-guide/` 下的 `Whitepaper Companion Podcast Agent Skills.en-orig.srt` 歸位至 `source/podcast/` 目錄。
* **全域清理**：清除隱藏垃圾檔案 `.DS_Store`。

### 2026-06-19 直播深度導讀 HTML 全面優化（本次 Session）

**原始 Prompt**：
```
day3 and day4的直播導讀html
要以ai-mentor(或is_mentor,如果有牽涉到資安的話）and deepguide skill，
針對srt中各階段討論次主題去深度導讀，雖然html已完成，還是可以優化，
請幫我審查及規劃（還是不生圖，先規劃生圖逐字稿）
→ phase 1 -> phase 2
→ 1.不要白皮書的中文圖，請規劃適當段落，以及生圖逐字稿，先放readme.md
   2.day1-day5的codelab，原來的URL內如果有圖檔，請將圖檔網址放到codelab導讀的適當位置
```

**完成事項**：

**Phase 1 — Bug 修正**
* `day3-deep-guide/index.html`：逐字稿 **402 個 turns** 全部修正講者 badge（原本全標成 Anant），按 SRT 分析正確指派 7 位講者（Smitha 藍、Anant 綠、Gabriella 琥珀、Julia 紫、Tanvi 青、Debanshu 紅、Paulong 橙）。
* 白皮書中文圖片（`images_cht/` 11 張）已從 `day3-deep-guide/index.html` **完全移除**，改為待自製插圖佔位。
* 圖片 CSS class `.fig` 已加入 HTML `<style>` 區塊。

**Phase 2 — ai-mentor 深度內容補寫**
* `#anatomy` 新增 `callout-think`：漸進式揭露真因是語意重疊（非 Token 量），Tanvi 的 Gradient Interference 洞察。
* `#evaluation` 新增 `callout-think`：Pass@K vs Trajectory Consistency 本質差異，Debanshu 的可信賴性定義。
* `#meta-skills` 新增 `callout-think`：模型跨架構不可攜性安全盲區，Gabriella 的 Skill Registry 預測。

**自製插圖（已完成）**：
* `day3-deep-guide/README.md` 保存圖 A–E 的完整生圖逐字稿與執行結果。
* 5 張圖已生成、歸檔並嵌入直播深度導讀 HTML。

**Codelab 圖片整合**：
* `antigravity-skills-guide.html`：加入 3 張 Google Codelabs CDN 官方截圖（Progressive Disclosure 架構、Antigravity 技能清單查詢、Agents CLI 載入確認）。

### 2026-06-19 直播深度導讀自製插圖完成

- 本次指令：`update readme.md`
- 使用 Codex CLI 工作階段內的 `imagegen` skill／內建 `image_gen`，完成圖 A–E。
- 圖片存於 `day3-deep-guide/images/`，均為 1672×941 PNG。
- 圖 A、B 已嵌入 `#anatomy`；圖 C、E 已嵌入 `#evaluation`；圖 D 已嵌入 `#meta-skills`。
- HTML parser 通過，本地圖片缺檔 0；桌機 1440×1000 與 iPhone 13 視窗截圖 QA 通過。
- 目前 Day 3 直播深度導讀圖片工作無待辦事項。

### 2026-06-20 阿魁 Day 3 白皮書導讀 URL 更新

- **原始 Prompt**：「阿魁day3白皮書導讀：https://meta-ghost.notion.site/Agent-Skills-AI-SOP-3857b792315a81dc9c0aff376ac46c29 請更新day3/index.html」
- **修正內容**：`index.html` 推薦頻道中阿魁卡片連結由舊測試 URL（`Agent-Skills-Agent-3837b792...`）更新為正式白皮書導讀 URL。
  - 新 URL：`https://meta-ghost.notion.site/Agent-Skills-AI-SOP-3857b792315a81dc9c0aff376ac46c29`
  - 標題改為：「阿魁｜白皮書導讀 × AI SOP」
  - 描述改為：阿魁的 Day 3 白皮書導讀筆記，深入解析 Agent Skills anatomy、評估機制，並整合 AI SOP 實作應用。
- **狀態**：推薦頻道卡片已正式指向公開 Day 3 白皮書導讀頁。

### 2026-06-20 推薦頻道改為雙卡片（對齊 Day2）

- **原始 Prompt**：「阿魁直播導讀也要保留，參考day2/index.html」
- **修正內容**：推薦頻道從單張（白皮書導讀）改為雙張，對齊 Day2 規格。
  - 卡片一：🎥 阿魁｜直播導讀（URL：`https://meta-ghost.notion.site/Agent-Skills-Agent-3837b792315a81109412dc844e6b5011`）
  - 卡片二：📝 阿魁｜白皮書導讀 × AI SOP（URL：`https://meta-ghost.notion.site/Agent-Skills-AI-SOP-3857b792315a81dc9c0aff376ac46c29`）
