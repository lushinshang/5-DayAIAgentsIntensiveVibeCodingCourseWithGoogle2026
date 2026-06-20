# Day 5 直播深度導讀 — 製作紀錄與生圖規劃

## 原始指令紀錄（逐字保留）

**指令 1（2026-06-20）**
```
read每一天的readme.md，然後我要說第五天直播的中文及原文逐字稿都放此，影片產製中。工作如下：
1.以AI-mentor and deepguide skill 針對逐字稿內容做深度導讀，存為md。
2.接著以md_to_html將上一點的md轉換為html(前四天的直播導讀html可參考），有適合生圖之處，規劃提示詞先存在readme.md，我事後呼叫codex cli處理。
```

**指令 2（2026-06-20）**
```
放 <video> 佔位，請執行
```

**指令 3（2026-06-20）**
```
1.補充影片連結：https://github.com/lushinshang/5-DayAIAgentsIntensiveVibeCodingCourseWithGoogle2026/releases/download/DAY_1_Livestream/DAY.5.Livestream.-.5-Days.of.AI.Agents.Intensive.Vibe.Coding.Course.With.Google.mp4
2.所有過程，狀態及提示詞更新到readme.md
```

**指令 4（2026-06-20）**
```
html和day5/html要互相連結
```

**指令 5（2026-06-20）**
```
update readme.md
```

---

## 已完成事項（2026-06-20 完成）

- [x] **逐字稿素材確認**：中文 SRT（zh-TW，1769 行）+ 英文 SRT（en-orig，1768 行）位於 `Day5/` 根目錄
- [x] **深度導讀 MD**：`day5-deep-guide.md`（六段式，含 3 個 AI-Mentor callout）
  - 段落：速度幻覺 / 真理來源 / 切分大象 / 三層防線 / 認知退化 / Agent 閉環
  - 附加：Codelab 洞察 / 隨堂測驗五題精解 / Capstone 介紹
  - skill：deep-guide + ai-mentor-agents
- [x] **標點規範化**：`day5-deep-guide.normalized.md`（normalize_punctuation.py，2 行有變動）
- [x] **HTML 轉換**：`index.html`（md_to_html skill）
  - Sticky nav（11 個錨點）
  - Hero 區：標題、副標、日期
  - `<video>` 播放器（影片連結已填入）
  - 4 欄導讀大綱卡片
  - 六個主要章節 + 3 個 callout
  - 5 張圖片佔位（onerror 隱藏，待生圖後自動顯示）
  - 隨堂測驗 5 張 quiz-card
  - Capstone 四軌 track-grid
  - 雙語摺疊逐字稿（14 段精選問答，含 7 位講者 badge）
  - Lightbox 點擊放大
  - 返回 Day5 主頁連結
  - html.parser PASS；桌機 1280×800 + 手機 390×844 截圖 QA PASS
- [x] **影片連結填入**：`https://github.com/lushinshang/5-DayAIAgentsIntensiveVibeCodingCourseWithGoogle2026/releases/download/DAY_1_Livestream/DAY.5.Livestream.-.5-Days.of.AI.Agents.Intensive.Vibe.Coding.Course.With.Google.mp4`
- [x] **生圖提示詞規劃**：5 張（圖 A–E，見下方，Kawaii 台灣風格 16:9）
- [x] **雙向連結整合**：
  - `Day5/index.html` 學習頻道新增「Day 5 直播深度導讀」卡片 → `day5-deep-guide/index.html`
  - `day5-deep-guide/index.html` nav（L136）+ footer（L697）均有 `← 返回 Day 5 主頁` → `../index.html`
  - 兩頁 html.parser PASS（指令 4 執行後驗證）
- [ ] **生圖執行**：5 張待使用者呼叫 Codex CLI 執行（`images/day5-fig-a` 至 `images/day5-fig-e`）

---

## 講者識別（供逐字稿參考）

| 講者 | 角色 | Badge 色 |
|------|------|---------|
| Smitha Kolen | 主持人，Google Cloud Developer Relations | 粉紅 `#d4507e` |
| Anant Navalgaria | 共同主持人 | 藍綠 `#176b75` |
| Ankur | 嘉賓，Google Cloud（Spanner Graph / ADK 專家） | 深綠 `#2e7d32` |
| Antonio | 嘉賓（PR 審核策略 / Agent 隊伍架構） | 橘 `#e65100` |
| Lee Boonstra | 嘉賓，白皮書作者 | 紫 `#6a1b9a` |
| Omar | 嘉賓（Gemma 4 / 混合推論） | 藍 `#1565c0` |
| Brenda | Kaggle 團隊，Capstone 介紹 | 金 `#f57f17` |

---

## 生圖規劃

以下 5 張插圖專為「Day 5 直播 AMA 討論概念」設計，風格為 **Kawaii 台灣風格 16:9（1672×941px）**，使用粉圓體繁體中文標籤，明亮色系。

---

### 圖 A：Vibe Coding vs SDD — 速度與永續性的取捨地圖

**嵌入位置**：`#section-1`（「速度幻覺」章節）正文之後

**檔名**：`images/day5-fig-a-vibe-vs-sdd.png`

**生圖提示詞**：
```
Create a split-screen comparison infographic in Kawaii Taiwanese illustration style (16:9, 1672x941px).
Use bright pastel colors, rounded fonts (Jf Open Huninn style), Traditional Chinese labels.

LEFT SIDE (coral/orange background): "Vibe Coding 速度衝刺"
- Rocket emoji launching upward
- Timeline: "10 分鐘 → 原型完成"
- Below: crumbling blocks labeled "程式碼是真理來源"
- Problem icons: ❌ 無法復現 ❌ 換框架就崩潰 ❌ 無人理解

RIGHT SIDE (mint/teal background): "SDD 規格驅動"
- Shield with document icon
- Timeline: "規格 → AI 生成程式碼 → 規格永續"
- Stable foundation blocks labeled "規格是真理來源"
- Benefit icons: ✅ 可重新生成 ✅ 跨語言移植 ✅ 人人可理解

CENTER DIVIDER: Arrow labeled "Vibe Coding 時代的關鍵轉換"

Bottom caption (small text): "程式碼可以被拋棄，規格不能 — Lee Boonstra"
```

---

### 圖 B：切分大象 — 微 Agent 網路架構圖

**嵌入位置**：`#section-3`（「切分大象」章節）正文之後

**檔名**：`images/day5-fig-b-elephant-slicing.png`

**生圖提示詞**：
```
Create a pipeline flow infographic in Kawaii Taiwanese style (16:9, 1672x941px).
Use soft blue/purple palette, rounded shapes, Traditional Chinese labels.

Title at top: "切分大象：微 Agent 架構 vs 單體 Agent"

LEFT COLUMN (red/warning style): "❌ 單體超級 Agent"
- One large elephant icon trying to hold everything
- Text: "開放式指令 → 上下文混亂 → 幻覺"
- Broken context window icon

RIGHT COLUMN (green/success style): "✅ 微 Agent 網路（ADK）"
Four connected small agent icons in a pipeline:
1. 🔍 搜尋 Agent → "Spanner Graph 依賴圖"
2. 🗺️ 影響分析 Agent → "修改前預測副作用"
3. ✂️ 任務拆解 Agent → "富含上下文的小塊任務"
4. 💻 編碼 Agent → "只做拼圖中的一塊"

Data layer at bottom (dark purple): "Spanner Graph + ANN 向量搜尋 = 三維程式碼藍圖"

Bottom badge: "Siemens 案例：數億行遺留程式碼庫的現代化"
```

---

### 圖 C：PR 審核三層防線

**嵌入位置**：`#section-4`（「三層防線」章節）正文之後

**檔名**：`images/day5-fig-c-three-tier-review.png`

**生圖提示詞**：
```
Create a pyramid/triangle tier infographic in Kawaii Taiwanese style (16:9, 1672x941px).
Use warm gradient colors (bottom=green, middle=yellow, top=red), Traditional Chinese labels.

Title: "PR 審核三層防線：防止工程師燃盡"

BOTTOM TIER (wide, green background): "第一層 — 全自動（低風險）"
- Icons: 拼字修正、次要依賴更新
- Label: "AI 處理 + CI 通過 → 自動合併"
- Tag: "零人工介入"

MIDDLE TIER (medium, yellow background): "第二層 — 批次摘要（中度風險）"
- Icons: batch summary document
- Label: "每日批次摘要 → 人類看摘要，不看每個 PR"
- Tag: "延後人工介入"

TOP TIER (narrow, coral/red background): "第三層 — 強制人工（高風險）"
- Icons: human + magnifier
- Label: "真正需要人類判斷的架構變更"
- Tag: "最少次介入"

Right side annotation: "遞迴對抗性審核層 → 正向飛輪效應"
Bottom warning: "⚠️ 對抗性層不能無限疊加：多層 = Token 浪費 + 混亂建置"
```

---

### 圖 D：認知退化 vs 認知進化 — 工程師的新技能樹

**嵌入位置**：`#section-5`（「認知退化」章節）正文之後

**檔名**：`images/day5-fig-d-cognitive-evolution.png`

**生圖提示詞**：
```
Create a skill tree / transformation infographic in Kawaii Taiwanese style (16:9, 1672x941px).
Use vibrant purple/gold palette, rounded badges, Traditional Chinese labels.

Title: "工程師的角色轉變：從程式碼編寫者到系統架構師"

LEFT BRANCH (fading, gray): "舊技能（會退化）"
- 語法熟練度
- 逐行程式碼審查
- 對「自己程式碼」的情感依戀
Arrow pointing down: "AI 已承擔這些工作"

CENTER (bright gold): "不變的核心"
- 系統底層直覺（WHY，不只是 HOW）
- 理解資安、可靠性、擴充性的根本
- 定義「什麼叫解決問題」的能力

RIGHT BRANCH (glowing, green): "新技能（需要培養）"
- 行為測試設計與審查
- 語意差異（Semantic Diffs）判讀
- Agent 系統邊界設計
- 規格書的結構化撰寫

Bottom quote: "你今天學到的方法，六個月後可能已過時。只有持續實作，才能建立不被工具綁定的系統直覺 — Omar"
```

---

### 圖 E：Agent 隊伍自我進化閉環

**嵌入位置**：`#section-6`（「自我進化閉環」章節）正文之後

**檔名**：`images/day5-fig-e-agent-squad-loop.png`

**生圖提示詞**：
```
Create a circular loop / flywheel infographic in Kawaii Taiwanese style (16:9, 1672x941px).
Use cool blue/teal palette with warm gold accents for human checkpoints, Traditional Chinese labels.

Title: "Agent 隊伍自我進化閉環"

CIRCULAR FLOW (clockwise, 6 stations):
1. 📝 規格書撰寫 → (人類介入點 🧑‍💻)
2. 🧪 測試套件共編 → (Agent + 人類)
3. 💻 程式碼 + 文件生成 → (Agent 全自動)
4. 🚀 基礎設施部署 → (Agent 全自動，無需 CLI)
5. 📊 軌跡 + 日誌收集 → (Agent 全自動)
6. 🔄 超級架構師 Agent → 回饋修改規格書 (人類審查 🧑‍💻)

Center of circle: "持續進化的系統" with flywheel icon

Outside annotations:
- "沙箱化（Sandboxing）：編碼 Agent 只能在預審骨架中填補空白"
- "Human-in-the-Loop 檢查點：設計、測試驗證、日誌審查、閉環"

Bottom: "這不是一個週末 Hackathon 原型，這是企業級 Agent 工程的最終形態"
```

---

## 生圖執行說明

所有圖片由使用者呼叫 Codex CLI 的 `image_gen` 工具執行，本 README 僅儲存提示詞。

執行格式參考：
```bash
# 逐張執行
codex --image-gen "images/day5-fig-a-vibe-vs-sdd.png" "<上方提示詞>"
```

---

## 素材來源

- 中文逐字稿：`../DAY 5 Livestream - 5-Days of AI Agents Intensive Vibe Coding Course With Google.zh-TW.srt`（1769 行）
- 英文逐字稿：`../DAY 5 Livestream - 5-Days of AI Agents Intensive Vibe Coding Course With Google.en-orig.srt`（1768 行）
- 白皮書：`../source/Spec-Driven Production Grade Development_Day_5.normalized.md`
- 參考樣板：`../day4-deep-guide/index.html`、`../day3-deep-guide/index.html`
