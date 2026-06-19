# 5-Day AI Agents: Intensive Vibe Coding Course With Google（2026）— 中文學習筆記專案

## 摘要

本目錄是 Google × Kaggle「5-Day AI Agents: Intensive Vibe Coding Course With
Google」（2026/06/15–06/19）課程的中文學習筆記彙整站。`index.html` 為整個
專案的入口首頁（課程介紹 + Day1-5 導覽），每個 `DayN/` 子目錄則放該日白皮書
的繁體中文長文網頁（依 Day1 的 pipeline 製作）。

**目前狀態（2026-06-19）**：Day1–Day5 全部完成並已連結。
根目錄 `index.html` 中 Day1–Day5 卡片全部為 `is-live`（可點擊）。課程五天白皮書中文學習頁製作完成。

**近期更新紀錄（2026-06-19）**：
- Day5 主頁（`Day5/index.html`）製作完成，主題：規格驅動生產級開發（SDD）。
- 已將根目錄 `index.html` 的 Day5 卡片從 `is-soon` 改為 `is-live`，連結至 `./Day5/index.html`。
- Day5 學習頻道三頁均已完成：Podcast 深度導讀、Codelab 1（Agent Runtime 部署）、Codelab 2（Vibecode 前端）。
- Day5 包含：1 張中文化 Figure（imagegen text-localization）、7 個 Snippets、17 條 Endnotes，以及 7 張已生成並通過桌機／手機 QA 的繁中資訊圖。
- Day1–Day5 都具備首頁 → Day 頁、Day 頁 → 首頁的雙向導覽；Day5 回程會定位至首頁的 Day5 卡片。

**舊紀錄（2026-06-17）**：
- 已確認根目錄 `index.html` 的 Day3 卡片為 live link，連到 `./Day3/index.html`。
- 已在 `Day2/index.html` 與 `Day3/index.html` 的 sticky 目錄列最前方補上
  `../index.html` 回首頁連結，文字為「← 返回課程首頁」；Day1 原本已有同樣連結。
- 已建立 `Day4/README.md`、`source/`、`pipeline/`、`images_cht/`、
  `podcast-deep-guide/`、`source/codelabs/`、`source/podcast/`、
  `source/livestream/` 與 `day4-deep-guide/`，作為 Day4 後續製作 scaffold。

---

## 目錄結構

```
.
├── README.md          ← 本檔案（專案總覽 + 接續指南）
├── index.html         ← 入口首頁：Kaggle 課程介紹（中文）+ Day1-5 導覽卡片
├── Day1/
│   ├── README.md       ← Day1 完整 pipeline 紀錄
│   ├── index.html      ← Day1 白皮書中文長文網頁（最終產出）
│   ├── source/         ← 原始 PDF + 中間產物
│   ├── pipeline/       ← PDF→Markdown 轉換腳本
│   └── ...guides/, *.mp4
├── Day2/
│   ├── README.md       ← Day2 完整 pipeline 紀錄
│   ├── index.html      ← Day2 白皮書中文長文網頁（最終產出）
│   ├── source/         ← 原始 PDF + 中間產物
│   ├── pipeline/       ← PDF→Markdown 轉換腳本
│   ├── images_cht/     ← 8 張中文化圖表
│   ├── antigravity-cli-guide/   ← 學習頻道導讀（deep-guide）
│   ├── mcp-knowledge-guide/     ← 學習頻道導讀（deep-guide）
│   └── *.mp4
├── Day3/
│   ├── README.md       ← Day3 完整 pipeline 紀錄
│   ├── index.html      ← Day3 白皮書中文長文網頁（最終產出）
│   ├── source/         ← 原始 PDF + 中英文 Markdown + 圖片中間產物
│   │   ├── codelabs/   ← 兩個官方 Codelab HTML snapshot
│   │   └── podcast/    ← Podcast 原始英文 SRT
│   ├── pipeline/       ← PDF 解析、圖表擷取、圖表中文化、Podcast 導讀腳本
│   ├── images_cht/     ← 11 張中文化圖表
│   ├── antigravity-skills-guide/ ← Antigravity Skills Codelab 深度導讀
│   ├── agents-cli-adk-guide/     ← Agents CLI + ADK Codelab 深度導讀
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
  常見問題 → 引用資訊。
- 原始來源：
  https://www.kaggle.com/competitions/5-day-ai-agents-intensive-vibecoding-course-with-google/overview
  （此頁為 SPA，`WebFetch` 抓不到內容，需用 Playwright 開瀏覽器等 JS render
  後讀 accessibility snapshot。）
- 「課程進度導覽」區塊（`#days`）是 Day1-5 的卡片：
  - 已完成的天數：`<a class="day-card is-live" href="./DayN/index.html">`
  - 未完成的天數：`<div class="day-card is-soon">...<span class="badge-soon">即將推出</span></div>`
- 配色與字型沿用 `Day1/index.html` 的 `:root` CSS 變數（`--accent:#a8554a`、
  `--bg:#f9f7f4`、Noto Sans TC），維持全站視覺一致。

---

## 後續維護指南

Day1–Day5 均已完成。若後續要重製既有頁面、補充學習頻道，或將此流程套用到新課程，可依下列方式維護。

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

3. **驗證**：
   - `python3 -m http.server <port>`（`file://` 協定下 Playwright 無法載入本機檔案）
   - 用 Playwright 開 `http://localhost:<port>/index.html`，確認：
     - console 無 error
     - Day1-N 卡片可點擊並正確導向 `DayN/index.html`
     - `DayN/index.html` 的 sticky 目錄列最前方有「← 返回課程首頁」並可回到 `../index.html`
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
