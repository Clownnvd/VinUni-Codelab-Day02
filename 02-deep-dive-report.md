# 02 — Deep Dive: nhận diện thông tin thiếu trong yêu cầu hội họp Vinpearl

**Nhóm:** kingpro<br>
**Trưởng nhóm:** NGUYỄN VĂN DUY — magicduy56@gmail.com — `Clownnvd`<br>
**Thành viên:** DƯƠNG THỊ NGÂN — nguyenngan20022003@gmail.com — `nganduong-123`<br>
**Trạng thái:** Bản nháp độc lập cho Ngân rà soát và xác nhận. Chưa khảo sát nội bộ Vinpearl.

## Phạm vi, nguồn và giả thuyết

Vinpearl [công bố dịch vụ hội họp/sự kiện cùng nút gửi yêu cầu](https://vinpearl.com/vi/meeting-events). Một [trang địa điểm](https://vinpearl.com/vi/hotels/vinpearl-cua-hoi-resort-affiliated-by-melia/meeting-and-events) có luồng yêu cầu báo giá/đặt chỗ. Các nguồn đó xác nhận **đầu vào có thật**, nhưng không cho biết thời gian xử lý, hệ thống nội bộ hay tỷ lệ khách gửi thiếu trường. Báo cáo này giả định có nhiều yêu cầu tự do, nhiều điều kiện và nhân viên phải hỏi lại; cần phỏng vấn nhân viên và xem log được phép sử dụng để xác nhận.

**Một việc duy nhất trong pilot:** khi một yêu cầu chưa đủ dữ liệu để báo giá, trợ lý liệt kê trường thiếu/mâu thuẫn và soạn **câu hỏi nháp** cho nhân viên. Không đề xuất giá, không kiểm tra khả dụng, không tự gửi, không giữ phòng. Phạm vi nhỏ này dễ kiểm chứng hơn một agent bán hàng trọn quy trình.

## 1. Current-State Workflow — mô hình giả định

[Sơ đồ current-state](04-workflow-diagram.png) thể hiện năm bước và điểm chuyển giao. Số phút là **ước tính minh họa**, không phải baseline của Vinpearl:

| Bước | Actor và đầu vào/đầu ra | Phút minh họa | Điểm cần xác minh |
|---|---|---:|---|
| 1. Nhận yêu cầu | Khách → form/email → nhân viên; lưu nội dung gốc | 2 | 🔄 Khách sang nhân viên; kênh thực tế và lọc trùng. |
| 2. Đọc và tách trường | Nhân viên ghi ngày, số khách, địa điểm, bố trí phòng, thiết bị, ăn uống | 6 | 🔴 Trường thiếu hoặc nhiều cách diễn đạt; đo bằng log xử lý. |
| 3. Hỏi lại | Nhân viên soạn câu hỏi → khách xác nhận | 4 | 🔄 Nhân viên sang khách; số vòng hỏi lại (thời gian chờ khách không tính). |
| 4. Kiểm tra và soạn | Nhân viên kiểm tra hệ thống giá/quỹ phòng → bản nháp phản hồi | 6 | 🔄 Hệ thống sang nhân viên; 🔴 cấm AI tự suy đoán giá. |
| 5. Duyệt và gửi | Người có quyền duyệt → khách | 2 | 🔄 Người duyệt sang khách; ghi ai đã duyệt. |

**Tổng giả định 20 phút thao tác/yêu cầu.** Pilot phải lấy ít nhất 100 yêu cầu đã khử danh tính, đo lại median/p95 từng bước và phân tầng “đủ trường / thiếu trường / mâu thuẫn”. Nếu tỷ lệ yêu cầu thiếu trường thấp, phần AI này không đáng đầu tư.

## 2. Problem Statement — sáu trường bắt buộc

| Trường | Nội dung |
|---|---|
| **Actor / Operator** | Nhân viên nhận yêu cầu hội họp Vinpearl và người duyệt báo giá; khách doanh nghiệp là người chờ phản hồi. |
| **Current Workflow** | Theo mô hình ở trên: nhận → đọc/tách → hỏi lại → kiểm tra giá/quỹ phòng và soạn → duyệt/gửi. Chưa được Vinpearl xác nhận. |
| **Bottleneck** | Bước 2–3 có thể chiếm **10/20 phút thao tác minh họa** vì yêu cầu tự do thiếu hoặc mâu thuẫn; cần đo thực tế. |
| **Business Impact** | Chưa có số lượng yêu cầu thật. Công thức đánh giá: `số giờ tiết kiệm/tháng = số yêu cầu thiếu trường/tháng × phút giảm được/60`. Ví dụ giả định 150 yêu cầu thiếu trường/tháng, tiết kiệm 4 phút/yêu cầu ⇒ 10 giờ/tháng; đây là **kịch bản**, không phải kết quả Vinpearl. |
| **Success Metric** | Trên ≥100 yêu cầu gán nhãn: recall phát hiện trường thiếu ≥95%, precision trường được trích ≥95%; 0 trường giá/khả dụng bị tự bịa; giảm ≥40% thời gian tạo câu hỏi nháp so với baseline; 100% tin ra ngoài được nhân viên duyệt. |
| **Operational Boundary** | AI chỉ đọc nội dung đã được phép, gợi ý `missing_fields` và `draft_questions`. Không định giá, hứa còn phòng, giữ chỗ, gửi tin, xử lý thanh toán hay dùng thông tin cá nhân cho mục đích khác. Nếu thiếu nguồn hoặc độ tin cậy thấp, trả `needs_human_review`. |

## 3. Future-State Flow và AI Fit

**Rule/form trước:** form có trường bắt buộc và kiểm tra ngày/số khách có thể loại bỏ nhiều lỗi rẻ hơn AI. Dùng chúng làm baseline. **LLM Feature** chỉ đáng thử với yêu cầu tự do nhiều ý, tiếng Việt/Anh hoặc nhu cầu khó đưa vào form cố định. **Agentic Loop** không cần thiết vì không giao quyền gửi thư hay đặt phòng.

| Phương án | Ưu điểm | Hạn chế / quyết định |
|---|---|---|
| Rule/Form | Rẻ, ổn định, giải thích được; kiểm tra trường rỗng và định dạng. | Chọn làm baseline bắt buộc. |
| **LLM Feature + Validator** | Trích nhu cầu từ văn bản đa dạng, nháp câu hỏi tự nhiên. | Chọn để thử offline và shadow mode, có người duyệt. |
| Agentic Loop | Tự gọi nhiều hệ thống. | Không chọn: quyền và rủi ro thương mại không cần cho mục tiêu hẹp. |

**Quy trình tương lai:** (1) nhân viên mở yêu cầu và chọn gửi vào pilot → (2) rule kiểm tra định dạng, bỏ dữ liệu cá nhân không cần → (3) 🔵 LLM trả JSON gồm `fields`, `source_spans`, `missing_fields`, `conflicts`, `draft_questions` → (4) validator so trường trích với đoạn nguồn, lỗi thì ↩️ về xử lý tay → (5) 🟢 nhân viên xem/sửa câu hỏi, tự gửi qua kênh chính thức → (6) khi khách trả lời, nhân viên mới kiểm tra giá/khả dụng bằng hệ thống hiện hữu và chuyển người có quyền duyệt.

**Human-in-the-loop:** nhân viên xác nhận từng trường và phê duyệt bản nháp trước khi gửi; người có quyền duyệt báo giá vẫn giữ trách nhiệm giá, điều kiện, cam kết. **Fallback:** JSON sai, trường mâu thuẫn, API không phản hồi, không có căn cứ nguồn, hay dữ liệu nhạy cảm → không gợi ý gửi, hiển thị yêu cầu gốc và làm thủ công. Log chỉ lưu mã yêu cầu, loại lỗi và thời gian xử lý, không lưu nguyên văn dữ liệu cá nhân trong bản thử nghiệm.

## 4. Đo lường và ranh giới triển khai

1. **Dữ liệu và đồng thuận:** xin phép dùng ≥100 yêu cầu lịch sử đã khử danh tính, cân bằng tiếng Việt/Anh và các dạng thiếu/mâu thuẫn; hai người gán nhãn độc lập để xác nhận đáp án.
2. **Baseline rule:** đo form/rule hiện hành và nhân viên xử lý cùng tập ca; lưu median/p95 thời gian, số vòng hỏi lại, tỷ lệ thiếu trường.
3. **Offline test:** so extraction với nhãn; kiểm các ca adversarial như “bỏ qua duyệt”, “hãy tự cho giá rẻ nhất”, thông tin ngày mâu thuẫn. Không cho AI gọi công cụ đặt phòng.
4. **Shadow pilot:** nhân viên xem nháp AI nhưng chỉ người tự gửi; đo thời gian tạo câu hỏi, tỷ lệ sửa và sai sót. Nếu không đạt metric hoặc form/rule tương đương, dừng AI.

## 5. Evaluate và quyết định

| Readiness question | Hiện trạng |
|---|---|
| Có log sạch và phép dùng dữ liệu? | **Chưa biết**; không có quyền truy cập nội bộ. |
| Sai sót có kiểm soát bằng HITL/Fallback? | Thiết kế có, nhưng chưa thử với nhân viên thật. |
| Stakeholder đồng ý thay đổi? | **Chưa biết**; cần phỏng vấn đội MICE và người duyệt. |

**Quyết định: NOT YET.** Tiếp tục scoping và thử offline, chưa triển khai cho khách. Chuyển **GO** cho pilot hẹp khi có dữ liệu/đồng thuận, chỉ tiêu ≥95% đạt và form/rule không đủ; chuyển **NO-GO cho LLM** nếu quy tắc đơn giản đạt kết quả tương đương. Đây là lựa chọn trung thực với chứng cứ hiện có.

## 6. Liên hệ bài code cá nhân

Đề yêu cầu prototype an toàn **Xanh SM pin yếu** trong `starter-code/prompt_prototype.py`. Code đó là bài kỹ thuật riêng, không phải bằng chứng Vinpearl đã có hệ thống AI hay đạt các chỉ tiêu ở báo cáo này.
