# Day 1 — The New SDLC With Vibe Coding（伴隨 Vibe Coding 誕生的新一代 SDLC）

## 摘要

本目錄將 Google「5-Day AI Agents Intensive Course」Day 1 白皮書 PDF
（`The New SDLC With Vibe Coding_Day_1.pdf`），透過「PDF 解析 → 圖文擷取 →
分段翻譯 → 圖片/佔位符對齊 → HTML 排版（md_to_html skill）→ 對照 PDF 校對 →
嵌入 Podcast」的流程，產出可直接在瀏覽器開啟的繁體中文長文網頁
`index.html`，內含 9 張原文圖表與一支白皮書同步 Podcast 影片播放器。

**最終產出**：`index.html`（雙擊或本機伺服器開啟即可閱讀）。
**Day 2 可參考**：下方「給 Day 2 的流程建議」一節，整理了本次流程中
可重用的腳本、決策原則與常見坑點。

---

## 目錄結構

```
Day1/
├── README.md                                          ← 本檔案
├── index.html                                          ← 最終輸出（繁中網頁）
├── The New SDLC With Vibe Coding_Day_1_images/         ← index.html 使用的 9 張圖（600 DPI）
├── Whitepaper Companion Podcast..._compressed.mp4      ← index.html 嵌入的 podcast 影片
├── source/                                             ← 原始素材與中間產物
│   ├── The New SDLC With Vibe Coding_Day_1.pdf         ← 原文 PDF（白皮書正本）
│   ├── The New SDLC With Vibe Coding_Day_1.md          ← docling 解析出的英文 Markdown
│   ├── The New SDLC With Vibe Coding_Day_1_zh_TW.md    ← 分段翻譯後合併的繁中 Markdown
│   └── The New SDLC With Vibe Coding_Day_1_images_Origin/ ← 第一次 docling 擷取（解析度較低，已被 600 DPI 版本取代，僅供備查）
└── pipeline/                                           ← PDF → Markdown 轉換用腳本（含硬編碼路徑，重用前需修改）
    ├── convert_pdf.py        ← 第一版 docling 轉換（images_scale=3.0）
    ├── match_figures.py      ← 檢視 docling 解析出的圖片清單與對應頁碼，用於人工比對 Figure 編號
    ├── reprocess_600dpi.py   ← 正式版：以 600 DPI（images_scale=5.0）重新擷取 9 張圖，並依 Figure 標題重新命名、插入 {{filename}} 佔位符
    ├── post_process.py       ← （早期版本）依編號 mapping 重新整理 figure*.png 並插入 markdown 圖片參考，已被 reprocess_600dpi.py 取代
    ├── split_md.py           ← 將英文 Markdown 切成 4 個 chunk，交給翻譯 agent 分段翻譯
    └── merge_translation.py  ← 將 4 個翻譯後的 chunk 合併回單一 zh_TW.md
```

---

## 完整流程（Pipeline）

1. **PDF → Markdown + 圖片擷取**
   使用 `docling`（`pipeline/reprocess_600dpi.py`）以 600 DPI
   (`images_scale=5.0`) 解析 PDF，輸出：
   - `source/The New SDLC With Vibe Coding_Day_1.md`（英文 Markdown，含 `{{Figure N ...}}` 佔位符）
   - `The New SDLC With Vibe Coding_Day_1_images/`（9 張圖表 PNG，檔名與佔位符一致）

   `pipeline/match_figures.py` 用於人工核對 docling 解析出的圖片清單與
   PDF 中 "Figure N:" 文字的對應關係（決定哪些 picture index 是「真正的
   9 張圖表」、哪些是裝飾性切圖）。

2. **英文 Markdown 分段翻譯**
   `pipeline/split_md.py` 將英文 Markdown 切成 4 個 chunk →
   交給翻譯 agent 逐段翻成繁體中文 → `pipeline/merge_translation.py`
   合併為 `source/The New SDLC With Vibe Coding_Day_1_zh_TW.md`。

3. **圖片檔名與佔位符對齊**
   - 統一所有圖片副檔名為 `.png`（部分 docling 輸出為 `.jpeg`，需 `mv`
     改名以符合 `{{Figure N ...png}}` 佔位符）。
   - 用 `sed` 將 `{{Figure N ...}}` 轉成標準 Markdown 圖片語法：
     `![Figure N ...](images_dir/Figure N ....png)`。

4. **md_to_html skill → `index.html`**
   以 `/Users/lanss/.claude/skills/md_to_html` skill 為基礎，將
   `zh_TW.md` + 圖片目錄整理成單一 standalone HTML：
   - 繁中排版（Noto Sans TC、`#f9f7f4` 底色、`#1a1a1a` 文字）。
   - sticky 橫向捲動導覽列（10 個章節錨點）。
   - 9 張圖表以 `<figure class="section-figure">` 呈現，搭配
     click-to-enlarge lightbox（`img.currentSrc`）。
   - 表格、blockquote、自訂 `.stat-box`（呈現 "Agent = Model + Harness,
     ~10% / ~90%"）、`<pre><code>` 程式碼片段。
   - 32 條尾註逐條轉為 `<a target="_blank" rel="noopener">` 連結。
   - 以 `python3 -m html.parser` 驗證語法，並用 Playwright 在
     1280×900（桌面）與 390×844（手機）截圖 QA。

5. **對照原文 PDF 做內容 double check**
   逐節比對 `index.html` 中文內容 vs. `source/.../_Day_1.md`（英文）
   與 `source/.../_zh_TW.md`，找出「翻譯過程中不小心順手修正/潤飾」的
   段落，逐項詢問使用者決定是否改回原文用字。

6. **嵌入 Podcast**
   將白皮書同步 Podcast（`.mp4`，h264 1280x720 + AAC）以
   `<video controls preload="metadata">` 嵌入頁首，並在導覽列加上
   `#podcast` 錨點。檔名含空白，`src` 需做 `%20` URL encoding。

---

## 對話需求紀錄（依時間順序）

1. **初始需求**：「依據 PDF 和 Kaggle whitepaper URL，用 md_to_html 將
   `_zh_TW.md` 及圖片目錄整理為 `index.html`（圖片位置依 `{{Figure X}}`
   佔位符）。」並要求先「理解意圖、重述」。

2. **澄清決策**：
   - 圖片檔名/副檔名與佔位符不一致時 → **先用 `mv` 統一改副檔名**，
     讓檔名與 `{{Figure X ...}}` 完全一致。
   - **直接套用現有 `_zh_TW.md` 的翻譯內容**（不在轉換階段順手改字），
     待 HTML 完成後再與 PDF 做 double check。

3. **建置 `index.html`**：以 9 個 task（對應 9 個章節）逐段填入內容、
   插入圖片、建表格與 stat-box，並完成語法驗證與 Playwright 截圖 QA。

4. **PDF double check**：逐節比對中英文，發現兩處「轉換時順手修正」：
   - AI Agents 五要素段落：原文（英文 + zh_TW）皆寫「**四個**部分」，
     但前面條列 5 項（Model/Tools/Memory/Orchestration/Deployment）——
     原文本身存在「條列 5 項卻說 4 個」的矛盾。
     → **決策：改回「四個」**，忠實呈現原文（含其矛盾），不自行修正。
   - 結論章節「AI 是一個乘數」：zh_TW 原文用詞「乘加」，HTML 潤飾為
     「放大」。
     → **決策：保留「放大」**（較通順）。
   - 三處明顯 OCR/排版錯字修復（「の」→「的」、英文 "and"→「和」、
     「起手點」→「起點」）。
     → **決策：保留修正版本**。

5. **嵌入 Podcast**：將
   `Whitepaper Companion Podcast Introduction to Agents and Vibe Coding_compressed.mp4`
   加入 `index.html`，新增 `#podcast` 導覽錨點與 `<video controls>`
   播放器區塊，驗證語法並截圖確認顯示正常。

6. **本次：目錄整理 + README**：將原始素材／中間產物移入 `source/`，
   轉換腳本移入 `pipeline/`，最終輸出（`index.html`、圖片目錄、mp4）
   留在根目錄以維持相對路徑正確；撰寫本 README 作為 Day 2 參考。

---

## 給 Day 2 的流程建議

- **可重用的腳本**（在 `pipeline/`）：`reprocess_600dpi.py` 是目前最完整
  的 PDF→Markdown+圖片 流程版本（600 DPI、自動命名圖片、自動插入
  `{{filename}}` 佔位符）。重用時務必：
  - 修改腳本內硬編碼的 `base_dir` / `pdf_path` 路徑為 Day 2 的目錄。
  - 修改 `figure_info` mapping（docling 解析出的 picture index 會因
    PDF 不同而不同，需先用 `match_figures.py` 重新核對）。
  - `convert_pdf.py` / `post_process.py` 為較早期版本，已被
    `reprocess_600dpi.py` 取代，僅供參考不建議直接重用。
- **翻譯流程**：`split_md.py`（切 chunk）/ `merge_translation.py`
  （合併翻譯結果）中的路徑指向特定 agent session 的 scratch 目錄，
  屬一次性腳本，Day 2 需依當次 session 路徑調整或重寫。
- **關鍵決策原則**：
  1. 圖片檔名一律統一為 `.png`，且與 `{{Figure X ...}}` 佔位符**逐字一致**
     （含空格、大小寫），避免 HTML `<img src>` 對不上。
  2. 翻譯內容轉 HTML 時**先忠實套用既有翻譯，不要邊轉邊潤飾**；
     潤飾/修正留到最後「對照原文 double check」階段，逐項列出讓使用者決定。
  3. OCR 來源的 Markdown 會混入大量「圖表內部標籤文字」碎片
     （如孤立的英文單字、數字、箭頭符號），轉 HTML 時需人工判斷哪些是
     正文、哪些是圖表碎片並予以剔除，僅保留有代表性的數據點
     （例如「~10% Model / ~90% Harness」可轉成 `.stat-box`）。
  4. `file://` 協定下 Playwright 無法載入本機檔案，QA 截圖前需先
     `python3 -m http.server <port>`，截圖後記得關閉伺服器並清除
     `.playwright-mcp/` 與 `qa_*.png` 暫存檔。
  5. 影片/檔名含空白時，`<video src="...">` 需做 `%20` URL encoding。
