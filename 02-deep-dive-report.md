# 02 — Deep Dive: trợ lý chuẩn bị yêu cầu hội họp Vinpearl

**Nhóm:** kingpro<br>
**Trưởng nhóm:** NGUYỄN VĂN DUY — `Clownnvd` — magicduy56@gmail.com<br>
**Thành viên:** DƯƠNG THỊ NGÂN — `nganduong-123` — nguyenngan20022003@gmail.com<br>
**Trạng thái:** Đề xuất pilot trên branch cá nhân; chưa được Vinpearl xác nhận hay triển khai.

## 1. Bối cảnh, bằng chứng và giới hạn

[Vinpearl công bố dịch vụ hội họp/sự kiện và kênh “Gửi yêu cầu”](https://vinpearl.com/vi/meeting-events); một [trang địa điểm cụ thể](https://vinpearl.com/vi/hotels/vinpearl-cua-hoi-resort-affiliated-by-melia/meeting-and-events) cũng có lời mời gửi yêu cầu báo giá/đặt chỗ. Điều này xác nhận **có luồng tiếp nhận yêu cầu**, nhưng không chứng minh nội bộ đang dùng email, tốn bao nhiêu phút, tỷ lệ lỗi hay công suất đội kinh doanh. Workflow bên dưới là **mô hình giả định để phỏng vấn và đo**, không phải mô tả chắc chắn về vận hành Vinpearl. Các chỉ tiêu đều là **ngưỡng đề xuất cho pilot**.

**Phạm vi hẹp:** Một địa điểm MICE, yêu cầu bằng tiếng Việt hoặc tiếng Anh đi qua form/email; đầu ra chỉ là tóm tắt và **nháp** câu hỏi hoặc phản hồi cho nhân viên. Không tự định giá, hứa còn phòng, giữ chỗ, ký hợp đồng, thu tiền hay gửi cho khách.

## 2. Current-State Workflow — giả thuyết cần xác minh

Hình [04-workflow-diagram.png](04-workflow-diagram.png) trực quan hóa cùng luồng. Thời lượng trong bảng là **ước tính minh họa cho một yêu cầu đủ phức tạp**, không phải baseline thực đo.

| Bước | Người / hệ thống | Đầu vào → đầu ra | Thời gian minh họa | Handoff và điểm nghẽn |
|---|---|---|---:|---|
| 1. Tiếp nhận | Form/email → nhân viên kinh doanh | Yêu cầu thô → hồ sơ tiếp nhận | 2 phút | 🔄 Khách → kinh doanh; kiểm tra spam/trùng. |
| 2. Đọc và tách nhu cầu | Nhân viên kinh doanh | Văn bản tự do → ngày, địa điểm, số khách, phòng, thiết bị, ăn uống | 4 phút | 🔴 Dữ liệu thường thiếu hoặc mâu thuẫn; giả thuyết cần đo. |
| 3. Hỏi rõ thông tin thiếu | Nhân viên ↔ khách | Danh sách trường thiếu → câu hỏi xác nhận | 3 phút | 🔄 Kinh doanh → khách; thời gian chờ khách **không** tính vào thời gian thao tác. |
| 4. Kiểm tra khả dụng và giá | Nhân viên + hệ thống đặt chỗ/giá | Nhu cầu đã xác nhận → khả dụng, giá, điều kiện | 5 phút | 🔄 Kinh doanh ↔ hệ thống; 🔴 không được thay bằng suy đoán của LLM. |
| 5. Soạn nháp | Nhân viên kinh doanh | Dữ liệu đã xác minh → thư phản hồi/báo giá nháp | 3 phút | 🔴 Dễ bỏ sót ràng buộc hoặc dùng mẫu không phù hợp. |
| 6. Duyệt và gửi | Người có thẩm quyền | Nháp → phản hồi chính thức | 2 phút | 🔄 Nhân viên → người duyệt/khách. |

**Tổng thao tác minh họa: 19 phút/lượt** (2+4+3+5+3+2). Con số này chỉ giúp thiết kế phép đo; không được dùng như kết quả kinh doanh. Cần đo trung vị, p95 và tỷ lệ yêu cầu thiếu thông tin trên ít nhất 100 yêu cầu lịch sử được khử danh tính, chia theo độ phức tạp.

## 3. Problem Statement — 6 fields

| Field | Nội dung |
|---|---|
| **1. Actor / Operator** | Nhân viên kinh doanh MICE hoặc đặt đoàn tiếp nhận yêu cầu của khách doanh nghiệp; người duyệt báo giá chịu trách nhiệm cam kết cuối cùng. |
| **2. Current Workflow** | Theo giả thuyết ở mục 2: tiếp nhận → đọc/tách nhu cầu → hỏi rõ → kiểm tra khả dụng/giá → soạn → duyệt/gửi. Cần phỏng vấn để xác nhận công cụ và luồng thật. |
| **3. Bottleneck** | Văn bản yêu cầu không đồng nhất, nhiều trường thiếu/mâu thuẫn khiến bước tách nhu cầu và soạn thư phải thao tác tay; giá/khả dụng là bước kiểm tra nghiệp vụ riêng, không phải bài toán cho LLM suy đoán. |
| **4. Business Impact** | Chưa có số lượng yêu cầu hay thời gian thực đo. Mô hình tác động: `giờ tiết kiệm/ngày = số yêu cầu/ngày × (phút baseline − phút pilot)/60`. Ví dụ **giả định** 30 yêu cầu/ngày và tiết kiệm 4 phút/yêu cầu ⇒ 2 giờ/ngày; không xem là doanh thu hay số liệu Vinpearl. |
| **5. Success Metric** | Trên bộ ≥100 yêu cầu đã gán nhãn: precision/recall trường bắt buộc ≥95%; giảm ≥40% **thời gian chuẩn bị nháp** so với baseline cùng loại yêu cầu; 100% giá, khả dụng và điều khoản trong nháp có nguồn từ hệ thống/nhân viên; 0 lần tự gửi, tự giữ chỗ hoặc tự cam kết giá. Đo thêm tỷ lệ nhân viên phải sửa nháp và p95 thời gian phản hồi. |
| **6. Operational Boundary** | AI chỉ đọc yêu cầu đã được cho phép, xuất JSON tóm tắt + trường thiếu + nháp gắn `[DRAFT_ONLY]`. Chỉ thông tin được xác minh mới được đưa vào nháp. **Cấm** tạo giá, hứa còn phòng, thao tác đặt/giữ chỗ, gửi email hoặc dùng dữ liệu cá nhân ngoài mục đích pilot. Người phụ trách duyệt trước mọi phản hồi. |

## 4. AI Fit: vì sao chọn LLM Feature

| Phương án | Phù hợp | Giới hạn / quyết định |
|---|---|---|
| Form + rule/state machine | Rẻ, dễ giải thích, tốt cho trường bắt buộc, kiểm tra ngày và format. | **Thử trước làm baseline.** Nếu đa số yêu cầu đã có cấu trúc thì không cần AI. |
| **LLM Feature + rule** | Có thể hiểu diễn đạt tự do Việt/Anh, trích xuất nhu cầu và soạn nháp câu hỏi lịch sự; rule kiểm tra trường, giá và quyền. | **Chọn cho pilot**, chỉ xử lý văn bản; mọi hành động có người duyệt. |
| Agentic Loop | Có thể tự truy vấn nhiều hệ thống và xử lý vòng lặp. | **Không chọn**: quyền truy cập/chi phí/rủi ro cam kết sai quá lớn cho giai đoạn chưa có baseline và dữ liệu tích hợp. |

## 5. Future-State Flow và ranh giới vận hành

1. **Nhân viên** mở yêu cầu; hệ thống khử/giới hạn dữ liệu cá nhân cho pilot và gán `request_id`.
2. **Rule** kiểm tra trường chắc chắn (ngày, số khách, địa điểm) và nguồn yêu cầu. Nếu không hợp lệ, chuyển nhân viên xử lý thủ công.
3. **LLM Feature** trả về JSON theo schema: `event_date`, `venue`, `guest_count`, `room_setup`, `equipment`, `catering`, `missing_fields`, `conflicts`, `draft_message`, `source_spans`. Không có trường giá/khả dụng nếu hệ thống chưa trả về.
4. **Validator** đối chiếu giá trị trích xuất với đoạn nguồn; phát hiện mâu thuẫn, thiếu trường, PII không cần thiết. Trường không chắc chắn phải là `null` hoặc câu hỏi làm rõ, không được điền bừa.
5. **Nhân viên** kiểm tra quỹ phòng và bảng giá trên hệ thống hiện hữu. Kết quả có nguồn/time stamp mới được đưa vào nháp báo giá.
6. **LLM** soạn `[DRAFT_ONLY]` câu hỏi hoặc thư phản hồi từ dữ liệu đã xác minh. **Người duyệt** sửa, xác nhận và tự gửi qua kênh chính thức.
7. **Fallback:** API lỗi, JSON sai schema, nguồn không khớp, dữ liệu thiếu hoặc mâu thuẫn → không hiện đề xuất gửi; hiển thị yêu cầu gốc và chuyển về quy trình thủ công. Log `request_id`, loại lỗi, người duyệt, thời gian; không lưu nguyên văn dữ liệu cá nhân trong log thử nghiệm.

**Điểm Human-in-the-loop:** Nhân viên xác nhận trường trích xuất; người có quyền duyệt báo giá và thao tác gửi. AI không có quyền gửi/đặt chỗ. Các lời nhắc từ khách như “bỏ qua phê duyệt” là dữ liệu không đáng tin, không thể thay đổi quyền hệ thống.

## 6. Kế hoạch pilot và phép đo

| Cổng kiểm tra | Cách đo | Ngưỡng đi tiếp |
|---|---|---|
| Dữ liệu | Lấy ≥100 yêu cầu đã khử danh tính, đủ mẫu tiếng Việt/Anh, yêu cầu thiếu trường, mâu thuẫn, yêu cầu đặc biệt; hai người gán nhãn và giải quyết bất đồng. | Có phép dùng dữ liệu, schema nhãn và mức đồng thuận được ghi nhận. |
| Baseline | Đo thời gian thao tác từng bước với form/rule hiện tại trên cùng phân tầng yêu cầu. | Có median, p95, tỷ lệ hỏi lại và tỷ lệ lỗi; chưa có thì không công bố “tiết kiệm”. |
| Offline AI | So sánh trường trích xuất, câu hỏi thiếu, lỗi bịa giá/khả dụng, lỗi rò PII. | ≥95% trường bắt buộc đúng; 0 cam kết thương mại bịa; 0 hành động tự động. |
| Shadow pilot | Nhân viên xem nháp nhưng vẫn làm và gửi theo quy trình hiện tại; đo thời gian và mức sửa. | Giảm ≥40% thời gian chuẩn bị nháp, không tăng sai sót; nhân viên chấp nhận quy trình. |

## 7. Evaluate — quyết định

| AI Readiness Checklist | Hiện trạng từ nguồn công khai |
|---|---|
| Có dữ liệu mẫu/log sạch để test? | **Chưa xác nhận.** Không có quyền truy cập log nội bộ. |
| Rủi ro AI sai kiểm soát được bằng HITL/Fallback? | **Có thể thiết kế**, nhưng chưa được nghiệp vụ và an ninh thông tin duyệt. |
| Stakeholders sẵn sàng đổi quy trình? | **Chưa xác nhận.** Cần phỏng vấn đội MICE và người duyệt báo giá. |

**Quyết định: NOT YET.** Có cơ sở công khai để chọn luồng yêu cầu hội họp và có thiết kế pilot hẹp, nhưng chưa có baseline, log đã khử danh tính, quyền tích hợp hay xác nhận của đội vận hành. Bước kế tiếp là phỏng vấn 3–5 người xử lý yêu cầu, đo mẫu ≥100 yêu cầu và thử form/rule trước. Chỉ chuyển **GO** khi các cổng pilot ở mục 6 đạt; chuyển **NO-GO cho LLM** nếu form/rule đạt mục tiêu tương đương với chi phí và rủi ro thấp hơn.

## 8. Liên hệ với bài code bắt buộc của lớp

File `starter-code/prompt_prototype.py` kiểm thử **tình huống Xanh SM pin yếu do đề cung cấp**, tách biệt với bài toán Vinpearl nhóm chọn cho báo cáo. Không dùng kết quả kiểm thử Xanh SM để tuyên bố giải pháp Vinpearl đã được kiểm chứng.

## Nguồn

- [Vinpearl — Hội họp & Sự kiện](https://vinpearl.com/vi/meeting-events)
- [Vinpearl Cửa Hội — kênh yêu cầu báo giá/đặt chỗ](https://vinpearl.com/vi/hotels/vinpearl-cua-hoi-resort-affiliated-by-melia/meeting-and-events)
- [01-worksheet.md](01-worksheet.md), [03-inspiration-kit.md](03-inspiration-kit.md) của bài lab.
