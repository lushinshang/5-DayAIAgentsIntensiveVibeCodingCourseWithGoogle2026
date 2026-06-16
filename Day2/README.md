# Day 2 — Agent Tools & Interoperability（Agent 工具與互操作性）

## 摘要

本目錄將 Google「5-Day AI Agents Intensive Course」Day 2 白皮書 PDF
（`source/Agent Tools & Interoperability_Day_2.pdf`），透過
「PDF 解析 → 圖文擷取（600 DPI）→ 多代理人並行翻譯 → HTML 排版 → 對照 PDF 校對
→ Podcast 嵌入 → 學習頻道 deep-guide 導讀」流程，使用 IBM Docling 引擎產出
可直接在瀏覽器開啟的繁體中文長文網頁 `index.html`，內含 8 張中文化圖表與一支
Podcast 影片播放器。

另外，本目錄補充整理了 2 份 Day 2 相關 Google Codelabs，採用
「deep-guide 白話繁中導讀 → codex_imagegen.py 生成 AI 資訊圖 → md_to_html 轉為
standalone HTML → Playwright 桌機/手機截圖 QA」流程，分別存放於：

- `antigravity-cli-guide/`
- `mcp-knowledge-guide/`

**最終產出**：`index.html`（雙擊或本機伺服器開啟即可閱讀）。  
**Day 3 可參考**：下方「給 Day 3 的流程建議」一節，整理了本次流程中
可重用的腳本、決策原則與 Day2 新增的模式。

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
├── pipeline/                                              ← PDF 解析與圖片處理腳本（參考 Day1 慣例）
│   ├── convert_day2.py                                    ← 初版轉換腳本（已廢棄）
│   └── reprocess_600dpi.py                               ← 正式版：600 DPI 重新擷取 8 張圖
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
├── podcast-deep-guide/                                   ← 學習頻道：Day 2 Podcast 深度導讀
│   ├── podcast-deep-guide.html                          ← 導讀頁面（deep-guide + md_to_html）
│   ├── podcast-deep-guide.md                            ← 原始 Markdown 稿
│   ├── podcast-deep-guide.normalized.md                 ← 標點正規化版（供建 HTML 用）
│   └── images/                                           ← 6 張 AI 生成圖（16:9 + 9:16 各 3 組）
│       ├── infographic_1.png / infographic_1_mobile.png  ← NxM → N+M 複雜度對比
│       ├── infographic_2.png / infographic_2_mobile.png  ← 五層協定棧總覽
│       └── infographic_3.png / infographic_3_mobile.png  ← AP2 授權命令 + 握手流程
├── Whitepaper Companion Podcast Agent Tools & Interoperability_compressed.mp4
└── source/                                                ← 所有原始素材集中存放
    ├── Agent Tools & Interoperability_Day_2.pdf           ← 原文 PDF（白皮書正本）
    ├── Agent Tools & Interoperability_Day_2.md            ← docling 解析出的英文 Markdown
    ├── Agent Tools & Interoperability_Day_2_zh.md         ← 繁體中文 Markdown（多代理人翻譯）
    ├── Agent Tools & Interoperability_Day_2_zh.normalized.md ← 中文標點正規化版（供 HTML 轉換用）
    ├── Agent Tools & Interoperability_Day_2_images/       ← 8 張原文圖表 PNG（600 DPI）
    └── Agent Tools & Interoperability_Day_2_images_cht/  ← 8 張中文化圖（原稿，檔名與原圖相同）
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

使用 Day1 的 `pipeline/convert_pdf.py`，修改 `__main__` 的 `pdf_path` 指向 Day2 PDF。
設定：`images_scale=3.0`（約 300 DPI），產出 18 張圖，需人工比對哪些是真正的 Figure。

### 2. 讀 Markdown 確認真正的 Figure

docling 將 PDF 中所有圖片元素一律解析為 `<!-- image -->` 佔位符（注意：Day2 用
`<!-- image -->`，Day1 用 `{{Figure N}}`，兩者格式不同）。閱讀 Markdown 全文，
逐一核對每個 `<!-- image -->` 前後是否有「Figure N:」caption：

- 18 個 `<!-- image -->` 中，只有 8 個真正對應「Figure 1～8」
- 其餘 10 個為封面圖示、TOC 插圖、Applied Tip 圖示等

### 3. 600 DPI 重新擷取 8 張主圖

使用 `pipeline/reprocess_600dpi.py`，以 `images_scale=5.0`（約 600 DPI）重跑，
`figure_info` dict 指定正確的 8 個 picture index：

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

產出：8 張圖，各約 79 KB ～ 211 KB，存放於 `source/..._images/`。

### 4. 多代理人並行翻譯

採用 4 個並行子代理同時翻譯英文 Markdown（817 行）：

- Agent 1：第 1–200 行（標題、目錄、Introduction、MCP Discovery）
- Agent 2：第 200–400 行（MCP Config/Debug/Toolkit、A2A 架構演進）
- Agent 3：第 400–600 行（A2A 實作/貨幣化、A2UI 介紹）
- Agent 4：第 600–817 行（A2UI Pattern/Canvas、AP2/UCP、結論/附註）

翻譯規則：技術術語保留英文縮寫附中文說明、程式碼區塊不翻譯、`<!-- image -->`
佔位符原樣保留、URL/人名/產品名稱保留英文。

產出：`source/Agent Tools & Interoperability_Day_2_zh.md`（791 行）

### 5. 中文化圖片 + 標點正規化

1. 將 `source/..._images_cht/` 內的 8 張中文化圖複製到 `Day2/images_cht/`（供 HTML 相對路徑引用）
2. 執行 `normalize_punctuation.py` 正規化中文標點，產出 `zh.normalized.md`（5 行有變動）

### 6. 建立 `index.html`

手工建立，不使用 `md_to_html` 的 `codex_imagegen.py`（白皮書主頁圖片已由 docling 擷取）：

- 藍色漸層 hero、sticky 橫向導覽列（8 個章節錨點 + Podcast + 學習頻道）
- 8 節正文：簡介 / MCP 視角 / 突破 NxM / A2A 架構 / 虛擬勞動力 / A2UI / AP2 & UCP / 附註
- 8 張 `<figure class="section-figure">` 圖表、✅/❌ do/don't 區塊、程式碼區塊、3 個表格、21 條附註
- click-to-enlarge lightbox（`img.currentSrc`）
- `python3 -m html.parser` 語法驗證 + Playwright 桌機（1280×800）與手機（390×844）截圖 QA

### 7. 對照原文 PDF 做內容 double check

逐節比對 `index.html` vs. `zh.md`，Day2 發現 3 項遺漏並補入：
1. Applied Tip 文字段落（3 處）
2. Vibe Coder Toolkit 條列缺 2 項
3. AI Agent Marketplace / x402 micropayments 段落

### 8. 嵌入 Podcast

將 `Whitepaper Companion Podcast..._compressed.mp4` 以 `<video controls>` 嵌入頁首，
導覽列新增 `#podcast` 錨點。檔名含空白與 `&`，`src` 需做完整 URL encoding：
`Whitepaper%20Companion%20Podcast%20Agent%20Tools%20%26%20Interoperability_compressed.mp4`

### 9. 學習頻道與 deep-guide 導讀

在 `index.html` 新增 `<section id="channels" class="channels-section">`，包含：

**學習頻道**（內部 HTML 導讀頁）：
- 🖥️ Antigravity CLI 白話導讀 → `antigravity-cli-guide/antigravity-cli-guide.html`
- 🔌 Google Developer Knowledge MCP 白話導讀 → `mcp-knowledge-guide/mcp-knowledge-guide.html`

**推薦頻道**（外部連結）：
- 📝 阿魁 Notion 學習筆記 → `https://meta-ghost.notion.site/...`

每份導讀的建立流程：
1. 以 `deep-guide` skill 輸入 Codelab 完整內容，產出 5 段式繁中導讀文章
2. 以 `codex_imagegen.py` 生成資訊圖（16:9 桌機版 + 9:16 手機版各一組）
3. 手工建立 standalone HTML：綠色主題、sticky nav、`<picture>` 響應式圖片、lightbox
4. `python3 -m html.parser` 驗證 + Playwright 桌機/手機截圖 QA

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
   → 改用 Day1 的 `pipeline/convert_pdf.py`，修改 `__main__` 中 `pdf_path` 指向 Day2 PDF。
   → 第一次執行：300 DPI，產出 18 張圖。

3. **提出問題**：「1. 600DPI　2. PDF 只有八張 figure　--- 請先確定」
   → 列出 18 張圖的檔案大小，發現數張僅 1.5～2.5KB（幾乎空白）。
   → 確認方式：閱讀已生成的 Markdown 全文，比對每個 `<!-- image -->` 前後的 caption。

4. **讀 PDF**：「你先 read pdf」
   → 閱讀 `Agent Tools & Interoperability_Day_2.md` 全文（817 行）。
   → 確認 PDF 共有 8 張 Figure，找出對應 docling picture index（5、7、12、13、14、15、16、17）。

5. **執行重新截取**：「重新執行並用 600dpi 截取正確的figure」
   → 建立並執行 `reprocess_600dpi.py`。結果：8/8 張全部成功，耗時約 19 秒（MPS 加速）。

6. **建立 README**：「參考 day1 的 readme.md，建立本目錄的 readme.md
   （包含所有執行過程與提示詞，為了後面三天參考續用，包含需求重新描述）」
   → 即本檔案。

7. **閱讀 Day1 & Day2 README 並摘要**：「先閱讀 day1 的 readme.md，then day2 的 readme.md」
   → 確認 Day1 已完成全部 10 個步驟，Day2 目前僅完成 PDF 解析。

8. **更新 README 並加入維護守則**：「update readme.md，並註記每次 update 都要包含執行歷程與提示詞」

9. **翻譯啟動**：「1」（選擇步驟1：翻譯）

10. **多代理人並行翻譯**：「將 Agent Tools & Interoperability_Day_2.md（英文）翻譯為繁體中文 Markdown，how about multi agents?」
    → 採用 4 個並行子代理，產出 `source/Agent Tools & Interoperability_Day_2_zh.md`（791 行）。

11. **中文化圖檔重新命名**：「Agent Tools & Interoperability_Day_2_images 是圖檔原稿，Agent Tools & Interoperability_Day_2_images_cht 是圖檔中文化，請將中文化圖檔檔名和原圖檔一樣」
    → 將 `_images_cht/` 內 `figure1.png` ～ `figure8.png` 批次重新命名為 `Figure N <Title>.png`。

12. **整理 source 目錄**：「參考 day1 and day2 的 readme.md，建立 source 目錄，相關檔案放入」
    → 新建 `source/`，移入 PDF、MD、中文 MD、兩組圖片目錄。

13. **更新 README**：「更新 readme.md」

14. **轉成 HTML**：「繼續 Day 2 剩餘步驟，轉成 HTML」
    → 將 8 張中文化圖複製到 `images_cht/`，正規化標點，手工建立 `index.html`。
    → `python3 -m html.parser` 驗證通過，Playwright 截圖 QA 通過。
    → 產出：`Day2/index.html`

15. **Double-check HTML vs PDF**：「1」（對照原始 PDF double check）
    → 發現 3 項遺漏（Applied Tip 段落、Vibe Coder Toolkit 2 項、x402 段落），全部補入。

16. **嵌入 Podcast 影片**：「podcast的影片在此目錄「Whitepaper Companion Podcast Agent Tools & Interoperability_compressed.mp4」」
    → 在 `index.html` 新增 `<section id="podcast">`，加入 `<video controls>`；TOC 新增錨點。

17. **新增學習頻道（channels section）**：「這兩個應該是建立完導讀 學習頻道」
    → 在 `index.html` 插入 `<section id="channels" class="channels-section">`，
      含 Antigravity CLI 與 MCP 兩個 channel card；TOC 新增「學習頻道」錨點。

18. **建立 Antigravity CLI 深度導讀**：「導讀請用ai-mentor and deepguide skill來處理」
    → `deep-guide` skill 生成文章「你以為在用 AI，其實你還在複製貼上」（5 段式）。
    → `codex_imagegen.py` 生成 6 張 AI 圖（16:9 + 9:16 各 3 組），因路徑含空格/括號，
      先輸出至 `/tmp/agy-cli-images/` 再 `cp` 至最終位置。
    → `antigravity-cli-guide.html` 驗證通過，Playwright QA 通過。

19. **建立 MCP 深度導讀**：（接續步驟 18）
    → `deep-guide` skill 生成文章「你的 AI 助理還活在去年」（5 段式）。
    → `codex_imagegen.py` 生成 4 張 AI 圖，輸出至 `/tmp/mcp-knowledge-images/` 再 `cp`。
    → `mcp-knowledge-guide.html` 含 JSON config 程式碼區塊，驗證通過，Playwright QA 通過。

20. **新增阿魁推薦頻道卡片**：「阿魁的學習網址：`https://meta-ghost.notion.site/...`」
    → channels section 新增第二個 group「推薦頻道」，加入阿魁 Notion 卡片（外部連結）。
    → URL 修正為完整版：
      `https://meta-ghost.notion.site/Vibe-Coding-Agent-Engineering-AI-code-3817b792315a8174b658e0fac71f556d`
    → group 標題由「延伸資源」改為「推薦頻道」。

21. **整理目錄結構**：「day2下的架構，py是不是要找地方放，參考day1」
    → 建立 `pipeline/`，將 `convert_day2.py`、`reprocess_600dpi.py` 移入，比照 Day1 慣例。

22. **啟用根目錄 Day2 卡片**：「2.幫我做，但是上一層的readme.md也要更新」
    → 根目錄 `index.html` Day2 卡片 `is-soon` → `is-live`，標籤改為 `<a href="./Day2/index.html">`。
    → 根目錄 `README.md` 狀態更新為「Day1、Day2 已完成」，目錄結構補入 Day2 架構。
    → HTML 驗證通過，Playwright 截圖確認 `is-live` 樣式正常。

23. **建立 Podcast 深度導讀**：「day2有『Whitepaper Companion Podcast Agent Tools & Interoperability.en-orig.srt』，可以用 ai-mentor and deep-guide skill 讀取 SRT 全文，生成主題式繁中導讀，再以 md_to_html 建立 HTML，放入學習頻道。」
    → `deep-guide` skill 輸入完整 SRT 逐字稿（278 段，約 22 分鐘），生成 5 段式文章「當你的 AI 還在手刻電線，全世界已在插雲端插頭」。
    → 三條比喻主軸：「專屬規格插頭→MCP NxM→N+M」、「承包商遇到歪斜牆壁→A2A/GOTO 問題」、「作曲家的樂譜→A2UI 安全宣告式 UI」、「凌晨兩點訂捲餅→AP2/UCP 無信任商務」。
    → `normalize_punctuation.py` 標點正規化（2 處），`codex_imagegen.py` 生成 6 張 AI 圖（16:9 × 3 + 9:16 × 3），輸出至 `/tmp/` 再 `cp` 至 `podcast-deep-guide/images/`。
    → 手工建立 `podcast-deep-guide.html`：藍色漸層 hero、sticky nav（8 個錨點）、3 個 `<picture>` 響應式資訊圖 + lightbox。
    → `python3 -m html.parser` 驗證通過，Playwright 桌機/手機截圖 QA 通過。
    → `index.html` 學習頻道新增「🎙️ Podcast 深度導讀」卡片，驗證通過。

24. **補充原文逐字稿**：「和day1的podcast的導讀html比較，這個html應該要補充逐字稿，請研究補充規劃」→「yes」
    → 比對 Day1 `podcast-deep-guide.html`，發現 Day1 有 `<section class="transcript-section" id="transcript">` + `<details>` 折疊面板裝載完整英文逐字稿，Day2 缺此區塊。
    → 新增三處：① CSS（`.transcript-section`、`.transcript-toggle`、`.transcript-body`）② sticky nav 末尾加「原文逐字稿」錨點 ③ 逐字稿區塊（SRT 278 段去時間戳，合併為 19 個可讀段落）。
    → 驗證通過。

25. **結合到 Day 2 主頁**：「結合到day2的html」
    → 更新 `index.html` Podcast 卡片說明，加入「含英文原文逐字稿」，與 Day1 卡片模式一致。

26. **Sticky Nav 加返回連結**：「我要參考day1/podcast的導讀一樣，上一頁放頂端」
    → 比對 Day1 做法：sticky nav 第一項為高亮顯示的「← 返回白皮書首頁」。
    → Day2 照樣：nav 第一項新增 `<a class="nav-back" href="../index.html">← 返回 Day 2 主頁</a>`，加 `.nav-back` 樣式（藍底高亮）。
    → 同時移除先前多餘的逐字稿底部返回連結。
    → 驗證通過。

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

9. 1（選擇步驟1：翻譯）

10. 將 Agent Tools & Interoperability_Day_2.md（英文）翻譯為繁體中文 Markdown，how about multi agents?

11. Agent Tools & Interoperability_Day_2_images是圖檔原稿，Agent Tools & Interoperability_Day_2_images_cht是圖檔中文化，請將中文化圖檔檔名和原圖檔一樣

12. 參考day1 and day2的readme.md，建立source目錄，相關檔案放入

13. 更新readme.md

14. 繼續 Day 2 剩餘步驟，轉成 HTML

15. 1（步驟1：對照原始 PDF double check HTML）

16. podcast的影片在此目錄「Whitepaper Companion Podcast Agent Tools & Interoperability_compressed.mp4」

17. 還有兩件事 https://codelabs.developers.google.com/antigravity-cli-hands-on?hl=zh-tw#0 和
    https://codelabs.developers.google.com/developer-knowledge-mcp-antigravity?hl=zh-tw#0
    --- 是不是需要導讀？

18. 這兩個應該是建立完導讀 學習頻道

19. 導讀請用ai-mentor and deepguide skill來處理

20. update readme

21. 阿魁的學習網址：https://meta-ghost.notion.site/Vibe-Coding-Agent-Engineering-AI-code-3817b792315a

22. 改一下ＵＲＬ
    https://meta-ghost.notion.site/Vibe-Coding-Agent-Engineering-AI-code-3817b792315a8174b658e0fac71f556d

23. 是「推薦頻道」

24. update readme

25. 依據readme.md，我還有什麼該做的嗎

26. 1.可以不做 / 2.幫我做，但是上一層的readme.md也要更新 / 3.Promo_Channel今天沒有圖

27. update readme.md

28. day2下的架構，py是不是要找地方放，參考day1

29. 為了第三天，目前的readme.md清楚嗎？（參考day1的readme.md)

30. ok（修正四個問題：對話需求紀錄亂序、完整流程補完、給 Day3 建議補新模式、腳本路徑更新）

31. update readme

32. day2有「Whitepaper Companion Podcast Agent Tools & Interoperability.en-orig.srt」，可以用 ai-mentor and deep-guide skill 讀取 SRT 全文，生成主題式繁中導讀，再以 md_to_html 建立 HTML，放入學習頻道。

33. 截圖看起來不錯，把這步驟更新到 README.md

34. 和day1的podcast的導讀html比較，這個html應該要補充逐字稿，請研究補充規劃

35. yes

36. 結合到day2的html

37. 我要參考day1/podcast的導讀一樣，上一頁放頂端

38. update readme
```

---

## 給 Day 3 的流程建議

### 可重用的腳本

| 腳本 | 用途 | 重用時需修改 |
|------|------|------------|
| `Day1/pipeline/convert_pdf.py` | 初版 docling 轉換（300 DPI） | `__main__` 的 `pdf_path` |
| `Day2/pipeline/reprocess_600dpi.py` | **正式版**：600 DPI + 只取真正 Figure | `base_dir`、`pdf_path`、`image_dir`、`md_output`、`figure_info` |

> 建議直接複製 `Day2/pipeline/reprocess_600dpi.py` 到 Day3 目錄並修改路徑與 `figure_info`。

### 判斷 Figure Index 的方法

每份 PDF 結構不同，docling 解析出的 picture 數量也不同。標準 SOP：

1. **先用 300 DPI 跑一次**，快速產出初版 Markdown 與圖片清單。
2. **閱讀 Markdown 全文**，找出所有 `<!-- image -->` 的行號，確認前後是否有「Figure N:」caption。
3. **依序計算 index**：每個 `<!-- image -->` 對應一個 picture index（從 0 開始）。
4. **確認圖片大小**輔助驗證：裝飾 icon 通常 < 5KB，真正的架構圖 > 50KB。
5. **填入 `figure_info`**，執行 `reprocess_600dpi.py` 以 600 DPI 重取。

### 關鍵決策原則（PDF → HTML）

1. **佔位符格式差異**：Day2 docling 產出 `<!-- image -->`，Day1 是 `{{Figure N}}`。
   Day3 PDF 格式未知，轉換前先確認佔位符格式。

2. **路徑中有特殊字元（空格、`&`、`(`）**，不要在 Python inline code（`-c` 參數）中拼字串，
   改用獨立腳本檔（`.py`）執行，讓 Python 直接處理路徑物件。

3. **`docling` 的 `images_scale` 換算**：
   - `images_scale=3.0` ≈ 300 DPI
   - `images_scale=5.0` ≈ 600 DPI（建議值，兼顧品質與速度）

4. **翻譯後不要邊轉 HTML 邊潤飾**，忠實套用既有翻譯，留到最後 double check 階段
   逐項列出讓使用者決定。

5. **影片/檔名含空白與特殊字元**時，`<video src="...">` 需做完整 URL encoding
   （`%20` = 空格，`%26` = `&`）。

6. **docling 執行時間參考**：7.5MB PDF（Day2），MPS 加速，約 20 秒完成。

### Day2 新增模式：deep-guide + md_to_html 導讀頁

#### codex_imagegen.py 路徑問題

專案路徑含空格與括號（`5-Day AI Agents Intensive Course with Google(2026)`）時，
`codex_imagegen.py` 無法接受含這些字元的輸出路徑。解法：

```bash
# 先輸出到 /tmp/
python3 ~/.claude/skills/md_to_html/scripts/codex_imagegen.py \
  --prompt "..." \
  --image /tmp/guide-images/section_1.png \
  --aspect 16:9

# 再 cp 到最終目錄
cp /tmp/guide-images/section_1.png "Day3/xxx-guide/images/section_1.png"
```

#### 9:16 mobile variant 注意事項

生成手機版圖片時，**不要用 `--ref` 傳入已有的 16:9 PNG 作為參考**——
codex CLI 0.137.0 以後，`--ref` 會導致 `no_image_gen_tool_use` 錯誤。
改用純文字 prompt 明確列出原圖的視覺元素（標題、標籤、人物、具體物件），
要求重新繪製成 9:16 直式版本。

#### HTML 模式（channels section）

`index.html` 的 channels section 固定兩個 group：

```html
<section id="channels" class="channels-section">
  <div class="channels-inner">
    <div class="channel-group">
      <h3>學習頻道</h3>       <!-- 內部 HTML 導讀頁 -->
      <div class="channel-grid">...</div>
    </div>
    <div class="channel-group">
      <h3>推薦頻道</h3>       <!-- 外部連結，target="_blank" -->
      <div class="channel-grid">...</div>
    </div>
  </div>
</section>
```

#### lightbox 使用 `currentSrc` 而非 `src`

`<picture>` 元素在手機上會切換到 `9:16` variant，lightbox 放大時若用 `.src`
會拿到 fallback 的 16:9 URL。務必用 `img.currentSrc || img.src`：

```js
lbImg.src = img.currentSrc || img.src;
```

### 環境注意事項

- Python 版本：3.9（系統 Python）
- docling 已安裝於：`/Users/lanss/Library/Python/3.9/lib/python/site-packages/`
- OCR 引擎：自動選擇 `ocrmac`（macOS 原生）
- GPU 加速：MPS（Apple Silicon）
- SSL Warning（`urllib3 v2 / LibreSSL`）：僅為警告，不影響功能，可忽略
- 圖片壓縮（若需要）：`/Users/lanss/projects/2_Practice/readpaper/compress_jpg.py --preserve-resolution`
