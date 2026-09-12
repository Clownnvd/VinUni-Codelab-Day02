"""Generate the current-state workflow artifact for kingpro's Vinpearl MICE scoping.

Leader: NGUYỄN VĂN DUY <magicduy56@gmail.com>
Member: DƯƠNG THỊ NGÂN <nguyenngan20022003@gmail.com>
All step durations are illustrative assumptions, not measured Vinpearl data.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "04-workflow-diagram.png"
FONT = Path(r"C:\Windows\Fonts\arial.ttf")
BOLD = Path(r"C:\Windows\Fonts\arialbd.ttf")


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(BOLD if bold else FONT), size)


def draw_lines(draw: ImageDraw.ImageDraw, lines: list[str], xy: tuple[int, int], line_height: int, **kwargs: object) -> None:
    x, y = xy
    for line in lines:
        draw.text((x, y), line, **kwargs)
        y += line_height


def main() -> None:
    img = Image.new("RGB", (2100, 720), "#f8fafc")
    d = ImageDraw.Draw(img)
    navy, muted, red, blue = "#10243a", "#4b647a", "#bb2438", "#2164a1"

    d.text((65, 36), "QUY TRÌNH HIỆN TẠI — YÊU CẦU HỘI HỌP VINPEARL", font=font(40, True), fill=navy)
    d.text((65, 94), "Mô hình giả định để scoping; thời lượng cần đo tại hiện trường", font=font(27), fill=muted)

    steps = [
        ("1. Tiếp nhận", ["Khách gửi form/email", "→ Hồ sơ yêu cầu"], "Kinh doanh", "2 phút", False),
        ("2. Tách nhu cầu", ["Đọc ngày, số khách,", "phòng, thiết bị..."], "Kinh doanh", "4 phút", True),
        ("3. Hỏi thông tin", ["Làm rõ trường thiếu", "và điều kiện khác"], "Kinh doanh ↔ Khách", "3 phút", False),
        ("4. Kiểm tra", ["Quỹ phòng, giá,", "điều kiện hợp đồng"], "Kinh doanh ↔ Hệ thống", "5 phút", False),
        ("5. Soạn nháp", ["Phản hồi yêu cầu", "hoặc báo giá nháp"], "Kinh doanh", "3 phút", True),
        ("6. Duyệt và gửi", ["Người có quyền duyệt", "rồi gửi cho khách"], "Người duyệt", "2 phút", False),
    ]
    left, top, width, height, gap = 65, 190, 300, 340, 40
    for i, (title, details, actor, duration, bottleneck) in enumerate(steps):
        x = left + i * (width + gap)
        fill = "#fff0f1" if bottleneck else "#ffffff"
        outline = red if bottleneck else "#b7c9d8"
        d.rounded_rectangle((x, top, x + width, top + height), radius=22, fill=fill, outline=outline, width=4)
        d.text((x + 20, top + 26), title, font=font(28, True), fill=navy)
        d.line((x + 20, top + 73, x + width - 20, top + 73), fill="#d9e3eb", width=2)
        draw_lines(d, details, (x + 20, top + 98), 38, font=font(22), fill=navy)
        d.text((x + 20, top + 207), actor, font=font(20), fill=muted)
        d.text((x + 20, top + 250), duration, font=font(24, True), fill=red if bottleneck else blue)
        if bottleneck:
            d.text((x + 20, top + 292), "ĐIỂM NGHẼN", font=font(19, True), fill=red)
        if i < len(steps) - 1:
            ax, ay = x + width + 8, top + height // 2
            d.line((ax, ay, ax + gap - 17, ay), fill=blue, width=5)
            d.polygon([(ax + gap - 17, ay - 10), (ax + gap - 17, ay + 10), (ax + gap - 3, ay)], fill=blue)

    d.text((65, 575), "Tổng thao tác minh họa: 19 phút/yêu cầu (chưa đo baseline)", font=font(27, True), fill=navy)
    d.text((65, 620), "Điểm nghẽn giả thuyết: đọc/tách nhu cầu và soạn phản hồi | Handoff: khách, kinh doanh, hệ thống, người duyệt", font=font(21), fill=muted)
    d.text((65, 667), "Nhóm kingpro | Nguyễn Văn Duy · magicduy56@gmail.com | Dương Thị Ngân · nguyenngan20022003@gmail.com", font=font(18), fill=muted)
    img.save(OUT)
    print(OUT)


if __name__ == "__main__":
    main()
