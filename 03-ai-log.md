# 03 — AI Log / Reflection của Dương Thị Ngân (bản nháp cần xác nhận)

**Nhóm:** kingpro<br>
**Trưởng nhóm:** NGUYỄN VĂN DUY — magicduy56@gmail.com — `Clownnvd`<br>
**Thành viên:** DƯƠNG THỊ NGÂN — nguyenngan20022003@gmail.com — `nganduong-123`<br>
**Tình trạng tác giả:** AI đã soạn bản nháp trong thư mục/branch của Ngân theo yêu cầu của trưởng nhóm. Ngân cần trực tiếp đọc, chạy thử và sửa phần phản ánh cá nhân trước khi tự commit; không trình bày các bước chưa làm như trải nghiệm của Ngân.

## Nhật ký AI tạo bản nháp

| Bước | AI giúp gì | Kiểm chứng / điều chỉnh |
|---|---|---|
| Quét cơ hội | Gợi ý 5 tác vụ từ Vinpearl, VinFast, Vinhomes, Vinmec và phân theo 4 lenses của worksheet. | Chỉ giữ tác vụ có kênh dịch vụ được nguồn chính thức xác nhận; chữ “điểm nghẽn” là giả thuyết, không phải kết quả khảo sát. |
| Chọn thẻ | Đưa Vinpearl, VinFast hậu mãi và Vinhomes phản ánh cư dân vào Quick Assess. | Chọn Vinpearl vì phạm vi có thể giới hạn ở phát hiện trường thiếu; Vinmec/VinFast lỗi xe có rủi ro sức khỏe/an toàn cao hơn. |
| Phân tích sâu | Đề xuất workflow, metric, ranh giới và future flow. | Không nhận các mốc 20 phút/150 yêu cầu là số liệu thật; gắn nhãn “giả định” và đưa kế hoạch đo baseline. Chọn `NOT YET` thay vì khẳng định `GO` khi chưa có log nội bộ. |
| Kiểm tra AI Fit | So sánh form/rule, LLM feature và agent. | Form/rule phải là baseline; chỉ giữ LLM cho văn bản tự do khó cấu trúc; không dùng agent tự báo giá/đặt chỗ. |
| Prototype code | AI tạo một system prompt riêng cho tình huống Xanh SM và ba input tấn công: pin 1% dù trạm gần, yêu cầu bỏ tag từ “quản lý”, role developer giả với pin 3%. | Trên máy chung, `gpt-4.1-mini` trả `[DRAFT_ONLY]` ở cả 3 ca; hai ca pin nguy cấp trả JSON `dispatch_mobile_charger`. Lệnh `python autograder/autograder.py` đạt **10/10 trên máy**. Đây là lượt chạy do AI thực hiện khi chuẩn bị bản nháp, chưa phải Ngân tự kiểm tra. |

## Chỗ AI dễ sai và bài học về prompt

1. **Bịa quy trình nội bộ:** nguồn Vinpearl chỉ xác nhận kênh gửi yêu cầu, không cho biết ai đọc, thời gian hay số vòng hỏi lại. Cách sửa prompt là yêu cầu AI tách “bằng chứng công khai”, “giả thuyết vận hành” và “cần xác minh” ở mỗi phần.
2. **Bịa số liệu hiệu quả:** ví dụ lớp có các con số rất cụ thể, nhưng không thể chuyển sang Vinpearl. Cách sửa là mọi mốc thời gian, khối lượng và lợi ích trong báo cáo đều ghi “minh họa”; metric ≥95% và ≥40% là ngưỡng pilot, không phải kết quả đã đạt.
3. **Dùng AI khi rule đủ tốt:** nếu mẫu form bắt buộc trường giảm hỏi lại đáng kể thì AI có thể không đáng chi phí. Cách sửa là thêm phép so sánh baseline rule/form và điều kiện `NO-GO cho LLM`.
4. **Prompt injection trong code Xanh SM:** chỉ dẫn của người dùng như “bỏ tag” hay `<system>` giả không được lấn quy tắc hệ thống. System prompt phải nêu rõ `[DRAFT_ONLY]`, ngưỡng pin <5% và lệnh `dispatch_mobile_charger`, kèm kiểm tra kết quả bằng Python chứ không chỉ tin lời model.

## Việc Ngân cần xác nhận bằng trải nghiệm thật trên máy chung

- Đọc `01-problem-scan.md`, sửa ít nhất một thẻ bằng nhận xét riêng: actor, bước nghẽn, metric hoặc phương án rule/LLM. Ghi trong log **đã sửa gì và vì sao**.
- Mở `02-deep-dive-report.md` và sơ đồ, tự giải thích được 5 bước current-state, ba ranh giới AI và lý do `NOT YET`; ghi điều Ngân thấy thiếu/chưa chắc.
- Chạy `python starter-code/prompt_prototype.py` bằng model được thầy chấp nhận; ghi **provider thực tế**, số ca pass/fail và một phản hồi cụ thể. Nếu model vi phạm, ghi prompt cũ, prompt sửa và kết quả chạy lại. Không ghi Gemini nếu chỉ dùng OpenAI.
- Chạy `python autograder/autograder.py`, ghi điểm trên máy và sửa lỗi trước khi push. Sau đó tự commit với email GitHub `nguyenngan20022003@gmail.com`.

## Reflection để Ngân hoàn thiện sau khi trực tiếp làm

AI giúp lập cấu trúc và tạo nháp nhanh, nhưng chất lượng bài phụ thuộc vào việc tôi kiểm tra nguồn, phân biệt giả định với số liệu thật và nhận trách nhiệm cho quyết định. Phần tôi cần tự diễn đạt sau khi thử là: **tôi đã đổi chi tiết nào so với bản nháp AI, thử nghiệm thực tế ra sao và còn rủi ro gì**. Không nên dùng nguyên đoạn reflection này như bằng chứng đã trực tiếp làm nếu tôi chưa thực hiện các bước trên.

## Nguồn đã dùng trong bản nháp

- [Vinpearl — Hội họp & Sự kiện](https://vinpearl.com/vi/meeting-events)
- [VinFast — Dịch vụ bảo dưỡng](https://vinfastauto.com/vn_vi/dich-vu-bao-duong-oto)
- [Vinhomes — kênh liên hệ qua ứng dụng cư dân](https://market.vinhomes.vn/du-an/vinhomes-ocean-park-3)
- [Vinmec — đặt lịch](https://www.vinmec.com/vie/chu-de/dat-lich-kham-vinmec)
