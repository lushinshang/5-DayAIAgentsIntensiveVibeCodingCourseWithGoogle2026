import math
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


BASE = Path(__file__).resolve().parents[1]
OUT_SOURCE = BASE / "source" / "Agent Skills_Day_3_images_cht"
OUT_HTML = BASE / "images_cht"
FONT_MEDIUM = "/System/Library/Fonts/STHeiti Medium.ttc"
FONT_LIGHT = "/System/Library/Fonts/STHeiti Light.ttc"


BLUE = "#1f73e8"
BLUE_FILL = "#e7f0ff"
GREEN = "#188b45"
GREEN_FILL = "#e5f5e9"
RED = "#e34234"
RED_FILL = "#fde8e5"
ORANGE = "#f08a00"
ORANGE_FILL = "#fff3cf"
GRAY = "#7e878c"
DARK = "#34393d"
LIGHT = "#f7f8f8"


def font(size, medium=True):
    return ImageFont.truetype(FONT_MEDIUM if medium else FONT_LIGHT, size)


def canvas(w, h):
    return Image.new("RGB", (w, h), "white")


def draw_text(draw, text, box, size=36, fill=DARK, medium=True, align="center", spacing=8):
    x1, y1, x2, y2 = box
    f = font(size, medium)
    max_w = x2 - x1
    lines = []
    for para in str(text).split("\n"):
        line = ""
        for ch in para:
            test = line + ch
            if draw.textbbox((0, 0), test, font=f)[2] <= max_w or not line:
                line = test
            else:
                lines.append(line)
                line = ch
        lines.append(line)
    line_h = size + spacing
    total_h = line_h * len(lines) - spacing
    y = y1 + ((y2 - y1 - total_h) / 2)
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=f)
        tw = bbox[2] - bbox[0]
        if align == "left":
            x = x1
        elif align == "right":
            x = x2 - tw
        else:
            x = x1 + (max_w - tw) / 2
        draw.text((x, y), line, font=f, fill=fill)
        y += line_h


def box(draw, xy, text="", fill=BLUE_FILL, outline=BLUE, width=4, radius=18, size=32, text_fill="#111", medium=True):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)
    if text:
        pad = 18
        draw_text(draw, text, (xy[0] + pad, xy[1] + pad, xy[2] - pad, xy[3] - pad), size=size, fill=text_fill, medium=medium)


def arrow(draw, p1, p2, color=GRAY, width=6, dashed=False):
    x1, y1 = p1
    x2, y2 = p2
    if dashed:
        steps = 22
        for i in range(0, steps, 2):
            a = i / steps
            b = min((i + 1) / steps, 1)
            draw.line((x1 + (x2 - x1) * a, y1 + (y2 - y1) * a, x1 + (x2 - x1) * b, y1 + (y2 - y1) * b), fill=color, width=width)
    else:
        draw.line((x1, y1, x2, y2), fill=color, width=width)
    ang = math.atan2(y2 - y1, x2 - x1)
    size = width * 4
    pts = [
        (x2, y2),
        (x2 - size * math.cos(ang - math.pi / 6), y2 - size * math.sin(ang - math.pi / 6)),
        (x2 - size * math.cos(ang + math.pi / 6), y2 - size * math.sin(ang + math.pi / 6)),
    ]
    draw.polygon(pts, fill=color)


def title(draw, text, w, y=50, size=54):
    draw_text(draw, text, (40, y, w - 40, y + 80), size=size, fill=DARK, medium=True)


def save(img, name):
    OUT_SOURCE.mkdir(parents=True, exist_ok=True)
    OUT_HTML.mkdir(parents=True, exist_ok=True)
    p = OUT_SOURCE / name
    img.save(p, "PNG")
    shutil.copyfile(p, OUT_HTML / name)


def fig1():
    img = canvas(1950, 1183)
    d = ImageDraw.Draw(img)
    d.line((975, 60, 975, 1120), fill="#d8dcdf", width=8)
    d.line((90, 590, 1860, 590), fill="#d8dcdf", width=8)
    draw_text(d, "觸發失敗", (150, 90, 850, 170), 54, DARK, True, "left")
    draw_text(d, "執行失敗", (1060, 90, 1800, 170), 54, DARK, True, "left")
    draw_text(d, "Token 腐化", (150, 660, 850, 740), 54, DARK, True, "left")
    draw_text(d, "迴歸", (1060, 660, 1800, 740), 54, DARK, True, "left")
    box(d, (160, 330, 430, 420), "代理人", "#a9c7f6", BLUE, 4, 12, 30)
    arrow(d, (445, 380), (680, 380))
    draw_text(d, "✕", (520, 325, 620, 420), 72, RED)
    box(d, (690, 440, 900, 520), "56% 未觸發", RED_FILL, RED, 4, 12, 28)
    box(d, (1080, 315, 1360, 430), "API", "#8eb2ee", BLUE, 4, 12, 38, "white")
    arrow(d, (1375, 375), (1535, 375))
    box(d, (1545, 300, 1810, 455), "已棄用 API", RED_FILL, RED, 4, 14, 30)
    box(d, (330, 810, 520, 900), "SKILL", BLUE_FILL, BLUE, 4, 12, 30)
    box(d, (330, 900, 520, 990), "SKILL", BLUE_FILL, BLUE, 4, 12, 30)
    box(d, (330, 990, 520, 1080), "SKILL", BLUE_FILL, BLUE, 4, 12, 30)
    box(d, (530, 830, 830, 910), "! 上下文溢出", ORANGE_FILL, ORANGE, 4, 12, 30)
    box(d, (1060, 790, 1325, 960), "新 skill", GREEN_FILL, "#55b870", 4, 14, 32)
    arrow(d, (1340, 875), (1530, 875), dashed=True)
    box(d, (1540, 790, 1810, 960), "既有 skill", RED_FILL, RED, 4, 14, 32)
    box(d, (1570, 980, 1780, 1060), "碰撞警報", RED_FILL, RED, 4, 12, 28)
    return img


def fig2():
    img = canvas(1959, 732)
    d = ImageDraw.Draw(img)
    box(d, (35, 270, 275, 390), "1. CI 單元測試", BLUE_FILL, "#6095f4", 4, 12, 27)
    arrow(d, (285, 330), (350, 330))
    box(d, (355, 265, 525, 395), "黃金\n資料集", "#f2f3f4", GRAY, 4, 18, 26)
    arrow(d, (535, 330), (615, 330))
    box(d, (620, 270, 860, 390), "2. LLM 裁判", GREEN_FILL, GREEN, 4, 12, 27)
    box(d, (620, 210, 860, 255), "位置互換", ORANGE_FILL, ORANGE, 3, 10, 22)
    arrow(d, (870, 330), (945, 330))
    box(d, (950, 270, 1190, 390), "3. 對抗測試", LIGHT, GRAY, 4, 12, 27)
    arrow(d, (1200, 330), (1260, 330))
    d.polygon([(1350, 250), (1430, 330), (1350, 410), (1270, 330)], fill="#f7f8f8", outline=GRAY)
    draw_text(d, "4.\n生產\n分流", (1290, 270, 1410, 390), 25)
    arrow(d, (1350, 250), (1350, 115))
    arrow(d, (1350, 410), (1350, 545))
    box(d, (1490, 55, 1615, 175), "Canary\n1%", GREEN_FILL, GREEN, 4, 10, 22)
    box(d, (1490, 470, 1615, 590), "Shadow\n100%", BLUE_FILL, BLUE, 4, 10, 22)
    arrow(d, (1625, 115), (1700, 320))
    arrow(d, (1625, 530), (1700, 340))
    box(d, (1730, 285, 1940, 405), "✅\n可行動上線", GREEN_FILL, GREEN, 4, 12, 27)
    return img


def fig3():
    img = canvas(1950, 1189)
    d = ImageDraw.Draw(img)
    for y in [380, 760]:
        d.line((90, y, 1030, y), fill="#d9dde0", width=5)
    draw_text(d, "精確軌跡", (90, 50, 600, 130), 42, DARK, True, "left")
    draw_text(d, "依序軌跡", (90, 430, 600, 510), 42, DARK, True, "left")
    draw_text(d, "任意順序軌跡", (90, 810, 650, 890), 42, DARK, True, "left")
    for row, y in enumerate([235, 610, 1010]):
        xs = [155, 525, 895]
        for i, x in enumerate(xs):
            d.ellipse((x - 65, y - 65, x + 65, y + 65), fill=BLUE_FILL, outline="#6aa0ff", width=4)
            draw_text(d, chr(65 + i), (x - 40, y - 35, x + 40, y + 35), 40, "#000")
        if row == 0:
            arrow(d, (225, y), (455, y))
            arrow(d, (595, y), (825, y))
        elif row == 1:
            arrow(d, (225, y), (455, y))
            arrow(d, (595, y), (825, y), "#2baa4b")
            d.ellipse((660, y + 40, 770, y + 150), fill=ORANGE_FILL, outline=ORANGE, width=4)
            draw_text(d, "D", (680, y + 65, 750, y + 125), 38, "#000")
        else:
            d.arc((220, y - 100, 830, y + 100), 190, 350, fill=GRAY, width=3)
            d.arc((220, y - 70, 830, y + 70), 190, 350, fill=GRAY, width=3)
    box(d, (1110, 50, 1880, 1140), "", "#f9fafb", GRAY, 3, 30)
    draw_text(d, "只看輸出：盲點", (1180, 80, 1810, 160), 50, DARK)
    d.line((1190, 300, 1360, 420, 1300, 760, 1450, 900, 1540, 680), fill=RED, width=7)
    d.polygon([(1520, 390), (1830, 720), (1415, 720)], fill="#df2f26")
    draw_text(d, "未驗證\n副作用", (1510, 510, 1740, 660), 42, "white")
    return img


def fig4():
    img = canvas(1951, 1361)
    d = ImageDraw.Draw(img)
    d.line((660, 30, 660, 1280), fill=GRAY, width=4)
    draw_text(d, "隔離測試", (105, 80, 530, 170), 54, DARK, True, "left")
    draw_text(d, "正式環境", (760, 80, 1250, 170), 54, DARK, True, "left")
    box(d, (250, 380, 410, 550), "Skill", LIGHT, DARK, 4, 8, 30)
    box(d, (175, 860, 490, 945), "準確率：90% ✅", GREEN_FILL, "#57b96b", 4, 12, 32)
    labels = ["法務", "支援", "付款", "商品", "合規", "分析", "帳戶", "帳單", "客服", "物流", "財務", "HR", "安全"]
    positions = [(970,310),(1150,210),(1335,205),(1515,290),(1640,420),(1680,610),(1620,810),(1450,990),(1260,1060),(1080,1050),(920,930),(825,740),(850,520)]
    for lab, (x, y) in zip(labels, positions):
        box(d, (x, y, x + 130, y + 165), lab, LIGHT, DARK, 3, 8, 24)
        d.line((x + 65, y + 82, 1300, 690), fill="#e2e6e8", width=4)
    box(d, (1245, 610, 1390, 765), "", BLUE_FILL, "#6aa0ff", 5, 12)
    box(d, (1170, 430, 1470, 520), "上下文腐化區", RED_FILL, RED, 4, 12, 30)
    box(d, (1170, 790, 1480, 880), "準確率：44.2% ✕", RED_FILL, RED, 4, 12, 32)
    box(d, (160, 1190, 490, 1270), "活躍上下文：2K", "#eceff1", GRAY, 4, 12, 30)
    box(d, (1160, 1190, 1510, 1270), "活躍上下文：50K+", "#eceff1", GRAY, 4, 12, 30)
    return img


def fig5():
    img = canvas(1950, 1218)
    d = ImageDraw.Draw(img)
    title(d, "Agents CLI：一次安裝，七個 skills，支援任何 coding agent", 1950, 40, 50)
    box(d, (100, 165, 540, 400), "", BLUE_FILL, BLUE, 4, 25)
    draw_text(d, "1. 開發者", (130, 225, 510, 270), 30, "#111")
    draw_text(d, "執行一個命令", (130, 262, 510, 300), 24, DARK, False)
    box(d, (140, 310, 500, 370), "$ uvx google-agents-cli setup", "#1f66d0", "#1550a9", 3, 10, 18, "white")
    arrow(d, (555, 280), (650, 280))
    box(d, (665, 165, 1305, 960), "", ORANGE_FILL, ORANGE, 4, 26)
    draw_text(d, "2. 安裝七個 skills", (710, 215, 1260, 255), 30, "#111")
    draw_text(d, "進既有 coding agent", (710, 255, 1260, 295), 24, DARK, False)
    skills = [("workflow", "生命週期 + 模型選擇"), ("adk-code", "ADK Python：agents / tools / states"), ("scaffold", "create / enhance / upgrade"), ("eval", "metrics / evalset / LLM 裁判"), ("deploy", "Agent Runtime / Cloud Run"), ("publish", "Gemini Enterprise 註冊"), ("observability", "Cloud Trace + BigQuery Analytics")]
    y = 325
    for a, b in skills:
        box(d, (705, y, 1265, y + 78), "", "#fffaf0", ORANGE, 3, 10)
        draw_text(d, a, (730, y + 8, 930, y + 70), 26, "#111", True, "left")
        draw_text(d, b, (900, y + 8, 1240, y + 70), 21, DARK, False)
        y += 90
    arrow(d, (1320, 280), (1410, 280))
    box(d, (1430, 165, 1870, 960), "", GREEN_FILL, GREEN, 4, 26)
    draw_text(d, "3. 任何 coding agent", (1470, 225, 1830, 265), 28, "#111")
    draw_text(d, "取得完整生命週期", (1470, 265, 1830, 305), 24, DARK, False)
    for i, lab in enumerate(["Gemini CLI", "Claude Code", "Codex CLI", "Antigravity", "任何相容 agent"]):
        box(d, (1470, 315 + i * 130, 1830, 405 + i * 130), lab, "#f3fbf5", GREEN, 4, 10, 28)
    box(d, (100, 1010, 1870, 1165), "一句話架構模式：\nGoogle 把 ASK 專業封裝成 7 個 skills，而不是單體 IDE；因此可組合進開發者既有 coding agent。", "#fff5e8", ORANGE, 3, 18, 28)
    return img


def fig6():
    img = canvas(1950, 1120)
    d = ImageDraw.Draw(img)
    title(d, "Demo 到部署的落差", 1950, 40, 58)
    d.line((200, 930, 1760, 930), fill=DARK, width=6)
    d.line((200, 930, 200, 190), fill=DARK, width=6)
    arrow(d, (1760, 930), (1810, 930), DARK, 6)
    arrow(d, (200, 930), (200, 160), DARK, 6)
    draw_text(d, "團隊信心", (90, 430, 170, 700), 34, DARK)
    draw_text(d, "部署週數", (790, 960, 1160, 1030), 38, DARK)
    pts = [(240,890),(350,620),(520,400),(700,260),(880,225),(1080,330),(1240,555),(1400,760),(1600,880),(1740,900)]
    d.line(pts, fill="#1d55ad", width=8, joint="curve")
    draw_text(d, "亢奮期\n截圖到處流傳", (700, 135, 1050, 220), 34, GREEN)
    draw_text(d, "現實咬人\n• 客戶資料很髒\n• auth 很複雜\n• security 有問題", (1210, 455, 1600, 630), 30, "#bf2020", True, "left")
    draw_text(d, "第 1 週\n「demo 可以跑！」", (320, 780, 650, 880), 30, DARK, True, "left")
    draw_text(d, "「為什麼會壞？」\n先怪模型", (1500, 790, 1880, 880), 30, DARK)
    draw_text(d, "破點很少是模型，而是環境適配。", (650, 1030, 1300, 1090), 30, DARK)
    return img


def fig7():
    img = canvas(1950, 1235)
    d = ImageDraw.Draw(img)
    title(d, "Context Rot：更大的窗口救不了你", 1950, 55, 58)
    d.line((270, 1020, 1810, 1020), fill=DARK, width=6)
    d.line((270, 1020, 270, 210), fill=DARK, width=6)
    draw_text(d, "任務準確率", (120, 520, 220, 740), 36, DARK)
    draw_text(d, "Prompt / context 大小（tokens）", (780, 1080, 1260, 1140), 38, DARK)
    for txt, x in [("0", 270), ("8K", 640), ("32K", 1020), ("128K", 1380), ("1M", 1770)]:
        draw_text(d, txt, (x - 60, 1030, x + 60, 1080), 28, DARK)
    for txt, y in [("100%", 210), ("50%", 610), ("0%", 1000)]:
        draw_text(d, txt, (180, y - 20, 255, y + 20), 28, DARK)
    d.line((270, 250, 1810, 250), fill=GRAY, width=3)
    d.line((650, 300, 1810, 475), fill="#1f66d0", width=5)
    pts = [(270,290),(500,310),(700,370),(860,480),(1010,640),(1180,830),(1400,940),(1650,990),(1780,1000)]
    d.line(pts, fill="#cc2020", width=8, joint="curve")
    draw_text(d, "早期指令\n開始被忽略", (890, 410, 1240, 500), 32, "#c91f1f")
    box(d, (1080, 705, 1385, 820), "lost in the middle\n區域", ORANGE_FILL, ORANGE, 4, 12, 30)
    draw_text(d, "我們希望如此", (1540, 205, 1810, 255), 28, DARK)
    draw_text(d, "更大窗口只是\n延後撞牆 →", (1360, 320, 1700, 410), 28, "#1765d8")
    draw_text(d, "18 個 frontier models 都在 context window 填滿前就開始退化", (500, 1150, 1450, 1210), 30, DARK)
    return img


def fig8():
    img = canvas(1434, 1068)
    d = ImageDraw.Draw(img)
    title(d, "Token 經濟學：大 Prompt vs. 技能庫", 1434, 35, 42)
    draw_text(d, "「一個大 Prompt」", (70, 120, 560, 180), 32, "#000")
    draw_text(d, "「技能庫」", (780, 120, 1290, 180), 32, "#000")
    box(d, (80, 220, 560, 845), "", RED_FILL, RED, 4, 24)
    for i, lab in enumerate(["樣式指南", "邊界案例（1-17）", "API 慣例", "資料倉儲規則", "品牌語氣"]):
        box(d, (110, 245 + i * 48, 530, 290 + i * 48), lab, "#fee9e7", "#f8c8c4", 2, 6, 18)
    box(d, (110, 505, 530, 610), "~15,000 tokens\n每一輪都載入", "#fff5f5", RED, 4, 8, 26)
    for i, lab in enumerate(["計價邏輯", "合規聲明", "格式範本", "語氣覆寫..."]):
        box(d, (110, 625 + i * 48, 530, 670 + i * 48), lab, "#fee9e7", "#f8c8c4", 2, 6, 18)
    box(d, (190, 875, 470, 940), "Context rot 啟動", RED_FILL, RED, 4, 10, 24)
    draw_text(d, "VS.", (655, 505, 755, 570), 34, "#000")
    box(d, (790, 220, 1290, 290), "標頭：約 50 skills × 80 tokens ≈ 4K", GREEN_FILL, GREEN, 4, 10, 22)
    draw_text(d, "永遠載入（index）", (850, 300, 1220, 340), 18, DARK)
    box(d, (790, 370, 1290, 535), "活躍 skill 本文\n~2,000 tokens\n任務結束後卸載", "#f7fff9", GREEN, 4, 10, 24)
    box(d, (790, 585, 1290, 760), "vendor-scorecard.md（未載入）\nstyle-pairing.md（未載入）\ncompliance.md（未載入）\n... 另外 47 個 ...", LIGHT, GRAY, 2, 8, 20)
    box(d, (790, 780, 1290, 885), "≈ 6,000 tokens 活躍\n（50 個 skills 可用）", GREEN_FILL, GREEN, 4, 10, 26)
    box(d, (880, 920, 1210, 985), "[OK] context 保持聚焦", GREEN_FILL, "#57b96b", 4, 10, 24)
    draw_text(d, "同樣 workflow capability，但任一時刻載入更少 tokens。", (300, 1000, 1140, 1050), 24, DARK)
    return img


def fig9():
    img = canvas(1951, 855)
    d = ImageDraw.Draw(img)
    box(d, (120, 430, 470, 555), "使用者請求", BLUE_FILL, "#6aa0ff", 4, 55, 34)
    arrow(d, (485, 492), (610, 492))
    box(d, (620, 360, 1120, 620), "ADK Runtime Agent", BLUE_FILL, "#6aa0ff", 4, 14, 36)
    arrow(d, (870, 345), (870, 240))
    box(d, (700, 125, 1040, 245), "skilltoolset API", GREEN_FILL, "#55b870", 4, 14, 32)
    arrow(d, (1060, 185), (1440, 185), dashed=True)
    box(d, (1460, 70, 1740, 245), "自動撰寫\nSKILL.md", ORANGE_FILL, ORANGE, 4, 24, 32)
    box(d, (1400, 365, 1810, 620), "本機檔案系統", "#60666a", GRAY, 4, 14, 36, "white")
    arrow(d, (1580, 250), (1580, 360))
    arrow(d, (1390, 492), (1130, 492))
    box(d, (1175, 435, 1340, 550), "LOAD_SKILL\nTOOL", "white", GRAY, 3, 60, 24)
    box(d, (1335, 650, 1595, 770), "合規稽核", "#fff8e8", ORANGE, 4, 40, 30)
    box(d, (1615, 650, 1850, 770), "安全檢查", "#fff8e8", ORANGE, 4, 40, 30)
    return img


def fig10():
    img = canvas(1955, 596)
    d = ImageDraw.Draw(img)
    box(d, (70, 95, 285, 245), "Target\nSKILL.md", BLUE_FILL, "#6aa0ff", 4, 15, 27)
    arrow(d, (180, 250), (180, 345))
    box(d, (80, 360, 285, 460), "提出\n修訂", ORANGE_FILL, ORANGE, 4, 10, 27)
    arrow(d, (290, 410), (380, 410))
    box(d, (385, 360, 590, 460), "評估\n套件", GREEN_FILL, "#55b870", 4, 10, 27)
    arrow(d, (600, 410), (690, 410))
    box(d, (700, 360, 900, 460), "準確率\n73%→81%", BLUE_FILL, "#6aa0ff", 4, 10, 27)
    arrow(d, (910, 410), (1000, 410))
    d.polygon([(1100, 310), (1180, 410), (1100, 510), (1020, 410)], fill=LIGHT, outline=GRAY)
    draw_text(d, "保留 / 回復\n決策", (1045, 350, 1155, 470), 25)
    arrow(d, (1185, 410), (1320, 410), GREEN, 5)
    box(d, (1330, 300, 1580, 510), "人工\n抽查 gate", RED_FILL, RED, 4, 12, 30)
    arrow(d, (1590, 410), (1710, 410))
    box(d, (1720, 300, 1930, 510), "升級為\n生產 skill", GREEN_FILL, GREEN, 4, 12, 28)
    d.line((1100, 300, 1100, 175, 285, 175), fill=GRAY, width=4)
    arrow(d, (285, 175), (285, 175), GRAY, 4)
    box(d, (640, 130, 750, 165), "Revert", LIGHT, GRAY, 3, 8, 20)
    return img


def fig11():
    img = canvas(1960, 1632)
    d = ImageDraw.Draw(img)
    title(d, "Skills-First 零售架構（示意）", 1960, 35, 54)
    draw_text(d, "generic 大型零售商，執行於商品化 agent runtime", (500, 110, 1460, 160), 26, DARK)
    box(d, (75, 200, 1885, 430), "", ORANGE_FILL, ORANGE, 3, 28)
    draw_text(d, "顧客接觸層（web、mobile、in-store、voice）", (140, 230, 1820, 275), 30, "#111")
    for i, lab in enumerate(["官網聊天", "Pro 行動 app", "店內 kiosk", "語音代理人", "簡訊"]):
        box(d, (120 + i * 355, 310, 420 + i * 355, 390), lab, "#fffaf0", ORANGE, 3, 10, 26)
    arrow(d, (980, 440), (980, 540))
    box(d, (75, 560, 1885, 1060), "", "#fff0df", "#d16b00", 3, 28)
    draw_text(d, "Agent runtime（ADK、Claude SDK 等）按需載入 skills", (150, 600, 1810, 645), 30, "#111")
    skills = [
        ("project-guidance", "如何鋪浴室磁磚？\n工法知識"),
        ("product-fit", "這個水龍頭相容嗎？"),
        ("materials-list", "project → grouped BOM\nfor Pros"),
        ("store-locator", "aisle 14, bay 7\nlive inventory"),
        ("code-compliance", "local building code\ndisclaimers"),
        ("review-summarize", "product reviews → pros / cons"),
        ("delivery-window", "last mile ETA & options"),
        ("+ 約 50 more", "由採購、供應鏈、法務等團隊擁有"),
    ]
    for i, (a, b) in enumerate(skills):
        row = i // 4
        col = i % 4
        x = 120 + col * 420
        y = 690 + row * 175
        box(d, (x, y, x + 390, y + 135), "", "#fff7ef", "#d16b00", 3, 10)
        draw_text(d, a, (x + 20, y + 18, x + 370, y + 58), 26, "#111")
        draw_text(d, b, (x + 30, y + 58, x + 360, y + 120), 22, DARK)
    arrow(d, (980, 1070), (980, 1170))
    box(d, (75, 1190, 1885, 1500), "", BLUE_FILL, BLUE, 3, 28)
    draw_text(d, "Tools / data layer — 透過 MCP 與 managed search integrations 存取", (150, 1225, 1810, 1270), 30, "#111")
    data = [("產品目錄", "2M+ SKUs"), ("庫存", "store-level stock + locations"), ("顧客 profile", "orders、returns、loyalty"), ("專案知識庫", "how-to guides、manuals"), ("向量搜尋", "reviews、spec sheets")]
    for i, (a, b) in enumerate(data):
        box(d, (120 + i * 355, 1325, 420 + i * 355, 1450), "", "#eff5ff", BLUE, 3, 10)
        draw_text(d, a, (140 + i * 355, 1340, 400 + i * 355, 1385), 24, "#111")
        draw_text(d, b, (140 + i * 355, 1385, 400 + i * 355, 1438), 18, DARK)
    draw_text(d, "Skills 承載判斷（品牌專業）。MCP 承載資料管線。模型可替換。", (300, 1520, 1660, 1580), 28, DARK)
    return img


FIGS = [
    ("Figure 1 Skill Failure Modes.png", fig1),
    ("Figure 2 Skill Trigger Gatekeeping.png", fig2),
    ("Figure 3 Evaluation-Driven Development Loop.png", fig3),
    ("Figure 4 Co-loaded Skills Performance Gap.png", fig4),
    ("Figure 5 Agents CLI Install Flow.png", fig5),
    ("Figure 6 Demo-to-Deploy Gap.png", fig6),
    ("Figure 7 Context Rot in Practice.png", fig7),
    ("Figure 8 Token Economics Skill Library.png", fig8),
    ("Figure 9 Production Histories to Procedural Memories.png", fig9),
    ("Figure 10 Meta-Skill Evaluation Gating.png", fig10),
    ("Figure 11 Skills-First Retail Architecture.png", fig11),
]


def main():
    for name, maker in FIGS:
        img = maker()
        save(img, name)
        print(name)


if __name__ == "__main__":
    main()
