# Day 4 — Vibe Coding Agent Security and Evaluation

## AI START HERE：執行設定專區

> 本區是所有 AI、subagent 與後續接手者的最高優先專案說明。  
> 開始工作前必須完整閱讀本區，不可只閱讀任務清單或依過往經驗自行推測。

### A. 指令優先順序

發生衝突時依下列順序處理：

1. 使用者最新指令。
2. 本「AI START HERE：執行設定專區」。
3. `Day4/README.md` 任務清單與驗收條件。
4. `source/day4-content-inventory.md` 內容完整性清冊。
5. Day3、Day2、Day1 的既有實作經驗。

舊的執行紀錄只代表當時結果；若後續已修正方法，以本設定專區與最新任務狀態為準。

### B. 每個 AI 必須遵守的工作方式

1. 先讀取：
   - `README.md`
   - `source/day4-content-inventory.md`
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
- `do_ocr=False`：本 PDF 具有原生文字層，OCRmac 會造成部分頁面處理失敗。
- `do_table_structure=True`。
- `generate_picture_images=True`。
- 圖片匯出 API：`picture.get_image(doc=result.document)`。
- Docling 是主要解析與抽圖方法。
- `pdfimages` 僅保留為底層內嵌圖與 smask 備查，不是正式圖的主要來源。
- AI 必須對照 PDF caption、頁碼、Markdown、raw images 與實際圖像內容判定正式 Figure。
- Day4 已確認正式 Figure 共 4 張。

### D. 翻譯與術語固定設定

- 使用台灣繁體中文，不使用中國大陸慣用語。
- 不摘要、不省略、不新增原文沒有的論點。
- 程式碼區塊不得翻譯或改動。
- 圖片路徑、URL、人名、模型名、API、產品名及縮寫不得任意修改。
- Endnotes 書目資料保留英文原文。
- 固定術語：
  - Agent：代理程式；產品名與複合技術名可依語境保留 Agent。
  - harness：執行框架／安全防護框架。
  - Effective Trust：有效信任。
  - observability：可觀測性。
  - evaluation：評估。
  - trajectory：軌跡。
  - Vibe Diff：保留英文，首次出現補「意圖與執行差異說明」。
- 長文可依語意切成互不重疊區塊交由多個 subagents 並行處理。
- 分段翻譯應使用適合技術長文的強模型；最終合併使用當下可用的最佳模型，逐段回看英文基準稿並統一術語與語氣。

### E. Figure 中文化固定設定

- task7 必須使用 `imagegen` skill，以原始英文 Figure 作為 edit target，採 `text-localization` 模式逐張中文化。
- 使用內建 `image_gen` 圖片編輯流程；開始編輯前先載入並檢視原圖。
- 必須明確要求只替換圖中文字，保留原始構圖、圖形、色彩、箭頭、連線、圖示、尺寸比例及資訊層級。
- PIL、SVG、HTML 僅可用於必要的後處理或修正，不作為 task7 的主要中文化方法。
- 中文圖檔名必須與英文正式 Figure 完全一致。
- 儘量維持原始尺寸與圖形關係。
- `API`、`SDK`、`MCP`、`ADK`、`IAM`、`LLM`、`OpenTelemetry` 等技術名稱依語境保留英文。
- AI 必須逐張檢查：
  - 翻譯正確性
  - 標籤與箭頭對應
  - 截字與重疊
  - 字級與可讀性
  - 是否改變原圖語意
- 此處所稱 QA 由 AI 執行，不代表要求使用者人工逐字檢查。

### F. Markdown／HTML 不可變與驗收基準

- 內容完整性基準：`source/day4-content-inventory.md`。
- 英文基準稿：`source/Vibe Coding Agent Security and Evaluation_Day_4.normalized.md`。
- 繁中基準稿：`source/Vibe Coding Agent Security and Evaluation_Day_4_zh.normalized.md`。
- 必須保留：
  - 4 張正式 Figure
  - 4 個 Python snippets
  - 7 pillars
  - Security Recap
  - 7 evaluation dimensions
  - 8 evaluation methods
  - Conclusion
  - 6 條 Endnotes
- HTML 學習頻道放在 Hero 後、正文前。
- 主頁學習頻道不放 Markdown 來源卡片。
- Podcast 與每個 Codelab 使用獨立導讀頁。
- Codelab 必須逐條整理全部官方 steps，不可只提供主線摘要。
- Livestream 是獨立後補流程，不阻塞白皮書主流程。

### G. 當前執行狀態（2026-06-19 更新）

#### 已完成

- task1–task9 全部完成（scaffold、Docling、圖片確認、內容清冊、MD 修復、繁中翻譯、Figure 中文化、HTML 前校對、主頁 index.html）。
- task11 Podcast 深度導讀：ai-mentor + deep-guide 風格重寫完成，含 5 段式深度分析 + 145 輪次雙說話者逐字稿 + 影片播放器。
- task12 Codelab 1 導讀（13步逐條整理 + deep-guide）：`secure-agentic-coding-guide/secure-agentic-coding-guide.html` 完成。
- task12 Codelab 2 導讀（11步）：已完成 deep-guide + ai-mentor 風格重寫，加入事件驅動架構、安全邊界、Human-in-the-loop、評估與企業部署限制分析。

#### 資訊圖（Kawaii 16:9，1792×1024）進度

| 頁面 | 檔案 | 狀態 |
|------|------|------|
| Podcast | `podcast-deep-guide/images/fig1-security-eval-dual-axis.png` | ✅ 完成 |
| Podcast | `podcast-deep-guide/images/fig2-seven-pillars.png` | ✅ 完成 |
| Podcast | `podcast-deep-guide/images/fig3-eval-dimensions.png` | ✅ 完成 |
| Codelab 1 | `secure-agentic-coding-guide/images/fig1-shift-left.png` | ✅ 完成 |
| Codelab 1 | `secure-agentic-coding-guide/images/fig2-stride-skill.png` | ✅ 完成 |
| Codelab 2 | `vibecode-ambient-expense-agent-guide/images/fig1-ambient-arch.png` | ✅ 完成 |
| Codelab 2 | `vibecode-ambient-expense-agent-guide/images/fig2-expense-flow.png` | ✅ 完成 |

#### 待完成事項（依序）

1. **task10**：PDF / MD / HTML 最終核對。
2. **task13**：4 個頁面的完整本地連結、溢出與最終截圖 QA。
3. **task14**：parent 入口改為 `is-live`。

---

### G2. Codex CLI 圖片生成提示詞（4 張待生成）

> 使用方式：在終端機執行以下指令，生成完成後把 PNG 複製到指定目錄。
> 成功標誌：codex 輸出 `1792×1024` 字樣。

#### 圖 CL1-1：安全左移三層防禦工作流

目標路徑：`Day4/secure-agentic-coding-guide/images/fig1-shift-left.png`

```bash
codex exec -s danger-full-access --skip-git-repo-check \
"Use the image_gen tool to create a HORIZONTAL landscape infographic at 1792x1024.
Save to /tmp/fig-cl1-shift-$(date +%s).png AND /tmp/fig-cl1-shift-left.png

Taiwan kawaii cute style, 粉圓體 font, wide horizontal 16:9 landscape format.
Topic: 安全左移三層防禦工作流

Show THREE horizontal swimlane rows (left to right flow):

ROW 1 - Top (light coral background):
  Label on left: 「IDE 建議層」
  Flow: cute dev robot at laptop → linter warning bubble '⚠️建議修改' → 開發者選擇接受
  Note: 可忽略，但有即時回饋

ROW 2 - Middle (mint green background):
  Label on left: 「Commit 閘道層」
  Flow: git commit icon → pre-commit robot → Semgrep scan → two outcomes:
    ✅ 通過：程式碼進入版本庫
    ❌ 阻擋：觸發自動重構迴圈
  Note: 強制閘道，CONTEXT.md 規則驅動自修復

ROW 3 - Bottom (teal blue background):
  Label on left: 「CI/CD 終極防線」
  Flow: cloud pipeline → SAST scanner → SCA scanner → Binary Authorization → ✅部署 or ❌拒絕
  Note: 遠端隔離，不可繞過

Top title: 安全左移：越早發現，修復成本越低
Right side: Cost curve showing cost increases from left to right
Cute shield robot holding a checkmark on the far right" 2>&1
```

生成後執行：
```bash
cp /tmp/fig-cl1-shift-left.png "Day4/secure-agentic-coding-guide/images/fig1-shift-left.png"
```

---

#### 圖 CL1-2：STRIDE 六面向 + TDD 閘道

目標路徑：`Day4/secure-agentic-coding-guide/images/fig2-stride-skill.png`

```bash
codex exec -s danger-full-access --skip-git-repo-check \
"Use image_gen to create a WIDE HORIZONTAL 1792x1024 landscape infographic.
Save to /tmp/fig-cl1-stride-$(date +%s).png AND /tmp/fig-cl1-stride.png

Taiwan kawaii cute style, 粉圓體 font, landscape 16:9.
Topic: STRIDE 威脅建模 + TDD Planning Gate

Left half: STRIDE Threat Model hexagon grid
Six hexagons arranged in 2 rows of 3, each with cute villain icon:
  S - 偽裝 Spoofing (mask icon, red)
  T - 竄改 Tampering (scissors icon, orange)
  R - 否認 Repudiation (eraser icon, yellow)
  I - 資訊揭露 Information Disclosure (spy icon, purple)
  D - 阻斷服務 Denial of Service (bomb icon, coral)
  E - 提權 Elevation of Privilege (crown icon, gold)
Title above hexagons: STRIDE 六面向威脅評估

Divider line in the middle (arrow pointing right)

Right half: TDD Planning Gate process
Step 1: User writes vague prompt bubble '幫我建折扣系統'
Arrow down
Step 2: Cute planning gate robot with clipboard
  Shows a plan document with mandatory section:
  '✅ Security Boundaries & Assertions'
  '- 防止重複兌換'
  '- 拒絕訪客帳號'
  '- 驗證使用者身分'
Arrow down  
Step 3: Code generation only AFTER security plan approved
Title above right half: TDD Planning Gate 安全優先計畫

Bottom banner: 安全是設計的一部分，不是最後的補丁" 2>&1
```

生成後執行：
```bash
cp /tmp/fig-cl1-stride.png "Day4/secure-agentic-coding-guide/images/fig2-stride-skill.png"
```

---

#### 圖 CL2-1：Ambient Agent 事件驅動架構

目標路徑：`Day4/vibecode-ambient-expense-agent-guide/images/fig1-ambient-arch.png`

```bash
codex exec -s danger-full-access --skip-git-repo-check \
"Use image_gen to create a WIDE HORIZONTAL 1792x1024 landscape infographic.
Save to /tmp/fig-cl2-ambient-$(date +%s).png AND /tmp/fig-cl2-ambient.png

Taiwan kawaii cute style, 粉圓體 font, landscape 16:9.
Topic: Ambient Agent 事件驅動架構

Show a horizontal pipeline flow (left to right):

Left side: Event sources (vertical stack of cute icons):
  📧 費用報告提交
  🔔 Pub/Sub 訊息
  ⚡ Eventarc 觸發
  All with arrow pointing right →

Center left: ADK 2.0 圖形工作流 (graph diagram)
  Show workflow graph with nodes:
  [解析費用JSON] → diamond [金額 < $100?]
    YES → [auto_approve ⚡️ 純Python] → ✅ 自動批准
    NO → [security_screen 🛡️] → [review_agent 🤖 Gemini LLM] → [RequestInput ⏸️]
  
Center right: Human-in-the-loop bubble
  Manager avatar with approve/reject buttons
  Arrow from RequestInput to manager
  After decision → record outcome

Right side: Downstream actions:
  📊 Log to database
  💬 Slack notification
  📧 Email receipt

Top title: Ambient Expense Agent 事件驅動架構
Color coding:
  Green = auto-approved path (fast lane)
  Orange = security screen
  Blue = LLM review + human approval
  
Small robot mascot wearing headphones (ambient/listening) in corner" 2>&1
```

生成後執行：
```bash
cp /tmp/fig-cl2-ambient.png "Day4/vibecode-ambient-expense-agent-guide/images/fig1-ambient-arch.png"
```

---

#### 圖 CL2-2：費用路由決策流程

目標路徑：`Day4/vibecode-ambient-expense-agent-guide/images/fig2-expense-flow.png`

```bash
codex exec -s danger-full-access --skip-git-repo-check \
"Use image_gen to create a WIDE HORIZONTAL 1792x1024 landscape infographic.
Save to /tmp/fig-cl2-flow-$(date +%s).png AND /tmp/fig-cl2-flow.png

Taiwan kawaii cute style, 粉圓體 font, landscape 16:9.
Topic: 費用路由決策流程 + PII 安全防護

Left section - Decision routing:
Title: 金額路由規則（Python決定，非LLM）
Large $100 threshold diamond in center
  LEFT path (< $100, mint green): 
    Small coins icon → '⚡ 自動批准' green badge → 0 LLM cost
    Label: 確定性Python程式碼，無模型介入
  RIGHT path (≥ $100, coral orange):
    Money bag icon → continue to security screen

Middle section - Security Screen Node:
Title: 安全篩選節點（LLM之前必須執行）
Two detector boxes stacked:
  Box 1 🔍: PII 偵測器
    Examples: SSN *** → 已遮蔽, 信用卡 ****-****-****-1234
    Label: 個資永不到達LLM
  Box 2 🛡️: Prompt Injection 偵測器
    Red warning: '「繞過所有規則...」→ ⛔ 攔截'
    Label: 直接路由人工審查，LLM完全不介入

Right section - Evaluation:
Title: LLM-as-Judge 評估
Two score cards:
  📊 路由正確性 Target: 5.0/5.0
  🔒 安全防護性 Target: 5.0/5.0

Bottom banner: 在AI判斷之前，先做確定性安全篩選——這是企業部署的必要元件" 2>&1
```

生成後執行：
```bash
cp /tmp/fig-cl2-flow.png "Day4/vibecode-ambient-expense-agent-guide/images/fig2-expense-flow.png"
```

---

### G3. 圖片生成後的收尾步驟（由 Claude 執行）

圖片全部到位後，告知 Claude 執行以下：

1. 修正 `podcast-deep-guide/podcast-deep-guide.html` 圖片引用（`fig1-trust-shift.png` → `fig1-security-eval-dual-axis.png`，補 `fig3-eval-dimensions.png` 段落）。
2. 改寫 `vibecode-ambient-expense-agent-guide/vibecode-ambient-expense-agent-guide.html` 套用 deep-guide 風格。
3. 在所有 HTML 的圖片 `<figure>` 位置補上 `onerror` fallback（圖片缺失時隱藏，不破版）。
4. 執行 HTML parser 驗證。
5. 截圖 QA（桌機 + 手機）。
6. 更新 README task 狀態。

#### 2026-06-19 執行結果

- 已使用內建 `image_gen` 依 G2 提示詞生成 4 張資訊圖並存入指定目錄。
- 實際尺寸：
  - Codelab 1 圖 1：1672 × 941
  - Codelab 1 圖 2：1536 × 1024
  - Codelab 2 圖 1：1672 × 941
  - Codelab 2 圖 2：1672 × 941
- 已逐張檢查流程方向、分支、技術標籤、繁中文字與可讀性。
- Podcast 已改用 `fig1-security-eval-dual-axis.png`，並於評估章節加入 `fig3-eval-dimensions.png`。
- Codelab 2 已以 deep-guide + ai-mentor 方式重寫導讀，保留官方 11 步與原始程式碼提示。
- Podcast 與 Codelab 2 已重做桌機、手機截圖。
- 三個 guide HTML 均通過 `python3 -m html.parser`，本地圖片引用未發現缺檔。

### H. 原始提示詞／指令完整紀錄

以下依目前可取得的對話與既有 README 紀錄，按時間順序逐字保存。不得改寫原句；新指令必須繼續往下追加。

1. `ok,但是要根據day2 and day3經驗規劃`
2. `參考day1，後續還會補livestream`
3. `go`
4. `看看readme.md，規劃一下待辦事項`
5. `問什麼要人工檢查圖中文字`
6. `pdf不是要看figure，由AI幫我決定？`
7. `還是看看day3/readme.md，決定day4程序`
8. `do 1-4`
9. `docling可以抽出圖片，請再做一次`
10. `readme`
    - 此指令所在回合由使用者中止，未作為完整工作需求執行。
11. `readme的steps要調整，然後tell me what's next`
12. `do task5`
13. `task6 但是可以使用多個subagent（with 適當的model）處理，在用最好的model合併整理`
14. `所有的提示詞(指令）都要寫入readme.md(設定專區），readme.md要讓每個ai都看得懂`
15. `所有的提示詞(指令）都要寫入readme.md(設定專區），readme.md要讓每個ai都看得懂`
16. `read readme.md , then say what's next?`
17. `中文化應該用imagegen skill`
18. `exec task7,先第一張圖`
19. `Image Gen skill`
20. `exec task7,先第一張圖,Image Gen skill`
21. `請將圖寫入 images_cht/`
22. `繼續Figure 2–4`
23. `do task8`
24. `update readme.md`
25. `go task9`
26. `podcast的逐字稿為「Whitepaper Companion Podcast Vibe Coding Agent Security and Evaluation.en-orig.srt」，影片連結為「https://github.com/...」，Codelab的URL為「https://codelabs.developers.google.com/secure-agentic-coding」和「https://codelabs.developers.google.com/vibecode-ambient-expense-agent」，請先規劃再執行`
27. `go`
28. `Podcast 頁面，Codelab 1，Codelab 2的導讀，應該是要以ai-mentor and deepguide skill做深度的導讀，適當的段落要生成圖片（資訊圖表，台灣AI/IT專家用語繁體中文粉圓體，japan kawaii style，16:9)`
29. `應該要用到codex cli的image gen skill`
30. `請整理目前狀況to readme.md，含提示詞先準備好，我請codex cli處理`
31. `do 1-3`

### I. 新指令追加格式

後續 AI 收到新指令時，在執行前於上方清單追加：

```text
25. `使用者原始指令，逐字保留`
```

如果回合被中止，也要保留原始指令並標示「回合中止」；不得刪除或重新編號既有項目。

### J. 已使用的 AI／subagent 工作提示詞

本節保存專案內實際交付給 subagent 的工作提示。平台層級的 system／developer 安全設定不屬於專案 README；使用者指令與專案內部 delegation prompt 必須記錄。

#### task6 Part 1 翻譯 subagent

```text
Workspace: /Users/lanss/projects/2_Practice/5-Day AI Agents Intensive Course with Google(2026)/Day4. 你負責繁中翻譯 Part 1。你不是唯一在 workspace 工作的 agent，不要回復或改動其他人的檔案。只可建立/修改 `source/.translation_chunks/day4_zh_part1.md`。來源 `source/Vibe Coding Agent Security and Evaluation_Day_4.normalized.md` 第 1-117 行（不要包含 Identity heading）。翻譯為精確自然的台灣繁體中文。保留 Markdown 層級、圖片路徑、URL、專有名詞、英文縮寫與 Figure 英文檔名；caption 翻譯，圖片路徑不可更動。術語第一次可用中文（English）。不省略、不摘要、不新增論點。完成後回報檔案。
```

模型設定：`gpt-5.4`、`reasoning_effort=high`。

#### task6 Part 2 翻譯 subagent

```text
Workspace: /Users/lanss/projects/2_Practice/5-Day AI Agents Intensive Course with Google(2026)/Day4. 你負責繁中翻譯 Part 2。你不是唯一在 workspace 工作的 agent，不要回復或改動其他人的檔案。只可建立/修改 `source/.translation_chunks/day4_zh_part2.md`。來源 `source/Vibe Coding Agent Security and Evaluation_Day_4.normalized.md` 第 118-220 行（Identity 起，Security Recap 銜接段落結束；不要包含 Evaluation heading）。台灣繁中，保留 Markdown、條列、專有名詞與縮寫。術語：agent 依語境譯代理程式或保留 Agent；harness 譯防護框架/執行框架；Effective Trust 譯有效信任；Vibe Diff 保留英文。不省略、不摘要、不新增。完成後回報檔案。
```

模型設定：`gpt-5.4`、`reasoning_effort=high`。

#### task6 Part 3 翻譯 subagent

```text
Workspace: /Users/lanss/projects/2_Practice/5-Day AI Agents Intensive Course with Google(2026)/Day4. 你負責繁中翻譯 Part 3。你不是唯一在 workspace 工作的 agent，不要回復或改動其他人的檔案。只可建立/修改 `source/.translation_chunks/day4_zh_part3.md`。來源 `source/Vibe Coding Agent Security and Evaluation_Day_4.normalized.md` 第 221-303 行（Evaluation 主章至 Observability: The Prerequisite for Evaluation 結束；不含 Applied tips）。台灣繁中。保留 Markdown、圖片路徑、Figure 英文檔名；caption 翻譯。完整保留 7 dimensions、8 methods。LLM-as-judge、Agent-as-judge、OpenTelemetry、SWE-bench 等保留英文。不省略、不摘要、不新增。完成後回報檔案。
```

模型設定：`gpt-5.4`、`reasoning_effort=high`。

#### task6 Part 4 翻譯 subagent

```text
Workspace: /Users/lanss/projects/2_Practice/5-Day AI Agents Intensive Course with Google(2026)/Day4. 你負責繁中翻譯 Part 4。你不是唯一在 workspace 工作的 agent，不要回復或改動其他人的檔案。只可建立/修改 `source/.translation_chunks/day4_zh_part4.md`。來源 `source/Vibe Coding Agent Security and Evaluation_Day_4.normalized.md` 第 304 行到檔尾（Applied tips、4 snippets、Conclusion、Endnotes）。台灣繁中。程式碼區塊完全不可翻譯或修改；Snippet captions 與正文翻譯。URL、模型名、API、產品名、人名與 Endnotes 書目資訊保留英文。保持 Markdown/code fence。不省略、不摘要、不新增。完成後回報檔案。
```

模型設定：`gpt-5.4`、`reasoning_effort=high`。

#### task6 最終合併與校訂 subagent

```text
Workspace: /Users/lanss/projects/2_Practice/5-Day AI Agents Intensive Course with Google(2026)/Day4. 你負責最高品質最終合併與編輯。你不是唯一在 workspace 工作的 agent，不要回復其他人檔案。只可建立/修改：`source/Vibe Coding Agent Security and Evaluation_Day_4_zh.md` 與 `source/Vibe Coding Agent Security and Evaluation_Day_4_zh.normalized.md`。請完整閱讀英文基準 `source/Vibe Coding Agent Security and Evaluation_Day_4.normalized.md` 以及四份譯稿 `source/.translation_chunks/day4_zh_part1.md` 至 `day4_zh_part4.md`。將四份譯稿合併成一篇完整、精確、自然的台灣繁體中文白皮書，並逐段對照英文確保不省略、不摘要、不新增論點。統一術語與語氣；建議 Agent 譯「代理程式」但產品名/複合技術名可保留 Agent，harness 視語境譯「執行框架」或「防護框架」，Effective Trust 譯「有效信任」，observability 譯「可觀測性」，evaluation 譯「評估」，trajectory 譯「軌跡」，Vibe Diff 保留英文並首次補中文說明。保留 Markdown heading 層級、4 張圖片的原始路徑與英文檔名。圖片 alt/caption 可翻譯。四個 Python code blocks 必須與英文逐字元相同，不可翻譯或格式化。URL、人名、模型名、API、產品名、縮寫與 Endnotes 書目資料保留英文。`_zh.normalized.md` 內容可與 `_zh.md` 相同。完成後回報你統一的關鍵術語與檔案。
```

模型設定：`gpt-5.5`、`reasoning_effort=xhigh`、`service_tier=priority`。

---

## 摘要

本目錄用於製作 Google「5-Day AI Agents Intensive Course」Day 4 的繁體中文學習頁。

Day 4 採用經 Day 1–Day 3 驗證後修正的標準流程：

**來源歸檔 → Docling 600 DPI 解析與抽圖 → AI 確認正式 Figure → 建立內容清冊
→ 修復英文 Markdown → 繁中 Markdown → 中文化 Figure → HTML 前完整性校對
→ 手工建立 HTML → PDF / MD / HTML 最終核對 → Podcast / Codelab → QA
→ 根目錄入口更新**。

另外參考 Day 1 經驗，Day 4 後續可能會補 livestream，因此本目錄一開始就預留：

- `source/livestream/`
- `day4-deep-guide/`
- `day4-deep-guide/images/`

Livestream 不阻塞白皮書主流程；等素材到齊後再以獨立 task 追加。

**目前狀態**：已完成 task1-task9。下一步是 task10「PDF / MD / HTML 最終核對」。Podcast SRT / 影片、Codelab URL 與 livestream 素材尚未取得。

- task1：Day4 scaffold 與白皮書來源歸檔完成。
- task2：Docling `images_scale=5.0` 解析完成，產出 437 行英文 Markdown 與 10 個 picture items。
- task3：AI 已確認 4 張正式 Figure，完成整理與命名。
- task4：已建立章節、Figure、Snippet、Endnotes 內容清冊。
- task5：已產出修復後英文基準稿，並通過內容結構與 Python 語法驗證。
- task6：已由 4 個 `gpt-5.4` subagents 分段翻譯，再由 `gpt-5.5` 統一合併校訂，產出繁中稿與 normalized 版本。
- task7：已使用 `imagegen` skill／內建 Image Gen 完成 4 張正式 Figure 的繁中在地化、視覺 QA 與雙目錄歸檔。
- task8：已完成 PDF、英文稿、繁中稿、內容清冊與中文 Figure 的 HTML 前完整性校對，並通過自動驗證。
- task8：已完成 PDF、英文稿、繁中稿、內容清冊與中文 Figure 的 HTML 前完整性校對，並通過自動驗證。

---

## 目錄結構

```
Day4/
├── README.md                         ← 本檔案：Day4 規劃與執行紀錄
├── index.html                        ← 預計：Day4 白皮書繁中主頁
├── desktop.png                       ← 預計：主頁桌機截圖 QA
├── mobile.png                        ← 預計：主頁手機截圖 QA
├── images_cht/                       ← 預計：HTML 正式引用的中文化 Figure
├── podcast-deep-guide/               ← 預計：Podcast 深度導讀頁
├── day4-deep-guide/                  ← 預留：Day4 livestream 深度導讀
│   └── images/                       ← 預留：livestream 導讀資訊圖
├── pipeline/
│   ├── convert_day4.py               ← 600 DPI Docling 解析
│   ├── extract_day4_figures.py       ← 整理 4 張正式 Figure
│   ├── normalize_day4_markdown.py     ← 修復並驗證英文基準稿
│   └── merge_day4_translation.py      ← 驗證繁中譯稿與不可變內容
└── source/
    ├── Vibe Coding Agent Security and Evaluation_Day_4.pdf
    ├── Vibe Coding Agent Security and Evaluation_Day_4.md
    ├── Vibe Coding Agent Security and Evaluation_Day_4.normalized.md
    ├── Vibe Coding Agent Security and Evaluation_Day_4.txt
    ├── Vibe Coding Agent Security and Evaluation_Day_4_images_docling_raw/
    ├── Vibe Coding Agent Security and Evaluation_Day_4_images_raw/  ← pdfimages 備查
    ├── Vibe Coding Agent Security and Evaluation_Day_4_images/
    ├── day4-content-inventory.md      ← 章節、Figure、Snippet、Endnotes 清冊
    ├── podcast/                      ← 預計：Podcast SRT / 影音來源歸檔
    ├── codelabs/                     ← 預計：官方 Codelab HTML snapshot
    └── livestream/                   ← 預留：livestream SRT / MP4 / transcript / Markdown
```

---

## Day4 任務清單

### task1：建立結構與來源歸檔（已完成）

- 建立 `source/`、`pipeline/`、`images_cht/`。
- 建立 `source/podcast/`、`source/codelabs/`。
- 依 Day1 經驗預留 `source/livestream/`、`day4-deep-guide/`、`day4-deep-guide/images/`。
- 白皮書已歸檔至：
  - `source/Vibe Coding Agent Security and Evaluation_Day_4.pdf`
- README 必須持續記錄：
  - 執行歷程
  - 原始 prompt
  - 已完成 / 未完成狀態
  - 遇到的問題與決策

### task2：Docling 600 DPI 解析與抽圖（已完成）

沿用 Day2 / Day3 經驗，初版解析直接使用正式規格：

- `images_scale=5.0`
- `do_ocr=False`（本 PDF 具有原生文字層）
- `do_table_structure=True`
- `generate_picture_images=True`

實際產出：

- `source/Vibe Coding Agent Security and Evaluation_Day_4.md`（437 行）
- `source/Vibe Coding Agent Security and Evaluation_Day_4_images_docling_raw/`（10 個 Docling picture items）
- `source/Vibe Coding Agent Security and Evaluation_Day_4_images_raw/`（18 個 `pdfimages` 備查檔，含 9 個主圖與 9 個 smask）
- `source/Vibe Coding Agent Security and Evaluation_Day_4.txt`（`pdftotext -layout` 備查）

執行結果：

- 初次沿用舊腳本時有兩個問題：使用已不適用 Docling 2.69.1 的 `picture.image`，且啟用不必要的 OCRmac，造成部分頁面 OCR stage 失敗。
- 已修正為 `picture.get_image(doc=result.document)`。
- 因 PDF 本身具有文字層，改用 `do_ocr=False`，避免 OCRmac 失敗使頁面 layout item 遺失。
- 重新執行後 Docling 偵測 10 個 picture items，並成功輸出 10 張圖片。
- 新版 Markdown 已保留 4 個 Figure caption，行數由 320 增加至 437。
- `pdfimages` 版本繼續保留，僅作底層內嵌圖與 smask 備查。

### task3：AI 確認並整理正式 Figure（已完成）

不要直接相信 raw image 數量。必須逐一對照：

- PDF caption
- 英文 Markdown
- `pdftotext` 結果
- raw image 清單

AI 已逐一查看候選圖片並對照 caption、頁碼及 `pdfimages -list`。判定結果：

| Figure | PDF 頁面 | raw 圖檔 | 正式檔名 |
|--------|----------|----------|----------|
| 1. The Secure Vibe Coding Agent Framework | 9 | `picture-006.png` | `Figure 1 Secure Vibe Coding Agent Framework.png` |
| 2. The vibe coding agent evaluation framework | 28 | `picture-007.png` | `Figure 2 Vibe Coding Agent Evaluation Framework.png` |
| 3. Evaluation dimensions for vibe coding agents | 30 | `picture-008.png` | `Figure 3 Evaluation Dimensions for Vibe Coding Agents.png` |
| 4. Evaluation methods and recommended dimensions | 32 | `picture-009.png` | `Figure 4 Evaluation Methods and Recommended Dimensions.png` |

排除項目：

- Docling `picture-000` 至 `picture-005`：封面、致謝頁與目錄裝飾圖。
- `pdfimages` 的奇數 `picture-011/013/015/017`：正式 Figure 的 smask 遮罩。

正式圖已整理至：

- `source/Vibe Coding Agent Security and Evaluation_Day_4_images/`

檔名規則：

- `Figure N <Title>.png`

保留 raw 目錄備查，不覆蓋原始抽圖。

### task4：建立 PDF 內容結構清冊（已完成）

已建立 `source/day4-content-inventory.md`，盤點：

- 完整章節與子章節。
- 4 張 Figure。
- 4 個 Python snippets。
- 7 個 evaluation dimensions 與 transversal Safety & Responsible AI。
- 8 種 evaluation methods。
- Security Recap、Conclusion 與 6 條 Endnotes。
- 無 Appendix，無獨立 `Table N` 正文表格。

此清冊是後續 Markdown 與 HTML 的驗收基準，不可只依 Docling 輸出判定內容完整。

### task5：修復與正規化英文 Markdown（已完成）

逐項對照 PDF 與 `day4-content-inventory.md`：

- 補入 4 張 Figure 的圖片引用與完整 caption。
- 修復 Docling 的斷字、黏字與 heading 層級。
- 將 4 個 Python snippets 整理成可讀 code block。
- 確認 7 pillars、Security Recap、7 evaluation dimensions、8 evaluation methods、Conclusion 與 6 條 Endnotes 完整。
- 產出可直接翻譯的英文基準稿；不改寫原文語意。

實際產出：

- `pipeline/normalize_day4_markdown.py`
- `source/Vibe Coding Agent Security and Evaluation_Day_4.normalized.md`

修復內容：

- 移除 Docling 重複目錄與裝飾圖 placeholder，保留原始 Docling Markdown 不覆寫。
- 重建 `#` 至 `####` 章節層級。
- 插入 4 張正式 Figure 的相對路徑與完整 caption。
- 將 4 個被壓成單行的 Python snippets 還原為可讀 code block。
- 修復已確認的斷字、黏字、HTML entity 與跨頁斷行。
- 保留原文段落、術語、英式拼字與 6 條 Endnotes，不進行內容改寫。

驗證結果：

- 4 張 Figure 引用及圖檔存在。
- 4 個 Python code block 均通過 `ast.parse` 語法檢查。
- 7 pillars、7 evaluation dimensions、8 evaluation methods 完整。
- Security Recap、Conclusion 與 6 條 Endnotes 完整。

### task6：產出繁中 Markdown（已完成）

產出：

- `source/Vibe Coding Agent Security and Evaluation_Day_4_zh.md`
- `source/Vibe Coding Agent Security and Evaluation_Day_4_zh.normalized.md`

翻譯規則：

- 技術術語保留英文縮寫，必要時補中文說明。
- 程式碼區塊不翻譯。
- URL、人名、產品名保留英文。
- 不在翻譯階段自行修正原意；修正留到 double check。

執行方式：

- Part 1：標題、致謝、Introduction、Security 主章至 MCP Spoofing。
- Part 2：Identity、Red/Blue/Green Security Teaming、Observability、Security Recap。
- Part 3：Evaluation 主章、7 dimensions、8 methods、benchmarks、evaluation observability。
- Part 4：Applied tips、4 個 Python snippets、Conclusion、Endnotes。
- 四個區塊由 `gpt-5.4` high-reasoning subagents 並行翻譯。
- 最終由 `gpt-5.5` xhigh-reasoning 逐段對照英文基準稿，統一術語、台灣用語、語氣與跨段銜接。

產出：

- `source/Vibe Coding Agent Security and Evaluation_Day_4_zh.md`
- `source/Vibe Coding Agent Security and Evaluation_Day_4_zh.normalized.md`

統一術語：

- Agent：代理程式；產品名與複合技術名依語境保留 Agent。
- harness：執行框架／安全防護框架。
- Effective Trust：有效信任。
- observability：可觀測性。
- evaluation：評估。
- trajectory：軌跡。
- Vibe Diff：保留英文，首次補「意圖與執行差異說明」。

驗證：

- 兩個繁中檔案內容完全一致。
- 英文與繁中稿皆有 174 個內容區塊、44 個 headings、28 個 bullets、13 個 numbered items。
- task6 完成當時，4 張 Figure 圖片路徑與英文稿一致；task8 已正式改為引用 `../images_cht/` 中文化 Figure。
- 4 個 Python code blocks 與英文基準稿逐字元相同，並通過 `ast.parse`。
- 7 pillars、7 evaluation dimensions、8 evaluation methods、Security Recap、Conclusion 與 6 條 Endnotes 完整。

### task7：中文化 Figure（已完成）

中文化圖放入：

- `source/<paper>_Day_4_images_cht/`
- `images_cht/`

要求：

- 中文化圖檔名與英文正式 Figure 完全一致。
- 盡量維持原尺寸，避免 HTML 版面跳動。
- `SKILL.md`、CLI 指令、API、SDK、MCP、ADK 等技術名稱依語境保留英文。
- 使用 `imagegen` skill 的內建 `image_gen` 編輯流程，以 4 張英文正式 Figure 為 edit target，採 `text-localization` 模式逐張中文化。
- 編輯時只替換圖中文字；原始構圖、圖形、色彩、箭頭、連線、圖示、尺寸比例與資訊層級必須保持不變。
- PIL、SVG 或 HTML 僅限必要的後處理與文字修正，不作為主要生成方式。
- 由 AI 逐張視覺檢查文字、箭頭、標籤對應、截字與版面；語意無法確定時才詢問使用者。

執行紀錄：

- Figure 1 已使用 `imagegen` skill／內建 `image_gen` 的 `text-localization` 編輯模式產生第一版。
- 第一版保留原始三層架構、七個支柱、圖示、箭頭、虛線稽核路徑與配色；繁中標籤未見明顯截字或重疊。
- 初次嘗試時內建工具只回傳預覽，未直接提供本機生成檔路徑；後續已從工作階段結果資料精確取回通過 QA 的 PNG，因此不需改用 CLI fallback。
- 收到指令 20 後重新從英文原圖執行，不沿用先前生成版本；本次內建 Image Gen 結果已通過結構與文字初步 QA：保留三層架構、3 個主動防禦區塊、7 個工作流程控制、7 個安全支柱、原始連線與虛線稽核路徑，且未新增解釋文字。
- 已從本工作階段的 Image Gen 結果資料精確取回通過 QA 的版本，寫入：
  - `images_cht/Figure 1 Secure Vibe Coding Agent Framework.png`
  - `source/Vibe Coding Agent Security and Evaluation_Day_4_images_cht/Figure 1 Secure Vibe Coding Agent Framework.png`
- Figure 1 輸出為 PNG、1629 × 965、約 1.1 MB；兩份檔案 SHA-256 均為 `e3619349dbd1e4eee88aef1be3fd774b33ea564b90b8582d8c974492e0277f4a`。
- Figure 1 已完成並通過視覺 QA。
- Figure 2–4 已使用相同 `text-localization` 流程完成，並逐張核對結構、標籤、矩陣圓點、截字與語意。
- 4 張正式 Figure 已全部寫入 `images_cht/` 與 `source/Vibe Coding Agent Security and Evaluation_Day_4_images_cht/`；兩個目錄的對應檔案 SHA-256 完全一致。
- 最終尺寸：
  - Figure 1：1629 × 965
  - Figure 2：1742 × 903
  - Figure 3：1643 × 957
  - Figure 4：1771 × 888
- task7 已完成；其後 task8 也已完成。

### task8：HTML 前完整性校對（已完成）

先比對：

- 原始 PDF
- 修復後英文 Markdown
- 繁中 Markdown
- `day4-content-inventory.md`

先在 Markdown 階段補齊缺漏，再進入 HTML，避免重演 Day3 完成 HTML 後才補章節、表格與 Endnotes。

執行結果：

- 依 `source/day4-content-inventory.md` 比對 41 頁原始 PDF、英文 normalized Markdown 與繁中 normalized Markdown。
- 修正 task7 後的 Figure 引用：兩份繁中 Markdown 現在均引用 `../images_cht/<英文正式檔名>.png`，避免後續 HTML 誤用英文圖。
- 更新 `pipeline/merge_day4_translation.py`，驗證繁中稿必須引用中文化 Figure，並繼續確保 4 個 Python code blocks 與英文稿逐字元一致。
- 新增 `pipeline/validate_day4_pre_html.py`，作為 task8 與後續 HTML 前的可重複驗證工具。

驗證結果：

- PDF：41 頁。
- 英文與繁中 Markdown：各 423 行、44 個 headings、4 張 Figure、4 個 Python snippets、28 個 bullets、13 個 numbered items。
- 內容：7 pillars、Security Recap、7 evaluation dimensions、8 evaluation methods、4 applied tips、Conclusion、6 條 Endnotes 全部存在。
- 4 個 Python snippets 與英文稿完全一致，均通過 `ast.parse`。
- 4 張繁中 Figure 在 `images_cht/` 與 `source/..._images_cht/` 的對應 SHA-256 完全一致，解析度均達最低驗收值。
- 未發現 `TODO`、`TBD`、`FIXME`、`<!-- image -->`、Appendix 或獨立 `Table N` 殘留。
- `python3 pipeline/validate_day4_pre_html.py`、`python3 pipeline/merge_day4_translation.py` 與所有 pipeline Python 檔案語法檢查均通過。

task8 完成。

### task9：建立 Day4 主頁 `index.html`（已完成）

版位沿用 Day2 / Day3 最終規格：

- Hero
- Hero 後立即放學習頻道
- Sticky nav
- 白皮書正文
- Figure + caption
- table / code block / checklist
- endnotes
- lightbox

主頁不放 Markdown 來源卡片；Markdown 是來源，不是學習頻道。

執行結果：

- 依繁中 normalized Markdown 建構，4 張 Figure 引用 `images_cht/`，4 個 Python code blocks 完整保留。
- 七大支柱使用 `.pillar-list` 卡片格式，7 個評估維度使用 `.dim-cards` 分組，安全回顧使用 2 欄 `.recap-grid`。
- 8 種評估方法製作為對照表格。
- 6 條 Endnotes 錨點連結完整。
- 學習頻道 Podcast / Codelab 卡片標記「即將推出」，不產生死連結。
- `python3 -m html.parser index.html` PASS。
- 桌機（1280×800）與手機（390×844）截圖 QA 通過，已存為 `desktop.png` / `mobile.png`。

### task10：PDF / MD / HTML 最終核對

逐節比對：

- 原始 PDF
- 英文 Markdown
- 繁中 Markdown
- HTML

特別檢查：

- 表格是否漏
- 7 pillars、Security Recap 是否完整
- applied tips 與 4 個 code snippets 是否完整
- 7 evaluation dimensions 與 8 evaluation methods 是否完整
- endnotes 是否完整
- Figure 順序與 caption 是否一致
- 手機版長 URL / code block 是否溢出

Day2 曾在此補回 Applied Tip、Toolkit 條列、x402 micropayments。  
Day3 曾在此補回 Conclusion、Evaluation Toolkit、trigger gate 細節、token budget implications、ownership model 與 36 條 endnotes。

### task11：Podcast 深度導讀

Podcast 獨立成頁，不直接塞入主頁。

預計產出：

- `podcast-deep-guide/podcast-deep-guide.md`
- `podcast-deep-guide/podcast-deep-guide.html`
- `podcast-deep-guide/desktop.png`
- `podcast-deep-guide/mobile.png`

要求：

- 使用 `ai-mentor` + `deep-guide`。
- Hero 正下方放 Podcast 影片播放器。
- 包含繁中主題式深度導讀。
- 包含英文原始逐字稿 `<details>`。
- 若 SRT 可辨識講者，逐字稿要分 speaker badge。
- 頁面需有返回 Day4 主頁連結。

### task12：Codelab / 學習頻道導讀

每個 Codelab 都要建立獨立本地導讀頁。

流程：

1. 保存官方 HTML snapshot 到 `source/codelabs/`。
2. 抽出官方 step 標題與關鍵內容。
3. 用 `deep-guide` 建立繁中白話導讀。
4. 建立 standalone HTML。
5. 產生 16:9 / 9:16 資訊圖。
6. 補「官方 Codelab 步驟對照」區塊。
7. HTML parser、連結、桌機 / 手機截圖 QA。

Day3 修正後的標準：所有官方 step 必須逐條整理出來，不只寫主線摘要。

### task13：QA

至少執行：

- `python3 -m html.parser index.html`
- `python3 -m html.parser podcast-deep-guide/podcast-deep-guide.html`
- 每個 Codelab guide HTML parser
- 本地 `href` / `src` 缺檔檢查
- 桌機截圖 QA
- 手機截圖 QA
- `.DS_Store` 檢查

### task14：更新 parent 入口

Day4 主頁完成並驗證後，更新上一層：

- `../index.html`：Day4 從 `is-soon` 改為 `is-live`，連到 `./Day4/index.html`。
- `../README.md`：狀態改為 Day1、Day2、Day3、Day4 已完成。
- `../README.md`：補 Day4 目錄與參考資源。

驗證：

- parent `index.html` HTML parser 通過。
- Day1-Day4 live links 對應檔案皆存在。

### task15：收尾整理

- 清掉 `.DS_Store`。
- 確認來源素材都在 `source/`。
- README 補完整執行紀錄與 prompt 紀錄。
- 明確列出 Day5 可重用經驗。

---

## Livestream 後補任務

以下任務等 Day4 livestream 素材到齊後再做，不阻塞 Day4 白皮書主流程。

### task16：Day4 livestream 素材歸檔

- SRT 放 `source/livestream/`。
- MP4 本地備份放 `source/livestream/`。
- GitHub Releases URL 記錄於 README。
- 產出純文字逐字稿：`source/livestream/day4-transcript.txt`。

### task17：Day4 livestream 深度導讀

建立：

- `day4-deep-guide/index.html`

要求：

- 使用 `deep-guide` + `ai-mentor`。
- Hero 正下方放直播影片播放器。
- 逐字稿用 `<details>` 摺疊。
- 若可辨識講者，參考 Day1 做 speaker badge。
- 頁面需有返回 Day4 主頁連結。

### task18：Livestream 資訊圖

產生：

- 16:9 桌機圖
- 9:16 手機圖

放入：

- `day4-deep-guide/images/`

HTML 使用 `<picture>` 響應式切換，並支援 lightbox。

### task19：整合回 Day4 主頁

- `Day4/index.html` 學習頻道新增「Day4 直播深度導讀」卡片。
- `day4-deep-guide/index.html` 加返回 Day4 主頁。
- 更新 `Day4/README.md`。
- 更新 parent `../README.md` 的 Day4 目錄。
- 重跑 HTML parser、本地連結與截圖 QA。

---

## README 維護守則

每次更新本 README 都必須包含：

1. 執行歷程：做了什麼、結果如何、遇到什麼問題。
2. 原始提示詞：逐字紀錄使用者下的指令。
3. 已完成與未完成狀態：避免將規劃寫成已完成。

目的：讓 Day5 及未來專案可以直接複用這份紀錄，不需重新推導流程。

---

## 對話需求紀錄

1. **根據 Day2 / Day3 經驗規劃 Day4**：「ok,但是要根據day2 and day3經驗規劃」
   → 已整理 Day2 的 600 DPI、真正 Figure 確認、Podcast / Codelab 導讀與 QA 經驗。
   → 已整理 Day3 的 `pdfimages` fallback、Podcast 分講者逐字稿、Codelab 官方步驟對照與資訊圖經驗。

2. **補入 livestream 後補設計**：「參考day1，後續還會補livestream」
   → 已讀取 Day1 README 的 livestream 深度導讀流程。
   → Day4 規劃新增 `source/livestream/`、`day4-deep-guide/` 與 task16-task19。

3. **開始建立 Day4 scaffold**：「go」
   → 已建立 Day4 基本目錄與本 README 規劃。

4. **依 Day3 程序執行前四項**：「do 1-4」
   → 將 PDF 歸檔到 `source/`。
   → 建立並執行 `pipeline/convert_day4.py`，以 Docling `images_scale=5.0` 產出英文 Markdown。
   → Docling 偵測到 0 張 picture，改用 `pdfimages` 抽出 18 個 raw 圖檔。
   → AI 查看候選圖片並對照 PDF caption 與頁碼，確認 4 張正式 Figure。
   → 建立並執行 `pipeline/extract_day4_figures.py`，整理正式英文 Figure。
   → 建立 `source/day4-content-inventory.md`，作為後續翻譯及 HTML 完整性核對基準。

5. **要求重新使用 Docling 抽圖**：「docling可以抽出圖片，請再做一次」
   → 確認目前 Docling 版本為 2.69.1，正確 API 為 `picture.get_image(doc)`。
   → 發現此 PDF 已有文字層，初版啟用 OCRmac 反而造成多頁 layout 處理失敗。
   → 將 `pipeline/convert_day4.py` 改為 `do_ocr=False`，保留 `images_scale=5.0` 與 `generate_picture_images=True`。
   → Docling 成功辨識並輸出 10 個 picture items，其中 4 張為正式 Figure。
   → 正式 Figure 已改由 Docling raw 圖重新產出；`pdfimages` 檔案保留作備查。

6. **調整 README 程序並確認下一步**：「readme的steps要調整，然後tell me what's next」
   → 將流程改為 Docling-first，明確記錄本 PDF 使用 `do_ocr=False` 與新版 `picture.get_image(doc)` API。
   → 將 AI Figure 判定、內容清冊、英文 Markdown 修復、HTML 前校對拆成獨立階段。
   → 下一步定為 task5：修復與正規化英文 Markdown。

7. **執行英文 Markdown 修復**：「do task5」
   → 建立 `pipeline/normalize_day4_markdown.py`，保留原始 Docling Markdown並另產英文基準稿。
   → 移除重複目錄、重建 heading 層級、插入 4 張 Figure、還原 4 個 Python snippets。
   → 修復 Docling 斷字、黏字與跨頁斷行。
   → 驗證 4 Figures、4 snippets、7 pillars、7 dimensions、8 methods 與 6 endnotes 完整。

8. **使用多個 subagents 執行繁中翻譯**：「task6 但是可以使用多個subagent（with 適當的model）處理，在用最好的model合併整理」
   → 依章節語意切成 4 個互不重疊區塊，由 4 個 `gpt-5.4` high-reasoning subagents 並行翻譯。
   → 使用 `gpt-5.5` xhigh-reasoning 回看英文與四份譯稿，執行最終合併、術語統一與台灣用語校訂。
   → 建立 `pipeline/merge_day4_translation.py`，驗證圖片路徑、Python code、pillars、dimensions、methods 與 Endnotes。
   → 產出 `_zh.md` 與 `_zh.normalized.md`，兩檔內容一致。
