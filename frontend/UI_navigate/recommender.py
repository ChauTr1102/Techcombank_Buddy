import streamlit as st
import pandas as pd
import requests
from datetime import datetime, timedelta
import requests
from streamlit_extras.bottom_container import bottom
from dotenv import load_dotenv
load_dotenv(dotenv_path="./endpoints.env")

st.title("🤖 Gợi ý sản phẩm cho khách hàng")
st.markdown("Theo dõi hoạt động tài chính của bạn một cách rõ ràng và trực quan.")

st.subheader("👤 Chọn User")
users = [
    "ad089c26-f733-4535-9901-bfbf827272b5",
    "1fce992a-435c-4363-917c-aed958213b43",
    "26b6cb73-8bb6-4bf5-a7a0-c932721e1df9",
    "51c75821-5a6e-4e29-948b-2ecfdc9cc12f",
    "3d29ae48-1838-44ba-ae30-8a8c4275d138",
    "6eb9c9f6-5fda-44af-a732-b838ab15e8e8",
    "e0da2e4f-4c18-4d59-8d77-3b608e4fa3ff"
]  # Danh sách users
selected_user = st.selectbox("Chọn user:", users)

custom_user = st.text_input("Hoặc nhập user ID khác:", value="")

# Final selected user (custom input overrides dropdown)
selected_user = custom_user if custom_user else selected_user

st.write(f"User đã chọn: {selected_user}")

st.title("Đề Xuất Sản Phẩm")
st.markdown("Phân tích chi tiêu và đề xuất sản phẩm phù hợp với users.")
def fetch_customer_segment(user_id):
    API_URL = "http://localhost:8000/customer_segment/"
    response = requests.post(API_URL, json={"user_id": user_id})
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Không thể lấy dữ liệu phân khúc khách hàng.")
        return None

customer_segment = fetch_customer_segment(selected_user)
if customer_segment:
    st.subheader("Thông tin phân khúc khách hàng")
    st.write(customer_segment)

    st.subheader("Gợi ý sản phẩm")
    if "suggested_products" in customer_segment:
        suggested_products = customer_segment["suggested_products"]
        if suggested_products:
            for product in suggested_products:
                st.write(f"- {product}")
        else:
            st.write("Không có sản phẩm gợi ý.")
    else:
        st.write("Không có thông tin gợi ý sản phẩm.")