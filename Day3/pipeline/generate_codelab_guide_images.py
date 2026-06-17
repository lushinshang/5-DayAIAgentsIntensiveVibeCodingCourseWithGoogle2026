from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
FONT_BOLD = "/System/Library/Fonts/STHeiti Medium.ttc"
FONT_REG = "/System/Library/Fonts/STHeiti Light.ttc"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, width: int) -> list[str]:
    lines: list[str] = []
    current = ""
    for ch in text:
        test = current + ch
        if draw.textbbox((0, 0), test, font=fnt)[2] <= width:
            current = test
        else:
            if current:
                lines.append(current)
            current = ch
    if current:
        lines.append(current)
    return lines


def rounded_box(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], fill: str, outline: str = "#d9d3c8") -> None:
    draw.rounded_rectangle(box, radius=18, fill=fill, outline=outline, width=2)


def draw_centered(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], text: str, fnt: ImageFont.FreeTypeFont, fill: str) -> None:
    x1, y1, x2, y2 = box
    lines = text.split("\n")
    line_h = fnt.size + 8
    y = y1 + ((y2 - y1) - line_h * len(lines)) / 2
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=fnt)
        draw.text((x1 + ((x2 - x1) - (bbox[2] - bbox[0])) / 2, y), line, font=fnt, fill=fill)
        y += line_h


def save_versions(name: str, render_func) -> None:
    folder = ROOT / name / "images"
    folder.mkdir(parents=True, exist_ok=True)
    for mobile, size, suffix in [(False, (1600, 900), ""), (True, (900, 1600), "-mobile")]:
        img = Image.new("RGB", size, "#f8f7f3")
        draw = ImageDraw.Draw(img)
        render_func(draw, size, mobile)
        img.save(folder / f"{name}{suffix}.png")


def render_antigravity(draw: ImageDraw.ImageDraw, size: tuple[int, int], mobile: bool) -> None:
    w, h = size
    draw.rectangle((0, 0, w, h), fill="#f8f7f3")
    title_f = font(54 if not mobile else 38, True)
    body_f = font(28 if not mobile else 30)
    small_f = font(24 if not mobile else 26)
    if mobile:
        draw.text((70, 54), "Antigravity Skills", font=title_f, fill="#163f44")
        draw.text((70, 104), "從大 Prompt 到按需載入", font=title_f, fill="#163f44")
        draw.text((74, 168), "metadata 常駐，內容觸發後載入", font=font(28), fill="#4f5b5d")
    else:
        draw.text((70, 54), "Antigravity Skills：從大 Prompt 到按需載入", font=title_f, fill="#163f44")
        draw.text((74, 128), "核心：metadata 常駐，body / references / scripts 只在觸發後載入。", font=body_f, fill="#4f5b5d")
    if not mobile:
        boxes = [
            (80, 250, 390, 430, "1\nSKILL.md\n觸發描述"),
            (470, 250, 780, 430, "2\nBody\n任務步驟"),
            (860, 250, 1170, 430, "3\nReferences\n長文件"),
            (1250, 250, 1560, 430, "4\nScripts\n確定性邏輯"),
        ]
        for i, box in enumerate(boxes):
            rounded_box(draw, box[:4], "#ffffff")
            draw_centered(draw, box[:4], box[4], font(30, True), "#176b75")
            if i < 3:
                x = box[2] + 22
                y = (box[1] + box[3]) // 2
                draw.line((x, y, x + 48, y), fill="#c2a84b", width=6)
                draw.polygon([(x + 48, y), (x + 30, y - 13), (x + 30, y + 13)], fill="#c2a84b")
        notes = [
            ("Basic Router", "description 決定何時觸發"),
            ("Asset Utilization", "template 不塞 prompt，必要時讀取"),
            ("Learning by Example", "用 golden examples 學模式"),
            ("Procedural Logic", "validation 交給 Python script"),
        ]
        y = 540
        for head, txt in notes:
            draw.text((110, y), head, font=font(26, True), fill="#163f44")
            draw.text((500, y), txt, font=small_f, fill="#3f484a")
            y += 58
    else:
        y = 250
        for label in ["SKILL.md：觸發描述", "Body：任務步驟", "References：長文件", "Scripts：確定性邏輯"]:
            rounded_box(draw, (80, y, w - 80, y + 140), "#ffffff")
            draw_centered(draw, (80, y, w - 80, y + 140), label, font(32, True), "#176b75")
            y += 185
        draw.text((80, y + 30), "四種 authoring pattern", font=font(34, True), fill="#163f44")
        for line in ["Basic Router", "Asset Utilization", "Learning by Example", "Procedural Logic"]:
            y += 62
            draw.text((105, y), line, font=font(28), fill="#3f484a")


def render_adk(draw: ImageDraw.ImageDraw, size: tuple[int, int], mobile: bool) -> None:
    w, h = size
    draw.rectangle((0, 0, w, h), fill="#f8f7f3")
    if mobile:
        draw.text((70, 54), "Agents CLI + ADK", font=font(38, True), fill="#163f44")
        draw.text((70, 104), "本機 Agent 開發生命週期", font=font(38, True), fill="#163f44")
        draw.text((74, 168), "scaffold / lint / playground / run", font=font(28), fill="#4f5b5d")
    else:
        draw.text((70, 54), "Agents CLI + ADK：本機 Agent 開發生命週期", font=font(52, True), fill="#163f44")
        draw.text((74, 128), "核心：用標準工具把 scaffold、理解、lint、playground、run 串成回饋循環。", font=font(27), fill="#4f5b5d")
    steps = [
        ("Setup", "認證\nskills"),
        ("Scaffold", "建立\n專案"),
        ("Inspect", "理解\nworkflow"),
        ("Lint", "健康\n檢查"),
        ("Run", "playground\nCLI"),
    ]
    if not mobile:
        x0, y0, bw, bh, gap = 70, 280, 270, 190, 35
        for i, (head, txt) in enumerate(steps):
            x = x0 + i * (bw + gap)
            rounded_box(draw, (x, y0, x + bw, y0 + bh), "#ffffff")
            draw.text((x + 24, y0 + 26), head, font=font(28, True), fill="#176b75")
            draw_centered(draw, (x + 20, y0 + 72, x + bw - 20, y0 + bh - 18), txt, font(25), "#3f484a")
            if i < 4:
                y = y0 + bh // 2
                draw.line((x + bw + 8, y, x + bw + gap - 8, y), fill="#c2a84b", width=5)
                draw.polygon([(x + bw + gap - 8, y), (x + bw + gap - 24, y - 11), (x + bw + gap - 24, y + 11)], fill="#c2a84b")
        rounded_box(draw, (210, 595, 1390, 790), "#eef6f4", "#cbdedb")
        draw.text((250, 630), "Demo-to-Deploy Gap 的前置解法", font=font(34, True), fill="#163f44")
        draw.text((250, 690), "先把本機開發變成可重跑流程，再談 eval、deploy、observability。", font=font(28), fill="#3f484a")
    else:
        y = 250
        for head, txt in steps:
            rounded_box(draw, (80, y, w - 80, y + 150), "#ffffff")
            draw.text((115, y + 28), head, font=font(32, True), fill="#176b75")
            draw.text((115, y + 82), txt.replace("\n", " / "), font=font(28), fill="#3f484a")
            y += 185
        draw.text((80, y + 20), "先穩定本機循環，再推向 production。", font=font(30, True), fill="#163f44")


def main() -> None:
    save_versions("antigravity-skills-guide", render_antigravity)
    save_versions("agents-cli-adk-guide", render_adk)


if __name__ == "__main__":
    main()
