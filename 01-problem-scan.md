# 01 — Problem Scan (bản nháp để Ngân rà soát)

**Nhóm:** kingpro<br>
**Trưởng nhóm:** NGUYỄN VĂN DUY — magicduy56@gmail.com — `Clownnvd`<br>
**Thành viên:** DƯƠNG THỊ NGÂN — nguyenngan20022003@gmail.com — `nganduong-123`<br>
**Nguồn soạn ban đầu:** AI hỗ trợ trưởng nhóm trên branch của Ngân. Ngân cần tự đọc, sửa và commit phần phân tích của mình trước khi nộp cá nhân.

## Phase 1 — SCAN

Các kênh dịch vụ dưới đây có nguồn công khai; **điểm nghẽn là giả thuyết cần xác minh**, không phải số liệu nội bộ. Bốn lenses của worksheet đều được dùng.

| # | Đơn vị | Lens | Cơ hội cần kiểm chứng | Cơ sở công khai |
|---|---|---|---|---|
| 1 | Vinpearl | Tốn thời gian | Yêu cầu hội họp nhiều điều kiện có thể cần nhân viên đọc, tìm trường thiếu và hỏi lại trước khi báo giá. | [Vinpearl có kênh gửi yêu cầu sự kiện](https://vinpearl.com/vi/meeting-events). |
| 2 | VinFast | Lặp lại | Phản hồi khách sau bảo dưỡng có thể cần tóm tắt và gán nhóm vấn đề để chuyển xưởng/CSKH. | [VinFast công bố bước gọi ghi nhận phản hồi sau dịch vụ](https://vinfastauto.com/vn_vi/dich-vu-bao-duong-oto). |
| 3 | Vinhomes | Pain từ người khác | Phản ánh về tiện ích/bảo trì có thể bị chuyển vòng giữa bộ phận nếu mô tả tự do không rõ. | [Vinhomes công bố kênh liên hệ qua Resident App](https://market.vinhomes.vn/du-an/vinhomes-ocean-park-3). |
| 4 | Vinmec | AI-upgrade | Người đặt lịch có thể cần tóm tắt nhu cầu trước khi nhân viên hướng dẫn chọn dịch vụ/chuyên khoa. | [MyVinmec có luồng đặt lịch](https://www.vinmec.com/vie/chu-de/dat-lich-kham-vinmec). Quyết định y tế phải do người có chuyên môn. |
| 5 | VinFast | AI-upgrade | Mô tả sự cố xe của khách có thể được cấu trúc thành phiếu triệu chứng để nhân viên dịch vụ xem lại. | [App VinFast nhận mô tả khi đặt dịch vụ](https://vinfastauto.com/vn_vi/node/9360). |

**Ba thẻ để đánh giá nhanh:** #1, #2, #3. #4 có rủi ro y tế cao; #5 liên quan an toàn xe và cần quy trình kỹ thuật. Trước khi quyết định dự án, cần hỏi một người vận hành thật về kênh, khối lượng và lỗi thường gặp.

## Phase 2 — QUICK-ASSESS

### Card A — Vinpearl: phát hiện yêu cầu hội họp còn thiếu thông tin

| Trường | Bản nháp phân tích |
|---|---|
| Actor | Nhân viên kinh doanh hội họp; khách doanh nghiệp chờ phản hồi. |
| Bài toán | Yêu cầu viết tự do thiếu ngày, số khách hoặc địa điểm có thể khiến nhân viên phải đọc lại và hỏi nhiều vòng. |
| Current workflow giả định | Nhận yêu cầu → đọc/tách nhu cầu → phát hiện thiếu → hỏi khách → kiểm tra phòng/giá → phản hồi. |
| Bottleneck | Đọc và hỏi rõ: **7 phút/lượt giả định**, chưa đo tại Vinpearl. |
| AI step | Trích trường có dẫn đoạn nguồn, phát hiện mâu thuẫn, soạn câu hỏi còn thiếu dạng nháp. |
| Metric pilot | Recall trường thiếu ≥95%; 0 giá/khả dụng do AI tự bịa; giảm ≥40% thời gian chuẩn bị bản nháp so với baseline đo được. |
| Quick architecture | **LLM Feature** để hiểu văn bản + rule kiểm tra trường bắt buộc + nhân viên duyệt. |

### Card B — VinFast: phân loại phản hồi hậu mãi

| Trường | Bản nháp phân tích |
|---|---|
| Actor | Nhân viên CSKH/xưởng; khách đã bảo dưỡng. |
| Bài toán | Ý kiến tự do sau dịch vụ có thể cần gán chủ đề và chuyển đúng bộ phận. |
| Current workflow giả định | Ghi nhận phản hồi → đọc ghi chú → chọn nhãn → chuyển xưởng/CSKH → theo dõi đóng phiếu. |
| Bottleneck | Đọc và gán nhãn: **4 phút/lượt giả định**, cần đo. |
| AI step | Đề xuất nhãn và tóm tắt; người phụ trách xác nhận. |
| Metric pilot | Macro-F1 ≥0,90 trên tập nhãn đã thống nhất; ≥95% phản ánh an toàn được chuyển người trực; giảm ≥30% thời gian gán nhãn. |
| Quick architecture | Rule cho từ khóa nguy hiểm; LLM chỉ tóm tắt trường hợp mơ hồ. |

### Card C — Vinhomes: định tuyến phản ánh cư dân

| Trường | Bản nháp phân tích |
|---|---|
| Actor | Cư dân, ban quản lý tòa nhà và bộ phận kỹ thuật. |
| Bài toán | Phiếu chứa nhiều vấn đề có thể được chuyển sai tuyến hoặc phải hỏi lại. |
| Current workflow giả định | Cư dân gửi → nhân viên đọc → xác định tòa/loại/sự khẩn → chuyển bộ phận → xử lý. |
| Bottleneck | Phân loại và chuyển: **5 phút/lượt giả định**, cần đo. |
| AI step | Tách các vấn đề trong một phiếu, gợi ý tuyến, đánh dấu ca khẩn cho người trực. |
| Metric pilot | ≥90% phiếu đến đúng tuyến lần đầu; ≥99% ca khẩn được người trực xem; giảm ≥25% lượt chuyển lại. |
| Quick architecture | Rule ưu tiên khẩn cấp + LLM Feature cho văn bản nhiều ý + người duyệt. |

## Lựa chọn cho nhóm và phản biện

**Chọn Card A — Vinpearl** để cùng hướng với báo cáo nhóm. Cơ hội tập trung vào **bản tóm tắt và câu hỏi còn thiếu**, không để AI ra giá hay đặt phòng. Bài toán có thể thử trên dữ liệu giả lập và sau đó đo với yêu cầu đã khử danh tính nếu Vinpearl cho phép. Phản biện quan trọng: nếu một form bắt buộc trường giải quyết phần lớn việc hỏi lại thì dùng form/rule, không cần LLM. Quyết định dùng AI chỉ được đưa ra sau phép so sánh với baseline đó.
