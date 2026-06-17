# Agent Skills Podcast 深度導讀：不要把整家公司塞進 Prompt

如果把一百萬頁標準作業流程丟進 AI，它不會自動變成最強員工。這集 Podcast 一開始就戳破一個很常見的誤解：更大的 context window 不等於更強的代理人。模型能「裝下」大量文字，和它能在正確時刻「用對」那些文字，是兩回事。

Day 3 白皮書談的 Agent Skills，真正想解決的不是「如何把更多資料塞進模型」，而是「如何讓模型只在需要時看到剛好足夠的程序知識」。這個轉向很重要，因為它把 Agent 工程的焦點從模型本身，移到模型周圍的工作環境、記憶結構、測試制度與組織治理。

## Skill 不是新模型，而是可版本控制的工作記憶

Podcast 用很直接的方式拆解 Agent Skill：它本質上是一個資料夾，裡面有必要的 `SKILL.md`，也可以有 `scripts/`、`references/`、`assets/`。這個結構的重點不是形式，而是把三種東西拆開：

- `SKILL.md`：告訴代理人這個 skill 何時該用、要做什麼、成功輸出長什麼樣子。
- `scripts/`：放可重複、可驗證、不要交給語言模型猜的 deterministic work。
- `references/`：放很長但不該常駐 prompt 的領域文件。
- `assets/`：放 schema、template、範本檔等可重用素材。

這等於把「知道這件事」和「每次都把全部內容背在腦中」分開。好的 skill 不要求模型永遠記住所有流程，而是讓模型在觸發到任務時，才讀取那一小段必要的程序記憶。

Podcast 裡用餐廳廚房作比喻：`SKILL.md` 像菜單，代理人先知道有哪些菜；真的有人點菜時，才去拿食譜、開機器、叫工具。這就是 progressive disclosure 的精神。

## MCP 給代理人「手」，Skill 給代理人「手藝」

這集 Podcast 特別釐清三個容易混在一起的東西：MCP、`AGENTS.md`、Agent Skill。

MCP 讓代理人連到外部系統，例如查 BigQuery、讀 Salesforce、呼叫內部 API。它提供的是 reach，也就是觸達能力。Skill 提供的是 know-how，也就是拿到資料後該怎麼做的程序知識。`AGENTS.md` 則比較像常駐的專案規範，例如整個專案都要用 TypeScript、測試要怎麼跑、commit 前要檢查什麼。

三者不是互斥，而是分工不同。真正穩健的代理人系統，通常會讓 skill 裡的步驟去呼叫 MCP 工具；也會把全域規則留在 `AGENTS.md`，把特定任務流程留在 skill。

這個分工一旦清楚，系統設計會變得比較乾淨：不要把所有任務規則都塞進全域 prompt，也不要以為有 MCP 就等於代理人知道怎麼完成業務流程。

## Token 經濟學：context 太多會讓模型變笨

Podcast 最有價值的一段，是把 Agent Skills 的流行原因拉回 token economics。過去很多團隊以為，只要 context window 夠大，就可以把所有工具、規則、文件、API spec 全部塞進去。白皮書和 Podcast 都指出，這會造成 attention dilution：模型雖然沒有報錯，但它的注意力被大量無關資訊稀釋，表現會安靜地變差。

Agent Skills 的設計是反過來的。假設有 50 個 workflow，不需要把 50 份完整流程都載入 prompt；只需要載入每個 skill 的簡短描述。Podcast 提到，50 個 skill 的 metadata 可能約 4,000 tokens；真的觸發其中一個 skill 時，再載入該 skill 的內容。其餘 49 個留在硬碟，不進 context。

這種設計的效果不是單純省錢，而是保護模型的短期注意力。對企業來說，這意味著 agent architecture 的關鍵問題不是「context window 能多大」，而是「哪些資訊有資格在此刻進入 context」。

當 skill library 大到數萬個時，連 metadata 都不該全部載入。Podcast 也提到更大規模的做法：用 retrieval 或 embedding 先從大量 skill descriptions 中挑出最相關的幾個，再交給代理人判斷。也就是 progressive disclosure 的下一層：連菜單都要先檢索。

## 多代理人沒有消失，但被迫回到真正需要它的場景

這集 Podcast 對 multi-agent architecture 的態度很務實：多代理人不是死了，但用途變窄了。

如果任務真的需要非同步平行，例如三個代理人同時研究三家公司，multi-agent 仍然合理。如果不同工作有截然不同的安全權限，例如 HR 代理人可讀薪資、行銷代理人只能看公開網頁，也應該拆成不同代理人。

但如果只是同一個代理人需要切換一百種物流流程，硬拆成一百個 worker agents，會帶來部署、記憶、權限、路由與維護成本。這種情況下，一個 general-purpose agent 動態載入一百個 skills，通常更簡潔，也更容易治理。

這裡的實務判斷很重要：不要把「專業化」等同於「一定要多代理人」。很多專業化其實是程序知識的切換，不是身份或權限的切換。

## 失敗不是模型不聰明，而是 skill 沒被測好

Podcast 引用白皮書裡幾個警訊：設計不良的 skill 可能讓代理人比沒有 skill 時更差；有些研究也指出 skill 可能根本沒被正確觸發。這提醒我們，skill 不是只要寫成 Markdown 就會變成能力。

常見失敗模式有四種：

- Trigger failure：description 太模糊，導致該觸發的不觸發，或不該觸發的亂觸發。
- Execution failure：內部步驟不清楚，工具呼叫順序錯誤，甚至產生幻覺。
- Token budget failure：references 太肥，反而破壞 context。
- Regression：新增一個 skill 後，搶走既有 skill 的觸發流量。

因此白皮書強調 evaluation-driven development。不是先寫 skill，再憑感覺試用；而是在寫 `SKILL.md` 前，先定義幾個 JSON eval cases：輸入是什麼、預期工具軌跡是什麼、輸出格式是什麼。

Podcast 對 trajectory scoring 的說明尤其關鍵。只看最後答案是不夠的，因為代理人可能「用危險方式碰巧得到正確結果」。例如客服代理人成功退款，但途中誤刪了使用者地址。Output-only scoring 會判定通過；trajectory scoring 才會抓到這種錯誤。

這是 Agent 工程與一般生成式 AI Demo 的分水嶺：生產環境在乎的不只是答案對不對，也在乎它走過哪些不可逆動作。

## 從 Demo 到 Production，真正重的是基礎設施

Podcast 提到一個很有衝擊力的觀察：成熟 coding agent 的大量工程其實不是 prompt reasoning loop，而是權限分類、session storage、retry logic、context compaction 等操作基礎設施。這也解釋了為什麼很多 agent demo 在本機看起來很強，一進 production 就破功。

Production agent 的難點不是「模型會不會回答」，而是：

- 它能不能在錯誤環境中拒絕危險操作？
- 它能不能把暫存資料保存到正確地方，而不是污染 context？
- 它能不能在工具失敗時重試、回報、降級？
- 它能不能用權限層級限制 skill 的行為？
- 它能不能讓人類在高風險節點介入？

Podcast 提到的三層升級很值得採用：Read-Only、Draft-Only、Action-Allowed。新的 skill 不該一開始就能執行真實操作。先讓它只讀資料，再讓它產出待審草稿，最後才在足夠評估與審核後允許不可逆動作。

這種設計讓 skill 變成可以治理的軟體資產，而不是一堆散落的 prompt。

## Meta-skill 的邊界：AI 可以提案，但不能直接掌權

Podcast 也談到 meta-skills：讓代理人協助撰寫、改善、甚至從使用紀錄中提議新的 skill。這很有吸引力，因為它能把成功的工作 trace 變成可重用流程，也能讓 library 隨著真實需求演化。

但這也是最容易失控的地方。若沒有乾淨的 eval suite，代理人可能把 description 改到只會通過測試，卻破壞真實觸發邊界；也可能讓新 skill 搶走重要舊 skill 的流量。

所以最務實的規則是：AI 產生的 skill 一律從 draft tier 開始，人類必須審核前幾次修改，且每次升級都要通過 regression suite。AI 可以加速制度化知識，但不能繞過制度。

## DAG 與 file message bus：不要把 context window 當資料庫

當代理人連續使用多個 skills 時，還會遇到另一個問題：前一個 skill 的大量輸出如果直接丟回聊天歷史，context 又會膨脹。Podcast 用 DAG orchestration 與 file message bus 解釋 production 解法。

DAG 定義任務依賴順序，避免流程互相循環。File message bus 則讓 skill 把大型中間結果存成檔案，只把檔案路徑交給下一個 skill。這樣模型不用把十萬行 JSON 全部讀進 prompt，只需要知道「資料在這裡，需要時再讀」。

這背後有一個很重要的工程原則：shift intelligence left。能用 deterministic code 保證的東西，不要用 prompt 祈禱模型記得。例如郵遞區號驗證、schema validation、雜湊、欄位轉換，都應該放進 scripts，而不是寫一句「請務必檢查」。

## 企業護城河不是模型，而是被整理過的組織記憶

Podcast 最後用大型居家修繕零售商作案例：顧客問「我想鋪浴室磁磚，需要哪些材料，星期二能送到嗎？」這個問題看似一句話，其實牽涉工程知識、材料估算、庫存、物流與交期。

傳統做法可能是 AI 團隊嘗試打造一個巨大零售助理，結果 AI 工程師不懂防水層、磁磚耗損率、木材等級、物流規則。Skills-first 的做法則不同：

- 工法團隊維護 project-guidance skill。
- 商品團隊維護 materials-list skill。
- 履約團隊維護 delivery-window skill。
- 代理人依任務順序載入這些 skill，必要時透過檔案傳遞中間結果。

這就是 Agent Skills 最深的商業意義：它把最懂流程的人變成 skill owner，而不是要求 AI 團隊替全公司背下所有知識。競爭者可以買到同樣的基礎模型，卻買不到一家公司長年累積、可版本控制、可評估、可部署的程序記憶。

## 明天可以怎麼開始

最實際的起點不是先建立一個宏大的 skill library，而是找一個高頻、低風險、流程明確的任務：

1. 找一位領域專家，錄下他如何完成一個手動 workflow。
2. 把步驟整理成第一版 `SKILL.md`。
3. 補三個 JSON eval cases，包含正向、邊界與負向案例。
4. 把 deterministic work 放進 `scripts/`。
5. 先放到 Read-Only tier。
6. 觀察 trigger accuracy、tool trajectory、輸出品質與 token budget。
7. 通過 regression suite 後，再考慮升到 Draft-Only。

這集 Podcast 的核心訊息可以濃縮成一句話：不要期待模型本身記住整家公司；要把公司的程序記憶整理成可觸發、可測試、可版本控制、可治理的 skills。Agent Skills 不是讓 AI 更神祕，而是讓 AI 工作流更像真正的工程系統。


---

## 來源

- Antigravity Skills Codelab：https://codelabs.developers.google.com/getting-started-with-antigravity-skills
- Agents CLI + ADK Lifecycle Codelab：https://codelabs.developers.google.com/agents-cli-adk-lifecycle
- 英文 SRT：`Whitepaper Companion Podcast Agent Skills.en-orig.srt`
