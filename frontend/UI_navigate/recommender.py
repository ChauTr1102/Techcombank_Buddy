import streamlit as st
import pandas as pd
import requests
from dotenv import load_dotenv
from streamlit_extras.bottom_container import bottom
import os
import json
import re

load_dotenv(dotenv_path="./endpoints.env")

st.title("🤖 Gợi ý sản phẩm cho khách hàng")
st.markdown("Theo dõi hoạt động tài chính và nhận gợi ý sản phẩm phù hợp.")

# --- User Selection ---
st.subheader("👤 Chọn User")
users = [
    "ad089c26-f733-4535-9901-bfbf827272b5",
    "1fce992a-435c-4363-917c-aed958213b43",
    "26b6cb73-8bb6-4bf5-a7a0-c932721e1df9",
    "51c75821-5a6e-4e29-948b-2ecfdc9cc12f",
    "3d29ae48-1838-44ba-ae30-8a8c4275d138",
    "6eb9c9f6-5fda-44af-a732-b838ab15e8e8",
    "e0da2e4f-4c18-4d59-8d77-3b608e4fa3ff"
]
selected_user = st.selectbox("Chọn từ danh sách:", users)
custom_user = st.text_input("Hoặc nhập User ID khác:")
selected_user = custom_user if custom_user else selected_user

st.markdown(f"**User đã chọn:** `{selected_user}`")

# --- API Calls ---
def fetch_customer_segment(user_id):
    API_URL = os.getenv("SEGMENT_API", "http://localhost:8000/customer_segment/")
    response = requests.post(API_URL, json={"user_id": user_id})
    return response.json() if response.status_code == 200 else None

def fetch_explanation_for_recommendation(data):
    API_URL = os.getenv("EXPLAIN_API", "http://localhost:8000/get_explain_for_eight_recommendation/")
    response = requests.post(API_URL, json={"data": f"""{data}"""})
    return response.json() if response.status_code == 200 else None

# --- Customer Segment Info ---
segment_data = fetch_customer_segment(selected_user)

if segment_data:
    st.markdown("## 🧬 Phân khúc khách hàng")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 👤 Thông tin khách hàng")
        info = segment_data.get("customer_info", {})
        st.write({
            "Tuổi": info.get("age"),
            "Tình trạng hôn nhân": info.get("marital_status"),
            "Nghề nghiệp": info.get("occupation"),
            "Số người trong hộ": info.get("household_size"),
            "Thu nhập tháng ($)": round(info.get("monthly_salary", 0), 2),
            "Thu nhập phân khúc": info.get("income_tier"),
        })

    with col2:
        st.markdown("### 📊 Thống kê phân khúc")
        stats = segment_data.get("segment_stats", {})
        demo = stats.get("demographics", {})
        st.write({
            "Tuổi TB": round(demo.get("avg_age", 0), 2),
            "Hôn nhân phổ biến": demo.get("common_marital_status"),
            "Nghề phổ biến": demo.get("common_occupation"),
            "Hộ trung bình": round(demo.get("avg_household_size", 0), 2),
        })

    # --- Top 3 Recommended Products ---
    st.markdown("## 🎯 Top 3 Gợi ý sản phẩm")
    recommendations = segment_data.get("product_recommendations", [])
    top3 = sorted(recommendations, key=lambda x: x["reward_value"], reverse=True)[:3]

    for i, product in enumerate(top3, 1):
        st.markdown(f"""
        <div style="border:1px solid #ccc;padding:15px;border-radius:10px;margin-bottom:10px;background-color:#f9f9f9">
            <b>#{i}. {product['category']}</b><br>
            <ul>
                <li><b>Tier:</b> {product['tier']}</li>
                <li><b>Loại phần thưởng:</b> {product['reward_type']}</li>
                <li><b>Giá trị phần thưởng:</b> {product['reward_value']}%</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# --- Explanation Section ---
st.markdown("## 📖 Giải thích gợi ý sản phẩm")
explanation = fetch_explanation_for_recommendation(segment_data)
if explanation:
    # Nếu raw là chuỗi, loại bỏ markdown fence và parse JSON
    if isinstance(explanation, str):
        # Loại bỏ ```json và ``` nếu có
        # Dùng regex để lấy phần giữa hai dấu ```
        m = re.search(r"```json\s*(\[\s*[\s\S]*?\])\s*```", explanation)
        json_str = m.group(1) if m else explanation.strip("` \n")
        try:
            data = json.loads(json_str)
            st.json(data)
        except json.JSONDecodeError as e:
            st.error(f"Lỗi phân tích JSON: {e}")
            # Hiện raw gốc để debug
            st.write(explanation)
    else:
        # Nếu đã là object (list/dict), render trực tiếp
        st.json(explanation)
else:
    st.warning("Không thể lấy dữ liệu giải thích.")
