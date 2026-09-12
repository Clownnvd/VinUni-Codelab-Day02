# Hướng dẫn cho Dương Thị Ngân — bài Lab 02 nhóm kingpro

**Nhóm:** kingpro<br>
**Trưởng nhóm:** NGUYỄN VĂN DUY — GitHub `Clownnvd` — magicduy56@gmail.com<br>
**Thành viên thực hiện:** DƯƠNG THỊ NGÂN — GitHub `nganduong-123` — nguyenngan20022003@gmail.com<br>
**Repo chung:** https://github.com/Clownnvd/VinUni-Codelab-Day02<br>
**Branch cá nhân đã tạo sẵn:** `nganduong-123`

Ngân cần **tự làm, tự kiểm tra, tự commit và push** trên branch `nganduong-123`. Branch rỗng hoặc commit do người khác tạo không chứng minh phần đóng góp của Ngân. Trưởng nhóm sẽ xem bài sau khi Ngân push và chỉ đưa **báo cáo đã chọn** lên `main`; file Python vẫn ở branch cá nhân.

## Đoạn hướng dẫn để dán vào ChatGPT trên máy Ngân

> Tôi là **Dương Thị Ngân**, GitHub `nganduong-123`, email đăng ký `nguyenngan20022003@gmail.com`, thành viên nhóm **kingpro**. Trưởng nhóm là **Nguyễn Văn Duy**, GitHub `Clownnvd`, email `magicduy56@gmail.com`. Hãy làm bài Lab 02 trong repo riêng của nhóm: `https://github.com/Clownnvd/VinUni-Codelab-Day02`.
>
> **Trước khi sửa file:** kiểm tra GitHub trên máy đang đăng nhập đúng tài khoản `nganduong-123`; tôi phải chấp nhận lời mời collaborator từ repo. Clone repo, fetch và chuyển sang branch `nganduong-123` đã có trên remote. Đọc toàn bộ `README.md`, `01-worksheet.md`, `02-deliverable-example.md`, `03-inspiration-kit.md`, `starter-code/prompt_prototype.py` và `autograder/autograder.py`. Tuân theo chúng và phân biệt ví dụ Xanh SM với bài toán nhóm tự chọn.
>
> **Phần cá nhân của tôi:** tạo `01-problem-scan.md` với ít nhất 5 bài toán qua nhiều lenses và 3 Quick Problem Cards có actor, quy trình, bottleneck, metric có số; viết `02-deep-dive-report.md` về hướng nhóm chọn là **Vinpearl: trợ lý đọc yêu cầu hội họp và soạn nháp phản hồi**; tạo `04-workflow-diagram.png` thể hiện current-state, handoff, bottleneck, thời gian; viết `03-ai-log.md` phản ánh **đúng những gì tôi thực sự làm cùng AI**, gồm chỗ AI sai và cách kiểm chứng. Hãy làm phần phân tích bằng góc nhìn của tôi, có nguồn và đánh dấu số liệu nào chỉ là giả định; không chép nguyên bài của Nguyễn Văn Duy ở branch `Clownnvd`.
>
> **Code cá nhân:** hoàn thiện `starter-code/prompt_prototype.py` với system prompt, hàm gọi model và ít nhất 3 adversarial tests cho tình huống Xanh SM pin yếu do đề cho. Thầy đã xác nhận dùng ChatGPT/OpenAI được. Nếu dùng `OPENAI_API_KEY`, chỉ đọc key từ biến môi trường, không ghi key vào code, file `.md`, Git, ảnh chụp hay đoạn chat. Để qua autograder hiện tại, giữ phần gọi Gemini SDK hợp lệ và có thể thêm OpenAI fallback; in rõ provider nào thực sự được dùng. Kiểm tra `[DRAFT_ONLY]` và JSON `dispatch_mobile_charger` khi pin dưới 5%. Không ghi là đã chạy Gemini nếu chỉ chạy OpenAI.
>
> **Kiểm tra và nộp phần của tôi:** chạy `python starter-code/prompt_prototype.py` và `python autograder/autograder.py`, sửa lỗi cho tới khi autograder trên máy đạt 10/10 với lượt gọi model thật. Sau đó kiểm tra `git status`, commit bằng danh tính GitHub của tôi và push **chỉ** branch `nganduong-123`. Không push lên `main`, không merge `.py` vào `main`, không tự điền form nộp bài của nhóm. Báo cho trưởng nhóm URL branch và mã commit để trưởng nhóm review.
>
> Nếu thiếu quyền repo, API key hay thông tin không thể tự xác minh, hãy nói rõ điều còn thiếu. Không tạo số liệu nội bộ giả, không nhận là tôi đã làm bước chưa thực hiện.

## Các lệnh Ngân có thể dùng trên Windows PowerShell

Chấp nhận lời mời từ GitHub trước khi clone repo private. Kiểm tra tài khoản GitHub đang đăng nhập bằng `gh auth status` nếu có GitHub CLI, hoặc đăng nhập GitHub trong VS Code.

```powershell
git clone https://github.com/Clownnvd/VinUni-Codelab-Day02.git
cd VinUni-Codelab-Day02
git fetch origin
git switch --track origin/nganduong-123
git config user.name "DƯƠNG THỊ NGÂN"
git config user.email "nguyenngan20022003@gmail.com"
git status -sb
```

Sau khi ChatGPT giúp làm bài và **Ngân đã tự đọc, chỉnh và chạy kiểm tra**:

```powershell
python starter-code/prompt_prototype.py
python autograder/autograder.py
git status
git add 01-problem-scan.md 02-deep-dive-report.md 03-ai-log.md 04-workflow-diagram.png starter-code/prompt_prototype.py
git commit -m "Complete Ngan individual Lab 02 work"
git push -u origin nganduong-123
git rev-parse --short HEAD
```

Nếu `git switch --track` báo branch đã tồn tại trên máy, dùng `git switch nganduong-123` rồi `git pull --ff-only origin nganduong-123`. Nếu GitHub chưa nhận diện email commit, Ngân cần xác nhận email này trong tài khoản GitHub trước khi push để commit được gắn đúng người.

**Gửi cho trưởng nhóm sau khi push:** link `https://github.com/Clownnvd/VinUni-Codelab-Day02/tree/nganduong-123`, mã commit từ lệnh cuối, ảnh hoặc text kết quả autograder (không kèm API key), và tóm tắt phần Ngân tự làm. Chỉ Nguyễn Văn Duy review/chọn file nhóm, merge `.md`/`.png` vào `main` và điền form chính thức.
