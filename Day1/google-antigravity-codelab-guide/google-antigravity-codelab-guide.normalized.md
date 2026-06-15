# Google Antigravity 入門白話導讀：把 AI Agent 從「聊天工具」變成「工作指揮中心」

> 來源：Google Codelab「Getting Started with Google Antigravity」  
> 原文網址：https://codelabs.developers.google.com/getting-started-google-antigravity

很多人第一次接觸 AI Agent，會把它想成「比較會寫程式的聊天機器人」。但 Google Antigravity 這份 codelab 想傳達的重點，其實不是又多了一個聊天視窗，而是開發工作正在往「多個 Agent 並行、可被監督、可被排程、可被限制權限」的模式移動。

換句話說，Antigravity 不是只讓你叫 AI 寫一段程式碼，而是讓你建立一個工作環境：Agent 知道自己可以看哪些資料夾、能用哪些工具、哪些操作需要你審核、完成工作後要留下什麼證據。這也是整份教學最值得抓住的主線。

## 先看清楚：Antigravity 不是單一產品，而是一套 Agent 生態系

這份 codelab 一開始先把 Antigravity 2.0 的角色說清楚。它已經不只是 IDE 裡面的一個 Agent 管理器，而是拆成一組產品：

- **Antigravity**：獨立桌面應用程式，也是這份教學的主角。它像是 AI Agent 的指揮中心，可以管理多個本機 Agent、排程任務、設定權限。
- **Antigravity IDE**：偏向開發者使用的 IDE，內建 Agent 管理、Artifacts，並理解你的程式碼庫。
- **Antigravity CLI**：命令列介面，適合在終端機和 Agent 互動，但這篇不教。
- **Antigravity SDK**：讓開發者用程式方式整合 Antigravity，也不在這篇範圍內。

所以，如果你只是想跟 Agent 對話，Antigravity 可以做到；但它真正想解決的是「如何管理 Agent 的工作邊界」。當 Agent 能夠讀檔、改檔、開瀏覽器、呼叫外部系統時，問題就不只是能不能做，而是它該不該做、做到哪裡、誰來檢查。

## 安裝：先準備好本機環境與 Google 帳號

安裝流程很直接：到 Google Antigravity 下載頁，依照你的作業系統下載 macOS、Linux 或 Windows 版本，安裝後用個人 Gmail 登入。

教學也提醒你需要：

- Chrome 瀏覽器。
- 個人 Gmail 帳號。
- 本機安裝 Antigravity。

登入後，Antigravity 會帶你完成初始設定，包括安全與資料使用政策、主題選擇，以及可選的 Google Developer Tools 外掛。這些外掛會安裝一些技能，讓 Antigravity 更容易和 Google 開發工具互動。不過 codelab 本身沒有深入這些外掛。

你也可以選擇安裝 Antigravity IDE。它不是必裝，但如果你想用比較傳統的 IDE 介面看檔案、改程式、和 Agent 對話，它會更接近開發者熟悉的工作方式。

## Project：Agent 不是在真空中工作，它需要明確的範圍

Antigravity 的核心概念是 **Project**。

這裡的 Project 不只是「一個資料夾」，而是 Agent 工作時可以使用的環境與邊界。你可以把一個或多個資料夾組成一個 Project。舉例來說，一個產品可能同時有 frontend repo 和 backend repo，Antigravity 允許你把它們放在同一個 Project 裡，讓 Agent 取得完整上下文。

教學中的示範流程是：

1。 在本機建立資料夾：`$HOME/agy2-projects/my-first-project`。
2。 在 Antigravity 點選 `Select Project`。
3。 建立 `New Project`。
4。 加入剛才建立的資料夾。
5。 建立 Project，開始第一個 conversation。

這個設計背後有一個很重要的思維：Agent 的能力越強，越需要被明確限制在正確的工作區域。Project 讓你可以分別管理不同任務的檔案存取、工具權限、MCP 設定與安全規則，而不是讓所有 Agent 都吃到同一包大雜燴設定。

## Conversation：同一個 Project 內，可以有多條任務脈絡

建立 Project 後，你就可以在裡面開始 conversation。每個 conversation 可以理解成一條任務脈絡。

例如，你可以先開一個 conversation 叫 `conv-introduction`，只是測試 Agent 和你打招呼、回答一些基本問題。接著你可以在同一個 Project 裡再開另一個 conversation，命名為 `conv-sportsnews`，專門詢問運動新聞。

這樣做的好處是，Project 管的是工作範圍，conversation 管的是對話脈絡。你不用為每一個小任務都重新建立 Project，也不用把所有任務都塞在同一條對話裡。

## Project Settings：真正重要的是權限與行為邊界

Project 建立後，Antigravity 會讓你調整專案層級的設定。這是整個工具中最值得認真看的地方，因為它決定 Agent 到底能不能自己動手。

主要設定包括：

- **Security Preset**：是否要求你審核終端機指令與檔案存取。
- **Agent Behaviour**：Agent 執行 implementation plan 時，需不需要先經過你的同意。
- **Local Permissions**：限制 Agent 可以存取的檔案路徑、URL 等。
- **MCP Tools**：指定這個 Project 能使用哪些 MCP 工具，而不是自動吃到所有全域 MCP Server。

白話說，這裡就是在替 Agent 裝上護欄。你可以讓它更自動，也可以要求它每一步都先問你。哪一種比較好，取決於任務風險。改 README 或產生草稿可以放寬一點；碰到 production code、憑證、資料庫、部署流程，就應該保守一些。

## Slash Commands：用 `/` 直接叫出特定能力

Antigravity 的聊天介面支援 slash commands。你在輸入框打 `/`，就可以看到可用指令。

教學中特別介紹兩個：

- `/browser`
- `/schedule`

`/browser` 會啟動 browser sub-agent，讓 Agent 透過 Chrome 做瀏覽器相關任務。這需要 Chrome，也需要允許 Chrome debugging session。因為瀏覽器操作可能接觸登入狀態、頁面資料或外部網站，所以 Antigravity 會先要求你的權限。

`/schedule` 則是讓你建立一次性或週期性任務。你可以用自然語言告訴 Agent 在某個時間做某件事，例如星期一、三早上 9 點執行，或每天固定提醒。

這兩個指令代表兩種常見 Agent 能力：一種是「幫你操作外部介面」，另一種是「在未來時間點自動執行」。它們都很方便，但也都需要權限管理。

## Scheduling：把 Agent 變成定時工作的助手

除了 slash command，Antigravity 也提供圖形介面建立排程任務。

教學示範了兩個簡單任務：

- 每天下午 5 點提醒你有會議。
- 每 20 分鐘提醒你休息。

這看起來像提醒工具，但真正的潛力在於：排程 prompt 不一定只能提醒，它也可以呼叫工具、查資料、和外部系統互動。也就是說，你可以讓 Agent 定期整理報表、檢查狀態、抓取資訊，甚至觸發某些工作流程。

這也帶來一個實務提醒：越是自動化的 Agent，越需要清楚的權限範圍與可追蹤紀錄。排程任務如果只是提醒，風險低；如果會呼叫外部系統，就要把 Project Settings 和 MCP 權限設定好。

## MCP Servers：把 Agent 接到真實工具與資料

MCP 是 Model Context Protocol。你可以把它想成一種讓 Agent 連接外部系統的標準方式。

Antigravity 支援本機與遠端 MCP Servers，也內建一些和 Google Cloud 服務相關的整合。你可以從 Settings 進入 Customizations，再透過 `Add MCP+` 新增 Server。

如果你已經有現成的 MCP 設定，也可以直接把它放到：

```text
$HOME/.gemini/config/mcp_config.json
```

新增後，回到 Antigravity 的 MCP Servers 區域刷新，就能看到設定好的 server。你也可以停用某些 server，或點進去查看它暴露了哪些 tools。

MCP 的價值在於讓 Agent 不只是憑模型記憶回答，而是能接上你的資料與工具。但同樣地，這也代表風險上升。把 MCP 工具限制在特定 Project 裡，是一個很實用的做法，避免所有專案都能碰到不必要的外部能力。

## Artifacts：Agent 不能只說「我做好了」，它要留下證據

Artifacts 是這份 codelab 裡最關鍵的觀念之一。

以前我們叫 AI 改 bug，AI 回你「已修正」，你還是得自己翻程式碼確認。Antigravity 的做法是讓 Agent 在工作過程中產生 Artifacts，作為可審核的工作紀錄。

主要 Artifacts 包括：

- **Task Lists**：開始做事前列出的任務清單。
- **Implementation Plan**：要怎麼改程式、改哪些地方、為什麼這樣改。
- **Walkthrough**：完成後的變更摘要與測試方式。
- **Code diffs**：實際修改差異，雖然技術上不一定被歸為 Artifact，但同樣可審核。
- **Screenshots**：UI 修改前後的畫面證據。

教學示範讓 Agent 寫一個 Node.js 命令列應用，取得 Google 的最新新聞。Agent 會先產生 implementation plan，等你同意後才繼續。接著它會建立 task plan、產生檔案，最後用 walkthrough 說明完成內容與驗證方式。

這背後的意義是：Agent 的工作應該可觀察、可回饋、可審核。尤其在軟體開發中，結果不是只看「有沒有產出檔案」，而是要看它的計畫是否合理、修改是否符合需求、測試是否可信。

## Antigravity IDE：需要看程式時，可以回到熟悉的開發介面

如果你安裝了 Antigravity IDE，可以從 Antigravity 的 Auxiliary Panel 開啟 IDE。

IDE 會顯示 Agent 產生的資料夾與檔案，也會提供 editor 和 Agent Panel。你可以在 IDE 裡看 `package.json`、`index.js`，也可以直接和 Agent 討論這些程式碼，要求它解釋、產生、修正。

這裡可以看到 Antigravity 的分工：獨立 App 像是任務管理與 Agent 指揮中心；IDE 則適合深入程式碼細節。不是每個工作都需要打開 IDE，但當你要審查程式、理解差異、修改檔案時，IDE 還是比較自然。

## Skills：不要把所有規則一次塞給 Agent，要在需要時才載入

最後一個大主題是 Skills。

教學先指出一個常見問題：模型很強，但它不知道你的團隊規範、專案慣例、審查標準。如果你把所有規則、工具說明、流程文件一次塞進 Agent context，會造成 tool bloat、成本上升、延遲增加，甚至讓 Agent 更混亂。

Skills 的解法是 **progressive disclosure**，也就是漸進式揭露。Skill 平常只是放著，只有當使用者請求符合它的 description 時，Agent 才載入完整內容。

Skill 可以放在三種範圍：

- **Global Scope**：`~/.gemini/skills/`，跨 Antigravity 產品與專案可用。
- **Product Scope**：例如 Antigravity 使用 `~/.gemini/antigravity/skills/`，只給特定產品用。
- **Project/Workspace Scope**：`<project-root>/.agents/skills/`，只在特定專案內可用。

一個典型 Skill 目錄長這樣：

```text
my-skill/
├── SKILL.md
├── scripts/
├── references/
└── assets/
```

其中 `SKILL.md` 是必備，裡面包含 metadata 和實際指令。`scripts`、`references`、`assets` 則是選配。

教學示範建立一個 `code-review` skill，放在：

```text
~/.gemini/antigravity/skills/code-review
```

這個 Skill 的 description 是用來審查程式變更，檢查 bug、風格問題與最佳實務。它的 instructions 則要求 Agent 檢查正確性、邊界情境、風格與效能，並提供具體、解釋原因、可替代方案的回饋。

接著，教學建立一個故意有問題的 `demo_bad_code.py`，再請 Agent `review the @demo_bad_code.py file`。理想情況下，Agent 會辨識這個請求符合 `code-review` skill，載入 skill 指令，然後依照審查清單給出意見。

這個設計非常實用。它讓團隊可以把穩定規範包成 Skill，而不是每次都在 prompt 裡重打一遍。更重要的是，Agent 不需要在每次任務都背著全部規則，只在需要時才載入。

## 把 10 個步驟串起來看：這不是工具教學，而是 Agent 工作模式教學

這份 codelab 表面上有 10 個步驟：介紹、安裝、介面、slash commands、排程、MCP、Artifacts、IDE、Skills、結論。可是如果把它們串起來，主軸其實很清楚：

1。 先安裝一個能管理 Agent 的本機指揮中心。
2。 用 Project 定義 Agent 的工作範圍。
3。 用 Conversation 管理不同任務脈絡。
4。 用 Settings 控制安全、審核與工具權限。
5。 用 Slash Commands 觸發特定能力。
6。 用 Scheduling 讓任務可以定時執行。
7。 用 MCP 連接真實資料與外部工具。
8。 用 Artifacts 建立信任與審查流程。
9。 用 IDE 深入程式碼。
10。 用 Skills 把團隊規範變成可重用能力。

它真正想教你的不是「按哪個按鈕」，而是 Agentic development 的基本治理邏輯：讓 Agent 有能力，但也要有邊界；讓 Agent 自動化，但也要能審查；讓 Agent 使用工具，但不能讓工具失控；讓 Agent 依照規範工作，但不要把所有規範永遠塞進 context。

## 實務上該怎麼開始

如果你要依照這份 codelab 開始練習，可以用下面這個順序：

1。 先安裝 Antigravity，完成登入與基本設定。
2。 建立一個乾淨測試資料夾，不要一開始就拿重要專案練習。
3。 建立 Project，只加入這個測試資料夾。
4。 開一條 conversation，測試基本對話與檔案理解。
5。 打開 Project Settings，確認安全預設與檔案權限。
6。 試用 `/browser`，理解瀏覽器權限流程。
7。 試用 Schedule，但先從提醒型任務開始。
8。 新增或檢查 MCP Server，但只開必要工具。
9。 讓 Agent 做一個小程式，觀察 implementation plan、task list、walkthrough。
10。 建立一個簡單 Skill，例如 code review、commit message、文件整理。

最重要的是，不要把 Agent 當成全自動黑箱。Antigravity 的設計其實在提醒你：未來開發者的工作不只是寫程式，而是設計 Agent 的工作環境、審核流程、工具邊界與知識載入方式。

## 一句話總結

Google Antigravity 這份入門教學的核心，不是「如何使用一個 AI 開發工具」，而是「如何把 AI Agent 放進一個可控、可審核、可擴充的工作系統裡」。

當你理解 Project、Permissions、MCP、Artifacts 和 Skills 之間的關係，就會發現 Antigravity 真正的價值不只是讓 AI 幫你做事，而是讓 AI 以一種比較接近工程流程的方式幫你做事。
