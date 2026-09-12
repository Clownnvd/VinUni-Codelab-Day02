# Hướng dẫn cho Dương Thị Ngân — bài Lab 02 nhóm kingpro

**Nhóm:** kingpro<br>
**Trưởng nhóm:** NGUYỄN VĂN DUY — GitHub `Clownnvd` — magicduy56@gmail.com<br>
**Thành viên thực hiện:** DƯƠNG THỊ NGÂN — GitHub `nganduong-123` — nguyenngan20022003@gmail.com<br>
**Repo chung:** https://github.com/Clownnvd/VinUni-Codelab-Day02<br>
**Branch cá nhân đã tạo sẵn:** `nganduong-123`

Hai người có thể dùng **cùng máy tính**. Thư mục `C:\nextjs_project\VinUni-Codelab-Day02-Ngan` và branch `nganduong-123` đã có **bản nháp do AI chuẩn bị, commit bởi `Clownnvd`**. Ngân cần trực tiếp đọc, sửa, kiểm tra rồi **tự commit và push thêm phần của mình**. Bản nháp của người khác không chứng minh đóng góp của Ngân. Trưởng nhóm sẽ xem bài sau khi Ngân push và chỉ đưa **báo cáo đã chọn** lên `main`; file Python vẫn ở branch cá nhân.

## Đoạn hướng dẫn để dán vào ChatGPT trên máy chung

> Đây là phần bài cá nhân của **Dương Thị Ngân**, GitHub `nganduong-123`, email đăng ký `nguyenngan20022003@gmail.com`, thành viên nhóm **kingpro**. Trưởng nhóm là **Nguyễn Văn Duy**, GitHub `Clownnvd`, email `magicduy56@gmail.com`. Hai người dùng chung một máy; hãy làm trong thư mục clone riêng `C:\nextjs_project\VinUni-Codelab-Day02-Ngan`. Repo nhóm: `https://github.com/Clownnvd/VinUni-Codelab-Day02`. Ngân sẽ trực tiếp xem, chỉnh và xác nhận phần việc của mình trước khi commit.
>
> **Trước khi sửa file:** Ngân chấp nhận lời mời collaborator và tự đăng nhập GitHub `nganduong-123` trên máy chung. Kiểm tra tài khoản thực sự được dùng để push, mở thư mục `C:\nextjs_project\VinUni-Codelab-Day02-Ngan`, fetch/pull branch `nganduong-123`. Đọc toàn bộ `README.md`, `01-worksheet.md`, `02-deliverable-example.md`, `03-inspiration-kit.md`, `starter-code/prompt_prototype.py` và `autograder/autograder.py`. Branch hiện có bản nháp AI để Ngân đánh giá, chưa phải bài đã được Ngân xác nhận.
>
> **Phần cá nhân của tôi:** rà từng file nháp đã có. `01-problem-scan.md` cần ≥5 bài toán và 3 Quick Problem Cards; tôi sẽ sửa ít nhất một thẻ bằng lập luận của mình. `02-deep-dive-report.md` phân tích hướng nhóm chọn **Vinpearl: trợ lý đọc yêu cầu hội họp và soạn nháp phản hồi**; tôi sẽ kiểm tra 6 fields, workflow, metric và quyết định. `04-workflow-diagram.png` phải khớp báo cáo; nếu sửa quy trình thì tạo lại ảnh. `03-ai-log.md` phải phản ánh **đúng các bước tôi trực tiếp làm cùng AI**, gồm chỗ AI sai và cách kiểm chứng; thay mọi câu chưa đúng với trải nghiệm của tôi. Không chép nguyên bài của Nguyễn Văn Duy ở branch `Clownnvd`.
>
> **Code cá nhân:** hoàn thiện `starter-code/prompt_prototype.py` với system prompt, hàm gọi model và ít nhất 3 adversarial tests cho tình huống Xanh SM pin yếu do đề cho. Thầy đã xác nhận dùng ChatGPT/OpenAI được. Nếu dùng `OPENAI_API_KEY`, chỉ đọc key từ biến môi trường, không ghi key vào code, file `.md`, Git, ảnh chụp hay đoạn chat. Để qua autograder hiện tại, giữ phần gọi Gemini SDK hợp lệ và có thể thêm OpenAI fallback; in rõ provider nào thực sự được dùng. Kiểm tra `[DRAFT_ONLY]` và JSON `dispatch_mobile_charger` khi pin dưới 5%. Không ghi là đã chạy Gemini nếu chỉ chạy OpenAI.
>
> **Kiểm tra và nộp phần của tôi:** chạy `python starter-code/prompt_prototype.py` và `python autograder/autograder.py`, sửa lỗi cho tới khi autograder trên máy đạt 10/10 với lượt gọi model thật. Sau đó kiểm tra `git status`, commit bằng danh tính GitHub của tôi và push **chỉ** branch `nganduong-123`. Không push lên `main`, không merge `.py` vào `main`, không tự điền form nộp bài của nhóm. Báo cho trưởng nhóm URL branch và mã commit để trưởng nhóm review.
>
> Nếu thiếu quyền repo, API key hay thông tin không thể tự xác minh, hãy nói rõ điều còn thiếu. Không tạo số liệu nội bộ giả, không nhận là tôi đã làm bước chưa thực hiện.

## Các lệnh Ngân có thể dùng trên Windows PowerShell

Ngân chấp nhận lời mời từ GitHub trước khi push repo private. Kiểm tra tài khoản đang đăng nhập bằng `gh auth status` nếu có GitHub CLI; nếu còn là `Clownnvd`, Ngân tự đăng nhập/chuyển sang `nganduong-123` trước khi push. Dùng thư mục riêng đã tạo sẵn:

```powershell
cd C:\nextjs_project\VinUni-Codelab-Day02-Ngan
git fetch origin
git switch nganduong-123
git pull --ff-only origin nganduong-123
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

Nếu GitHub chưa nhận diện email commit, Ngân cần xác nhận email này trong tài khoản GitHub trước khi push để commit được gắn đúng người. Lệnh `git config user.name/email` chỉ đặt danh tính commit; cần kiểm tra tài khoản xác thực thực sự khi push bằng `gh auth status` hoặc VS Code.

**Gửi cho trưởng nhóm sau khi push:** link `https://github.com/Clownnvd/VinUni-Codelab-Day02/tree/nganduong-123`, mã commit từ lệnh cuối, ảnh hoặc text kết quả autograder (không kèm API key), và tóm tắt phần Ngân tự làm. Chỉ Nguyễn Văn Duy review/chọn file nhóm, merge `.md`/`.png` vào `main` và điền form chính thức.
