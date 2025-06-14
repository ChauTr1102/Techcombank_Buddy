import streamlit as st
from streamlit_extras.card import card
from streamlit_extras.stylable_container import stylable_container



st.title("💳 Techcombank Credit Cards")
st.markdown("Chọn thẻ phù hợp với nhu cầu của bạn và đăng ký ngay hôm nay!")

# Bộ lọc loại thẻ
card_type = st.selectbox(
    "🔍 Lọc theo loại thẻ",
    ["Tất cả", "Thẻ tín dụng", "Thẻ ghi nợ", "Thẻ quốc tế"]
)

# Dữ liệu mẫu các loại thẻ
credit_cards = [
    {
        "name": "Techcombank Visa Signature",
        "type": "Thẻ tín dụng",
        "image": "https://techcombank.com.vn/the/visa-signature.png",
        "features": [
            "Hoàn tiền đến 2%",
            "Ưu đãi phòng chờ hạng thương gia",
            "Miễn phí thường niên năm đầu"
        ],
    },
    {
        "name": "Techcombank Visa Debit",
        "type": "Thẻ ghi nợ",
        "image": "https://techcombank.com.vn/the/visa-debit.png",
        "features": [
            "Rút tiền mọi lúc mọi nơi",
            "Thanh toán online dễ dàng",
            "Quản lý chi tiêu qua app"
        ],
    },
    {
        "name": "Techcombank JCB DreamCard",
        "type": "Thẻ quốc tế",
        "image": "https://techcombank.com.vn/the/jcb-dreamcard.png",
        "features": [
            "Trả góp lãi suất 0%",
            "Ưu đãi tại Nhật Bản & châu Á",
            "Quản lý dễ dàng trên Mobile Banking"
        ],
    },
]

# Lọc dữ liệu theo loại thẻ
if card_type != "Tất cả":
    filtered_cards = [c for c in credit_cards if c["type"] == card_type]
else:
    filtered_cards = credit_cards

# Hiển thị các thẻ
cols = st.columns(3)

for idx, card_data in enumerate(filtered_cards):
    with cols[idx % 3]:
        with stylable_container(
            key=card_data["name"],
            css_styles="""
                background-color: #f9f9f9;
                padding: 1rem;
                border-radius: 1rem;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                margin-bottom: 2rem;
            """,
        ):
            st.image(card_data["image"], width=200)
            st.subheader(card_data["name"])
            st.markdown(f"**Loại:** {card_data['type']}")
            st.markdown("### Ưu điểm:")
            for f in card_data["features"]:
                st.markdown(f"- ✅ {f}")
            if st.button("📝 Đăng ký ngay", key=f"apply_{idx}"):
                st.success(f"Bạn đã chọn đăng ký: **{card_data['name']}**")
