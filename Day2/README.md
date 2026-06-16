# Day 2 — Agent Tools & Interoperability（Agent 工具與互操作性）

## 摘要

本目錄將 Google「5-Day AI Agents Intensive Course」Day 2 白皮書 PDF
（`source/Agent Tools & Interoperability_Day_2.pdf`），透過
「PDF 解析 → 圖文擷取（600 DPI）→ Markdown 輸出 → 繁體中文翻譯 → HTML 排版」流程，
使用 IBM Docling 引擎與多代理人並行翻譯策略產出：

- `index.html`（最終繁中網頁，雙擊即可在瀏覽器開啟）
- `images_cht/`（8 張中文化圖，供 index.html 引用）
- `source/Agent Tools & Interoperability_Day_2.md`（英文 Markdown，含 `<!-- image -->` 佔位符）
- `source/Agent Tools & Interoperability_Day_2_zh.md`（繁體中文 Markdown，791 行）
- `source/Agent Tools & Interoperability_Day_2_images/`（8 張原文主圖，600 DPI PNG）
- `source/Agent Tools & Interoperability_Day_2_images_cht/`（8 張中文化圖原稿，同檔名）

白皮書主題涵蓋 **MCP**（Model Context Protocol）、**A2A**（Agent-to-Agent）、
**A2UI**（Agent-to-UI）、**AP2 & UCP**（Agent Payments / Universal Commerce）
四大 Agent 互操作協定，以及 Vibe Coder 的實務工具組。

**Day 3 可參考**：下方「給 Day 3 的流程建議」一節，整理了本次流程中
可重用的腳本、決策原則與常見坑點。

---

## 目錄結構

```
Day2/
├── README.md                                              ← 本檔案
├── index.html                                             ← 最終輸出（繁中網頁，雙擊即可開啟）
├── images_cht/                                            ← index.html 使用的 8 張中文化圖
│   ├── Figure 1 Ecosystem of Agent Protocols.png
│   ├── Figure 2 Steps for Onboarding an MCP Server.png
│   ├── Figure 3 Monolithic Multi-agent Architecture.png
│   ├── Figure 4 Distributed Multi-Agent Architecture.png
│   ├── Figure 5 A2A Server and Client Supply and Demand.png
│   ├── Figure 6 Agent-as-a-Service AaaS Lifecycle.png
│   ├── Figure 7 User Agent Canvas Interaction Flow.png
│   └── Figure 8 AP2 and UCP Ecosystem.png
├── convert_day2.py                                        ← 初版轉換腳本（已廢棄）
├── reprocess_600dpi.py                                    ← 正式版：600 DPI 重新擷取 8 張圖
├── antigravity-cli-guide/                                 ← 學習頻道：Antigravity CLI 深度導讀
│   ├── antigravity-cli-guide.html                        ← 導讀頁面（deep-guide + md_to_html）
│   └── images/                                           ← 6 張 AI 生成圖（16:9 + 9:16 各 3 組）
│       ├── isolation-gap.png / isolation-gap-mobile.png
│       ├── permission-modes.png / permission-modes-mobile.png
│       └── two-exits.png / two-exits-mobile.png
├── mcp-knowledge-guide/                                   ← 學習頻道：Google Developer Knowledge MCP 導讀
│   ├── mcp-knowledge-guide.html                          ← 導讀頁面（deep-guide + md_to_html）
│   └── images/                                           ← 4 張 AI 生成圖（16:9 + 9:16 各 2 組）
│       ├── training-cutoff.png / training-cutoff-mobile.png
│       └── mcp-architecture.png / mcp-architecture-mobile.png
└── source/                                                ← 所有原始素材集中存放
    ├── Agent Tools & Interoperability_Day_2.pdf           ← 原文 PDF（白皮書正本）
    ├── Agent Tools & Interoperability_Day_2.md            ← docling 解析出的英文 Markdown
    ├── Agent Tools & Interoperability_Day_2_zh.md         ← 繁體中文 Markdown（多代理人翻譯）
    ├── Agent Tools & Interoperability_Day_2_zh.normalized.md ← 中文標點正規化版（供 HTML 轉換用）
    ├── Agent Tools & Interoperability_Day_2_images/       ← 8 張原文圖表 PNG（600 DPI）
    │   ├── Figure 1 Ecosystem of Agent Protocols.png
    │   ├── Figure 2 Steps for Onboarding an MCP Server.png
    │   ├── Figure 3 Monolithic Multi-agent Architecture.png
    │   ├── Figure 4 Distributed Multi-Agent Architecture.png
    │   ├── Figure 5 A2A Server and Client Supply and Demand.png
    │   ├── Figure 6 Agent-as-a-Service AaaS Lifecycle.png
    │   ├── Figure 7 User Agent Canvas Interaction Flow.png
    │   └── Figure 8 AP2 and UCP Ecosystem.png
    └── Agent Tools & Interoperability_Day_2_images_cht/  ← 8 張中文化圖（原稿，檔名與原圖相同）
        ├── Figure 1 Ecosystem of Agent Protocols.png
        ├── Figure 2 Steps for Onboarding an MCP Server.png
        ├── Figure 3 Monolithic Multi-agent Architecture.png
        ├── Figure 4 Distributed Multi-Agent Architecture.png
        ├── Figure 5 A2A Server and Client Supply and Demand.png
        ├── Figure 6 Agent-as-a-Service AaaS Lifecycle.png
        ├── Figure 7 User Agent Canvas Interaction Flow.png
        └── Figure 8 AP2 and UCP Ecosystem.png
```

---

## PDF 內容概要

白皮書作者：Kanchana Patlolla、Łukasz Olejniczak、Pier Paolo Ippolito

### 主要章節

| 章節 | 主題 |
|------|------|
| Introduction | Agent 協定生態全覽（MCP/A2A/A2UI/AP2/UCP） |
| MCP：Vibe Coder 視角 | Discovery（登錄中心）→ Configuration（scope/auth）→ Connection（handshake） |
| Bypassing the NxM Problem | MCP 將整合複雜度從 O(N×M) 降至 O(N+M) |
| A2A 互操作性 | Monolithic → Distributed 多 Agent 架構演進 |
| Building the Virtual Workforce | Agent Card、Registry、A2A Server/Client 實作 |
| A2A 商業化 | Agent-as-a-Service（AaaS）、GCP Marketplace、x402 微支付 |
| A2UI | Generative UI、安全沙盒渲染、catalog 18 組元件 |
| AP2 & UCP | 自主採購、自主支付、Guardrails 機制 |

### 8 張主圖對應

| Figure | 標題 | Picture Index（0-based） |
|--------|------|--------------------------|
| 1 | Ecosystem of Agent Protocols | 5 |
| 2 | Steps for Onboarding an MCP Server | 7 |
| 3 | Monolithic Multi-agent Architecture | 12 |
| 4 | Distributed Multi-Agent Architecture | 13 |
| 5 | A2A Server and Client Supply and Demand | 14 |
| 6 | Agent-as-a-Service AaaS Lifecycle | 15 |
| 7 | User Agent Canvas Interaction Flow | 16 |
| 8 | AP2 and UCP Ecosystem | 17 |

> **說明**：docling 共偵測到 18 個 picture；其中 index 0–4 為封面/TOC 裝飾圖，
> index 6/8–11 為 Applied Tip icon 或小示意圖（KB 級），僅 index 5、7、12–17
> 對應 Markdown 中明確標示「Figure N:」的 8 張主圖。

---

## 完整流程（Pipeline）

### 1. 初版 PDF → Markdown + 圖片擷取（300 DPI）

使用 Day1 的 `pipeline/convert_pdf.py`，修改 `__main__` 的 `pdf_path` 指向 Day2 PDF：

```python
# pipeline/convert_pdf.py __main__ 修改後
if len(sys.argv) > 1:
    pdf_path = sys.argv[1]
else:
    pdf_path = ".../Day2/Agent Tools & Interoperability_Day_2.pdf"
```

設定：`images_scale=3.0`（約 300 DPI），`generate_picture_images=True`，
`table_structure_options.mode = TableFormerMode.ACCURATE`。

產出：18 張圖（`figure1.png` ～ `figure18.png`），需人工比對哪些是真正的 Figure。

### 2. 讀 Markdown 確認真正的 Figure

docling 將 PDF 中所有圖片元素（含裝飾 icon、TOC 頁插圖）一律解析為
`<!-- image -->` 佔位符。透過閱讀 Markdown 全文，逐一核對每個
`<!-- image -->` 前後的文字，確認哪些緊接在「Figure N:」caption 之後：

- 18 個 `<!-- image -->` 中，只有 8 個真正對應「Figure 1～8」
- 其餘 10 個為封面圖示、TOC 插圖、Applied Tip 圖示、Debugging 示意圖等

### 3. 600 DPI 重新擷取 8 張主圖

使用 `reprocess_600dpi.py`，設定：

```python
pipeline_options.images_scale = 5.0   # ≈ 600 DPI
pipeline_options.generate_picture_images = True
```

並用 `figure_info` dict 指定 8 個正確的 picture index：

```python
figure_info = {
    5:  (1, "Figure 1 Ecosystem of Agent Protocols"),
    7:  (2, "Figure 2 Steps for Onboarding an MCP Server"),
    12: (3, "Figure 3 Monolithic Multi-agent Architecture"),
    13: (4, "Figure 4 Distributed Multi-Agent Architecture"),
    14: (5, "Figure 5 A2A Server and Client Supply and Demand"),
    15: (6, "Figure 6 Agent-as-a-Service AaaS Lifecycle"),
    16: (7, "Figure 7 User Agent Canvas Interaction Flow"),
    17: (8, "Figure 8 AP2 and UCP Ecosystem"),
}
```

執行流程：
1. 清空舊圖目錄
2. 重跑 docling（約 20 秒，MPS 加速）
3. 只儲存 8 張指定圖，檔名依 Figure 標題命名（已過 `sanitize_filename`）
4. 儲存格式：PNG，dpi=(600, 600)

產出：8 張圖，各約 79 KB ～ 211 KB。

---

## README 維護守則

> **每次更新 README 都必須包含**：
> 1. 執行歷程（做了什麼、結果如何、遇到什麼問題）
> 2. 原始提示詞（逐字紀錄使用者下的指令）
>
> 目的：讓 Day 3–5 及未來專案可以直接複用這份紀錄，不需重新推導流程。

---

## 對話需求紀錄（依時間順序）

1. **初始需求**：「參考 Day1 的內容，以 ibm docling 將此目錄的 PDF 解析為 MD 和圖檔」

2. **確認腳本來源**：「day1 有寫好的 py」
   → 確認改用 Day1 的 `pipeline/convert_pdf.py`，修改 `__main__` 中 `pdf_path`
   指向 Day2 PDF 路徑，並同時支援命令列參數（`sys.argv[1]`）以便日後複用。
   → 第一次執行：300 DPI，產出 18 張圖。

3. **提出問題**：「1. 600DPI　2. PDF 只有八張 figure　--- 請先確定」
   → 列出 18 張圖的檔案大小，發現數張僅 1.5～2.5KB（幾乎空白）。
   → 確認方式：閱讀已生成的 Markdown 全文，比對每個 `<!-- image -->` 前後的 caption。

4. **讀 PDF**：「你先 read pdf」
   → 閱讀 `Agent Tools & Interoperability_Day_2.md` 全文（817 行）。
   → 確認 PDF 共有 8 張 Figure（Figure 1～8），並找出各自對應的
   `<!-- image -->` 在 Markdown 的行號（136、192、316、360、445、523、670、754），
   以及對應 docling picture index（5、7、12、13、14、15、16、17）。

5. **執行重新截取**：「重新執行並用 600dpi 截取正確的figure」
   → 建立並執行 `reprocess_600dpi.py`。
   → 結果：8/8 張全部成功，耗時約 19 秒（MPS 加速）。

6. **建立 README**：「參考 day1 的 readme.md，建立本目錄的 readme.md
   （包含所有執行過程與提示詞，為了後面三天參考續用，包含需求重新描述）」
   → 即本檔案。

7. **閱讀 Day1 & Day2 README 並摘要**：「先閱讀 day1 的 readme.md，then day2 的 readme.md」
   → 依序讀取兩份 README，確認 Day1 已完成全部 10 個步驟（PDF 解析 → 翻譯 → HTML → QA → 壓縮 → Podcast → Codelabs → 頻道卡片 → deepguide），
     Day2 目前僅完成 PDF 解析（Markdown + 8 張 600 DPI PNG）。
   → 向使用者摘要兩份文件的執行狀態與四大主題（MCP / A2A / A2UI / AP2/UCP）。

8. **更新 README 並加入維護守則**：「update readme.md，並註記每次 update 都要包含執行歷程與提示詞」
   → 在「對話需求紀錄」上方新增「README 維護守則」區塊，明定每次更新必須包含執行歷程與原始提示詞。
   → 將第 7、8 筆紀錄補入本節。
   → 同步將第 7、8 條提示詞補入「附錄：原始 Prompt 逐句紀錄」。

9. **翻譯啟動**：「1」（選擇步驟1：翻譯）
   → 確認任務為將 `Agent Tools & Interoperability_Day_2.md`（817行英文）翻譯為繁體中文 Markdown。

10. **多代理人並行翻譯**：「將 Agent Tools & Interoperability_Day_2.md（英文）翻譯為繁體中文 Markdown，how about multi agents?」
    → 採用 4 個並行子代理同時翻譯策略：
      - Agent 1：第 1–200 行（標題、目錄、Introduction、MCP Discovery）
      - Agent 2：第 200–400 行（MCP Config/Debug/Toolkit、A2A 架構演進）
      - Agent 3：第 400–600 行（A2A 實作/貨幣化、A2UI 介紹）
      - Agent 4：第 600–817 行（A2UI Pattern/Canvas、AP2/UCP、結論/附註）
    → 各子代理完成後，由主代理收集並合併為完整繁體中文 Markdown。
    → 產出：`source/Agent Tools & Interoperability_Day_2_zh.md`（791 行）
    → 翻譯規則：技術術語保留英文縮寫附中文說明、程式碼區塊不翻譯、`<!-- image -->` 佔位符原樣保留、URL/人名/產品名稱保留英文。

11. **中文化圖檔重新命名**：「Agent Tools & Interoperability_Day_2_images 是圖檔原稿，Agent Tools & Interoperability_Day_2_images_cht 是圖檔中文化，請將中文化圖檔檔名和原圖檔一樣」
    → 將 `_images_cht/` 內的 `figure1.png` ～ `figure8.png`，
      批次重新命名為與 `_images/` 完全相同的檔名（`Figure N <Title>.png`）。

12. **整理 source 目錄**：「參考 day1 and day2 的 readme.md，建立 source 目錄，相關檔案放入」
    → 新建 `source/` 目錄，將以下檔案移入：
      - `Agent Tools & Interoperability_Day_2.pdf`
      - `Agent Tools & Interoperability_Day_2.md`
      - `Agent Tools & Interoperability_Day_2_zh.md`
      - `Agent Tools & Interoperability_Day_2_images/`
      - `Agent Tools & Interoperability_Day_2_images_cht/`
    → 根目錄僅保留 `README.md`、`convert_day2.py`、`reprocess_600dpi.py`（工具腳本）。

13. **更新 README**：「更新 readme.md」
    → 同步更新摘要、目錄結構、對話需求紀錄（第 11～13 筆）與附錄 Prompt。

14. **轉成 HTML**：「繼續 Day 2 剩餘步驟，轉成 HTML」
    → 執行流程：
      1. 將 8 張中文化圖從 `source/Agent Tools & Interoperability_Day_2_images_cht/` 複製到 `Day2/images_cht/`（供 HTML 相對路徑引用）。
      2. 以 `md_to_html` skill 的 `normalize_punctuation.py` 正規化中文標點，產出 `zh.normalized.md`（共 5 行有變動）。
      3. 手工建立 `index.html`：藍色漸層 hero、sticky 橫向導覽列（8 個章節錨點）、全文 8 節內容（簡介 / MCP 視角 / 突破 NxM / A2A 架構 / 虛擬勞動力 / A2UI / AP2 & UCP / 附註）、8 張 `<figure class="section-figure">` 圖表、✅/❌ do/don't 區塊、複雜度示意、程式碼區塊、3 個表格、21 條附註、click-to-enlarge lightbox。
      4. 跳過 zh.md 中 10 個裝飾性 `<!-- image -->`（TOC 頁、Applied Tip icon 等）。
      5. `python3 -m html.parser` 語法驗證通過。
      6. Playwright 桌機（1280×800）與手機（390×844）截圖 QA：8 張圖全部 200 OK，版面無溢出。
    → 產出：`Day2/index.html`（含 `Day2/images_cht/` 8 張圖）

15. **Double-check HTML vs PDF**：「1」（選擇步驟1：對照原始 PDF double check）
    → 逐行比對 `zh.md` 與 `index.html`，發現 3 項遺漏：
      1. Applied Tips 小圖示（`✅` do/don't 表格）—— 3 處 Applied Tip 文字段落未渲染
      2. 「Vibe Coder Toolkit」條列內容遺漏 2 項目
      3. 「AI Agent Marketplace / x402 micropayments」段落文字缺少
    → 全部修補至 `index.html`，重新截圖確認。

16. **嵌入 Podcast 影片**：「podcast的影片在此目錄「Whitepaper Companion Podcast Agent Tools & Interoperability_compressed.mp4」」
    → 在 `index.html` 新增 `<section id="podcast">` 於 `</header>` 之後，
      加入 `<video controls>` 嵌入本機 mp4；TOC 導覽列新增「Podcast」錨點連結。
    → 影片 src：`Whitepaper%20Companion%20Podcast%20Agent%20Tools%20%26%20Interoperability_compressed.mp4`

17. **新增學習頻道（channels section）**：「這兩個應該是建立完導讀 學習頻道」
    → 參考 Day1 html 的 channels-section 樣式，在 `index.html` 中 podcast section 之前插入
      `<section id="channels" class="channels-section">`，含兩個 channel card：
      - 🖥️ Antigravity CLI 白話導讀 → `antigravity-cli-guide/antigravity-cli-guide.html`
      - 🔌 Google Developer Knowledge MCP 白話導讀 → `mcp-knowledge-guide/mcp-knowledge-guide.html`
    → TOC 新增「學習頻道」錨點。

18. **建立 Antigravity CLI 深度導讀**：「導讀請用ai-mentor and deepguide skill來處理」
    → 使用 `deep-guide` skill 生成文章「你以為在用 AI，其實你還在複製貼上」（5 段式）。
    → 使用 `md_to_html` skill 的 `codex_imagegen.py` 生成 6 張 AI 圖（16:9 + 9:16 各 3 組），
      路徑問題（空格/括號）透過輸出到 `/tmp/agy-cli-images/` 再 cp 方式解決。
    → `antigravity-cli-guide.html`：綠色主題、sticky nav、lightbox、`<picture>` 響應式圖片。
    → `python3 -m html.parser` 驗證通過，Playwright 桌機/手機截圖 QA 通過。

19. **建立 MCP 深度導讀**：（本次對話）
    → 使用 `deep-guide` skill 生成文章「你的 AI 助理還活在去年」（5 段式）。
    → 使用 `codex_imagegen.py` 生成 4 張 AI 圖（16:9 + 9:16 各 2 組），
      輸出至 `/tmp/mcp-knowledge-images/` 後 cp 至 `mcp-knowledge-guide/images/`。
    → `mcp-knowledge-guide.html`：含 JSON config 程式碼區塊、MCP 架構圖、時間牆圖示。
    → `python3 -m html.parser` 驗證通過，Playwright 桌機/手機截圖 QA 通過。

---

## 附錄：原始 Prompt 逐句紀錄（供 Day 3-5 複用）

```
1. 參考Day1的內容，以ibm docling將此目錄的pdf解析為MD和圖檔

2. day1有寫好的py

3. 1.600DPI
   2.PDF只有八張figure
   ---
   請先確定

4. 你先read pdf

5. 重新執行並用600dpi截取正確的figure

6. 參考day1的readme.md，建立本目錄的readme.md
   （包含所有執行過程與提示詞，為了後面三天參考續用，包含需求重新描述）

7. 先閱讀day1的readme.md，then day2的readme.md

8. update readme.md，並註記每次update都要包含執行歷程與提示詞

9. 1
   （選擇步驟1：翻譯）

10. 將 Agent Tools & Interoperability_Day_2.md（英文）翻譯為繁體中文 Markdown，how about multi agents?

11. Agent Tools & Interoperability_Day_2_images是圖檔原稿，Agent Tools & Interoperability_Day_2_images_cht是圖檔中文化，請將中文化圖檔檔名和原圖檔一樣

12. 參考day1 and day2的readme.md，建立source目錄，相關檔案放入

13. 更新readme.md

14. 繼續 Day 2 剩餘步驟，轉成 HTML

15. 1
    （步驟1：對照原始 PDF double check HTML）

16. podcast的影片在此目錄「Whitepaper Companion Podcast Agent Tools & Interoperability_compressed.mp4」

17. 還有兩件事 https://codelabs.developers.google.com/antigravity-cli-hands-on?hl=zh-tw#0 和 https://codelabs.developers.google.com/developer-knowledge-mcp-antigravity?hl=zh-tw#0 --- 是不是需要導讀？

18. 這兩個應該是建立完導讀 學習頻道

19. 導讀請用ai-mentor and deepguide skill來處理

20. update readme
```

---

## 給 Day 3 的流程建議

### 可重用的腳本

| 腳本 | 用途 | 重用時需修改 |
|------|------|------------|
| `Day1/pipeline/convert_pdf.py` | 初版 docling 轉換（300 DPI） | `__main__` 的 `pdf_path` |
| `Day2/reprocess_600dpi.py` | **正式版**：600 DPI + 只取真正 Figure | `base_dir`、`pdf_path`、`image_dir`、`md_output`、`figure_info` |

> 建議直接複製 `Day2/reprocess_600dpi.py` 到 Day3 目錄並修改路徑與 `figure_info`。

### 判斷 Figure Index 的方法

每份 PDF 結構不同，docling 解析出的 picture 數量也不同。
標準作業程序（SOP）：

1. **先用 300 DPI 跑一次**（`convert_pdf.py`），快速產出初版 Markdown 與圖片清單。
2. **閱讀 Markdown 全文**，找出所有 `<!-- image -->` 的行號，
   逐一確認其前後是否有「Figure N:」caption。
3. **依序計算 index**：每個 `<!-- image -->` 對應一個 picture index（從 0 開始），
   累積計數即可得到真正 Figure 的 index。
4. **確認圖片大小**輔助驗證：裝飾 icon 通常 < 5KB，真正的架構圖 > 50KB。
5. **填入 `figure_info`**，執行 `reprocess_600dpi.py` 以 600 DPI 重取。

### 關鍵決策原則

1. **路徑中有特殊字元（如 `&`）時**，不要在 Python inline code（`-c` 參數）
   中拼字串，改用獨立腳本檔（`.py`）執行，讓 Python 直接處理路徑物件。

2. **docling 的 `images_scale` 換算**：
   - `images_scale=3.0` ≈ 300 DPI
   - `images_scale=5.0` ≈ 600 DPI（建議值，兼顧品質與速度）

3. **600 DPI 圖片大小**：每張約 80–400KB（PNG），若需壓縮可參考 Day1 的
   `readpaper/compress_jpg.py --preserve-resolution`，在不改變解析度的情況下縮小。

4. **不要直接重用 Day1 `reprocess_600dpi.py`**：其 `figure_info` 是 Day1 專屬的
   picture index，不同 PDF 的 index 完全不同，務必重新分析後再填入。

5. **docling 執行時間參考**：
   - 7.5MB PDF（Day2），MPS 加速，約 20 秒完成
   - 若 PDF 更大或無 GPU，時間等比例增加

### 環境注意事項

- Python 版本：3.9（系統 Python）
- docling 已安裝於：`/Users/lanss/Library/Python/3.9/lib/python/site-packages/`
- OCR 引擎：自動選擇 `ocrmac`（macOS 原生）
- GPU 加速：MPS（Apple Silicon）
- SSL Warning（`urllib3 v2 / LibreSSL`）：僅為警告，不影響功能，可忽略
