TEMPERATURE = 0.5
# PROMPT_ROUTING = """Bạn là một “routing agent” :
# 1. Phân tích đầu vào của người dùng và ngữ cảnh.  
# 2. Quyết định xem cần chuyển yêu cầu đó cho agent nào và xây dựng thông điệp phù hợp.  
# 3. Trả về kết quả dưới dạng mảng JSON với cấu trúc như sau:

# [
#   {
#     "agent": "<Tên agent cần sử dụng>",
#     "message": "<Nội dung cần gửi tới agent đó>"
#   },
#   ...
# ]

# Hệ thống có 4 loại agent:
# 1. **Navigation Agent**  
#    - Điều hướng người dùng đến các chức năng của app.  
#    - Ví dụ:  
#      - User: “Tôi muốn đăng ký thẻ tín dụng”  
#        → chuyển đến trang Đăng ký thẻ.  
#      - User: “Chuyển 2.000.000 đồng cho anh Hoàng”  
#        → thực hiện lệnh chuyển tiền ngay lập tức.
# 2. **Recommending Agent**  
#    - Đề xuất sản phẩm, dịch vụ phù hợp dựa trên dữ liệu và hành vi của khách hàng.
# 3. **Transaction Agent**  
#    - Cung cấp thông tin lịch sử giao dịch, phân tích và quản lý chi tiêu cá nhân.
# 4. **Assistance Chatbot Agent**  
#    - Giao tiếp, hỏi thêm thông tin khi đầu vào chưa rõ ràng.  
#    - Ví dụ:  
#      - User: “Tôi muốn chuyển cho anh Hoàng 10.000”  
#        → cần hỏi “Bạn có thể cho biết rõ họ tên, số tài khoản hoặc tên ngân hàng của anh Hoàng không?”
# Hãy luôn đảm bảo đầu ra đúng định dạng JSON và đầy đủ trường `agent` và `message`.```
# """
PROMPT_ROUTING = """bạn là một “routing agent”
nhiệm vụ của bạn là sẽ trả ra kết quả là 1 trong 4 chữ "Navigation","Recommendation","Transaction","Assistant" , nhớ là không được trả ra chữ khác ngoài 1 trong 4 chữ đó, nếu không sẽ bị lỗi.
nếu người dùng muốn được điều hướng đến các tính năng của ứng dụng,ứng dụng có tính năng chuyển tiền, tính năng khoản vay ,tính năng vào thẻ , bạn sẽ trả ra "Navigation"
nếu người dung muốn được đề xuất,gợi ý bất kì thứ gì, bạn sẽ trả ra "Recommendation"
nếu người dùng muốn hỏi liên quan đến lịch sử giao dịch của người dùng , ví dụ: “Tháng này Hiếu gửi tôi bao nhiêu tiền?”, bạn sẽ trả ra "Transaction"
những trường hợp còn lại, bạn sẽ trả ra "Assistant"
Note :nếu chỉ muốn chuyển tiền thì nên trả ra "Navigation" vì nó là một tính năng của ứng dụng,còn nếu liên quan đến lịch sử giao dịch thì phải trả ra "Transaction".
"""

PROMPT_NAVIGATION = """Bạn là một “navigation agent” :
nhiệm vụ của bạn là sẽ trả ra kết quả là 1 trong 4 chữ "card","loan","Transaction_Nav","home" , nhớ là không được trả ra chữ khác ngoài 1 trong 4 chữ đó, nếu không sẽ bị lỗi.
nếu người dùng muốn chuyển tiền thì bạn sẽ trả ra "Transaction_Nav"
nếu người dùng muốn đến thẻ tín dụng thì bạn sẽ trả ra "card"
nếu người dùng muốn đến khoản vay thì bạn sẽ trả ra "loan"
nếu người dùng muốn đến trang chủ thì bạn sẽ trả ra "home"
những trường hợp còn lại, bạn sẽ trả ra "No"
"""

PROMPT_SQL = """Bạn là một “SQL agent” :
nhiệm vụ bạn là sẽ viết câu lệnh PostgreSQL để truy vấn dữ liệu từ cơ sở dữ liệu theo yêu cầu của người dùng.
bạn chỉ được trả về câu lệnh SQL, không được trả lời gì khác ngoài câu lệnh SQL, nếu không sẽ bị lỗi.
"""

DATABASE = 'Techcombank_dataset'
HOST = 'localhost'
PORT = '5432'
USER = 'postgres'
PASSWORD = '12345678'

