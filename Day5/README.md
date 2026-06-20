# Day 5 — Spec-Driven Production Grade Development in the Age of Vibe Coding

## AI START HERE：執行設定專區

> 本區是所有 AI、subagent 與後續接手者的最高優先專案說明。  
> 開始工作前必須完整閱讀本區，不可只閱讀任務清單或依過往經驗自行推測。

### A. 指令優先順序

發生衝突時依下列順序處理：

1. 使用者最新指令。
2. 本「AI START HERE：執行設定專區」。
3. `Day5/README.md` 任務清單與驗收條件。
4. `source/day5-content-inventory.md` 內容完整性清冊。
5. Day4、Day3、Day2、Day1 的既有實作經驗（尤其 Day4 task15 整理的可重用經驗）。

舊的執行紀錄只代表當時結果；若後續已修正方法，以本設定專區與最新任務狀態為準。

### B. 每個 AI 必須遵守的工作方式

1. 先讀取：
   - `README.md`
   - `source/day5-content-inventory.md`（task4 完成後）
   - 與目前 task 直接相關的來源檔及腳本。
2. 執行任何新使用者指令前，先把該指令**逐字**追加到本區的「原始提示詞／指令完整紀錄」。
3. 不得把規劃寫成已完成；只有產物存在且驗證通過後才能標示完成。
4. 每次完成工作都要更新：
   - 目前狀態
   - 對應 task
   - 執行結果
   - 問題與技術決策
   - 驗證結果
5. 可由 AI 判定的事項直接完成，不要求使用者人工挑選：
   - 正式 Figure 判定
   - 圖片與 caption 對應
   - 內容完整性核對
   - 圖片文字與版面視覺 QA
6. 只有語意確實無法判斷、需要新權限或缺少關鍵來源時才詢問使用者。
7. 不覆寫原始來源：
   - 原始 PDF 保留。
   - Docling 原始 Markdown 保留。
   - raw images 保留。
   - 修復或翻譯結果另存新檔。
8. 所有頁面與資料必須使用繁體中文台灣用語；技術專有名詞依設定保留英文。

### C. PDF 與 Figure 固定設定

- 使用 Docling 2.69.1。
- `images_scale=5.0`。
- `do_ocr=False`：本 PDF 具有原生文字層，OCRmac 會造成部分頁面處理失敗（Day4 確認教訓）。
- `do_table_structure=True`。
- `generate_picture_images=True`。
- 圖片匯出 API：`picture.get_image(doc=result.document)`（Docling 2.69.1 正確 API）。
- Docling 是主要解析與抽圖方法。
- `pdfimages` 僅保留為底層內嵌圖與 smask 備查，不是正式圖的主要來源。
- AI 必須對照 PDF caption、頁碼、Markdown、raw images 與實際圖像內容判定正式 Figure。
- Day5 預計正式 Figure：**1 張**（Figure 1: Example of a Custom Code Review Runtime Architecture）。
  - 若 Docling 解析結果與預期不符，以 AI 逐一對照 PDF 實際內容為準，不以數量預設值強制判定。

### D. 翻譯與術語固定設定

- 使用台灣繁體中文，不使用中國大陸慣用語。
- 不摘要、不省略、不新增原文沒有的論點。
- 程式碼區塊不得翻譯或改動（含 Python、YAML、Markdown skill 檔）。
- 圖片路徑、URL、人名、模型名、API、產品名及縮寫不得任意修改。
- Endnotes 書目資料保留英文原文。
- 固定術語：

  **繼承自 Day4**
  - Agent：代理程式；產品名與複合技術名可依語境保留 Agent。
  - harness：執行框架／安全防護框架。
  - evaluation：評估。
  - observability：可觀測性。
  - vibe coding：保留英文。

  **Day5 新增術語**
  - SDD（Spec-Driven Development）：規格驅動開發；縮寫 SDD 首次補全名，後續可保留 SDD。
  - spec / specification：規格文件。
  - MCP（Model Context Protocol）：保留 MCP，首次補「模型情境協定」。
  - guardrails：護欄。
  - Human-in-the-Loop：保留英文，首次補「人工介入迴圈」。
  - Policy Server：政策伺服器。
  - Context Hygiene：脈絡衛生。
  - Zero-Trust：零信任。
  - Sandboxing：沙箱化。
  - BDD（Behavior Driven Development）：行為驅動開發；縮寫 BDD 首次補全名。
  - Code Review：程式碼審查。
  - Sustainability：永續性（指開發團隊的長期可維護性，非環保語境）。
  - Antigravity：保留英文（Google 內部 Coding Agent 產品名）。
  - Gemini CLI：保留英文。

- 長文可依語意切成互不重疊區塊交由多個 subagents 並行處理。
- 分段翻譯應使用適合技術長文的強模型；最終合併使用當下可用的最佳模型，逐段回看英文基準稿並統一術語與語氣。

### E. Figure 中文化固定設定

- task7 必須使用 `imagegen` skill，以原始英文 Figure 作為 edit target，採 `text-localization` 模式逐張中文化。
- 使用內建 `image_gen` 圖片編輯流程；開始編輯前先載入並檢視原圖。
- 必須明確要求只替換圖中文字，保留原始構圖、圖形、色彩、箭頭、連線、圖示、尺寸比例及資訊層級。
- PIL、SVG、HTML 僅可用於必要的後處理或修正，不作為 task7 的主要中文化方法。
- 中文圖檔名必須與英文正式 Figure 完全一致。
- 儘量維持原始尺寸與圖形關係。
- `MCP`、`SDD`、`LLM`、`API`、`SDK`、`ADK`、`BDD`、`YAML` 等技術名稱依語境保留英文。
- AI 必須逐張檢查：翻譯正確性、標籤與箭頭對應、截字與重疊、字級與可讀性、是否改變原圖語意。
- 此處所稱 QA 由 AI 執行，不代表要求使用者人工逐字檢查。

### F. Markdown／HTML 不可變與驗收基準

- 內容完整性基準：`source/day5-content-inventory.md`。
- 英文基準稿：`source/Spec-Driven Production Grade Development_Day_5.normalized.md`。
- 繁中基準稿：`source/Spec-Driven Production Grade Development_Day_5_zh.normalized.md`。
- 必須保留：
  - 1 張正式 Figure
  - 7 個 Snippets（Snippet 1–7，混合 Python / YAML / Markdown，不得翻譯程式碼）
  - 4 個主章節（SDD、MCP、Team Culture、Zero-Trust）
  - Summary
  - 17 條 Endnotes
- Snippet 驗收規則（依檔案類型）：
  - `.py`：`ast.parse` 語法驗證（Snippet 1、2、5、6、7）。
  - `.yaml`：`yaml.safe_load` 語法驗證（Snippet 4）。
  - `.md`：內容完整性比對，不做語法驗證（Snippet 3）。
- HTML 學習頻道放在 Hero 後、正文前。
- 主頁學習頻道不放 Markdown 來源卡片。
- Podcast 與每個 Codelab 使用獨立導讀頁。
- Codelab 必須逐條整理全部官方 steps，不可只提供主線摘要（Day3/Day4 確認標準）。
- Livestream 是獨立後補流程，不阻塞白皮書主流程。

### G. 當前執行狀態（2026-06-19 更新）

#### 已完成

- **task1**：scaffold 建立完成（source/、pipeline/、images_cht/、podcast-deep-guide/、day5-deep-guide/ 等）。
- **task2**：Docling `do_ocr=False` + `images_scale=5.0` 解析完成，產出 452 行英文 Markdown，9 個 picture items，pdfimages 備查 16 個，pdftotext 備查。
- **task3**：AI 確認正式 Figure 1 張（picture-002.png → `Figure 1 Custom Code Review Runtime Architecture.png`），已整理至 `source/..._images/`。
- **task4**：`source/day5-content-inventory.md` 建立完成，盤點：31 個 ## headings、1 張 Figure、7 個 Snippets（Python×5+YAML×1+Markdown×1）、17 條 Endnotes。
- **task5**：`source/Spec-Driven Production Grade Development_Day_5.normalized.md` 修復完成（439 行）。修復項目：H1 heading、HTML entities、標題層級、程式碼區塊語言標識、Figure 1 引用、Snippet 5 label。`pipeline/normalize_day5_markdown.py` 驗證 PASS。
- **task6**：三個 Haiku subagents 並行翻譯（Part 1: SDD 章節、Part 2: MCP+Team Culture、Part 3: Zero-Trust+Summary+Endnotes），Sonnet 主導最終合併與術語統一。產出：
  - `source/Spec-Driven Production Grade Development_Day_5_zh.md`（413 行）
  - `source/Spec-Driven Production Grade Development_Day_5_zh.normalized.md`（413 行）
  - 驗證：5 個 Python + 1 個 YAML + 1 個 Markdown code blocks、Figure 1 引用、H1、無 HTML entity 殘留，全部 PASS。

- **task7**：Figure 1 中文化完成。imagegen text-localization 模式，2351×563 px，SHA-256 兩目錄一致（e1c88124...）。視覺 QA 通過：知識圖形、程式碼脈絡、GQL·ANN·文字、子代理程式管道、搜尋→影響分析→任務分解→編碼，GQL/ANN/PR/main 保留英文。
  - **注意：task3 Haiku 圖片判定有誤，正式 Figure 應為 picture-008.png（191KB，架構圖），已於 task7 修正。picture-002.png 為封面水晶裝飾圖。**

- **task8**：HTML 前完整性校對完成。`pipeline/validate_day5_pre_html.py` PASS（0 errors，5 warnings 均為 Docling 單行壓縮導致的 ast.parse/yaml.safe_load 失敗，非內容問題）。驗收項目全部通過：H1、Figure 1 引用、7 Snippets（Python×5+YAML×1+Markdown×1）、4 主章節+Summary、17 Endnotes、無 HTML entity 殘留、繁中稿不引用英文原圖。

- **task9**：`index.html` 建立完成（44KB）。`python3 -m html.parser` PASS。7 Snippets、17 Endnotes、Figure 1 lightbox、sticky nav、學習頻道（Podcast+Codelab 標記即將推出）、桌機（1280×800）+ 手機（390×844）截圖 QA 通過。唯一 console error 為 favicon.ico 404，不影響頁面。

- **task10**：PDF / MD / HTML 最終核對完成。修正項目：fn13（ADK）與 fn17（Siemens）正文引用遺漏已補入。最終驗證全部 PASS：html.parser ✅、7 Snippets ✅、fn1–fn17 全部定義且引用 ✅、Figure 1 圖檔存在 ✅、overflow 防護 ✅、繁中稿 Endnotes 17 條 ✅。

- **task11**：Podcast 深度導讀完成。SRT 歸檔至 source/podcast/。`podcast-deep-guide/podcast-deep-guide.html`（348 行）：Hero + 影片播放器（GitHub Releases MP4）+ 5 段繁中導讀 + 3 個圖片佔位（onerror 隱藏）+ 繁中逐字稿 details 折疊（155 輪次，分 Speaker A/B）。html.parser PASS。
- **task12**：兩個 Codelab 導讀完成。Codelab 快照已存 source/codelabs/。
  - `agent-runtime-deploy-guide/agent-runtime-deploy-guide.html`（400 行）：12 步驟逐條深度導讀 + 2 圖佔位 + 步驟對照表。html.parser PASS。
  - `vibecode-frontend-guide/vibecode-frontend-guide.html`（541 行）：10 步驟（步驟 8 展開 6 子步驟）+ 端對端情境對照表 + 2 圖佔位。html.parser PASS。
  - 圖片提示詞（7 張）已存 `source/day5-image-prompts.md`；7 張繁中資訊圖已於 2026-06-19 使用內建 `imagegen` 完成並通過桌機／手機 QA。
- **task13**：QA 完成。4 頁 html.parser 全 PASS。console errors 僅圖片 404（尚未生成，onerror 隱藏）+ favicon.ico 404，不影響頁面。桌機 + 手機截圖各頁均通過。
- **task14**：`../index.html` Day5 已從 `is-soon` 改為 `is-live`，連至 `./Day5/index.html`。Day1–5 全部 is-live，目標檔案全部存在。html.parser PASS。

- **task15**：收尾整理完成（2026-06-19）。.DS_Store 清除、source/ 素材確認完整、README 同步、指令紀錄更新至指令 13。

- **7 張資訊圖後補**（2026-06-19，指令 13）：使用內建 `imagegen` 產生 7 張 1672×941 PNG，已放入 Podcast（3 張）、Agent Runtime Codelab（2 張）、Vibecode Codelab（2 張）的 `images/` 目錄。
  - 技術決策：實際輸出檔名以 HTML `src` 為準，並同步修正 `source/day5-image-prompts.md` 內 4 組舊檔名。
  - 問題修正：`podcast-deep-guide.html` 原 CSS 將 `.section-figure img` 設為 `display:none`，已改為顯示並置中。
  - 驗證：7 張圖皆為有效 PNG、三頁 `html.parser` PASS、桌機 1440×1000 與手機 390×844 截圖 QA PASS，所有資訊圖均正常顯示。

- **Day5 與課程首頁雙向串聯**（2026-06-19，指令 14）：`../index.html#day5` 的 Day5 卡片連至 `./Day5/index.html`；Day5 sticky nav 回程連至 `../index.html#day5`。上層課程狀態同步改為 Day 1–Day 5 全部完成。兩頁 `html.parser` 與連結目標檢查 PASS。

#### 後補待辦（不阻塞主流程）

- **Livestream 深度導讀**（task16–19）：**部分完成（2026-06-20）**
  - ✅ 中英文 SRT 逐字稿已放入 `Day5/` 根目錄（各 1769/1768 行）
  - ✅ `day5-deep-guide/day5-deep-guide.md`：六段式深度導讀 + 3 個 ai-mentor callout（deep-guide skill + ai-mentor-agents skill 執行）
  - ✅ `day5-deep-guide/index.html`：含 `<video>` 播放器（影片連結已填入）、雙語摺疊逐字稿、返回 Day5 主頁連結；html.parser PASS；桌機 1280×800 + 手機 390×844 截圖 QA PASS
  - ✅ `day5-deep-guide/README.md`：5 張生圖提示詞（圖 A–E，Kawaii 台灣風格 16:9）+ 指令 1–5 完整紀錄
  - ✅ 影片連結已填入：`https://github.com/lushinshang/5-DayAIAgentsIntensiveVibeCodingCourseWithGoogle2026/releases/download/DAY_1_Livestream/DAY.5.Livestream.-.5-Days.of.AI.Agents.Intensive.Vibe.Coding.Course.With.Google.mp4`
  - ✅ **雙向連結**：`Day5/index.html` 學習頻道新增直播導讀卡片 → `day5-deep-guide/index.html`；導讀頁 nav + footer 均有回程連結 → `../index.html`；兩頁 html.parser PASS
  - ⏳ 5 張資訊圖待生成（`images/day5-fig-a` 至 `images/day5-fig-e`，提示詞在 `day5-deep-guide/README.md`）

---

### H. 原始提示詞／指令完整紀錄

以下依目前可取得的對話與既有 README 紀錄，按時間順序逐字保存。不得改寫原句；新指令必須繼續往下追加。

1. `依據day4/readme，先規劃day5/readme`
2. `read readme,參考day1-day4的readme.md，規劃本日執行步驟`
3. `sonnet 4.6主導，use many subagent usiing haiku to go task 1-6 ，all finish then update readme.md`
4. `do task7,提醒生圖之前prompt先準備好`
5. `ok`（確認 task7 imagegen prompt 並執行）
6. `do task8`
7. `do task9`
8. `do task10`
9. `postcast srt有兩個我放好了，codelab有[URL1]和[URL2]，你先觀察再提供規劃`
10. `補充影片連結「https://github.com/...mp4」，重新規劃`
11. `會生哪些圖？`
12. `先建立提示詞不生圖，其他依規劃執行。我事後請codex cli協助生圖`
13. `do 1`
14. `index.html和../index.html建立串聯`
15. `../readme.md需要更新？`
16. `請更新`
17. `read每一天的readme.md，然後我要說第五天直播的中文及原文逐字稿都放此，影片產製中。工作如下：1.以AI-mentor and deepguide skill 針對逐字稿內容做深度導讀，存為md。2.接著以md_to_html將上一點的md轉換為html(前四天的直播導讀html可參考），有適合生圖之處，規劃提示詞先存在readme.md，我事後呼叫codex cli處理。`
18. `放 <video> 佔位，請執行`
19. `1.補充影片連結：https://github.com/lushinshang/5-DayAIAgentsIntensiveVibeCodingCourseWithGoogle2026/releases/download/DAY_1_Livestream/DAY.5.Livestream.-.5-Days.of.AI.Agents.Intensive.Vibe.Coding.Course.With.Google.mp4 2.所有過程，狀態及提示詞更新到readme.md`
20. `html和day5/html要互相連結`
21. `update readme.md`

### I. 新指令追加格式

後續 AI 收到新指令時，在執行前於上方清單追加：

```text
N. `使用者原始指令，逐字保留`
```

如果回合被中止，也要保留原始指令並標示「回合中止」；不得刪除或重新編號既有項目。

### J. 已使用的 AI／subagent 工作提示詞

本節保存專案內實際交付給 subagent 的工作提示。平台層級的 system／developer 安全設定不屬於專案 README；使用者指令與專案內部 delegation prompt 必須記錄。

#### task6 翻譯 subagent（3 個 Haiku 並行）

**Part 1（SDD 章節，行 1–187）**
```
工作目錄：Day5。你負責繁中翻譯 Part 1（行 1–187）。只可建立 source/.translation_chunks/day5_zh_part1.md。
來源：source/Spec-Driven Production Grade Development_Day_5.normalized.md 第 1–187 行。
台灣繁體中文，保留 Markdown 層級、圖片路徑、URL、專有名詞。術語：SDD=規格驅動開發、vibe coding 保留英文、Agent=代理程式、BDD=行為驅動開發、token 保留英文。
```

**Part 2（MCP+Team Culture，行 188–299）**
```
工作目錄：Day5。你負責繁中翻譯 Part 2（行 188–299）。只可建立 source/.translation_chunks/day5_zh_part2.md。
來源：第 188–299 行（MCP 起至 Zero-Trust 前）。台灣繁體中文，Snippets 完全不翻譯，MCP 首次補「模型情境協定」，Tier 1/2/3 保留英文。
```

**Part 3（Zero-Trust+Summary+Endnotes，行 300–439）**
```
工作目錄：Day5。你負責繁中翻譯 Part 3（行 300–439）。只可建立 source/.translation_chunks/day5_zh_part3.md。
來源：第 300–439 行（Zero-Trust 起至檔尾）。Endnotes 書目資料保留英文原文，Snippets 完全不翻譯。
術語：Zero-Trust=零信任、guardrails=護欄、Sandboxing=沙箱化、HITL 保留、Policy Server=政策伺服器。
```

#### task11 Podcast 導讀 subagent

```
工作目錄：Day5。建立 podcast-deep-guide/podcast-deep-guide.html。
素材：source/podcast/（英文 + 繁中 SRT 各 1064 行）。
影片：https://github.com/lushinshang/5-DayAIAgentsIntensiveVibeCodingCourseWithGoogle2026/releases/download/DAY_1_Livestream/Whitepaper.Companion.Podcast.Spec-Driven.Production.Grade.Development.in.the.Age.of.Vibe.Coding_compressed.mp4
結構：Hero + <video> 播放器 + 5 段繁中深度導讀（速度幻覺/SDD/MCP+三層審查/團隊文化/零信任護欄）+ 3 圖佔位（onerror 隱藏）+ 繁中逐字稿 <details>（分 Speaker A/B）。沿用 Day5 主頁 CSS 風格。
```

#### task12a Codelab 1 導讀 subagent

```
工作目錄：Day5。建立 agent-runtime-deploy-guide/agent-runtime-deploy-guide.html。
來源：source/codelabs/codelab1-agent-runtime.html（Playwright 快照）。
12 步驟逐條深度導讀，補「為什麼」與企業視角。2 圖佔位（onerror 隱藏）。官方步驟對照表。沿用 Day5 CSS。
```

#### task12b Codelab 2 導讀 subagent

```
工作目錄：Day5。建立 vibecode-frontend-guide/vibecode-frontend-guide.html。
來源：source/codelabs/codelab2-vibecode-frontend.html（Playwright 快照）。
10 步驟，步驟 8 展開 6 子步驟（含提示詞注入防禦實戰）。端對端情境對照表 + 官方步驟對照表。2 圖佔位（onerror 隱藏）。沿用 Day5 CSS。
```

---

## 摘要

本目錄用於製作 Google「5-Day AI Agents Intensive Course」Day 5 的繁體中文學習頁。

Day 5 採用經 Day 1–Day 4 驗證後修正的標準流程：

**來源歸檔 → Docling 600 DPI 解析與抽圖 → AI 確認正式 Figure → 建立內容清冊
→ 修復英文 Markdown → 繁中 Markdown → 中文化 Figure → HTML 前完整性校對
→ 手工建立 HTML → PDF / MD / HTML 最終核對 → Podcast / Codelab → QA
→ 根目錄入口更新**。

參考 Day 1 / Day 4 經驗，Day 5 後續可能補 livestream，因此本目錄一開始就預留：

- `source/livestream/`
- `day5-deep-guide/`
- `day5-deep-guide/images/`

**Day5 與 Day4 的主要差異**：

| 項目 | Day4 | Day5 |
|------|------|------|
| 正式 Figure | 4 張 | 1 張 |
| Snippet | 4 個（Python） | 7 個（Python / YAML / MD）|
| Endnotes | 6 條 | 17 條 |
| 作者 | 4 人 | 1 人（Lee Boonstra）|
| 頁數 | 41 頁 | 38 頁 |

**目前狀態**：scaffold 尚未建立。下一步是 task1。Podcast SRT / 影片、Codelab URL 與 livestream 素材尚未取得。

---

## 目錄結構（預計）

```
Day5/
├── README.md                         ← 本檔案：Day5 規劃與執行紀錄
├── index.html                        ← 預計：Day5 白皮書繁中主頁
├── desktop.png                       ← 預計：主頁桌機截圖 QA
├── mobile.png                        ← 預計：主頁手機截圖 QA
├── images_cht/                       ← 預計：HTML 正式引用的中文化 Figure
├── podcast-deep-guide/               ← 預計：Podcast 深度導讀頁
├── day5-deep-guide/                  ← 預留：Day5 livestream 深度導讀
│   └── images/                       ← 預留：livestream 導讀資訊圖
├── pipeline/
│   ├── convert_day5.py               ← Docling 解析
│   ├── extract_day5_figures.py       ← 整理正式 Figure
│   ├── normalize_day5_markdown.py    ← 修復並驗證英文基準稿
│   └── merge_day5_translation.py     ← 驗證繁中譯稿與不可變內容
└── source/
    ├── Day_5_v3.pdf                  ← 原始 PDF（已存在）
    ├── Spec-Driven Production Grade Development_Day_5.md
    ├── Spec-Driven Production Grade Development_Day_5.normalized.md
    ├── Spec-Driven Production Grade Development_Day_5.txt
    ├── Spec-Driven Production Grade Development_Day_5_images_docling_raw/
    ├── Spec-Driven Production Grade Development_Day_5_images_raw/
    ├── Spec-Driven Production Grade Development_Day_5_images/
    ├── Spec-Driven Production Grade Development_Day_5_zh.md
    ├── Spec-Driven Production Grade Development_Day_5_zh.normalized.md
    ├── day5-content-inventory.md
    ├── podcast/
    ├── codelabs/
    └── livestream/
```

---

## Day5 任務清單

### task1：建立結構與來源歸檔

- 建立 `source/`、`pipeline/`、`images_cht/`。
- 建立 `source/podcast/`、`source/codelabs/`、`source/livestream/`。
- 預留 `day5-deep-guide/`、`day5-deep-guide/images/`。
- 確認白皮書已歸檔：`source/Day_5_v3.pdf`（已存在）。
- README 必須持續記錄執行歷程、原始 prompt、已完成 / 未完成狀態、遇到的問題與決策。

### task2：Docling 解析與抽圖

沿用 Day4 正式規格（`do_ocr=False`、`images_scale=5.0`、`generate_picture_images=True`、`picture.get_image(doc=result.document)`）。

預期產出：

- `source/Spec-Driven Production Grade Development_Day_5.md`
- `source/Spec-Driven Production Grade Development_Day_5_images_docling_raw/`（若干 picture items）
- `source/Spec-Driven Production Grade Development_Day_5_images_raw/`（`pdfimages` 備查）
- `source/Spec-Driven Production Grade Development_Day_5.txt`（`pdftotext -layout` 備查）

注意：Docling picture item 數量 ≠ 正式 Figure 數量；task3 再逐一判定。

### task3：AI 確認並整理正式 Figure

對照：PDF caption、頁碼、Markdown、pdftotext、raw image 清單，逐一判定正式 Figure。

Day5 預計 1 張：

| Figure | PDF 頁面（預計） | 正式檔名 |
|--------|-----------------|----------|
| 1. Example of a Custom Code Review Runtime Architecture | 待確認 | `Figure 1 Custom Code Review Runtime Architecture.png` |

正式圖整理至：`source/Spec-Driven Production Grade Development_Day_5_images/`

### task4：建立 PDF 內容結構清冊

建立 `source/day5-content-inventory.md`，盤點：

- 完整章節與子章節（4 個主章節 + Summary）。
- 1 張 Figure。
- 7 個 Snippets（Snippet 1–7，逐一記錄檔名、語言、對應章節）。
- 17 條 Endnotes（逐條確認）。
- 確認無獨立 Table N 正文表格（若有則補記）。

此清冊是後續 Markdown 與 HTML 的驗收基準，不可只依 Docling 輸出判定內容完整。

### task5：修復與正規化英文 Markdown

逐項對照 PDF 與 `day5-content-inventory.md`：

- 補入 1 張 Figure 的圖片引用與完整 caption。
- 修復 Docling 的斷字、黏字與 heading 層級。
- 將 7 個 Snippets 整理成可讀 code block（保留原始語言、縮排、不翻譯）。
- 確認 4 個主章節、Summary 與 17 條 Endnotes 完整。
- 產出可直接翻譯的英文基準稿；不改寫原文語意。

驗證：

- 1 張 Figure 引用及圖檔存在。
- Python Snippets 通過 `ast.parse`；YAML Snippet 通過 `yaml.safe_load`；MD Snippet 內容完整。
- 章節結構完整（含 Summary 與 Endnotes）。

### task6：產出繁中 Markdown

產出：

- `source/Spec-Driven Production Grade Development_Day_5_zh.md`
- `source/Spec-Driven Production Grade Development_Day_5_zh.normalized.md`

翻譯規則：

- 術語依 D 節固定設定。
- 程式碼區塊（Python / YAML / MD）完全不翻譯。
- URL、人名、產品名保留英文；Endnotes 書目資料保留英文。
- 不摘要、不省略、不新增論點。

執行方式（建議，依實際行數調整）：

- 依語意分 3–4 個互不重疊區塊，由 `gpt-5.4` high-reasoning subagents 並行翻譯。
- 最終由 `gpt-5.5` xhigh-reasoning 逐段對照英文基準稿，統一術語、台灣用語、語氣與跨段銜接。

### task7：中文化 Figure（1 張）

中文化圖放入：

- `source/Spec-Driven Production Grade Development_Day_5_images_cht/`
- `images_cht/`

要求：

- 中文化圖檔名與英文正式 Figure 完全一致。
- 使用 `imagegen` skill 的內建 `image_gen` text-localization 模式。
- 只替換圖中文字；原始構圖、色彩、箭頭、尺寸比例必須保持不變。
- 完成後逐張視覺 QA：翻譯正確性、標籤對應、截字、可讀性。
- 兩個目錄的對應檔案 SHA-256 必須完全一致。

### task8：HTML 前完整性校對

先比對 PDF、英文 Markdown、繁中 Markdown、`day5-content-inventory.md`，確認：

- 1 張 Figure 引用正確（`../images_cht/<英文正式檔名>.png`）。
- 7 個 Snippets 完整，Python 通過 `ast.parse`，YAML 通過 `yaml.safe_load`。
- 4 個主章節、Summary、17 條 Endnotes 完整。
- 繁中稿 Figure 引用指向 `../images_cht/`（不可引用英文原圖）。

建立 `pipeline/validate_day5_pre_html.py` 作為可重複驗證工具。

### task9：建立 Day5 主頁 `index.html`

版位沿用 Day4 最終規格：

- Hero（標題、副標、作者、描述）
- Hero 後立即放學習頻道（Podcast / Codelab 卡片）
- Sticky nav
- 白皮書正文（4 個主章節 + Summary）
- Figure + caption（1 張，lightbox）
- 7 個 code block（含語言標示）
- Endnotes（17 條，錨點連結）
- lightbox

主頁不放 Markdown 來源卡片。Podcast / Codelab 卡片若素材未到位，標記「即將推出」。

### task10：PDF / MD / HTML 最終核對

逐節比對：

- 原始 PDF
- 英文 Markdown
- 繁中 Markdown
- HTML

特別檢查：

- 7 個 Snippets 是否完整（含 YAML、MD 類型）
- 4 個主章節與 Summary 是否完整
- 17 條 Endnotes 是否完整（比 Day4 多 11 條，務必逐條核對）
- Figure 順序與 caption 是否一致
- 手機版長 URL / code block 是否溢出

### task11：Podcast 深度導讀

素材：Podcast SRT / 影片連結（TBD）。

預計產出：

- `podcast-deep-guide/podcast-deep-guide.md`
- `podcast-deep-guide/podcast-deep-guide.html`
- `podcast-deep-guide/desktop.png`
- `podcast-deep-guide/mobile.png`
- `podcast-deep-guide/images/`（Kawaii 16:9 資訊圖）

要求：

- 使用 `ai-mentor` + `deep-guide` skill。
- Hero 正下方放 Podcast 影片播放器。
- 含繁中主題式深度導讀（5 段式）。
- 含英文原始逐字稿 `<details>` 折疊（可辨識講者則加 speaker badge）。
- 適當段落生成 Kawaii 台灣風格 16:9 資訊圖（粉圓體，繁體中文）。
- 頁面需有返回 Day5 主頁連結。

### task12：Codelab 導讀

Codelab URL：TBD。

流程：

1. 保存官方 HTML snapshot 到 `source/codelabs/`。
2. 抽出官方 step 標題與關鍵內容（必須逐條整理，不只寫主線摘要）。
3. 用 `deep-guide` + `ai-mentor` 建立繁中白話導讀。
4. 建立 standalone HTML。
5. 產生 Kawaii 16:9 資訊圖。
6. 補「官方 Codelab 步驟對照」區塊。
7. HTML parser、連結、桌機 / 手機截圖 QA。

### task13：QA

至少執行：

- `python3 -m html.parser index.html`
- `python3 -m html.parser podcast-deep-guide/podcast-deep-guide.html`（若已完成）
- 每個 Codelab guide HTML parser（若已完成）
- 本地 `href` / `src` 缺檔檢查（用 Python 腳本，比手動快）
- 桌機截圖 QA（1280×800）
- 手機截圖 QA（390×844）
- `.DS_Store` 檢查與清除
- Console errors 確認（用 Playwright + 本地 HTTP server，`file://` 協定被封鎖）

### task14：更新 parent 入口

Day5 主頁完成並驗證後，更新上一層：

- `../index.html`：Day5 從 `is-soon` 改為 `is-live`，連到 `./Day5/index.html`。
- `../README.md`：狀態改為 Day1–Day5 已完成。

驗證：

- parent `index.html` HTML parser 通過。
- Day1–Day5 live links 對應檔案皆存在。

### task15：收尾整理

- 清掉 `.DS_Store`。
- 確認來源素材都在 `source/`。
- README 補完整執行紀錄與 prompt 紀錄。
- 整理可重用經驗（若有 Day6）。

---

## Livestream 後補任務

以下任務等 Day5 livestream 素材到齊後再做，不阻塞 Day5 白皮書主流程。

### task16：Day5 livestream 素材歸檔

- SRT 放 `source/livestream/`。
- MP4 本地備份放 `source/livestream/`。
- 產出純文字逐字稿：`source/livestream/day5-transcript.txt`。

### task17：Day5 livestream 深度導讀

建立：

- `day5-deep-guide/index.html`

要求：

- 使用 `deep-guide` + `ai-mentor`。
- Hero 正下方放直播影片播放器。
- 逐字稿用 `<details>` 摺疊，若可辨識講者加 speaker badge。
- 頁面需有返回 Day5 主頁連結。

### task18：Livestream 資訊圖

產生 16:9 桌機圖，放入 `day5-deep-guide/images/`。

### task19：整合回 Day5 主頁

- `Day5/index.html` 學習頻道新增「Day5 直播深度導讀」卡片。
- 更新 `Day5/README.md` 與 parent `../README.md`。
- 重跑 HTML parser、本地連結與截圖 QA。

---

## README 維護守則

每次更新本 README 都必須包含：

1. 執行歷程：做了什麼、結果如何、遇到什麼問題。
2. 原始提示詞：逐字紀錄使用者下的指令。
3. 已完成與未完成狀態：避免將規劃寫成已完成。

目的：讓未來專案可以直接複用這份紀錄，不需重新推導流程。

## 異動紀錄

### 2026-06-19 目錄架構標準化調整
* **推薦資源新增**：於 `index.html` 新增推薦頻道群組，並補入「阿魁｜白皮書導讀」Notion 卡片。
* **檔案位置整理**：將 `Day_5_v3.pdf` 歸位至 `source/` 目錄。
* **全域清理**：清除隱藏垃圾檔案 `.DS_Store`。

### 2026-06-19 Codelab 導讀圖片整合（本次 Session）

**背景**：Day5 兩個 codelab guide HTML 的 `<figure>` 圖片均指向不存在的本地路徑（`images/fig*.png`），透過 `onerror` 靜默隱藏，讀者完全看不到圖片。本次以 source codelabs HTML 中的 Google Codelabs 官方 CDN URL 取代。

**完成事項**：

`agent-runtime-deploy-guide.html`：
* Step 8（測試代理）新增 2 張官方截圖：`a23afce3888c7503.png`（$50 費用自動核准）、`de22644fd583c1cb.png`（$150 費用觸發 Human-in-the-Loop）。
* Step 9（監控）與 Step 12（恭喜）以官方 Cloud Trace 截圖 `63ce8452b91239a2.png` 取代無效本地路徑。
* 來源：`source/codelabs/codelab1-agent-runtime.html` 官方 CDN。

`vibecode-frontend-guide.html`：
* 引言：新增 `architecture-simple.png`（事件驅動拓撲高階架構圖）。
* Step 3：新增 `frontend.png`（Vibecode 生成的費用審批 Dashboard 截圖）。
* Step 7：以官方 `architecture.png` 取代無效 `images/fig1-pubsub-frontend-arch.png`。
* Step 8.5：以 `architecture-simple.png` 取代無效 `images/fig2-prompt-injection-defense.png`。
* Step 8.6：新增 `agent-runtime.png`（Agent Runtime Playground 執行追蹤截圖）。
* 來源：`source/codelabs/codelab2-vibecode-frontend.html` 官方 CDN。
