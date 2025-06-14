import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.card import card

st.title("🏦 Techcombank Loans")
st.markdown("Khám phá các giải pháp vay phù hợp với nhu cầu của bạn.")

# Giới thiệu nhanh
st.info("""
Techcombank cung cấp đa dạng các gói vay: vay mua nhà, vay tiêu dùng, vay ô tô... 
Lãi suất ưu đãi, thủ tục đơn giản, phê duyệt nhanh chóng.
""")

# Các gói vay
st.subheader("📋 Danh sách gói vay hiện có")

col1, col2 = st.columns(2)

with col1:
    card(
        title="Vay mua nhà",
        text="Lãi suất từ 7.5%/năm, thời hạn tới 35 năm.",
        image="https://techcombank.com.vn/_next/image?url=%2Fimages%2Fhome-loan.png&w=384&q=75",
        url="#",
    )
    card(
        title="Vay tiêu dùng tín chấp",
        text="Không cần tài sản đảm bảo. Hạn mức tới 300 triệu.",
        image="https://techcombank.com.vn/_next/image?url=%2Fimages%2Fpersonal-loan.png&w=384&q=75",
        url="#",
    )

with col2:
    card(
        title="Vay mua xe",
        text="Hỗ trợ lên đến 80% giá trị xe. Kỳ hạn tới 7 năm.",
        image="https://techcombank.com.vn/_next/image?url=%2Fimages%2Fcar-loan.png&w=384&q=75",
        url="#",
    )
    card(
        title="Vay kinh doanh",
        text="Tối đa 5 tỷ đồng cho hộ kinh doanh cá thể.",
        image="https://techcombank.com.vn/_next/image?url=%2Fimages%2Fbusiness-loan.png&w=384&q=75",
        url="#",
    )

# Thông tin thêm
with stylable_container("loan_apply_box", css_styles="padding: 1rem; border: 1px solid #ccc; border-radius: 10px;"):
    st.subheader("📞 Đăng ký tư vấn vay")
    st.text_input("Họ và tên")
    st.text_input("Số điện thoại")
    st.selectbox("Chọn loại vay", ["Vay mua nhà", "Vay tiêu dùng", "Vay mua xe", "Vay kinh doanh"])
    st.button("📤 Gửi đăng ký tư vấn")
