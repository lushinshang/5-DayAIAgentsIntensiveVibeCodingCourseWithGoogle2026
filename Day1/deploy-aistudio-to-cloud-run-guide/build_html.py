from __future__ import annotations

import html
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "deploy-aistudio-to-cloud-run-guide.normalized.md"
OUTPUT = ROOT / "deploy-aistudio-to-cloud-run-guide.html"


def slugify(text: str) -> str:
    slug = re.sub(r"[^\w\u4e00-\u9fff]+", "-", text.lower()).strip("-")
    return slug or "section"


def inline_md(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    return escaped


def flush_paragraph(parts: list[str], out: list[str]) -> None:
    if parts:
        out.append(f"<p>{inline_md(' '.join(parts))}</p>")
        parts.clear()


def convert_markdown(markdown_text: str) -> tuple[str, list[tuple[str, str]]]:
    out: list[str] = []
    nav: list[tuple[str, str]] = []
    paragraph: list[str] = []
    code_lines: list[str] = []
    in_code = False
    in_quote = False
    list_type: str | None = None

    def close_list() -> None:
        nonlocal list_type
        if list_type:
            out.append(f"</{list_type}>")
            list_type = None

    def close_quote() -> None:
        nonlocal in_quote
        if in_quote:
            out.append("</blockquote>")
            in_quote = False

    for raw in markdown_text.splitlines():
        line = raw.rstrip()

        if line.startswith("```"):
            flush_paragraph(paragraph, out)
            close_quote()
            close_list()
            if in_code:
                out.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
                code_lines = []
                in_code = False
            else:
                in_code = True
            continue

        if in_code:
            code_lines.append(line)
            continue

        if not line:
            flush_paragraph(paragraph, out)
            close_quote()
            close_list()
            continue

        heading = re.match(r"^(#{1,3})\s+(.+)$", line)
        if heading:
            flush_paragraph(paragraph, out)
            close_quote()
            close_list()
            level = len(heading.group(1))
            text = heading.group(2).strip()
            section_id = slugify(text)
            if level == 2:
                nav.append((section_id, text))
            out.append(f'<h{level} id="{html.escape(section_id)}">{inline_md(text)}</h{level}>')
            continue

        if line.startswith("> "):
            flush_paragraph(paragraph, out)
            close_list()
            if not in_quote:
                out.append("<blockquote>")
                in_quote = True
            out.append(f"<p>{inline_md(line[2:].strip())}</p>")
            continue

        bullet = re.match(r"^-\s+(.+)$", line)
        ordered = re.match(r"^\d+[.。]\s+(.+)$", line)
        if bullet or ordered:
            flush_paragraph(paragraph, out)
            close_quote()
            wanted = "ul" if bullet else "ol"
            if list_type != wanted:
                close_list()
                out.append(f"<{wanted}>")
                list_type = wanted
            item = bullet.group(1) if bullet else ordered.group(1)
            out.append(f"<li>{inline_md(item.strip())}</li>")
            continue

        close_quote()
        close_list()
        paragraph.append(line.strip())

    flush_paragraph(paragraph, out)
    close_quote()
    close_list()
    return "\n".join(out), nav


def render_page(article_html: str, nav: list[tuple[str, str]]) -> str:
    nav_html = "\n".join(
        f'<a href="#{html.escape(section_id)}">{html.escape(title)}</a>'
        for section_id, title in nav
    )
    return f"""<!doctype html>
<html lang="zh-Hant-TW">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>從 AI Studio 到 Cloud Run：Vibe Coding 部署白話導讀</title>
  <meta name="description" content="以白話方式整理 Google codelab，說明如何從 AI Studio 建立 web app 原型，部署到 Cloud Run，並清理雲端資源。">
  <style>
    :root {{
      --bg: #f5f8f4;
      --paper: #fffef9;
      --text: #25251f;
      --muted: #6b6a5d;
      --line: #dce7d9;
      --accent: #3f6f3b;
      --accent-strong: #254f2a;
      --accent-soft: #e8f3e6;
      --code-bg: #eef0e5;
      --shadow: rgba(41, 64, 34, 0.09);
    }}
    * {{ box-sizing: border-box; }}
    html {{ scroll-behavior: smooth; }}
    body {{
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Noto Sans TC", "PingFang TC", "Microsoft JhengHei", sans-serif;
      color: var(--text);
      background:
        radial-gradient(circle at top right, rgba(87, 132, 72, 0.14), transparent 32rem),
        linear-gradient(180deg, #fbfaf0 0%, var(--bg) 36rem);
      line-height: 1.72;
      letter-spacing: 0;
    }}
    .hero {{
      max-width: 960px;
      margin: 0 auto;
      padding: 62px 24px 28px;
      text-align: center;
    }}
    .eyebrow {{
      margin: 0 0 16px;
      color: var(--accent);
      font-size: 0.92rem;
      font-weight: 750;
    }}
    h1 {{
      margin: 0;
      font-size: clamp(2rem, 4vw, 3.35rem);
      line-height: 1.17;
      text-wrap: balance;
    }}
    .lead {{
      max-width: 720px;
      margin: 22px auto 0;
      color: var(--muted);
      font-size: 1.08rem;
    }}
    .nav-wrap {{
      position: sticky;
      top: 0;
      z-index: 10;
      background: rgba(245, 248, 244, 0.9);
      backdrop-filter: blur(14px);
      border-block: 1px solid rgba(220, 231, 217, 0.9);
    }}
    nav {{
      max-width: 1120px;
      margin: 0 auto;
      padding: 10px 24px;
      display: flex;
      gap: 8px;
      overflow-x: auto;
      scrollbar-width: thin;
    }}
    nav a {{
      flex: 0 0 auto;
      color: var(--accent-strong);
      background: rgba(255, 254, 249, 0.78);
      border: 1px solid rgba(63, 111, 59, 0.18);
      border-radius: 999px;
      padding: 7px 12px;
      text-decoration: none;
      font-size: 0.9rem;
      line-height: 1.25;
    }}
    main {{
      max-width: 1120px;
      margin: 0 auto;
      padding: 34px 24px 72px;
    }}
    article {{
      max-width: 760px;
      margin: 0 auto;
      padding: 38px min(5vw, 54px);
      background: rgba(255, 254, 249, 0.88);
      border: 1px solid rgba(220, 231, 217, 0.92);
      border-radius: 18px;
      box-shadow: 0 18px 52px var(--shadow);
      overflow-wrap: anywhere;
    }}
    article > h1 {{ display: none; }}
    h2 {{
      margin: 2.2em 0 0.7em;
      font-size: clamp(1.42rem, 2.4vw, 2rem);
      line-height: 1.32;
      text-wrap: balance;
    }}
    h3 {{
      margin: 1.8em 0 0.55em;
      font-size: 1.16rem;
    }}
    p {{ margin: 0 0 1.05em; }}
    ul, ol {{
      margin: 0 0 1.2em;
      padding-left: 1.45em;
    }}
    li {{ margin: 0.35em 0; }}
    blockquote {{
      margin: 0 0 1.7em;
      padding: 16px 18px;
      border-left: 4px solid var(--accent);
      background: var(--accent-soft);
      color: var(--accent-strong);
      border-radius: 0 12px 12px 0;
    }}
    blockquote p:last-child {{ margin-bottom: 0; }}
    code {{
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 0.92em;
      background: var(--code-bg);
      border-radius: 5px;
      padding: 0.12em 0.35em;
    }}
    pre {{
      overflow-x: auto;
      overflow-wrap: normal;
      margin: 0 0 1.35em;
      padding: 16px;
      background: #252a20;
      color: #fbf8e9;
      border-radius: 12px;
      line-height: 1.55;
    }}
    pre code {{
      background: transparent;
      color: inherit;
      padding: 0;
    }}
    strong {{ color: var(--accent-strong); }}
    a {{ color: var(--accent); }}
    @media (max-width: 720px) {{
      .hero {{
        text-align: left;
        padding-top: 42px;
      }}
      article {{
        padding: 28px 20px;
        border-radius: 14px;
      }}
      nav {{ padding-inline: 16px; }}
      main {{ padding-inline: 14px; }}
    }}
  </style>
</head>
<body>
  <header class="hero">
    <p class="eyebrow">Day 1 補充導讀</p>
    <h1>從 AI Studio 到 Cloud Run</h1>
    <p class="lead">把官方 codelab 的 6 個步驟整理成白話流程：先用 vibe coding 做出原型，再部署成雲端服務，最後清理資源避免成本外溢。</p>
  </header>
  <div class="nav-wrap" aria-label="章節導覽">
    <nav>
      {nav_html}
    </nav>
  </div>
  <main>
    <article>
{article_html}
    </article>
  </main>
</body>
</html>
"""


def main() -> None:
    article_html, nav = convert_markdown(SOURCE.read_text(encoding="utf-8"))
    OUTPUT.write_text(render_page(article_html, nav), encoding="utf-8")
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
