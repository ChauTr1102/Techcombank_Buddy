import streamlit as st
import pandas as pd
from datetime import datetime, timedelta


st.title("📈 Giao Dịch Gần Đây")
st.markdown("Theo dõi hoạt động tài chính của bạn một cách rõ ràng và trực quan.")

# Giả lập dữ liệu giao dịch
@st.cache_data
def load_transactions():
    return pd.DataFrame([
        {"Ngày": datetime.now() - timedelta(days=1), "Loại giao dịch": "Chuyển tiền", "Số tiền": -500000, "Mô tả": "Chuyển khoản đến Nguyễn Văn A"},
        {"Ngày": datetime.now() - timedelta(days=2), "Loại giao dịch": "Nhận tiền", "Số tiền": 1200000, "Mô tả": "Lương tháng 6"},
        {"Ngày": datetime.now() - timedelta(days=3), "Loại giao dịch": "Mua hàng", "Số tiền": -350000, "Mô tả": "Thanh toán Tiki"},
        {"Ngày": datetime.now() - timedelta(days=4), "Loại giao dịch": "Rút tiền ATM", "Số tiền": -200000, "Mô tả": "ATM Techcombank"},
        {"Ngày": datetime.now() - timedelta(days=5), "Loại giao dịch": "Nhận tiền", "Số tiền": 200000, "Mô tả": "Bạn bè chuyển"},
    ])

df = load_transactions()

# Bộ lọc
with st.expander("🔍 Lọc giao dịch"):
    col1, col2 = st.columns(2)
    with col1:
        from_date = st.date_input("Từ ngày", datetime.now() - timedelta(days=7))
    with col2:
        to_date = st.date_input("Đến ngày", datetime.now())
filtered_df = df[(df["Ngày"].dt.date >= from_date) & (df["Ngày"].dt.date <= to_date)]

# Hiển thị bảng
display_df = filtered_df.copy()
display_df["Số tiền"] = display_df["Số tiền"].apply(lambda x: f"₫{x:,.0f}".replace(",", "."))  # Format kiểu Việt Nam
display_df["Ngày"] = display_df["Ngày"].dt.strftime("%d-%m-%Y")  # Format ngày đẹp

st.dataframe(display_df, use_container_width=True, hide_index=True)

# Tổng kết
total_in = filtered_df[filtered_df["Số tiền"] > 0]["Số tiền"].sum()
total_out = filtered_df[filtered_df["Số tiền"] < 0]["Số tiền"].sum()

col3, col4 = st.columns(2)
with col3:
    st.success(f"💸 Tổng tiền vào: ₫{total_in:,.0f}")
with col4:
    st.error(f"💳 Tổng chi tiêu: ₫{abs(total_out):,.0f}")

