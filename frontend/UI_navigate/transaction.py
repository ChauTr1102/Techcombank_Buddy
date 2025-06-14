import streamlit as st
import pandas as pd
import requests
from datetime import datetime, timedelta

st.title("📈 Giao Dịch Gần Đây")
st.markdown("Theo dõi hoạt động tài chính của bạn một cách rõ ràng và trực quan.")

st.subheader("👤 Chọn User")
users = ["User 1", "User 2", "User 3", "User 4", "User 5"]  # Danh sách users
selected_user = st.selectbox("Chọn user:", users)

# Gọi API tự động khi user thay đổi
if selected_user:
    try:
        # Gọi API backend
        response = requests.post("http://localhost:8000/test_db/")  # Thay đổi URL theo backend của bạn

        if response.status_code == 200:
            st.success(f"✅ Đã tải dữ liệu thành công cho {selected_user}")
            # Có thể lưu response data vào session state nếu cần
            st.session_state['api_response'] = response.json()
        else:
            st.error(f"❌ Lỗi khi gọi API: {response.status_code}")
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Không thể kết nối đến backend: {str(e)}")


@st.cache_data
def load_transactions():
    return pd.DataFrame()


df = load_transactions()

# Kiểm tra nếu có dữ liệu
if not df.empty:
    # Bộ lọc
    with st.expander("🔍 Lọc giao dịch"):
        col1, col2 = st.columns(2)
        with col1:
            from_date = st.date_input("Từ ngày", datetime.now() - timedelta(days=7))
        with col2:
            to_date = st.date_input("Đến ngày", datetime.now())

        filtered_df = df[(df["Ngày"].dt.date >= from_date) & (df["Ngày"].dt.date <= to_date)]

    # Hiển thị bảng
    st.dataframe(
        filtered_df.sort_values(by="Ngày", ascending=False),
        use_container_width=True,
        column_config={
            "Số tiền": st.column_config.NumberColumn(format="₫{:,.0f}"),
            "Ngày": st.column_config.DateColumn(format="DD-MM-YYYY"),
        },
        hide_index=True,
    )

    # Tổng kết
    total_in = filtered_df[filtered_df["Số tiền"] > 0]["Số tiền"].sum()
    total_out = filtered_df[filtered_df["Số tiền"] < 0]["Số tiền"].sum()

    col3, col4 = st.columns(2)
    with col3:
        st.success(f"💸 Tổng tiền vào: ₫{total_in:,.0f}")
    with col4:
        st.error(f"💳 Tổng chi tiêu: ₫{abs(total_out):,.0f}")
else:
    st.info("📊 Chưa có dữ liệu giao dịch để hiển thị.")

st.title("Đề Xuất Sản Phẩm")
st.markdown("Phân tích chi tiêu và đề xuất sản phẩm phù hợp với bạn.")


# Tạo DataFrame trống cho notifications
@st.cache_data
def load_notifications():
    return pd.DataFrame(columns=[
        "Nhóm Phân Cụm",
        "Đề Xuất Sản Phẩm",
        "Lý Do Đề Xuất"
    ])


notifications_df = load_notifications()

# Hiển thị bảng thông báo
if not notifications_df.empty:
    st.dataframe(
        notifications_df,
        use_container_width=True,
        column_config={
            "Nhóm Phân Cụm": st.column_config.TextColumn("Nhóm Phân Cụm", width="medium"),
            "Đề Xuất Sản Phẩm": st.column_config.TextColumn("Đề Xuất Sản Phẩm", width="medium"),
            "Lý Do Đề Xuất": st.column_config.TextColumn("Lý Do Đề Xuất", width="large"),
        },
        hide_index=True,
    )
else:
    # Hiển thị bảng trống để minh họa cấu trúc
    st.markdown("**Cấu trúc bảng thông báo:**")
    sample_df = pd.DataFrame({
        "Nhóm Phân Cụm": [""],
        "Đề Xuất Sản Phẩm": [""],
        "Lý Do Đề Xuất": [""]
    })
    st.dataframe(
        sample_df,
        use_container_width=True,
        column_config={
            "Nhóm Phân Cụm": st.column_config.TextColumn("Nhóm Phân Cụm", width="medium"),
            "Đề Xuất Sản Phẩm": st.column_config.TextColumn("Đề Xuất Sản Phẩm", width="medium"),
            "Lý Do Đề Xuất": st.column_config.TextColumn("Lý Do Đề Xuất", width="large"),
        },
        hide_index=True,
    )