# 01 — Problem Scan & Quick Assess

**Nhóm:** kingpro<br>
**Trưởng nhóm:** NGUYỄN VĂN DUY — `Clownnvd` — magicduy56@gmail.com<br>
**Thành viên:** DƯƠNG THỊ NGÂN — `nganduong-123` — nguyenngan20022003@gmail.com<br>
**Trạng thái:** Bản phân tích cá nhân trên branch `Clownnvd`; cần nhóm rà soát trước khi chọn bản đưa lên `main`.

## Phạm vi và cách đọc số liệu

Đây là bài scoping dựa trên các kênh dịch vụ công khai và [inspiration kit](03-inspiration-kit.md) của lớp, **không phải kết quả khảo sát nội bộ**. Các điểm nghẽn là giả thuyết cần kiểm chứng bằng phỏng vấn nhân viên và log tác vụ. Mọi thời gian hiện tại ghi “chưa đo”; các con số bên dưới là **mục tiêu pilot**, không phải thành tích hay số liệu Vinpearl/Vingroup đã công bố.

## Phase 1 — SCAN: 5 cơ hội qua 4 lenses

| # | Đơn vị | Lens | Giả thuyết bài toán vận hành | Cơ sở công khai / điều cần xác minh |
|---|---|---|---|---|
| 1 | Vinpearl | Tốn thời gian | Nhân viên kinh doanh phải đọc yêu cầu hội họp/đặt chỗ có nhiều điều kiện, gom các trường còn thiếu, kiểm tra quỹ phòng và soạn nháp phản hồi. | [Vinpearl có kênh gửi yêu cầu hội họp, sự kiện](https://vinpearl.com/vi/meeting-events). Cần xác minh lượng yêu cầu, kênh tiếp nhận và thời gian xử lý thực tế. |
| 2 | Vinhomes | Lặp lại | Phản ánh cư dân bằng ngôn ngữ tự do cần được gán loại yêu cầu, mức ưu tiên và bộ phận tiếp nhận; nhân viên có thể phải phân loại lại. | [Vinhomes công bố kênh liên hệ ban quản lý qua ứng dụng Vinhomes Resident](https://market.vinhomes.vn/du-an/vinhomes-ocean-park-3). Cần xác minh taxonomy và tỉ lệ chuyển sai. |
| 3 | VinFast | AI-upgrade | Mô tả lỗi xe bằng tiếng Việt đời thường cần chuyển thành phiếu tiếp nhận có cấu trúc để cố vấn dịch vụ kiểm tra, không phải chẩn đoán tự động. | [Ứng dụng VinFast cho phép mô tả dịch vụ và đặt sửa chữa/bảo dưỡng](https://vinfastauto.com/vn_vi/node/9360). Cần xác minh chất lượng mô tả đầu vào và quy trình tiếp nhận. |
| 4 | Vinmec | Pain từ người khác | Người đặt khám chưa biết chọn chuyên khoa phù hợp có thể cần hỗ trợ thu thập thông tin trước khi nhân viên y tế tư vấn. | [MyVinmec hỗ trợ đặt lịch và tìm bác sĩ](https://www.vinmec.com/vie/chu-de/dat-lich-kham-vinmec). Cần xác minh có thật tình trạng đặt sai chuyên khoa; rủi ro y tế khiến bài toán chưa phù hợp pilot ngắn. |
| 5 | VinFast | Lặp lại | Phản hồi sau bảo dưỡng bằng văn bản cần nhóm chủ đề và chuyển đúng xưởng/phòng chăm sóc khách hàng. | [VinFast công bố bước gọi khách ghi nhận phản hồi sau dịch vụ](https://vinfastauto.com/vn_vi/dich-vu-bao-duong-oto). Cần xác minh có log văn bản và thời gian phân loại thủ công. |

**Chọn ba bài toán để Quick Assess:** #1, #2 và #3. Chúng có đầu vào ngôn ngữ tự nhiên, một bước hỗ trợ rõ ràng và có thể giữ quyết định cuối cùng ở người phụ trách. #4 có nguy cơ gây hiểu nhầm y tế; #5 có thể đủ sức giải bằng nhãn/rule nếu biểu mẫu phản hồi đã có cấu trúc.

## Phase 2 — QUICK-ASSESS

### Card 1 — Vinpearl: chuẩn bị nháp báo giá hội họp

| Trường | Nội dung |
|---|---|
| Bài toán một câu | Chuyển yêu cầu hội họp nhiều điều kiện thành bản tóm tắt có cấu trúc và nháp câu hỏi/báo giá để nhân viên kinh doanh duyệt. |
| Actor | Nhân viên kinh doanh MICE/đặt đoàn và khách doanh nghiệp chờ phản hồi. |
| Workflow hiện tại — **giả thuyết** | 1. Nhận form/email → 2. Đọc và tách ngày, số khách, địa điểm, phòng, thiết bị → 3. Hỏi thông tin còn thiếu → 4. Kiểm tra khả dụng và giá trong hệ thống → 5. Soạn phản hồi, xin duyệt và gửi. |
| Bottleneck cần đo | Bước 2–3, 5: hiểu yêu cầu tự do và soạn phản hồi; **10 phút/lượt minh họa** trong workflow giả định 19 phút, **chưa có số thực đo**. |
| AI hỗ trợ | Trích xuất trường, đánh dấu trường còn thiếu, soạn **nháp** câu hỏi hoặc phản hồi từ dữ liệu đã được nhân viên cung cấp. |
| Metric pilot có số | Trích đúng ≥95% các trường bắt buộc trên tập kiểm thử đã gán nhãn; giảm ≥40% thời gian chuẩn bị nháp so với baseline đo cùng nhóm; 0 báo giá/giữ phòng được gửi tự động. |
| Quick architecture | **LLM Feature + rule kiểm tra trường + người duyệt**. Không dùng Agent tự đặt phòng. |

### Card 2 — Vinhomes: phân loại phản ánh cư dân

| Trường | Nội dung |
|---|---|
| Bài toán một câu | Đề xuất loại và tuyến xử lý cho phản ánh cư dân viết tự do trên kênh tiếp nhận. |
| Actor | Cư dân, nhân viên chăm sóc cư dân và ban quản lý tòa nhà. |
| Workflow hiện tại — **giả thuyết** | 1. Cư dân gửi phản ánh → 2. Nhân viên đọc → 3. Chọn loại/mức ưu tiên → 4. Chuyển bộ phận → 5. Bộ phận xác nhận hoặc chuyển lại. |
| Bottleneck cần đo | Bước 2–4, đặc biệt phản ánh có nhiều vấn đề; **4 phút/lượt giả định để lập pilot**, cần đo thực tế. |
| AI hỗ trợ | Gợi ý nhãn, tóm tắt vấn đề và tuyến tiếp nhận; rule bắt từ khóa khẩn cấp để chuyển người trực. |
| Metric pilot có số | Macro-F1 ≥0,90 trên bộ nhãn được thống nhất; ≥95% phiếu khẩn được chuyển người trực; giảm ≥30% thời gian phân loại so với baseline. |
| Quick architecture | **Rule cho khẩn cấp + LLM Feature cho văn bản mơ hồ**; nhân viên xác nhận trước khi giao việc. |

### Card 3 — VinFast: chuẩn hóa mô tả lỗi cho phiếu dịch vụ

| Trường | Nội dung |
|---|---|
| Bài toán một câu | Tóm tắt mô tả sự cố xe của khách thành phiếu tiếp nhận có cấu trúc để cố vấn dịch vụ kiểm tra. |
| Actor | Chủ xe, nhân viên tiếp nhận và kỹ thuật viên xưởng. |
| Workflow hiện tại — **giả thuyết** | 1. Khách nhập mô tả → 2. Nhân viên hỏi bổ sung → 3. Ghi triệu chứng/điều kiện phát sinh → 4. Chuyển cố vấn dịch vụ → 5. Kỹ thuật viên xác minh. |
| Bottleneck cần đo | Bước 2–3 khi mô tả thiếu/không chuẩn; **5 phút/lượt giả định để lập pilot**, cần đo thực tế. |
| AI hỗ trợ | Gợi ý câu hỏi làm rõ và nháp phiếu triệu chứng; không suy đoán mã lỗi hay hướng dẫn tiếp tục lái xe. |
| Metric pilot có số | ≥95% phiếu nháp có đủ trường triệu chứng, bối cảnh và mức khẩn; 0 khuyến nghị an toàn xe được gửi không qua cố vấn; giảm ≥25% lượt hỏi lại. |
| Quick architecture | **LLM Feature ở khâu tóm tắt**, rule cho cảnh báo nguy hiểm, cố vấn duyệt. |

## Phản biện và lựa chọn để Deep Dive

**Chọn Card 1 — Vinpearl MICE** cho báo cáo chi tiết. Ngôn ngữ của yêu cầu hội họp thường đa dạng, trong khi kiểm tra giá và quỹ phòng có thể tách thành bước xác định bằng hệ thống hiện hữu. Phạm vi pilot chỉ hỗ trợ nhân viên đọc và soạn nháp, không cho AI tạo cam kết thương mại. Card 2 phụ thuộc taxonomy và quy tắc khẩn cấp của từng khu đô thị; Card 3 liên quan an toàn xe và cần quy trình kỹ thuật chính thức. Đây là **quyết định scoping sơ bộ**, cần xác nhận với nhóm và nhân viên nghiệp vụ.

**Stress-test lập luận:** Một biểu mẫu bắt buộc các trường sẽ rẻ và đáng tin hơn AI với yêu cầu đơn giản. Chỉ triển khai LLM nếu mẫu yêu cầu tự do chiếm tỷ lệ đủ lớn, việc hỏi lại tốn thời gian đo được, và phép thử A/B chứng minh lợi ích sau khi trừ chi phí vận hành. Nếu không, chọn rule/form thay thế.
