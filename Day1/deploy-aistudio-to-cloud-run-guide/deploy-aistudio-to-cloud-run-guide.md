# 從 AI Studio 到 Cloud Run：把 Vibe Coding 原型變成可上線服務

> 來源：Google Codelab「Deploy from AI Studio to Cloud Run」  
> 原文網址：https://codelabs.developers.google.com/deploy-from-aistudio-to-run

很多 AI 開發教學只停在「生成一個 demo」。畫面跑起來了、按鈕能動了，看起來像完成一半，但真正的產品問題才剛開始：這個東西要怎麼給別人用？要部署在哪裡？需要自己架伺服器嗎？用完測試資源後，會不會默默產生成本？

這份 codelab 的重點就在這裡。它不是要教你寫一個複雜系統，而是用一個很小的 web app 示範完整路徑：先在 Google AI Studio 用 vibe coding 快速做出原型，再直接部署到 Cloud Run，最後記得清理資源。

如果說 AI Studio 解決的是「我能不能很快把想法做出來」，Cloud Run 解決的就是「我能不能把這個做出來的東西穩定放到雲端執行」。

## 這份教學真正要你學會什麼

官方 codelab 的目標很明確，你會學到三件事：

1. 在 Google AI Studio 用 vibe coding 建立簡單 web application。
2. 測試產生出來的 application 是否符合預期。
3. 把 application 部署到 Cloud Run。

它的前提門檻不高，只需要你對 web application 有基本概念，並準備一個瀏覽器，例如 Chrome 或 Firefox。

但實務上，這份教學的價值不只是三個操作步驟，而是讓你看到一條新的開發管線：從 prompt 產生原型，到 cloud deployment，中間不需要先手動建立一大堆專案結構、CI/CD 或伺服器設定。

## 開始前：帳號與 Starter Tier 的限制要先看懂

教學開始前要求你準備 Google Account。官方也特別提醒：最好使用個人帳號，而不是公司或學校帳號。

原因很實際。公司或學校帳號可能有管理員限制，導致你不能啟用 lab 需要的 API，或不能完成部署流程。這不是技術問題，而是帳號權限問題。很多人第一次卡住，不是 prompt 寫錯，而是帳號被組織政策擋住。

接著你要進入 Google AI Studio，並同意服務條款。教學也提到，如果你使用 Google Cloud Starter Tier，可以免費部署最多兩個 full-stack applications。這句話很重要，因為它代表這個 lab 可以用低成本方式完成，但也不代表你可以無限制部署。

白話說，開始前要確認三件事：

- 你有可用的個人 Google 帳號。
- 你可以進入 Google AI Studio。
- 你知道 Starter Tier 有免費部署數量限制。

## Prototype：用一句 prompt 把想法變成可操作介面

進入 Google AI Studio 後，官方先請你看右上角的 Settings panel。這裡可以選模型、預設 framework，也可以提供 system instructions。

這一步很容易被忽略，但它其實決定了 AI Studio 產生應用程式時的基本方向。模型影響生成能力，framework 影響專案結構，system instructions 則像是你給整個生成過程的長期規則。

接著，教學給了一段具體 prompt：

```text
Create a formal looking frontend application that has two buttons: "Snowflakes" and "Balloons".
If the user clicks on the "Snowflakes" button, snowflakes of medium size should start falling on the screen from top to bottom for 5 seconds.
If the user clicks on the "Balloons" button, balloons of medium size should start floating from the bottom of the screen and float to the top for 5 seconds.
```

這個 prompt 看起來簡單，但它示範了 vibe coding 最基本的寫法：不要只說「做一個漂亮網站」，而是描述介面、互動、觸發條件與持續時間。

拆開來看，它其實包含四種需求：

- 視覺風格：formal looking frontend application。
- 介面元素：兩個按鈕，分別是 Snowflakes 和 Balloons。
- 互動行為：點 Snowflakes 後雪花從上往下掉。
- 動畫規則：中等大小，持續 5 秒；氣球則從下往上飄 5 秒。

AI Studio 會根據這段描述生成 web application。官方說生成過程大約需要 2 到 3 分鐘，中間可能會要求你選擇設計方案。

這裡的重點不是雪花或氣球，而是你可以用自然語言快速形成一個可操作的 frontend prototype。對產品探索、課堂練習、內部工具草稿來說，這種速度很有價值。

## 修正原型：Vibe Coding 不是一次生成就結束

官方也提醒，如果產生出來的 application 有問題，可以繼續用額外 prompt 修正。

例如：

```text
Increase the size of the snowflakes to twice their current size
```

這代表 AI Studio 的工作方式比較像「反覆對齊」，而不是「一次交付」。你先把需求說出來，讓系統產生版本一；看到結果後，再用更具體的 prompt 修改。

這也是 vibe coding 和傳統規格書最大的差異之一。你不一定一開始就知道所有細節，但你可以用可見結果來校準需求。只要修改 prompt 足夠具體，AI Studio 就能幫你迭代。

不過，這也有一個重要限制：越接近正式產品，越不能只靠感覺調整。你仍然需要測試按鈕是否真的觸發正確動畫、持續時間是否接近 5 秒、不同瀏覽器或螢幕尺寸是否正常。

## Deploy to Cloud Run：從可看 demo 變成可被連線的服務

當 application 準備好後，下一步就是部署到 Cloud Run。

官方流程是：

1. 在頁面右上角點擊 `Publish`。
2. 開啟 `Deploy app on Google Cloud` 對話框。
3. 選擇 Cloud Project，或使用 Default Gemini Project。
4. 如果找不到自己的 project，可以使用 `Import project`。
5. 如果系統要求，選擇 `Individual` 作為 organization type，並填入街道地址。
6. 點擊 `Publish your app`，等待部署到 Cloud Run。
7. 部署完成後，點擊 App URL 開啟雲端上的 web application。

這一段看起來像 UI 操作，但背後發生的是 AI Studio 幫你把應用程式包裝並部署到 Google Cloud 的 serverless 執行環境。Cloud Run 的好處是你不用自己管理伺服器，也不用先配置 VM、安裝 runtime 或處理底層基礎設施。

官方也提到，AI Studio 會自動產生 Cloud Run service name。這降低了入門摩擦，讓你不用一開始就處理命名、部署指令、服務設定等細節。

但你仍然要知道自己部署到了哪個 Google Cloud project，因為後續管理、成本、清理資源都和 project 有關。

## Clean up：教學做完後，別忘了 Unpublish

很多初學者完成部署後，會很自然地關掉頁面，覺得 lab 結束了。但官方特別放了一個 Clean up 步驟：為了避免 Google Cloud 帳戶產生費用，要點擊 `Unpublish app`。

這一步非常重要。雲端服務和本機 demo 不一樣，只要資源還在，就可能持續被計算、被存取、被計費。即使這個 lab 有 Starter Tier 和免費部署額度，你也應該養成「做完實驗就清理」的習慣。

白話說，部署不是最後一步，清理才是完整實驗的收尾。

## 這 6 個步驟串起來，其實是一條最短上線路徑

官方 codelab 總共有 6 個主要章節：

1. Overview
2. Before you begin
3. Prototype
4. Deploy to Cloud Run
5. Clean up
6. Congratulations

如果用工程流程來看，它們對應的是：

- **Overview**：確認你要學的是從原型到部署。
- **Before you begin**：處理帳號、條款、Starter Tier 前置條件。
- **Prototype**：用 AI Studio 產生 frontend application。
- **Deploy to Cloud Run**：把 application 發布到 serverless 雲端環境。
- **Clean up**：避免實驗資源造成後續費用。
- **Congratulations**：確認你已完成從 vibe coding 到 cloud deployment 的閉環。

這裡最值得記住的是「閉環」兩個字。很多 AI 工具展示只做到 prototype，但這份教學把 prototype 接到 deployment，讓你看到 AI-assisted development 可以怎麼進入比較完整的開發流程。

## 實務上該怎麼用這份教學

如果你要把這份 codelab 當成練習，可以照下面的方式做：

1. 先用官方 prompt 做出雪花與氣球版本，不要急著改需求。
2. 確認兩個按鈕都能觸發動畫。
3. 用第二段 prompt 修改其中一個行為，例如動畫大小、速度或顏色。
4. 看 AI Studio 是否能正確保留原功能，同時完成你的修改。
5. 點擊 Publish 部署到 Cloud Run。
6. 打開 App URL，確認雲端版本和 AI Studio 預覽版一致。
7. 做完後點擊 Unpublish app。

如果你想進一步練習，可以把 prompt 改成更貼近日常需求，例如：

- 建立一個簡單投票頁面。
- 建立一個課堂倒數計時器。
- 建立一個待辦事項清單。
- 建立一個產品功能展示頁。

但不管做什麼，都要保留同一個流程：先明確描述互動，再測試結果，最後部署與清理。

## 下一步可以接什麼

官方在最後推薦了幾份文件：

- Prompt Design Strategies：學習如何設計更穩定的 prompt、system instructions、few-shot examples 與輸出格式。
- Function Calling with the Gemini API：讓 Gemini 連接外部工具與 API，輸出結構化資料並觸發真實邏輯。
- Text-to-Speech Generation：使用 Gemini API 產生語音，控制語音風格，並在 AI Studio 的 Voice Library 測試聲音。

這些方向剛好對應三種進階能力：

- prompt 更準，讓生成結果更接近需求。
- function calling 讓應用程式能做真實任務，不只是展示畫面。
- text-to-speech 讓應用程式有語音互動能力。

也就是說，這份 codelab 是一個很小的入口。真正往後走，會從「做出畫面」進到「串接模型、工具、API 與多模態能力」。

## 一句話總結

「Deploy from AI Studio to Cloud Run」這份 codelab 的核心，是把 AI 生成原型接上雲端部署流程。

它讓你看到一個很務實的新工作方式：用 AI Studio 快速把想法做成 web app，用 Cloud Run 讓它變成可被連線的服務，最後用 Unpublish 把實驗資源收乾淨。這不是大型系統架構教學，但它完整示範了 AI 原型進入真實部署的最短路徑。
