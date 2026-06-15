from __future__ import annotations

import html
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "google-antigravity-codelab-guide.normalized.md"
OUTPUT = ROOT / "google-antigravity-codelab-guide.html"


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
    lines = markdown_text.splitlines()
    out: list[str] = []
    nav: list[tuple[str, str]] = []
    paragraph: list[str] = []
    in_code = False
    code_lines: list[str] = []
    list_type: str | None = None
    in_quote = False

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

    for raw in lines:
        line = raw.rstrip()

        if line.startswith("```"):
            flush_paragraph(paragraph, out)
            close_quote()
            close_list()
            if in_code:
                out.append(
                    '<pre><code>'
                    + html.escape("\n".join(code_lines))
                    + "</code></pre>"
                )
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
            out.append(
                f'<h{level} id="{html.escape(section_id)}">{inline_md(text)}</h{level}>'
            )
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
        ordered = re.match(r"^\d+\.\s+(.+)$", line)
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
  <title>Google Antigravity 入門白話導讀</title>
  <meta name="description" content="以白話方式整理 Google Antigravity codelab，說明 Project、權限、MCP、Artifacts、IDE 與 Skills 的實務意義。">
  <style>
    :root {{
      --bg: #f7f4ee;
      --paper: #fffdf8;
      --text: #26231f;
      --muted: #6e665d;
      --line: #e4d9ca;
      --accent: #2f6f73;
      --accent-soft: #e6f1ef;
      --code-bg: #f0e8dc;
      --shadow: rgba(58, 45, 30, 0.08);
    }}
    * {{ box-sizing: border-box; }}
    html {{ scroll-behavior: smooth; }}
    body {{
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Noto Sans TC", "PingFang TC", "Microsoft JhengHei", sans-serif;
      color: var(--text);
      background:
        radial-gradient(circle at top left, rgba(47, 111, 115, 0.12), transparent 34rem),
        linear-gradient(180deg, #fbf7ef 0%, var(--bg) 34rem);
      line-height: 1.72;
      letter-spacing: 0;
    }}
    .hero {{
      max-width: 960px;
      margin: 0 auto;
      padding: 64px 24px 28px;
      text-align: center;
    }}
    .eyebrow {{
      margin: 0 0 16px;
      color: var(--accent);
      font-size: 0.92rem;
      font-weight: 700;
    }}
    h1 {{
      margin: 0;
      font-size: clamp(2.1rem, 4vw, 3.4rem);
      line-height: 1.16;
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
      background: rgba(247, 244, 238, 0.9);
      backdrop-filter: blur(14px);
      border-block: 1px solid rgba(228, 217, 202, 0.86);
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
      color: #355154;
      background: rgba(255, 253, 248, 0.72);
      border: 1px solid rgba(47, 111, 115, 0.16);
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
      background: rgba(255, 253, 248, 0.86);
      border: 1px solid rgba(228, 217, 202, 0.84);
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
      color: #355154;
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
      margin: 0 0 1.35em;
      padding: 16px;
      background: #292620;
      color: #fff7e8;
      border-radius: 12px;
      line-height: 1.55;
      overflow-wrap: normal;
    }}
    pre code {{
      background: transparent;
      color: inherit;
      padding: 0;
    }}
    strong {{ color: #1f4f52; }}
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
    <h1>Google Antigravity 入門白話導讀</h1>
    <p class="lead">把官方 codelab 的 10 個步驟整理成可讀的工程觀念：Agent 要有能力，也要有邊界、權限、證據與可重用規範。</p>
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
