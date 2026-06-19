"""
建立 Day 3 直播深度導讀 index.html
參考 Day 1 & Day 2 day-deep-guide/index.html 的結構與樣式
"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TRANSCRIPT_FILE = os.path.join(BASE_DIR, "../source/livestream/transcript_fragment.html")
OUTPUT_FILE = os.path.join(BASE_DIR, "index.html")

if not os.path.exists(TRANSCRIPT_FILE):
    # Fallback
    transcript_html = "<p>逐字稿整理中...</p>"
else:
    with open(TRANSCRIPT_FILE, "r", encoding="utf-8") as f:
        transcript_html = f.read()

VIDEO_URL = "https://github.com/lushinshang/5-DayAIAgentsIntensiveVibeCodingCourseWithGoogle2026/releases/download/DAY_1_Livestream/DAY.3.Livestream.-.5-Days.of.AI.Agents.Intensive.Vibe.Coding.Course.With.Google_compressed.mp4"

HTML = f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>從 Skills 實踐走向系統化評估：解構 Agent 技能的核心運作與安全防護線</title>
<meta name="description" content="Kaggle × Google 5-Day AI Agents Intensive Course Day 3 直播深度導讀。Skill Anatomy、漸進式載入、評估驅動開發迴圈、Meta-Skills 治理。">
<style>
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

:root {{
  --bg: #f9f7f4;
  --text: #1a1a1a;
  --text-light: #555;
  --accent: #a8554a; /* Day3 主題色，偏紅棕色 */
  --accent-soft: #f7eded;
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
.nav-back:hover {{ background: #8e3f35 !important; }}

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
.video-label strong {{ color: #eba0ac; }}
.video-inner video {{
  width: 100%; display: block;
  max-height: 560px; background: #000;
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

/* TRANSCRIPT DETAILS */
details.transcript-section {{
  background: #fff; border: 1px solid var(--border);
  border-radius: 12px; padding: 24px; margin: 60px 0;
  box-shadow: 0 4px 16px rgba(0,0,0,0.03);
}}
details.transcript-section summary {{
  font-weight: 700; font-size: 18px; cursor: pointer;
  color: var(--accent); outline: none; list-style: none;
  display: flex; justify-content: space-between; align-items: center;
}}
details.transcript-section summary::-webkit-details-marker {{ display: none; }}
details.transcript-section summary::after {{
  content: "▼"; font-size: 12px; transition: transform 0.2s;
}}
details[open].transcript-section summary::after {{
  transform: rotate(180deg);
}}
.transcript-wrap {{
  margin-top: 24px; border-top: 1px solid var(--border);
  padding-top: 20px; display: flex; flex-direction: column; gap: 24px;
}}
.transcript-turn {{
  display: flex; flex-direction: column; gap: 6px;
  padding-bottom: 16px; border-bottom: 1px dashed var(--border);
}}
.transcript-turn:last-child {{ border-bottom: none; }}
.spk-badge {{
  font-size: 11px; font-weight: 700; padding: 3px 10px;
  border-radius: 8px; border: 1px solid; align-self: flex-start;
  letter-spacing: 0.02em;
}}
.transcript-turn p {{ margin-bottom: 0; }}
.transcript-turn p.zh {{ font-weight: 500; font-size: 15px; color: var(--text); }}
.transcript-turn p.en {{ font-size: 13.5px; color: var(--text-light); }}

@media (max-width: 768px) {{
  .page-wrap {{ padding: 0 16px 60px; }}
  .hero {{ padding: 36px 0 24px; }}
  .video-inner {{ border-radius: 10px; }}
  details.transcript-section {{ padding: 16px; }}
}}
</style>
</head>
<body>

<nav>
  <div class="nav-inner">
    <a href="../index.html" class="nav-back">← 返回 Day 3 首頁</a>
    <a href="#intro">導讀簡介</a>
    <a href="#anatomy">Skill Anatomy</a>
    <a href="#evaluation">評估開發圈</a>
    <a href="#governance">治理與溢出</a>
    <a href="#meta-skills">Meta-Skills</a>
    <a href="#transcript">中英雙語逐字稿</a>
  </div>
</nav>

<div class="page-wrap">
  <header class="hero">
    <span class="hero-tag">Day 3 Livestream AMA</span>
    <h1>從 Skills 實踐走向系統化評估：解構 Agent 技能的核心運作與安全防護線</h1>
    <div class="hero-meta">
      <p><strong>對談嘉賓</strong>：Smitha Kolan, Anant Nalgaria, Tanvi Singhal, Gabriella Hernandez, Paulong, Julia, Debanshu</p>
      <p><strong>核心議題</strong>：解決 prompt 膨脹與 context rot、精確評估工具軌跡與 token 預算，以及生產環境下的自修復安全治理。</p>
    </div>
  </header>

  <section class="video-section">
    <div class="video-inner">
      <div class="video-label">📺 <strong>Google Live Stream</strong>: Day 3 直播導讀與 AMA</div>
      <video controls preload="metadata">
        <source src="{VIDEO_URL}" type="video/mp4">
        您的瀏覽器不支援 HTML5 影片播放。
      </video>
    </div>
  </section>

  <main>
    <article>
      <section id="intro">
        <h2>導讀簡介：Skills 作為 Agent 演進的關鍵里程碑</h2>
        <p>在 Kaggle 和 Google 五天 AI Agent 密集課程的第三天，直播焦點圍繞在 <strong>Agent Skills（技能）</strong>。主辦人 Anant 與主持人 Smitha 指出，若要讓通用型 AI 代理在實務中具備專家般的執行力，絕不能靠無限制地擴增 System Prompt。這不僅會造成 Context Rot（脈絡腐爛），還會使 API Token 預算如流水般消耗，甚至大幅增加執行錯誤率。</p>
        <p>這場 AMA 邀請到了 Google 內部推動 Agent Skills 與 ADK（Agent Development Kit）的專家群，從技術細節到架構設計，共同探討如何將 domain experts 的 runbook/SOP，結晶化為 Agent 的「程序記憶」（procedural memory）。</p>
      </section>

      <section id="anatomy">
        <h2>第一章：Skill Anatomy — 漸進式載入的 USBC 協定</h2>
        <p>與會專家 Gabriella 與 Julia 強調，<strong>Skill 是一個精心設計的資料夾 primitive</strong>。它的核心是 <code>SKILL.md</code> 文件，並依據 <strong>Progressive Disclosure（漸進式揭露）</strong> 原則進行運作：</p>
        <div class="callout callout-def">
          <span class="callout-label">核心概念：漸進式揭露</span>
          <p>Agent 在初始狀態下，只會載入所有 Skill 的 <strong>metadata</strong>（名稱、描述與 trigger 觸發條件）。直到任務需求明確匹配、觸發閘門（Trigger Gate）開啟時，才會完整載入 <strong>body</strong> 內容。至於 references、assets 與 scripts 輔助腳本，則只有在執行期間被具體呼叫時才會按需載入。這完美解決了對話載入過多上下文的瓶頸。</p>
        </div>
        <p>這代表 Skill 的管理就像是「提示工程的動態載入系統」。它使得開發者可以把龐大的企業知識、API 說明與任務腳本封裝在一個個靈活的小模組中，隨插即用。</p>
      </section>

      <section id="evaluation">
        <h2>第二章：評估驅動開發圈 — 精確量化工具軌跡</h2>
        <p>當開發者進入生產環境時，如何評估技能的好壞成為了最棘手的課題。Tanvi 與 Debanshu 指出，技能評估不能只看最終輸出（Output Quality），而必須追蹤 <strong>Tool Trajectory（工具執行軌跡）</strong>：</p>
        <ul>
          <li><strong>觸發精準度（Trigger Precision）</strong>：Agent 是否在對的時間調用正確的 Skill，不造成過度調用（Over-invocation）或漏掉關鍵 Skill。</li>
          <li><strong>Token 預算限制（Token Budgeting）</strong>：如何在長對話中維持 Context Hygiene（脈絡衛生），藉由傳遞 pointer（指標）而非傳遞整個大資料集，來控制 API 成本。</li>
          <li><strong>軌跡合理性（Trajectory Auditing）</strong>：Agent 執行過程中是否有無效重複的 loop，或是嘗試呼叫無權限的 tools。</li>
        </ul>
        <p>這需要建立起一套自動化的評估 pipeline。在開發階段便將 assertion 寫進 eval datasets 中，在 pre-commit 或 CI/CD 流程中自動執行檢測，確保 Agent 在升級技能時不會發生向下相容性（backward compatibility）崩壞。</p>
      </section>

      <section id="governance">
        <h2>第三章：生產環境治理與 Context Overflow 的生存之道</h2>
        <p>直播中社群提問了許多關鍵痛點，特別是「如何防止 Agent 在執行複雜任務時耗盡 API 額度並陷入死循環？」。</p>
        <div class="callout callout-warn">
          <span class="callout-label">警告：無限循環與 API 預算黑洞</span>
          <p>當 Agent 無法順利完成任務，但 System Prompt 中缺乏明確的終止機制時，Agent 會嘗試不斷重試，並陷入不斷讀取歷史對話、重複產生相同無效指令的 loop。這不僅耗盡 token 預算，還會引起 Context Overflow。</p>
        </div>
        <p>Kanchana 與 Anant 建議從架構層面進行硬性防衛：</p>
        <ol>
          <li><strong>最大迭代上限（Max Iterations Cap）</strong>：在 ADK 中設置硬上限，限制 Agent 在單次任務中工具呼叫的次數，超標則強制「大聲失敗」（fail loudly）。</li>
          <li><strong>異常流量與異常行為偵測</strong>：透過 OTel（OpenTelemetry）與 GCP Cloud Trace 監控執行軌跡，及時向政策伺服器（Policy Server）匯報並觸發 Kill Switch。</li>
          <li><strong>分級模型調用</strong>：在路由與檢測等低複雜度關卡使用輕量模型（如 Gemini Flash），而將需要深度推理的步驟留給高級模型（如 Gemini Pro），實踐 Token 經濟學。</li>
        </ol>
      </section>

      <section id="meta-skills">
        <h2>第四章：Meta-Skills — 技能自體結晶與安全盲區</h2>
        <p>直播的 AMA 提到了一個極具前瞻性的概念：<strong>Meta-Skills（元技能）</strong>。意即 Agent 依據自己在生產環境中成功的 execution trajectory，自己結晶化（crystalize）並撰寫出新的 <code>SKILL.md</code>，將其納入 Skills 庫，實現「自我進化」（Self-Improving）。</p>
        <p>然而，專家們提醒，這是一把雙面刃。如果 Agent 可以在沒有人類審查（Human-in-the-loop）的情況下自訂技能，極有可能引入惡意的 execution flow，或者在代碼中埋下安全性漏洞。因此，即便實現 Meta-Skills，也必須在其加入生產環境之前，經過嚴格的自動化沙箱測試（Sandboxing）與安全性掃描閘門。</p>
      </section>

      <section id="conclusion">
        <h2>結語：建立你自己的「程序記憶庫」</h2>
        <p>誠如 DevRel 主管 Paulong 與 Anant 的總結，Agent Skills 就像是早期軟體開發中的<strong>巨集（Macros）</strong>，用以自動化並重複高難度動作。這項範式的建立意味著我們從「編寫代碼（vibe coding）」走向了「規則治理」。開發者現在應該著手將日常重複的工作流整理為 Skills 庫，這才是未來多代理人生態系統中最寶貴的企業知識資產。</p>
      </section>

      <hr>

      <section id="transcript">
        <details class="transcript-section">
          <summary>🎤 點此展開直播完整中英雙語逐字稿</summary>
          <div class="transcript-wrap">
            {transcript_html}
          </div>
        </details>
      </section>
    </article>
  </main>
</div>

</body>
</html>
"""

# 建立輸出目錄並寫入
os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(HTML)

print("index.html template generated successfully at day3-deep-guide/index.html")
