"""Render Ngan's proposed current-state Vinpearl MICE workflow.

Nhóm kingpro — NGUYỄN VĂN DUY <magicduy56@gmail.com>,
DƯƠNG THỊ NGÂN <nguyenngan20022003@gmail.com>.
Every duration is an illustrative scoping assumption, not Vinpearl internal data.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "04-workflow-diagram.png"
REGULAR = r"C:\Windows\Fonts\arial.ttf"
BOLD = r"C:\Windows\Fonts\arialbd.ttf"


def f(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(BOLD if bold else REGULAR, size)


def main() -> None:
    im = Image.new("RGB", (1920, 790), "#f7f9fc")
    d = ImageDraw.Draw(im)
    dark, blue, gray, red = "#183047", "#1767a1", "#54697b", "#b52639"
    d.text((70, 36), "CURRENT-STATE: YÊU CẦU HỘI HỌP VINPEARL", font=f(41, True), fill=dark)
    d.text((70, 96), "Giả thuyết để phỏng vấn và đo baseline — chưa xác nhận quy trình nội bộ", font=f(25), fill=gray)

    cards = [
        ("1. NHẬN", ["Khách gửi form", "hoặc email", "→ yêu cầu gốc"], "Khách → Kinh doanh", "2 phút", False),
        ("2. TÁCH TRƯỜNG", ["Ngày, số khách,", "địa điểm, phòng,", "thiết bị, ăn uống"], "Nhân viên", "6 phút", True),
        ("3. HỎI LẠI", ["Phát hiện thiếu", "hoặc mâu thuẫn", "→ hỏi khách"], "Kinh doanh ↔ Khách", "4 phút", True),
        ("4. KIỂM TRA", ["Quỹ phòng, giá", "trên hệ thống", "→ soạn phản hồi"], "Kinh doanh ↔ Hệ thống", "6 phút", False),
        ("5. DUYỆT/GỬI", ["Người có quyền", "kiểm nội dung", "→ gửi cho khách"], "Người duyệt", "2 phút", False),
    ]
    x0, y0, width, height, gap = 70, 210, 320, 390, 40
    for n, (name, lines, actor, minutes, bottleneck) in enumerate(cards):
        x = x0 + n * (width + gap)
        d.rounded_rectangle(
            (x, y0, x + width, y0 + height), radius=18,
            fill="#fff1f2" if bottleneck else "#ffffff",
            outline=red if bottleneck else "#b4c6d5", width=4,
        )
        d.text((x + 20, y0 + 25), name, font=f(27, True), fill=dark)
        d.line((x + 20, y0 + 78, x + width - 20, y0 + 78), fill="#d8e3ec", width=2)
        for j, line in enumerate(lines):
            d.text((x + 20, y0 + 104 + j * 41), line, font=f(22), fill=dark)
        d.text((x + 20, y0 + 260), actor, font=f(20), fill=gray)
        d.text((x + 20, y0 + 308), minutes, font=f(26, True), fill=red if bottleneck else blue)
        if bottleneck:
            d.text((x + 20, y0 + 350), "BOTTLENECK?", font=f(17, True), fill=red)
        if n < len(cards) - 1:
            ax, ay = x + width + 5, y0 + 190
            d.line((ax, ay, ax + 20, ay), fill=blue, width=5)
            d.polygon([(ax + 19, ay - 9), (ax + 19, ay + 9), (ax + 32, ay)], fill=blue)
            d.text((ax + 5, ay - 45), f"H{n + 1}", font=f(17, True), fill=blue)

    d.text((70, 635), "Tổng thao tác giả định: 20 phút/yêu cầu; không tính thời gian chờ khách", font=f(27, True), fill=dark)
    d.text((70, 681), "H1: khách → KD | H2: KD → khách | H3: khách → KD | H4: KD → người duyệt", font=f(21), fill=gray)
    d.text((70, 730), "kingpro | Nguyễn Văn Duy: magicduy56@gmail.com | Dương Thị Ngân: nguyenngan20022003@gmail.com", font=f(18), fill=gray)
    im.save(OUT)
    print(OUT)


if __name__ == "__main__":
    main()
