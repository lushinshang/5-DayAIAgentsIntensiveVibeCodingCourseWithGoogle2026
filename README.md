# 5-Day AI Agents: Intensive Vibe Coding Course With Google（2026）— 中文學習筆記專案

## 摘要

本目錄是 Google × Kaggle「5-Day AI Agents: Intensive Vibe Coding Course With
Google」（2026/06/15–06/19）課程的中文學習筆記彙整站。`index.html` 為整個
專案的入口首頁（課程介紹 + Day1-5 導覽），每個 `DayN/` 子目錄則放該日白皮書
的繁體中文長文網頁（依 Day1 的 pipeline 製作）。`capstone.html` 為獨立的專案實踐頁面，包含評分標準、案例研究、工具箱、提交流程等資源。

**目前狀態（2026-06-21）**：Day1–Day5 全部完成並已連結。Capstone 專案獨立頁面已建立。
- 根目錄 `index.html` 中 Day1–Day5 卡片全部為 `is-live`（可點擊）
- Capstone 專案頁面 `capstone.html` 已獨立完成，與首頁星形互聯
- 課程五天白皮書中文學習頁製作完成

**近期更新紀錄（2026-06-21 Capstone 獨立頁面）**：
- **Capstone 專案獨立頁面建立**：新增 `capstone.html`，包含完整的實踐資源導向：
  - 快速開始（3 步驟計數器）
  - 評分標準（表格：35% 功能性、25% 代碼、20% 創新、20% 文檔）
  - 案例研究（3 個往年優秀案例卡片）
  - 工具箱（Claude Code、Gemini API、Kaggle Notebook、Discord）
  - 提交流程（7 步驟 + 檢查清單）
  - 時程（6 個關鍵時間點：課程進行中 → Capstone 開放 → 開發期 → 截止 → 評審 → 獲獎公布）
  - 常見問題（7 個 FAQ，涵蓋個人/團隊、API 費用、代碼引用、評分、超期提交等）
- **index.html 導覽更新**：
  - 頂部 sticky nav 中加入「Capstone 專案」導覽連結
  - Day 卡片後方加入 Capstone CTA 區塊（漸變背景、標題、截止時間、行動按鈕）
  - CTA 設計將學員導向完整的 capstone.html 資源中心
- **星形導航架構**：
  - index.html ↔ capstone.html 雙向互聯（首頁可進 Capstone，Capstone 可回首頁）
  - capstone.html footer 提供 Day1-5 快速連結
  - 樣式一致性：兩頁共用 CSS 變數系統（同色彩、字型、響應式佈局）

**近期更新紀錄（2026-06-19 第三批）**：
- **外部推薦閱讀資源更新**：於 Day 1, 3, 4, 5 的 `index.html` 資源頻道中，補齊了快半拍 AI 實驗室的 Day 1 心得、阿魁 Day 3/4 直播導讀、阿魁 Day 4/5 白皮書導讀 Notion 卡片，方便使用者點擊閱讀外部精彩心得與解析。
- **GitHub Pages 部署優化重構（手動上傳優化）**：為了方便手動在 GitHub 網頁上傳部署，執行了專案結構重構：
  - 將所有與網頁直接發布無關的開發資源（各天別的 `source/` 與 `pipeline/` 目錄）統一收納至根目錄下的 `dev_resources/` 中。
  - **重要：手動網頁上傳時，請勿選取 `dev_resources/` 資料夾，只選取其他檔案與資料夾拖放上傳即可。**
  - **防範 404 連結壞軌修正**：將被 `Day2/index.html` 引用的中文白皮書 PDF 移至 `Day2/images_cht/`，並修正 href 引用路徑；將被 Day 3/4 Podcast 指南引用的字幕 `.srt` 檔案移入對應的 `podcast-deep-guide/` 發布目錄中。

**近期更新紀錄（2026-06-19 第二批）**：
- **Day3 直播導讀 HTML 全面優化**：修正逐字稿 402 turns 講者 badge（全錯 → 7 位正確著色）；移除白皮書中文圖（11 張）；補寫 3 個 ai-mentor `callout-think` 深度段落（語意重疊才是 Context Rot 真因、Pass@K vs Trajectory Consistency、Meta-Skills 跨模型安全盲區）。
- **Day4 直播導讀 HTML 全面優化**：修正 7 處 Markdown `**text**` 未渲染問題；移除白皮書中文圖（4 張）；補寫 2 個 is-mentor 深度段落（三層確定性防禦、Effective Trust UEBA 類比）。
- **Day3/Day4 生圖規劃**：建立 `day3-deep-guide/README.md`（圖 A-E）與 `day4-deep-guide/README.md`（圖 F-J），含完整生圖逐字稿與 session prompt 留存，待後續生圖工具執行。
- **Day1–Day5 Codelab 導讀圖片整合**：從各 Day source codelabs HTML 提取官方 Google CDN 圖片 URL，插入對應的 codelab guide 導讀 HTML（Day3 `antigravity-skills-guide` 3 張、Day5 `agent-runtime-deploy-guide` 3 張、Day5 `vibecode-frontend-guide` 4 張）；並修復 Day5 兩個 guide 中所有因本地路徑不存在而被 `onerror` 靜默隱藏的圖片。

**近期更新紀錄（2026-06-19 第一批）**：
- **全域目錄架構標準化重構**：統一了 Day 1 ~ Day 5 的一級子目錄配置。完成了 Day 1 `images_cht/` 更名與 HTML 圖片參照修正；Day 2/3/5 原始 PDF 及 Podcast 資源歸位至 `source/` 和 `source/podcast/`；清理重複字幕與隱藏檔案，使五天的目錄結構高度一致。
- Day5 主頁（`Day5/index.html`）製作完成，主題：規格驅動生產級開發（SDD）。
- 已將根目錄 `index.html` 的 Day5 卡片從 `is-soon` 改為 `is-live`，連結至 `./Day5/index.html`。
- Day5 學習頻道三頁均已完成：Podcast 深度導讀、Codelab 1（Agent Runtime 部署）、Codelab 2（Vibecode 前端）。
- Day5 包含：1 張中文化 Figure（imagegen text-localization）、7 個 Snippets、17 條 Endnotes，以及 7 張已生成並通過桌機／手機 QA 的繁中資訊圖。
- Day1–Day5 都具備首頁 → Day 頁、Day 頁 → 首頁 the 雙向導覽；Day5 回程會定位至首頁的 Day5 卡片。

**舊紀錄（2026-06-17）**：
- 已確認根目錄 `index.html` 的 Day3 卡片為 live link，連到 `./Day3/index.html`。
- 已補齊 Day3 直播深度導讀（`day3-deep-guide/index.html`），整合 402 輪 7 位講者識別之雙語摺疊逐字稿。
- 已在 `Day2/index.html` 與 `Day3/index.html` 的 sticky 目錄列最前方補上
  `../index.html` 回首頁連結，文字為「← 返回課程首頁」；Day1 原本已有同樣連結。
- 已建立 `Day4/README.md`、`source/`、`pipeline/`、`images_cht/`、
  `podcast-deep-guide/`、`source/codelabs/`、`source/podcast/`、
  `source/livestream/` 與 `day4-deep-guide/`，作為 Day4 後續製作 scaffold。

---

## 目錄結構

```
.
├── README.md                  # 本檔案（專案總覽 + 接續指南）
├── index.html                 # 入口首頁：Kaggle 課程介紹（中文）+ Day1-5 導覽卡片 + Capstone CTA
├── capstone.html              # Capstone 專案獨立頁面：評分標準、案例、工具箱、提交流程、時程、FAQ
├── Day1/
│   ├── README.md              # Day1 完整 pipeline 紀錄與異動紀錄
│   ├── index.html             # Day1 白皮書中文長文網頁（最終產出）
│   ├── images_cht/            # 9 張已壓縮的課程圖表
│   ├── day1-deep-guide/       # 學習頻道導讀（deep-guide）
│   ├── deploy-aistudio-to-cloud-run-guide/      # Codelab 1 深度導讀
│   ├── google-antigravity-codelab-guide/        # Codelab 2 深度導讀
│   └── podcast-deep-guide/    # Podcast 深度導讀網頁
├── Day2/
│   ├── README.md              # Day2 完整 pipeline 紀錄與異動紀錄
│   ├── index.html             # Day2 白皮書中文長文網頁（最終產出）
│   ├── desktop.png            # 桌面版網頁預覽圖
│   ├── images_cht/            # 8 張中文化圖表 + 白皮書中文 PDF 教材
│   ├── day2-deep-guide/       # 學習頻道導讀（deep-guide）
│   ├── antigravity-cli-guide/ # Codelab 1 深度導讀
│   ├── mcp-knowledge-guide/   # Codelab 2 深度導讀
│   └── podcast-deep-guide/    # Podcast 深度導讀網頁
├── Day3/
│   ├── README.md       ← Day3 完整 pipeline 紀錄 (含異動紀錄)
│   ├── index.html      ← Day3 白皮書中文長文網頁（最終產出）
│   ├── desktop.png     ← 桌面版網頁預覽圖
│   ├── mobile.png      ← 手機版網頁預覽圖
│   ├── images_cht/     ← 11 張中文化圖表
│   ├── source/         ← 原始 PDF + 中英文 Markdown + 圖片中間產物
│   │   ├── codelabs/   ← 兩個官方 Codelab HTML snapshot
│   │   ├── livestream/ ← 直播原始中英字幕與逐字稿
│   │   └── podcast/    ← Podcast 原始英文 SRT 字幕 (歸位)
│   ├── pipeline/       ← PDF 解析、圖表擷取、圖表中文化、直播與 Podcast 導讀腳本
│   ├── day3-deep-guide/          ← Day 3 直播深度導讀網頁（最終產出）
│   └── podcast-deep-guide/       ← Podcast 深度導讀與英文 SRT 副本
└── Day4/
    ├── README.md       ← Day4 完整 pipeline 紀錄
    ├── index.html      ← Day4 白皮書中文長文網頁（最終產出）✅
    ├── source/         ← Day4 PDF、Podcast、Codelab、livestream 素材
    ├── pipeline/       ← Day4 PDF / 圖表 / 導讀處理腳本
    ├── images_cht/     ← Day4 中文化 Figure
    ├── podcast-deep-guide/       ← Podcast 深度導讀
    ├── secure-agentic-coding-guide/   ← Codelab 1 深度導讀
    ├── vibecode-ambient-expense-agent-guide/ ← Codelab 2 深度導讀
    └── day4-deep-guide/          ← livestream 深度導讀
└── Day5/
    ├── README.md       ← Day5 完整 pipeline 紀錄
    ├── index.html      ← Day5 白皮書中文長文網頁（最終產出）✅
    ├── source/         ← Day5 PDF、Podcast SRT、Codelab 快照、中間產物
    ├── pipeline/       ← Day5 Docling 解析、正規化、驗證腳本
    ├── images_cht/     ← Day5 中文化 Figure（1 張）
    ├── podcast-deep-guide/           ← Podcast 深度導讀（含影片播放器）
    ├── agent-runtime-deploy-guide/   ← Codelab 1：Agent Runtime 部署導讀
    └── vibecode-frontend-guide/      ← Codelab 2：Vibecode 前端導讀
```

`Day1/`–`Day5/` 全部完成並連結至根目錄首頁。

---

## index.html（入口首頁）說明

- 內容是 Kaggle 競賽頁面 `overview` 的繁體中文翻譯（台灣 AI/IT 業界語氣），
  章節：課程進度導覽 → 課程介紹 → 運作方式 → 每日課程內容 → 本次新增 →
  常見問題 → Capstone 專案 → 引用資訊。
- 原始來源：
  https://www.kaggle.com/competitions/5-day-ai-agents-intensive-vibecoding-course-with-google/overview
  （此頁為 SPA，`WebFetch` 抓不到內容，需用 Playwright 開瀏覽器等 JS render
  後讀 accessibility snapshot。）
- 「課程進度導覽」區塊（`#days`）是 Day1-5 的卡片：
  - 已完成的天數：`<a class="day-card is-live" href="./DayN/index.html">`
  - 未完成的天數：`<div class="day-card is-soon">...<span class="badge-soon">即將推出</span></div>`
  - **新增 Capstone CTA 區塊**（`#days` 之後）：包含 Capstone 專案簡介、截止時間、「查看 Capstone 專案 →」按鈕
    - 背景漸變 `linear-gradient(135deg,rgba(168,85,74,0.08) 0%,...)`
    - 引導已完成課程的學員進入 `capstone.html` 資源中心
- **頂部 sticky nav 更新**：加入「Capstone 專案」導覽連結（`<a href="./capstone.html">`），便於從任何位置快速切換
- 配色與字型沿用 `Day1/index.html` 的 `:root` CSS 變數（`--accent:#a8554a`、
  `--bg:#f9f7f4`、Noto Sans TC），維持全站視覺一致。

---

## 後續維護指南

Day1–Day5 均已完成，Capstone 專案獨立頁面已建立。若後續要重製既有頁面、補充學習頻道、或更新 Capstone 規則，或將此流程套用到新課程，可依下列方式維護。

1. **製作或重製單日白皮書網頁**（比照 `Day1/README.md` 的完整 pipeline）：
   - 取得當日白皮書 PDF + Kaggle whitepaper URL + companion podcast（如有）
   - 在 `DayN/` 下建立 `source/`、`pipeline/`，依序執行：
     PDF → Markdown + 圖片擷取（docling 600 DPI）→ 分段翻譯 →
     圖片/佔位符對齊 → `md_to_html` skill 排版 → 對照 PDF double check →
     嵌入 podcast → 圖片壓縮（`compress_jpg.py --preserve-resolution`）
   - 完成後在 `DayN/` 寫一份 `README.md`，記錄流程與決策（給 DayN+1 參考）

2. **更新根目錄 `index.html` 的課程卡片**：
   - 找到 `#days` 區塊中對應 `DAY N` 的卡片
   - 將：
     ```html
     <div class="day-card is-soon">
       <div class="day-num">DAY N</div>
       <h4>...</h4>
       <p>...</p>
       <span class="badge-soon">即將推出</span>
     </div>
     ```
     改成：
     ```html
     <a class="day-card is-live" href="./DayN/index.html">
       <div class="day-num">DAY N</div>
       <h4>...</h4>
       <p>...</p>
     </a>
     ```
     （移除 `badge-soon`，標籤改為 `<a>`，class 改為 `is-live`）

3. **更新或維護 Capstone 頁面** (`capstone.html`)：
   - **更新截止時間**：找到 `<span>⏰ 截止：2026/07/06 23:59 PT</span>` 和 timeline 區塊，更新為新時間
   - **更新案例研究**：在 `.case-study-grid` 中修改或新增 `.case-card`（包含 emoji、標題、敘述、標籤）
   - **更新工具箱**：在 `.resource-grid` 中修改 `.resource-card` 的連結與名稱
   - **更新評分標準**：修改 `.rubric-table` 中的配分百分比或評分維度
   - **更新 FAQ**：在 `<dl class="faq">` 中增刪 `<dt>`/`<dd>` 對

4. **驗證**：
   - `python3 -m http.server <port>`（`file://` 協定下 Playwright 無法載入本機檔案）
   - 用 Playwright 開 `http://localhost:<port>/index.html`，確認：
     - console 無 error
     - Day1-N 卡片可點擊並正確導向 `DayN/index.html`
     - Capstone CTA 區塊可見，「查看 Capstone 專案 →」按鈕可點擊並導向 `./capstone.html`
     - `DayN/index.html` 的 sticky 目錄列最前方有「← 返回課程首頁」並可回到 `../index.html`
     - `capstone.html` 的頂部導覽有「← 回首頁」可回到 `./index.html`，footer 有 Day1-5 快速連結
     - 尚未完成的天數仍正確顯示「即將推出」（若適用）
   - 截圖 QA 後記得關閉伺服器並清除 `.playwright-mcp/` 暫存檔

---

## 參考資源

- **Day1 完整 pipeline 與逐句 prompt 紀錄**：`Day1/README.md`
  （含可重用腳本說明、6 條關鍵決策原則、Day1 熱門分享追蹤待辦）
- **Day2 完整 pipeline 與學習頻道導讀紀錄**：`Day2/README.md`
- **Day3 Agent Skills pipeline、Podcast 與兩個 Codelab 導讀紀錄**：`Day3/README.md`
- **Day4 規劃 scaffold 與 livestream 後補流程**：`Day4/README.md`
- **Kaggle 課程原頁**：
  https://www.kaggle.com/competitions/5-day-ai-agents-intensive-vibecoding-course-with-google/overview
