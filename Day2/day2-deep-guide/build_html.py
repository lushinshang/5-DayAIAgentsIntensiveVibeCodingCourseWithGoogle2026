"""
建立 Day 2 直播深度導讀 index.html
參考 Day 1 day1-deep-guide/index.html 的結構與樣式
"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TRANSCRIPT_FILE = os.path.join(BASE_DIR, "../source/livestream/transcript_fragment.html")

with open(TRANSCRIPT_FILE, "r", encoding="utf-8") as f:
    transcript_html = f.read()

VIDEO_URL = "https://github.com/lushinshang/5-DayAIAgentsIntensiveVibeCodingCourseWithGoogle2026/releases/download/DAY_1_Livestream/DAY.2.Livestream.-.5-Days.of.AI.Agents.Intensive.Vibe.Coding.Course.With.Google_compressed.mp4"

HTML = f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>你的整合程式碼，正在成為技術債：從協定棧理解 Agent 時代的新基礎設施</title>
<meta name="description" content="Kaggle × Google 5-Day AI Agents Intensive Course Day 2 直播深度導讀。MCP/A2A/A2UI/AP2 四層協定棧、Token 是新石油、資料庫的 Agent-first 轉型。">
<style>
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

:root {{
  --bg: #f9f7f4;
  --text: #1a1a1a;
  --text-light: #555;
  --accent: #2d5be3;
  --accent-soft: #e8eefb;
  --warn: #c0392b;
  --warn-soft: #fdf0ef;
  --tip: #1a7a4a;
  --tip-soft: #edfaf3;
  --q-soft: #fdf8ed;
  --border: #e0ddd8;
  --nav-bg: rgba(249,247,244,0.95);
  --font: "Noto Sans TC", "PingFang TC", "Microsoft JhengHei", sans-serif;
}}

html {{ scroll-behavior: smooth; }}
body {{
  font-family: var(--font);
  background: var(--bg);
  color: var(--text);
  font-size: 16px;
  line-height: 1.68;
  -webkit-font-smoothing: antialiased;
}}

/* NAV */
nav {{
  position: sticky; top: 0; z-index: 100;
  background: var(--nav-bg);
  backdrop-filter: blur(8px);
  border-bottom: 1px solid var(--border);
  height: 56px; display: flex; align-items: center;
}}
.nav-inner {{
  max-width: 1120px; margin: 0 auto; padding: 0 24px;
  width: 100%; overflow-x: auto; white-space: nowrap;
  scrollbar-width: none; display: flex; gap: 6px;
}}
.nav-inner::-webkit-scrollbar {{ display: none; }}
nav a {{
  display: inline-block; padding: 6px 14px; font-size: 13px;
  color: var(--text-light); text-decoration: none;
  border-radius: 20px; transition: background 0.18s, color 0.18s; flex-shrink: 0;
}}
nav a:hover {{ background: var(--accent-soft); color: var(--accent); }}
.nav-back {{
  background: var(--accent) !important; color: #fff !important;
  font-weight: 700;
}}
.nav-back:hover {{ background: #1e3fad !important; }}

/* PAGE WRAP */
.page-wrap {{ max-width: 1120px; margin: 0 auto; padding: 0 24px 80px; }}

/* HERO */
.hero {{ padding: 56px 0 40px; max-width: 720px; margin: 0 auto; }}
.hero-tag {{
  display: inline-block; font-size: 12px; letter-spacing: 0.08em;
  text-transform: uppercase; color: var(--accent); background: var(--accent-soft);
  padding: 4px 12px; border-radius: 12px; margin-bottom: 20px;
}}
.hero h1 {{
  font-size: clamp(1.9rem, 4.5vw, 3.2rem); font-weight: 800;
  line-height: 1.22; color: var(--text); text-wrap: balance; margin-bottom: 20px;
}}
.hero-meta {{
  font-size: 14px; color: var(--text-light);
  border-left: 3px solid var(--border); padding-left: 14px; line-height: 1.6;
}}

/* VIDEO */
.video-section {{
  margin: 0 0 56px;
}}
.video-inner {{
  background: #1e1e2e; border-radius: 14px; overflow: hidden;
  box-shadow: 0 6px 32px rgba(0,0,0,0.18);
}}
.video-label {{
  background: #1e1e2e; color: #a6adc8;
  font-size: 13px; padding: 10px 20px;
  border-bottom: 1px solid #313244;
}}
.video-label strong {{ color: #89b4fa; }}
.video-inner video {{
  width: 100%; display: block;
  max-height: 560px; background: #000;
}}

/* SUMMARY FIGURE */
figure.summary-figure {{ margin: 36px 0 48px; padding: 0; }}
figure.summary-figure img {{
  width: 100%; max-width: 700px; display: block; margin: 0 auto;
  border-radius: 12px; object-fit: contain;
  box-shadow: 0 6px 24px rgba(0,0,0,0.10); cursor: zoom-in;
}}

/* ARTICLE */
article {{ max-width: 720px; margin: 0 auto; }}
article h2 {{
  font-size: clamp(1.25rem, 3vw, 1.65rem); font-weight: 700;
  line-height: 1.3; margin: 56px 0 20px; color: var(--text);
  text-wrap: balance; padding-bottom: 10px; border-bottom: 2px solid var(--border);
}}
article p {{ margin-bottom: 18px; }}
article strong {{ font-weight: 700; }}
article ul, article ol {{ margin: 12px 0 20px 24px; }}
article li {{ margin-bottom: 8px; }}
article code {{
  font-family: "SF Mono","Fira Code","Consolas",monospace;
  font-size: 0.88em; background: #eeecea;
  padding: 2px 6px; border-radius: 4px;
}}
article pre {{
  background: #1e1e2e; color: #cdd6f4;
  padding: 20px 24px; border-radius: 10px;
  overflow-x: auto; font-size: 14px; line-height: 1.6; margin: 24px 0;
}}
article pre code {{ background: none; padding: 0; color: inherit; }}
hr {{ border: none; border-top: 1px solid var(--border); margin: 40px 0; }}

/* CALLOUT BOXES */
.callout {{
  border-radius: 10px; padding: 16px 20px; margin: 24px 0;
  font-size: 15px; line-height: 1.65;
}}
.callout-label {{
  font-weight: 700; font-size: 13px; display: block;
  margin-bottom: 6px; letter-spacing: 0.03em;
}}
.callout-def {{ background: var(--accent-soft); border-left: 4px solid var(--accent); }}
.callout-def .callout-label {{ color: var(--accent); }}
.callout-tip {{ background: var(--tip-soft); border-left: 4px solid var(--tip); }}
.callout-tip .callout-label {{ color: var(--tip); }}
.callout-warn {{ background: var(--warn-soft); border-left: 4px solid var(--warn); }}
.callout-warn .callout-label {{ color: var(--warn); }}
.callout-think {{ background: var(--q-soft); border-left: 4px solid #d4a017; }}
.callout-think .callout-label {{ color: #9a6f00; }}

/* SECTION FIGURES */
figure.section-figure {{ margin: 32px 0; }}
figure.section-figure img {{
  width: 100%; max-width: 860px; display: block; margin: 0 auto;
  border-radius: 10px; object-fit: contain;
  box-shadow: 0 4px 20px rgba(0,0,0,0.09); cursor: zoom-in;
}}
figure.section-figure figcaption {{
  text-align: center; font-size: 13px; color: var(--text-light);
  margin-top: 10px; line-height: 1.54;
}}

/* FORMULA BLOCK */
.formula-block {{
  background: #1e1e2e; color: #cdd6f4;
  border-radius: 12px; padding: 28px 32px; margin: 28px 0; text-align: center;
}}
.formula-main {{
  font-size: clamp(1.4rem, 4vw, 2rem); font-weight: 800;
  letter-spacing: 0.02em; color: #89b4fa; margin-bottom: 8px;
}}
.formula-sub {{ font-size: 14px; color: #a6adc8; }}

/* PROTOCOL LAYERS */
.protocol-stack {{
  display: flex; flex-direction: column; gap: 12px; margin: 24px 0;
}}
.protocol-layer {{
  display: flex; gap: 16px; align-items: flex-start;
  background: #fff; border: 1px solid var(--border);
  border-radius: 10px; padding: 16px 20px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}}
.protocol-layer-num {{
  font-size: 22px; font-weight: 900; color: var(--accent);
  min-width: 32px; text-align: center; flex-shrink: 0; line-height: 1;
  padding-top: 2px;
}}
.protocol-layer-body {{ flex: 1; }}
.protocol-layer-title {{ font-weight: 700; font-size: 15px; margin-bottom: 4px; }}
.protocol-layer-desc {{ font-size: 14px; color: var(--text-light); line-height: 1.55; }}

/* TOKEN TABLE */
.token-tips {{
  background: #1e1e2e; color: #cdd6f4;
  border-radius: 12px; padding: 24px 28px; margin: 24px 0;
}}
.token-tips h4 {{ color: #89b4fa; font-size: 14px; margin-bottom: 14px; letter-spacing: 0.06em; }}
.token-tips ul {{ list-style: none; padding: 0; margin: 0; }}
.token-tips li {{
  padding: 6px 0; border-bottom: 1px solid #313244;
  font-size: 14px; line-height: 1.55; display: flex; gap: 10px;
}}
.token-tips li:last-child {{ border-bottom: none; }}
.token-tips .tip-icon {{ color: #a6e3a1; flex-shrink: 0; }}

/* CLOSING QUOTE */
.closing-quote {{
  border-left: 4px solid var(--accent); background: var(--accent-soft);
  padding: 20px 24px; border-radius: 0 10px 10px 0;
  font-size: 1.1rem; line-height: 1.7; margin: 28px 0; font-style: italic;
}}

/* TRANSCRIPT */
.transcript-section {{
  max-width: 720px; margin: 64px auto 0; padding-top: 40px;
  border-top: 2px solid var(--border);
}}
.transcript-section h2 {{
  font-size: 1.2rem; font-weight: 700; margin-bottom: 16px; color: var(--text);
}}
.transcript-toggle {{
  width: 100%; cursor: pointer; list-style: none;
  background: #fff; border: 1px solid var(--border);
  border-radius: 10px; padding: 14px 20px;
  font-size: 14px; color: var(--text-light);
  transition: background 0.15s; margin-bottom: 0;
}}
.transcript-toggle:hover {{ background: var(--accent-soft); }}
details[open] .transcript-toggle {{ border-radius: 10px 10px 0 0; }}
.transcript-body {{
  background: #fff; border: 1px solid var(--border); border-top: none;
  border-radius: 0 0 10px 10px; padding: 24px;
  font-size: 14px; line-height: 1.72; color: var(--text);
}}
.transcript-turn {{ margin-bottom: 20px; }}
.transcript-turn:last-child {{ margin-bottom: 0; }}
.spk-badge {{
  display: inline-block; font-size: 11px; font-weight: 700;
  padding: 3px 10px; border-radius: 12px; border: 1px solid;
  margin-bottom: 6px; letter-spacing: 0.02em;
}}
.transcript-turn p {{
  margin: 0; color: var(--text-light); line-height: 1.72;
}}

/* LIGHTBOX */
.lightbox {{
  display: none; position: fixed; inset: 0; z-index: 999;
  background: rgba(0,0,0,0.92); align-items: center; justify-content: center;
  flex-direction: column; gap: 14px;
}}
.lightbox.is-open {{ display: flex; }}
.lightbox img {{
  max-width: 92vw; max-height: 88vh; border-radius: 8px;
  box-shadow: 0 8px 40px rgba(0,0,0,0.5); object-fit: contain;
}}
.lightbox-hint {{ color: rgba(255,255,255,0.5); font-size: 13px; }}

/* FOOTER */
footer {{
  margin-top: 64px; padding: 24px 0 0;
  border-top: 1px solid var(--border);
  font-size: 13px; color: var(--text-light); text-align: center;
  max-width: 720px; margin-left: auto; margin-right: auto;
}}

@media (max-width: 640px) {{
  .protocol-layer {{ flex-direction: column; gap: 8px; }}
  .protocol-layer-num {{ font-size: 18px; }}
}}
</style>
</head>
<body>

<!-- NAV -->
<nav>
  <div class="nav-inner">
    <a class="nav-back" href="../index.html">← 返回 Day 2 主頁</a>
    <a href="#sec-nxm">NxM 問題</a>
    <a href="#sec-protocols">協定棧</a>
    <a href="#sec-token">Token 新石油</a>
    <a href="#sec-database">資料庫轉型</a>
    <a href="#sec-boundary">邊界消融</a>
    <a href="#sec-video">直播影片</a>
    <a href="#transcript">原文逐字稿</a>
  </div>
</nav>

<div class="page-wrap">

  <!-- HERO -->
  <div class="hero">
    <span class="hero-tag">Day 2 直播深度導讀 · 2026-06-17</span>
    <h1>你的整合程式碼，正在成為技術債</h1>
    <p class="hero-meta">
      Kaggle × Google 5-Day AI Agents Intensive Course — Day 2<br>
      主題：MCP / A2A / A2UI / AP2 四層協定棧 · Token 是新石油 · Agent-first 資料庫<br>
      講者：Smitha Kohlan、Anant Navalgariya、Alan、Kanchana、Mike、Pierre、Fran Hinkelman
    </p>
  </div>

  <!-- VIDEO SECTION (Hero 正下方，參考 Day 1 做法) -->
  <div class="video-section" id="sec-video">
    <div class="video-inner">
      <div class="video-label"><strong>▶ Day 2 直播錄影</strong> — Agent Tools &amp; Interoperability</div>
      <video controls preload="metadata">
        <source src="{VIDEO_URL}" type="video/mp4">
        您的瀏覽器不支援影片播放，請直接下載觀看。
      </video>
    </div>
  </div>

  <!-- SUMMARY FIGURE — NxM 複雜度對比 -->
  <figure class="summary-figure" id="sec-start">
    <picture>
      <source media="(max-width: 640px)" srcset="images/nxm-complexity-mobile.png">
      <img src="images/nxm-complexity.png" alt="MCP 協定將整合複雜度從 O(N×M) 降為 O(N+M)">
    </picture>
  </figure>

  <!-- ARTICLE -->
  <article>

    <!-- Section 1: NxM -->
    <h2 id="sec-nxm">五個模型、十個工具——恭喜你，欠了五十筆整合債</h2>

    <p>想像一個工程師的日常。他的 Coding Agent 要連 GitHub 拉 Issue、連 BigQuery 跑數據、連 Jira 更新狀態、連自家 API 撈設定，再連 Slack 發通知。五個工具，一個模型，五條客製程式碼。還算好。</p>

    <p>幾個月後，組織決定同時跑 Gemini、Claude，加一個開源模型做比較。工具也從五個長到十個。</p>

    <p>你打開試算表計算了一下：三個模型 × 十個工具 = <strong>三十條整合要維護</strong>。每次有任何一個工具的 API 改版，全部都得跟著動。某個廠商偷偷把參數名稱從 <code>user_id</code> 改成 <code>userId</code>，你下午三點接到的 PagerDuty 警報就能說明問題的規模。</p>

    <div class="formula-block">
      <div class="formula-main">O(N × M) → O(N + M)</div>
      <div class="formula-sub">N 個模型 × M 個工具 → 只需 N + M 個標準連接<br>這是 MCP 對 AI 整合複雜度的根本重設</div>
    </div>

    <p>這不是特例。這是 Day 2 白皮書開宗明義點出的 <strong>NxM 問題</strong>——業界所有 AI 整合工程師都在同一個沼澤裡打滾，只是深度不同。</p>

    <div class="callout callout-def">
      <span class="callout-label">📌 核心命題</span>
      NxM 問題的根本，不是工程師不夠勤快，而是整個行業缺少一個共同語言。回想網際網路的誕生：在 TCP/IP 確立之前，不同廠商的電腦根本無法互相溝通。協定的出現，終結了「翻譯大戰」。AI Agent 的現況，幾乎是在重演同一部戲。
    </div>

    <!-- Section 2: Protocol Stack -->
    <h2 id="sec-protocols">協定棧：從插頭到合約，四層解決四個問題</h2>

    <p>Day 2 白皮書提出了一套完整的協定棧，解決 Agent 連接世界時的四個不同問題。理解這四層，才能看懂整個 Agent 生態系的設計邏輯。</p>

    <div class="protocol-stack">
      <div class="protocol-layer">
        <div class="protocol-layer-num">1</div>
        <div class="protocol-layer-body">
          <div class="protocol-layer-title">MCP — 工具連接的 USB-C</div>
          <div class="protocol-layer-desc">Model Context Protocol。解決「模型連工具」的問題。定義標準介面，讓任何 MCP 相容工具可接上任何 MCP 相容模型，不需客製配對程式碼。複雜度從 O(N×M) 降為 O(N+M)。</div>
        </div>
      </div>
      <div class="protocol-layer">
        <div class="protocol-layer-num">2</div>
        <div class="protocol-layer-body">
          <div class="protocol-layer-title">A2A — Agent 之間的外交語言</div>
          <div class="protocol-layer-desc">Agent to Agent Protocol。解決「Agent 協作」的問題。已捐贈 Linux 基金會。讓 Agent 透過 Registry 發現彼此、閱讀 Agent Card、非同步委派任務。判斷原則：需要結果用 MCP，需要另一個 Agent 負責一段工作用 A2A。</div>
        </div>
      </div>
      <div class="protocol-layer">
        <div class="protocol-layer-num">3</div>
        <div class="protocol-layer-body">
          <div class="protocol-layer-title">A2UI — 讓 Agent 能驅動你的設計系統</div>
          <div class="protocol-layer-desc">Agent to UI Protocol。解決「Agent 輸出 UI」的問題。不讓 Agent 生成任意程式碼，而是組合來自 Catalog 的元件，輸出聲明式 JSON 配置。你的設計系統、品牌語言、無障礙設計全部保留，Agent 只決定「需要什麼 UI」。</div>
        </div>
      </div>
      <div class="protocol-layer">
        <div class="protocol-layer-num">4</div>
        <div class="protocol-layer-body">
          <div class="protocol-layer-title">AP2 / UCP — Agent 的採購部門與支付閘道</div>
          <div class="protocol-layer-desc">Agent Payment Protocol + Universal Commerce Protocol。解決「Agent 執行商業交易」的問題。嚴格的人工簽核授權（mandate）限定條件——最多花多少、買什麼類別、在哪個供應商範圍。Agent 在這個沙箱裡行動，跑不出去。</div>
        </div>
      </div>
    </div>

    <figure class="section-figure" id="fig-protocols">
      <picture>
        <source media="(max-width: 640px)" srcset="images/nxm-complexity-mobile.png">
        <img src="images/nxm-complexity.png" alt="MCP 協定將整合複雜度從 O(N×M) 降為 O(N+M)">
      </picture>
      <figcaption>MCP 作為統一標準介面，讓 N 個模型 × M 個工具的整合問題，從 O(N×M) 降為線性的 O(N+M)</figcaption>
    </figure>

    <div class="callout callout-tip">
      <span class="callout-label">💡 設計系統的正確心態</span>
      A2UI 不是在取代設計系統，而是在讓 Agent 能驅動設計系統。你的前端、你的元件庫、你的樣式，全部保留。Agent 學會的是你的 UI 語言，不是自己發明一套。這個邊界很清楚：你的品牌識別是護城河，Agent 幫你讓它更靈活地服務使用者。
    </div>

    <div class="callout callout-warn">
      <span class="callout-label">⚠️ MCP 的安全邊界不能事後補</span>
      MCP 強迫你在設計階段就思考安全邊界。一個資料庫的 MCP 工具，應該只開放 SELECT，完全鎖死 DDL 和 DML。安全不是功能，是架構決策——讓 Agent 操作生產資料庫的讀寫副本，而不是主庫，這類選擇必須在設計 MCP 工具時就做好。
    </div>

    <!-- Section 3: Token -->
    <h2 id="sec-token">Token 是新石油——但大多數人還沒意識到</h2>

    <figure class="section-figure">
      <picture>
        <source media="(max-width: 640px)" srcset="images/token-oil-mobile.png">
        <img src="images/token-oil.png" alt="Token 是新石油：從資料到精煉燃料">
      </picture>
      <figcaption>資料是原料，Token 才是精煉燃料——模型路由、快取、精簡提示詞、一鍵切斷，是 Agent 時代的省油策略</figcaption>
    </figure>

    <p>整場 Q&amp;A 裡，有一句話讓人停下來重複讀了幾遍：</p>

    <div class="closing-quote">
      <p><em>「如果說過去十年的口號是『資料是新石油』，那在 AI Agent 的時代，Token 就是新石油。資料只是原料，Token 才是那個真正驅動引擎的精煉燃料。」</em></p>
    </div>

    <p>當一個 Agent 持續運行、反覆呼叫工具、與其他 Agent 協作、在 A2UI 生成 UI，每一步都在燃燒 Token。一個設計不良的 Agent 可以在幾小時內燒掉整個月的 API 預算。企業已經開始對員工的 AI 使用設置 Token 配額——這不是暫時管控，而是訊號：<strong>Token 的財務管理，將成為 Agent 時代的核心工程能力</strong>。</p>

    <div class="token-tips">
      <h4>▸ 省 Token 的四個架構策略</h4>
      <ul>
        <li><span class="tip-icon">◆</span> <strong>模型選擇分層</strong>：不是所有任務都需要最強的模型。路由簡單任務給輕量模型，省下的 Token 用在真正需要推理的地方。</li>
        <li><span class="tip-icon">◆</span> <strong>快取重複呼叫</strong>：重複的工具呼叫、重複的文件讀取，是 Token 浪費的重災區。快取命中 = 零 Token 成本。</li>
        <li><span class="tip-icon">◆</span> <strong>Prompt 工程仍有效</strong>：要求 Agent 用條列格式回應而不是長段落，可顯著降低輸出 Token 數。工程師使用「請用bullet points」這個簡單技巧節省了大量成本。</li>
        <li><span class="tip-icon">◆</span> <strong>Kill Switch 要內建</strong>：不是事後加上去的功能，而是架構設計的一部分。ADK 的 <code>max_iterations</code> 參數、Cloud 層的帳單預算上限，都是防護機制的一環。</li>
      </ul>
    </div>

    <div class="callout callout-think">
      <span class="callout-label">🧪 架構思考驗證</span>
      你的 Agent 系統，有沒有辦法在不停機的情況下，知道「現在的 Token 消耗速率是否異常」？如果沒有，你的 Kill Switch 其實是事後補救而不是預防性設計。
    </div>

    <!-- Section 4: Database -->
    <h2 id="sec-database">資料庫，還沒準備好迎接 Agent</h2>

    <p>有一個觀察在整場直播中相對低調，卻值得認真對待：<strong>我們的資料庫，是為人類設計的</strong>。</p>

    <p>它的介面、它的錯誤訊息、它的查詢語言、它的回傳格式——全部都在假設使用者是一個看著螢幕、能理解上下文、會重試的人類。但 Agent 是截然不同的消費者。它沒有人類的風險直覺，它可能在毫秒內發出一百個查詢、它無法自行判斷「這個錯誤代碼代表什麼、我應該退後還是重試」。</p>

    <p>真正的 Agent-first 資料庫架構，意味著：</p>
    <ul>
      <li>讓 Agent 可以透過 <strong>SSE（Server-Sent Events）</strong> 直接串流資料，而不必透過外部 orchestration</li>
      <li>提供 <strong>Agent 專屬的 RBAC</strong>（角色存取控制），而不是讓 Agent 用人類帳號登入</li>
      <li>回傳的 <strong>Payload 要為 Agent 的理解能力優化</strong>，而不是為人類的閱讀習慣優化</li>
      <li>內建 <strong>Telemetry</strong>，讓監控系統能追蹤 Agent 的行為模式</li>
    </ul>

    <div class="callout callout-def">
      <span class="callout-label">📌 Agent Experience ≠ Developer Experience</span>
      過去幾十年，資料庫廠商一直在優化「開發者體驗」（DX）。現在，當 Agent 成為資料庫的主要使用者，我們需要開始思考「Agent 體驗」（AX）。這不只是技術問題，而是誰先重新設計好 AX，誰就在 Agent-first 世界取得先機。
    </div>

    <!-- Section 5: Boundary -->
    <h2 id="sec-boundary">邊界正在消失，但責任沒有</h2>

    <figure class="section-figure">
      <picture>
        <source media="(max-width: 640px)" srcset="images/db-evolution-mobile.png">
        <img src="images/db-evolution.png" alt="資料庫必須從 Human-first 進化為 Agent-first">
      </picture>
      <figcaption>Human-first 資料庫為人類設計，Agent-first 資料庫為 Agent 最佳化：SSE 串流、結構化 JSON、代理 RBAC、內建遙測</figcaption>
    </figure>

    <p>整場直播的最後，有人問了一個讓所有講者都停下來思考的問題：<strong>下一個 AI 重大突破，會來自更好的基礎模型，還是來自 Agent 自主開發工具？</strong></p>

    <p>答案是：都是，但更重要的問題是，突破的計量單位正在改變。過去我們計算模型的 benchmark 分數。現在我們開始計算整個系統的效能：正確的模型、正確的上下文、正確的時機、正確的工具組合。<strong>「Loop Engineering」</strong>這個新詞出現在直播中——不只優化模型，而是優化整個 Agent 的運行迴圈。</p>

    <p>同時，另一個更深層的變化正在發生：<strong>開發者和消費者之間的邊界，正在消融</strong>。一個從來不是職業工程師的人，靠著 Vibe Coding 工具寫出了一個產品，賣出了十位數的估值。這不是單一事件，而是一個正在加速的趨勢。</p>

    <div class="callout callout-warn">
      <span class="callout-label">⚠️ 自由度增加，責任感不會自動跟上</span>
      把你學會的協定，用在保護使用者資料、設計透明的授權機制、內建可觀測性——這才是從 Vibe Coding 走向 Agentic Engineering 的完整路程。協定讓 Agent 能說話，你的設計讓 Agent 說的話值得信任。
    </div>

    <div class="closing-quote">
      <p><em>「就像一輛車，你可以開得多快都可以，但路上還有其他人。你有能力做到很多事，但你也有責任去設計好的架構、保護使用者的資料。」</em></p>
    </div>

    <hr>

  </article>

  <!-- TRANSCRIPT SECTION -->
  <section class="transcript-section" id="transcript">
    <h2>原文逐字稿（含講者識別）</h2>
    <details>
      <summary class="transcript-toggle">
        ▸ 展開英文原文逐字稿（共 60 段，含 Smitha / Anant / Alan / Kanchana / Mike / Pierre / Fran 講者識別）
      </summary>
      <div class="transcript-body">
        {transcript_html}
      </div>
    </details>
  </section>

  <footer>
    <p>本文整合 Kaggle × Google 5-Day AI Agents Intensive Course Day 2 直播內容，結合 deep-guide 敘事框架與 ai-mentor-agents 教學框架撰寫。</p>
  </footer>

</div><!-- /page-wrap -->

<!-- Lightbox -->
<div class="lightbox" id="lightbox">
  <span class="lightbox-hint">點擊或按 Esc 關閉</span>
  <img src="" alt="">
</div>

<script>
(function(){{
  var lightbox = document.getElementById("lightbox");
  var lightboxImg = lightbox.querySelector("img");
  function openLightbox(img){{
    lightboxImg.src = img.currentSrc || img.src;
    lightboxImg.alt = img.alt;
    lightbox.classList.add("is-open");
  }}
  function closeLightbox(){{
    lightbox.classList.remove("is-open");
    lightboxImg.src = "";
  }}
  document.querySelectorAll("figure img").forEach(function(img){{
    img.addEventListener("click", function(){{ openLightbox(img); }});
  }});
  lightbox.addEventListener("click", closeLightbox);
  document.addEventListener("keydown", function(e){{
    if(e.key === "Escape") closeLightbox();
  }});
}})();
</script>

</body>
</html>"""

out_path = os.path.join(BASE_DIR, "index.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(HTML)
print(f"完成：{out_path} ({len(HTML)} chars)")
