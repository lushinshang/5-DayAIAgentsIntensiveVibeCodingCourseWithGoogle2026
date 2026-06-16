# 5-Day AI Agents: Intensive Vibe Coding Course With Google（2026）— 中文學習筆記專案

## 摘要

本目錄是 Google × Kaggle「5-Day AI Agents: Intensive Vibe Coding Course With
Google」（2026/06/15–06/19）課程的中文學習筆記彙整站。`index.html` 為整個
專案的入口首頁（課程介紹 + Day1-5 導覽），每個 `DayN/` 子目錄則放該日白皮書
的繁體中文長文網頁（依 Day1 的 pipeline 製作）。

**目前狀態（2026-06-16）**：Day1、Day2 已完成並已連結；Day3-5 尚未建立，根目錄
`index.html` 中對應卡片顯示「即將推出」（灰階、不可點擊）。

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
└── Day2/
    ├── README.md       ← Day2 完整 pipeline 紀錄
    ├── index.html      ← Day2 白皮書中文長文網頁（最終產出）
    ├── source/         ← 原始 PDF + 中間產物
    ├── pipeline/       ← PDF→Markdown 轉換腳本
    ├── images_cht/     ← 8 張中文化圖表
    ├── antigravity-cli-guide/   ← 學習頻道導讀（deep-guide）
    ├── mcp-knowledge-guide/     ← 學習頻道導讀（deep-guide）
    └── *.mp4
```

`DayN/`（N=3~5）尚未建立，建立時請比照 `Day1/`、`Day2/` 的結構。

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

## 給下一位 AI 的接續指南：如何新增 Day2-5

1. **製作該日白皮書網頁**（比照 `Day1/README.md` 的完整 pipeline）：
   - 取得當日白皮書 PDF + Kaggle whitepaper URL + companion podcast（如有）
   - 在 `DayN/` 下建立 `source/`、`pipeline/`，依序執行：
     PDF → Markdown + 圖片擷取（docling 600 DPI）→ 分段翻譯 →
     圖片/佔位符對齊 → `md_to_html` skill 排版 → 對照 PDF double check →
     嵌入 podcast → 圖片壓縮（`compress_jpg.py --preserve-resolution`）
   - 完成後在 `DayN/` 寫一份 `README.md`，記錄流程與決策（給 DayN+1 參考）

2. **更新根目錄 `index.html`**：
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
     - 其餘天數仍正確顯示「即將推出」
   - 截圖 QA 後記得關閉伺服器並清除 `.playwright-mcp/` 暫存檔

---

## 參考資源

- **Day1 完整 pipeline 與逐句 prompt 紀錄**：`Day1/README.md`
  （含可重用腳本說明、6 條關鍵決策原則、Day1 熱門分享追蹤待辦）
- **Kaggle 課程原頁**：
  https://www.kaggle.com/competitions/5-day-ai-agents-intensive-vibecoding-course-with-google/overview
