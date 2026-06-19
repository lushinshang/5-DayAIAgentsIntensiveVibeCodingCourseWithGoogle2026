# Day 1 — The New SDLC With Vibe Coding（伴隨 Vibe Coding 誕生的新一代 SDLC）

## 摘要

本目錄將 Google「5-Day AI Agents Intensive Course」Day 1 白皮書 PDF
（`The New SDLC With Vibe Coding_Day_1.pdf`），透過「PDF 解析 → 圖文擷取 →
分段翻譯 → 圖片/佔位符對齊 → HTML 排版（md_to_html skill）→ 對照 PDF 校對 →
圖片壓縮」的流程，產出可直接在瀏覽器開啟的繁體中文長文網頁
`index.html`，內含 9 張原文圖表（已壓縮）。

白皮書同步 Podcast 影片播放器已移至 `podcast-deep-guide/podcast-deep-guide.html` 頂端；
Day 1 直播錄影播放器位於 `day1-deep-guide/index.html` 頂端（Hero 正下方）。

另外，本目錄也補充整理了 2 份 Day 1 相關 Google Codelabs，皆採用
「讀取官方網頁 → deep-guide 白話繁中導讀 Markdown → md-to-phtml
轉為 standalone HTML → Playwright 桌機/手機截圖 QA」流程，分別存放於：

- `google-antigravity-codelab-guide/`
- `deploy-aistudio-to-cloud-run-guide/`

**最終產出**：`index.html`（雙擊或本機伺服器開啟即可閱讀）。
**Day 2 可參考**：下方「給 Day 2 的流程建議」一節，整理了本次流程中
可重用的腳本、決策原則與常見坑點。

---

## 目錄結構

```
Day1/
├── README.md                                          ← 本檔案
├── index.html                                         ← 主入口網頁（白皮書繁中版 + 學習/推薦頻道）
├── google-antigravity-codelab-guide/                  ← Google Antigravity codelab 白話導讀
│   ├── google-antigravity-codelab-guide.md
│   ├── google-antigravity-codelab-guide.normalized.md
│   ├── google-antigravity-codelab-guide.html
│   ├── build_html.py
│   ├── desktop.png
│   └── mobile.png
├── deploy-aistudio-to-cloud-run-guide/                ← AI Studio → Cloud Run codelab 白話導讀
│   ├── deploy-aistudio-to-cloud-run-guide.md
│   ├── deploy-aistudio-to-cloud-run-guide.normalized.md
│   ├── deploy-aistudio-to-cloud-run-guide.html
│   ├── build_html.py
│   ├── desktop.png
│   └── mobile.png
├── podcast-deep-guide/                                ← Podcast 白皮書深度導讀
│   ├── podcast-deep-guide.md                          ← 繁中主題式導讀 Markdown
│   └── podcast-deep-guide.html                        ← Standalone HTML（含英文逐字稿附錄）
├── day1-deep-guide/                                   ← Day 1 直播深度導讀（deep-guide + ai-mentor-agents）
│   ├── index.html                                     ← Standalone HTML（含 7 位講者識別逐字稿）
│   └── images/                                        ← Codex CLI 生成圖片（各 16:9 + 9:16 行動版）
│       ├── summary.png / summary-mobile.png           ← 全文摘要手寫筆記 banner
│       ├── vibe-vs-agentic.png / …-mobile.png         ← Vibe Coding vs Agentic Engineering 比較圖
│       └── harness.png / harness-mobile.png           ← Agent = Model + Harness 公式圖
├── Promo_Channel/                                     ← 推薦頻道素材
│   └── Day1.jpg                                       ← 歐罵罵推薦頻道首頁圖
├── The New SDLC With Vibe Coding_Day_1_images/        ← index.html 使用的 9 張圖（600 DPI 壓縮版）
├── source/                                            ← 原始素材與中間產物
│   ├── The New SDLC With Vibe Coding_Day_1.pdf        ← 原文 PDF（白皮書正本）
│   ├── The New SDLC With Vibe Coding_Day_1.md         ← docling 解析出的英文 Markdown
│   ├── The New SDLC With Vibe Coding_Day_1_zh_TW.md   ← 分段翻譯後合併的繁中 Markdown
│   ├── The New SDLC With Vibe Coding_Day_1_images_Origin/ ← 第一次 docling 擷取（低解析度備查）
│   ├── podcast/                                       ← Podcast 逐字稿與影音相關素材
│   │   └── Whitepaper Companion Podcast Introduction to Agents and Vibe Coding.en-orig.srt
│   ├── podcast/                                       ← Podcast 逐字稿與影音相關素材
│   │   ├── Whitepaper Companion Podcast Introduction to Agents and Vibe Coding.en-orig.srt
│   │   └── Whitepaper Companion Podcast..._compressed.mp4  ← podcast-deep-guide.html 嵌入的影片
│   └── livestream/                                    ← Day 1 直播原始素材
│       ├── DAY 1 Livestream - 5-Day AI Agents Intensive Vibe Coding Course With Google.en-orig.srt
│       ├── DAY 1 Livestream..._compressed.mp4         ← 本地備份（HTML 使用 GitHub Releases URL）
│       ├── day1-transcript.txt                        ← 去除 SRT 時間戳的純文字逐字稿
│       └── day1-deep-guide.md                         ← 深度導讀 Markdown 草稿
└── pipeline/                                          ← PDF → Markdown 轉換用腳本
    ├── convert_pdf.py
    ├── match_figures.py
    ├── reprocess_600dpi.py
    ├── post_process.py
    ├── split_md.py
    └── merge_translation.py
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
   `<video controls preload="metadata">` 嵌入 `index.html` 頁首（初始版本）。
   後來將播放器**移至 `podcast-deep-guide/podcast-deep-guide.html` 頂端**
   （Hero 正下方），並從 `index.html` 移除 `#podcast` 區塊、nav 連結與對應 CSS，
   讓主頁保持乾淨，播放功能集中在導讀頁面。
   檔名含空白，`src` 需做 `%20` URL encoding。

7. **圖片壓縮**
   600 DPI 擷取出的 9 張 PNG 原始檔每張約 4.5–5.9MB（總計 ~90MB），
   使用 `/Users/lanss/projects/2_Practice/readpaper/compress_jpg.py
   --preserve-resolution`（無損 PNG 壓縮：256 色調色盤 + Floyd-Steinberg
   抖色 → optipng/pillow 重壓縮）逐檔壓縮並覆蓋原檔，**解析度不變**，
   總大小降至約 11MB（各檔約 160KB–2.5MB）。壓縮後重新驗證
   `index.html` 語法並以 Playwright 截圖確認圖片清晰度。

8. **補充 Google Codelabs 導讀**
   使用者提供 2 個 Day 1 相關 codelab URL，要求以相同做法整理：
   - `https://codelabs.developers.google.com/getting-started-google-antigravity`
   - `https://codelabs.developers.google.com/deploy-from-aistudio-to-run`

   執行流程：
   - 以網頁讀取工具取得官方 codelab 全文與章節結構。
   - 使用 `deep-guide` 風格改寫為白話易懂的繁體中文 Markdown，重點不是逐字翻譯，
     而是整理「為什麼這些步驟重要、怎麼操作、實務上要注意什麼」。
   - 在 `Day1/` 下建立獨立子目錄，避免混入白皮書主頁素材。
   - 用 `md-to-phtml` 流程執行中文標點正規化：
     `normalize_punctuation.py <article>.md -o <article>.normalized.md`
   - 建立各自的 `build_html.py`，將正規化後 Markdown 轉為可直接開啟的
     standalone HTML；包含文章 hero、sticky 橫向章節導覽、閱讀卡片、
     code block、blockquote、桌機/手機響應式排版。
   - 以 `python3 -m html.parser <output>.html` 驗證 HTML 語法。
   - 用 Playwright 產生 `desktop.png` 與 `mobile.png` 截圖 QA。

   QA 中發現並修正的問題：
   - `google-antigravity-codelab-guide`：手機版來源網址太長造成卡片溢出，
     在 article CSS 補上 `overflow-wrap: anywhere`，並讓 `pre` 維持
     `overflow-wrap: normal`。
   - `deploy-aistudio-to-cloud-run-guide`：中文標點正規化會把 Markdown ordered
     list 的 `1.` 轉成 `1。`，導致轉換器沒有辨識清單；已修改 `build_html.py`
     的 ordered-list regex，同時支援 `1.` 與 `1。`。

    產出：
    - `google-antigravity-codelab-guide/google-antigravity-codelab-guide.html`
    - `deploy-aistudio-to-cloud-run-guide/deploy-aistudio-to-cloud-run-guide.html`

9. **學習與推薦頻道資源整合**
   - 於主頁 [index.html](file:///Users/lanss/projects/2_Practice/5-Day%20AI%20Agents%20Intensive%20Course%20with%20Google(2026)/Day1/index.html) 設計並新增了資源頻道卡片區塊（學習與推薦頻道各二個），搭配微陰影、滑過浮起動畫，並在導覽列（TOC）加入「資源頻道」跳轉錨點。
   - 為了維護瀏覽體驗，修改了兩份 Codelabs 的 HTML 導讀頁面，在其頂部導覽列最左側新增「← 返回白皮書首頁」按鈕，指向 `../index.html`。
   - 採用 `python3 -m html.parser` 對所有 HTML 進行語法校對以確保網頁結構合規。

10. **Podcast 白皮書深度導讀**
    - 讀取 `source/podcast/Whitepaper Companion Podcast Introduction to Agents and Vibe Coding.en-orig.srt`（1001 行，250 個字幕段落，21 分鐘）全文。
    - 以 `ai-mentor` 動態路由框架（產業報告維度）+ `deepguide` 5 段式隱形大師敘事結構，產出流暢繁中主題式導讀文章（`podcast-deep-guide/podcast-deep-guide.md`）。
    - 以 `md_to_html` 排版規範建立 `podcast-deep-guide.html`：sticky 橫向導覽列（8 個章節錨點）、莫蘭迪暖色系、表格、blockquote、callout 卡片、頁底附錄（摺疊式 `<details>` 展示英文原文逐字稿，一字未改，僅做段落化整理）。
    - 同步將 `podcast-deep-guide` 加入 `index.html` 學習頻道（第三張卡片）。
    - 採用 `python3 -m html.parser` 驗證兩個 HTML 語法正確。

11. **Day 1 直播深度導讀（day1-deep-guide）**
    - 建立全域 skill `ai-mentor-agents`（`~/.claude/skills/ai-mentor-agents/`），參考 `ai-mentor.skill` 結構，融合 10 位 AI Agents 實踐者人格（Karpathy、Andrew Ng、Logan/DeepMind、李宏毅等），並定義教學六段式格式（📌定義→💡比喻→🔧技術→🏭實戰→⚠️誤解→🧪驗證）。
    - 以 `grep` 過濾 SRT 時間戳，產出純文字逐字稿 `source/livestream/day1-transcript.txt`（357 行、47KB）。
    - 同時啟用 `deep-guide`（敘事層：流動論述、強烈開場、章節邏輯連結）與 `ai-mentor-agents`（教學層：callout 框）撰寫導讀文章，存入 `source/livestream/day1-deep-guide.md`，共 10 章節，核心命題：「實作的能力不再是瓶頸；規格的品質，才是新的瓶頸。」
    - 以 `md_to_html` 流程建立 `day1-deep-guide/index.html`：
      - Codex CLI 生成 3 組共 6 張資訊圖（手寫筆記風摘要 banner、Vibe vs Agentic 比較圖、Agent Harness 公式圖，各含 16:9 桌機版與 9:16 行動版）。
      - `<picture>` + CSS `aspect-ratio` 切換桌機/行動圖片版本，所有圖片支援 lightbox 點擊放大。
      - 4 種 callout 色系（藍/綠/紅/黃）對應 📌💡⚠️🧪 四類 ai-mentor 教學元素。
      - 新增含講者識別的摺疊逐字稿區塊（`<details>`）：Python 腳本依 `>>` 切換符號與稱謂關鍵字，自動為 7 位 Google 講者標注色系 badge（Smitha/Anand/Logan/Partha/Jamie/Sham/Fran）。
    - 整合進主入口：`index.html` 學習頻道新增「🎬 Day 1 直播深度導讀」卡片；`day1-deep-guide/index.html` 導覽列新增「← 返回 Day 1」連結。
    - 根目錄整理：SRT、純文字逐字稿、Markdown 草稿移入 `source/livestream/`。
    - `python3 -m html.parser` 驗證語法，Playwright 截圖 QA（桌機 1280px + 行動 390px）。
    - **影片播放器位置調整（後續）**：
      - Day 1 直播錄影（GitHub Releases MP4）播放器移至 `day1-deep-guide/index.html` Hero 正下方（頂端）。
      - Podcast 播放器移至 `podcast-deep-guide/podcast-deep-guide.html` Hero 正下方（頂端）。
      - `index.html` 的 `#podcast` 影片區塊、nav 連結、對應 CSS 一併移除，主頁改為純導覽入口。

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

6. **目錄整理 + README**：將原始素材／中間產物移入 `source/`，
   轉換腳本移入 `pipeline/`，最終輸出（`index.html`、圖片目錄、mp4）
   留在根目錄以維持相對路徑正確；撰寫本 README 作為 Day 2 參考。

7. **圖片壓縮**：`The New SDLC With Vibe Coding_Day_1_images/` 內 9 張圖
   檔太大（~90MB），要求用 `readpaper/compress_jpg.py` 壓縮並覆蓋原檔。
   該腳本提供兩種模式：
   - `--preserve-resolution`：保留原解析度，用 256 色調色盤 + 抖色，
     每張約 2.4MB（總計 ~22MB），背景會出現輕微網點抖色噪點。
   - 預設模式：解析度降至 ~50% + 32 色調色盤，每張約 850KB
     （總計 ~7.7MB），但 lightbox 放大時文字較模糊、色彩更失真。
   → **決策：選擇 `--preserve-resolution`**（保留解析度與文字銳利度，
     接受些微抖色噪點），實測總大小降至 ~11MB。

---

## 待辦：Day 1 熱門分享追蹤（2026-06-15 記錄）

2026 課程於 **2026-06-15 ~ 06-19** 進行，本白皮書即 2026 版 Day 1
（"Introduction to Agents & Vibe Coding"）。記錄當天搜尋結果，**之後可
回來複查**是否有更完整的心得/分享：

- 2026-06-15（Day 1 剛開始）搜尋時，多數 GitHub repo 都只有初始 commit
  或空白 README，尚無實質心得內容。較活躍的幾個：
  - [divya-gh/5Day_AI_Agents_Intensive_Vibe_Coding_Course_With_Google](https://github.com/divya-gh/5Day_AI_Agents_Intensive_Vibe_Coding_Course_With_Google)
  - [StevenTapscott/Kaggle-AI-Agents](https://github.com/StevenTapscott/Kaggle-AI-Agents)（規劃了 `Day01/Whitepaper-Notes.md`）
  - [Shibu4064/5-Day-AI-Agents-Intensive-Vibe-Coding-Course-With-Google](https://github.com/Shibu4064/5-Day-AI-Agents-Intensive-Vibe-Coding-Course-With-Google)
  - [PhamQuangSon/5-day-ai-agent](https://github.com/PhamQuangSon/5-day-ai-agent)
  - [Reefat004/Google-AI-Agents-Course](https://github.com/Reefat004/Google-AI-Agents-Course)
  - [AnhQuoc1234/5-Day-AI-Agents](https://github.com/AnhQuoc1234/5-Day-AI-Agents)
- Kaggle Discord 有專屬頻道供學員交流，但**訊息不被搜尋引擎索引**，需
  直接登入 Discord 查看：[Join the new AI Agents Vibe Coding Course](https://blog.google/innovation-and-ai/technology/developers-tools/kaggle-genai-intensive-course-vibe-coding-june-2026/)
- **建議**：Day 1 截止日（約 06-16）之後，重新用
  `gh search repos "5-Day AI Agents Intensive" --sort updated` 搜尋，
  屆時內容會比較完整。

---

## 附錄：原始 Prompt 逐句紀錄（供 Day 2-5 複用）

以下依時間順序列出本次對話中使用者實際下的指令原文（前 2 則因跨越對話
壓縮，僅能還原大意，其餘為逐字紀錄）。Day 2-5 可參考相同句式直接下指令。

1. （初次需求，大意）依據 PDF 和 Kaggle whitepaper 網址，用 `md_to_html`
   skill 將 `_zh_TW.md` 翻譯內容與圖片目錄整理為 `index.html`，圖片位置
   依 `{{Figure X ...}}` 佔位符對應；並要求先理解意圖、重述再開始。

2. （建置過程中的澄清，大意）圖片檔名與佔位符不一致時，先用 `mv` 統一
   副檔名對齊佔位符；翻譯內容直接套用 `_zh_TW.md` 既有文字，不要邊轉邊
   潤飾，潤飾留到最後 double check 階段。

3. 「拿原文 PDF做內容 double check」

4. 「Whitepaper Companion Podcast Introduction to Agents and Vibe Coding_compressed.mp4為這個白皮書的podcast，html找一個地方協助播放」

5. 「將這個目錄做整理收納，並就起到迄今所有需求全部都做成readme.md，開頭是摘要。我希望可以讓Day2作爲參考」

6. 「The New SDLC With Vibe Coding_Day_1_images內的圖檔太大，以readpaper下的compress_jpg.py壓縮，並覆蓋原檔案」

7. 「source下有原始圖檔，請檢查」

8. 「原來的中文圖不滿意，啟動codex cli重新生圖，提示詞為「圖片內容翻譯為台灣IT人員常用語繁體中文，重新生圖」，生完的圖檔檔名和原圖檔一致，存到「The New SDLC With Vibe Coding_Day_1_images」目錄」
   （後接「理解我的意圖，重述」——要求先重述再執行；使用者後續回覆已自行完成此項處理，故本次對話未實際執行。）

9. 「我已經完成圖檔的處理了
   另外
   用deepresearch從discord的Kaggle頻道尋找有沒有關於5-Day的第一天熱門分享」

10. 「主要是for今年的，不是去年的，或者看看github」

11. 「幫我注記在readme.md，以後回來可以查查」

12. 「從一開始到目前的prompt都記錄在readme.md，為了後面的四天可以當作參考」（本項）

13. 「read https://codelabs.developers.google.com/getting-started-google-antigravity」
    → 先讀取 Google Antigravity codelab，確認主題、章節與重點。

14. 「這一個網頁總共有10步驟，是嗎」
    → 回覆該 codelab 共有 10 個章節：
    Introduction、Installation、Antigravity Interface、Slash Commands、
    Scheduling Commands、MCP Servers、Artifacts、Antigravity IDE、Skills、
    Conclusion。

15. 「use deepduide將這個網頁的內容整理成md，要白話易懂，然後用md-to-phtml轉為html」
    → 使用者隨即中斷此輪，未完成產出。

16. 「use deepduide將這個網頁的內容整理成md，要白話易懂，然後用md-to-phtml轉為html，在Day1下建立一個適當的目錄，存入」
    → 實際執行：
    - 使用 `deep-guide` 將 Antigravity codelab 整理成白話繁中 Markdown。
    - 使用 `md-to-phtml` 流程轉為 standalone HTML。
    - 建立 `Day1/google-antigravity-codelab-guide/`。
    - 產出 Markdown、normalized Markdown、HTML、`build_html.py`、桌機/手機截圖。
    - 以 `python3 -m html.parser` 驗證，並用 Playwright 截圖 QA。

17. 「還有一個也是一樣做法「https://codelabs.developers.google.com/deploy-from-aistudio-to-run」
    也是在Day1下建立一個適當的目錄放入」
    → 實際執行：
    - 讀取「Deploy from AI Studio to Cloud Run」codelab。
    - 整理成白話繁中 Markdown，主線是 AI Studio vibe coding 原型、
      Cloud Run 部署、Unpublish 清理資源。
    - 建立 `Day1/deploy-aistudio-to-cloud-run-guide/`。
    - 產出 Markdown、normalized Markdown、HTML、`build_html.py`、桌機/手機截圖。
    - 修正 ordered list 因中文標點正規化造成的解析問題。

18. 「執行過程補充到Day1的readme.md」
    → 將兩份 codelab 的產出目錄、處理流程、QA 修正事項與 prompt 紀錄補入本檔案。

19. 「執行幾件事情：
    1. index.html新增兩個學習頻道，連接到「deploy-aistudio-to-cloud-run-guide」和「google-antigravity-codelab-guide」的html，而這兩個地方的html也要新增一個返回上一頁的按鈕
    2. 新增兩個推薦頻道，一個是歐罵罵，一個是阿魁。前者連到Promo_Channel的Day1.jpg，後者連到「https://meta-ghost.notion.site/Vibe-Coding-AI-3807b792315a8114a299c0bb609634c7?source=copy_link」
    ok，先確認jpg的存在，然後依規劃執行」
    → 實際執行：
    - 確認 `Promo_Channel/Day1.jpg` 確實存在於 `Day1/Promo_Channel/Day1.jpg`。
    - 修改兩份 Codelabs HTML 頁面，在其頂部 `<nav>` 導覽列最左側新增「← 返回白皮書首頁」連結。
    - 修改 `index.html`，於 `<style>` 中加入 `.channels-section` 的卡片式樣式，並於 `<nav class="toc">` 加入「資源頻道」跳轉連結。同時在 Podcast 區塊下方、`<main>` 之前插入全新的 `#channels` 區塊，提供雙欄（行動裝置為單欄）卡片設計，滑過時有微陰影與浮起特效。
    - 採用 `python3 -m html.parser` 驗證三個修改後的 HTML 檔案皆語意正確。

20. 「繼續更新readme.md」
    → 實際執行：
    - 更新 `README.md` 的目錄結構，加入 `Promo_Channel/Day1.jpg`。
    - 於「完整流程（Pipeline）」中新增步驟 9「學習與推薦頻道資源整合」，完整寫下 HTML 卡片區塊、返回按鈕實作與 HTML 語意校對。
    - 將此 Prompt 紀錄補入對話歷史。
21. 「我在source下建立的一個podcast the directory，放個podcast的逐字稿srt」
    → 實際執行：
    - 更新 `README.md` 的目錄結構樹，在 `source/` 底下新增 `podcast/` 目錄與英文原始逐字稿 `Whitepaper Companion Podcast Introduction to Agents and Vibe Coding.en-orig.srt`。
    - 將此紀錄更新於對話歷史中，並向使用者回報與提問下一步的逐字稿處理（如翻譯或字幕軌掛載）。

22. 「參考claude code的skills建立agy的deepguide and md_to_html這兩個skill」
    → 實際執行：
    - 將 Claude 的 `md_to_html` 技能目錄及其子檔案複製至 `/Users/lanss/.gemini/skills/md_to_html`。
    - 將目前的 `/Users/lanss/.gemini/skills/deep-guide` 目錄複製至 `/Users/lanss/.gemini/skills/deepguide`。
    - 修改 `/Users/lanss/.gemini/skills/deepguide/SKILL.md` 中 frontmatter 的名稱為 `deepguide`。
    - 確認 `codex_imagegen.py` 與 `normalize_punctuation.py` 被順利複製且不包含寫死路徑。

23. 「我的skill是要全域的」
    → 實際執行：
24. 「參考https://www.youtube.com/watch?v=cbzmr7vt4XA及其背景資訊，以ai-mentor and deepguide skill將其逐字稿實施主題式導讀，建立一個適當的目錄存入。接著以md_to_html建立html。（理解我的意圖，重述）」
    → 重述後確認規劃：讀取 SRT 全文，用 ai-mentor 分析主題，deepguide 產出導讀文章，md_to_html 建立 HTML，HTML 最後以 `<details>` 附上原文逐字稿（段落化，一字不改）。

26. 「推薦頻道新增保哥（https://doggy8088.github.io/the-new-sdlc-with-vibe-coding/index.html）」
    → 實際執行：
    - 在 `index.html` 推薦頻道區塊的阿魁卡片後方，新增保哥卡片（🐕 圖示），
      連結指向 `https://doggy8088.github.io/the-new-sdlc-with-vibe-coding/index.html`。
    - `python3 -m html.parser` 驗證語法正確。
    - 更新 README.md 對話歷史。

27. 「read DAY 1 Livestream - 5-Day AI Agents Intensive Vibe Coding Course With Google.en-orig.srt，如果要比照podcast的導讀，應該要怎麼下指令？」
    → 分析 SRT 格式（357 行純文字、47KB），說明兩種方式：先萃取純文字再下 deep-guide 指令（推薦），或直接貼文字。

28. 「幫我執行方式一」
    → 萃取 SRT 純文字（`day1-transcript.txt`），讀取全文後呼叫 deep-guide skill 撰寫導讀文章。

29. 「除了deepguide外，也請加入ai-mentor（請參考codex cli的ai-mentor skill，建立自己的）」
    → 解壓縮 `ai-mentor.skill` 讀取結構（iPAS 考試準備導師），並建立全域 `ai-mentor-agents` skill（`~/.claude/skills/ai-mentor-agents/`），融合 10 位 AI Agents 實踐者，含 SKILL.md 與 references/experts.md。接著合體 deep-guide + ai-mentor-agents 撰寫完整導讀，存入 `source/livestream/day1-deep-guide.md`。

30. 「執行 /md_to_html 將文章轉為網頁」
    → 以 `md_to_html` skill 執行完整流程：Codex CLI 生成 3 組 6 張資訊圖（各 16:9 + 9:16）、建置 `day1-deep-guide/index.html`、語法驗證、Playwright 截圖 QA。

31. 「這個html也是從srt整理出來的，所以應該仿照podcast導讀也放逐字稿（而且逐字稿應該要辨識講者）」
    → 撰寫 Python 腳本依 `>>` 切換符號與稱謂關鍵字識別 7 位 Google 講者，為每位講者設定色系 badge，注入摺疊式逐字稿區塊至 `day1-deep-guide/index.html`。

32. 「1. 與podcast導讀一樣整併到day1/index.html，並且有回到上一頁功能
    2. day1根目錄的檔案參考目錄架構收納整理
    3. 更新readme」
    → 本次執行（見 Pipeline 步驟 11）。

33. 「我有將livestream放到 GitHub Releases URL，請仿照podcast幫我建立播放功能」
    → 在 `day1-deep-guide/index.html` 文章底部新增 `<section id="livestream">` 影片播放器，
      nav 加入「直播影片」錨點，CSS 樣式與 podcast 區塊一致。

34. 「1. 直播影片放html頂端 2. podcast影片也放到podcast導讀的html頂端」
    → 將 `day1-deep-guide/index.html` 的直播影片 section 從文章底部移至 Hero 正下方，
      調整 CSS（移除 `border-top`，改為底部 margin）；
      在 `podcast-deep-guide/podcast-deep-guide.html` Hero 後插入 Podcast 影片區塊（加對應 CSS）。

35. 「既然移到了podcast導讀的html了，day1的html影片播放可以拿掉」
    → 從 `index.html` 移除 `<section id="podcast">` 影片區塊、nav 的「同步 Podcast」連結、
      及 `.podcast` / `.podcast-inner` / `.podcast video` CSS，主頁改為純導覽頁面。

36. 「更新 README 反映這個變更」
    → 更新摘要、目錄結構說明、Pipeline 步驟 6 與 11，並補充對話需求紀錄 33–36。

37. 「mp4應該要移動到適合的目錄」
    → 將兩支 MP4 從根目錄移入對應 `source/` 子目錄：
      - Podcast MP4 → `source/podcast/`（與 SRT 同目錄）
      - 直播 MP4 → `source/livestream/`（與 SRT 及逐字稿同目錄）
    → 更新 `podcast-deep-guide.html` 的 `<video src>` 路徑（`../` 改為 `../source/podcast/`）。
    → 更新 README 目錄結構，移除根目錄的 MP4 條目，補充至各 `source/` 子目錄。

25. 「補充需求，html最後提供不改字，優化段落形式的逐字稿」 → 「yes」
    → 實際執行：
    - 讀取 SRT 逐字稿全文（1001 行，250 段，21 分鐘）。
    - 以 `ai-mentor`（產業報告/商業戰略維度）分析主題：Vibe Coding vs. Agentic Engineering、Context 工程六要素、Context Rot、Harness = 90%、指揮者/編排者模式、80% 問題、Token 經濟學、師徒斷層。
    - 以 `deepguide` 5 段式隱形大師結構，產出流暢繁中主題式導讀 Markdown 文章，存入 `Day1/podcast-deep-guide/podcast-deep-guide.md`。
    - 以 `md_to_html` 規範建立 `podcast-deep-guide.html`：sticky 導覽列（8 個錨點 + 返回首頁）、莫蘭迪暖色系、六欄 Context 比較表、blockquote 金句框、callout 卡片；頁底以 `<details class="transcript-toggle">` 展示完整英文原文逐字稿（一字未改，僅去除時間戳記、SRT 序號，依語意合併為段落）。
    - 同步將 `podcast-deep-guide` 加入 `index.html` 學習頻道（🎙️ 第三張卡片）。
    - `python3 -m html.parser` 驗證 `podcast-deep-guide.html` 與更新後的 `index.html` 語法均正確。
    - 更新 README.md 目錄結構樹（新增 `podcast-deep-guide/`）、Pipeline 步驟 10、對話歷史。

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
  6. docling 高解析度（600 DPI）擷取出的圖檔通常每張數 MB，發佈前用
     `/Users/lanss/projects/2_Practice/readpaper/compress_jpg.py
     --preserve-resolution <file> -o <file>` 逐張壓縮並覆蓋，可在不
      改變解析度與檔名（不影響 `<img src>`）的情況下大幅縮小檔案。
  6. 影片/檔名含空白時，`<video src="...">` 需做 `%20` URL encoding。

---

## 更新紀錄

### 阿魁頻道卡片修正（2026-06-17）

**問題說明**：阿魁的分享分為兩種類型，Day1 原本只有「筆記」卡片，缺少「直播導讀」卡片。
Day2 / Day3 的直播導讀 URL 各錯位一天（Day2 放了 Day1 的、Day3 放了 Day2 的）。

**修正內容**：

- `Day1/index.html`
  - 原有阿魁卡片標題改為「阿魁｜筆記」，URL 不變
  - 新增「阿魁｜直播導讀」卡片（🎥），URL：
    `https://meta-ghost.notion.site/Vibe-Coding-Agent-Engineering-AI-code-3817b792315a8174b658e0fac71f556d`

- `Day2/index.html`
  - 阿魁卡片 URL 由 Day1 直播導讀改為 Day2 直播導讀：
    `https://meta-ghost.notion.site/Agent-3827b792315a817b9ce3c8b24046021f`
  - 標題改為「阿魁｜直播導讀」，圖示改為 🎥

- `Day3/index.html`
  - 標題改為「阿魁｜直播導讀」，圖示改為 🎥
  - ⚠️ URL 仍為 Day2 直播導讀，待阿魁提供 Day3 正確 URL 後更新

## 異動紀錄

### 2026-06-19 目錄架構標準化調整
* **推薦資源新增**：於推薦頻道中補入「快半拍AI實驗室｜Day 1 心得」卡片。
* **目錄架構一致化**：統一將圖片資料夾命名為 `images_cht/`，以對齊 Day 2~5 的命名規範。
* **HTML 路徑修正**：更新 `index.html` 中所有圖片的相對引用路徑為 `images_cht/`。
* **全域清理**：清除隱藏垃圾檔案 `.DS_Store`。
