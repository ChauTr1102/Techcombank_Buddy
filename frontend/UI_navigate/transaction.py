import streamlit as st
import pandas as pd
import requests
from datetime import datetime

st.title("📈 Giao Dịch Gần Đây")
st.markdown("Theo dõi hoạt động tài chính của bạn một cách rõ ràng và trực quan.")

API_URL = "http://localhost:8000/transaction_history/"

@st.cache_data
def load_transactions():
    resp = requests.get(API_URL)
    resp.raise_for_status()
    data = resp.json()
    df = pd.DataFrame(data, columns=[
        "sender_name",
        "receiver_name",
        "amount_str",
        "note",
        "created_at"
    ])
    df["amount"] = (
        df["amount_str"]
          .str.replace(r"[\$,]", "", regex=True)
          .astype(float)
          .astype(int)
    )
    df["created_at"] = (
        pd.to_datetime(df["created_at"], utc=True)
          .dt.tz_convert("Asia/Bangkok")
    )
    current_user = "Nguyễn Ngọc Hoàng"
    df["signed_amount"] = df.apply(
        lambda r: -r["amount"] if r["sender_name"] == current_user else r["amount"],
        axis=1
    )
    return df

# Load data
df = load_transactions()

# Determine date range
if not df.empty:
    min_date = df["created_at"].dt.date.min()
    max_date = df["created_at"].dt.date.max()
else:
    min_date = max_date = datetime.now().date()

# Initialize session state for filters
if "from_date" not in st.session_state:
    st.session_state.from_date = min_date
if "to_date" not in st.session_state:
    st.session_state.to_date = max_date

# Add reset button at top-right
col1, col2 = st.columns([9, 1])
with col2:
    if st.button("🔄 Reset Data"):
        st.session_state.from_date = min_date
        st.session_state.to_date = max_date

# Date filters
with st.expander("🔍 Lọc giao dịch", expanded=True):
    c1, c2 = st.columns(2)
    with c1:
        st.date_input(
            "Từ ngày",
            value=st.session_state.from_date,
            min_value=min_date,
            max_value=max_date,
            key="from_date"
        )
    with c2:
        st.date_input(
            "Đến ngày",
            value=st.session_state.to_date,
            min_value=min_date,
            max_value=max_date,
            key="to_date"
        )

filtered = df[
    (df["created_at"].dt.date >= st.session_state.from_date) &
    (df["created_at"].dt.date <= st.session_state.to_date)
]

# Prepare display
display = filtered.copy()
display["Ngày"] = display["created_at"].dt.strftime("%d-%m-%Y %H:%M")
display["Số tiền"] = display["signed_amount"].apply(
    lambda x: f"{'-' if x < 0 else ''}₫{abs(x):,}".replace(",", ".")
)
display = display[["Ngày", "sender_name", "receiver_name", "Số tiền", "note"]]
display.columns = ["Ngày", "Người gửi", "Người nhận", "Số tiền", "Mô tả"]

st.dataframe(display, use_container_width=True, hide_index=True)

# Summary
total_in = filtered.loc[filtered["signed_amount"] > 0, "signed_amount"].sum()
total_out = filtered.loc[filtered["signed_amount"] < 0, "signed_amount"].sum()

col3, col4 = st.columns(2)
with col3:
    st.success(f"💸 Tổng tiền vào: ₫{total_in:,.0f}".replace(",", "."))
with col4:
    st.error(f"💳 Tổng chi tiêu: ₫{abs(total_out):,.0f}".replace(",", "."))
