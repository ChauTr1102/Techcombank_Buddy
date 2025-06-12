import streamlit as st
from dotenv import load_dotenv
import altair as alt
from helper import get_ranking, get_ranking_score, get_analysis

# Tải biến môi trường
load_dotenv()

# Thiết lập cấu hình trang
st.set_page_config(
    page_title="Techcombank Buddy",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",

)
# Header với logo Techcombank
st.image("static/logo_techcombank.png", width=200)  # Thay bằng đường dẫn logo thực tế
st.title("Techcombank Buddy")
st.markdown("**Hệ thống gợi ý sản phẩm cá nhân hóa dành cho khách hàng Techcombank**")

# Sidebar
st.sidebar.header("Điều hướng")
page = st.sidebar.selectbox("Chọn chức năng", ["Trang chủ","Tổng quan sản phẩm", "Gợi ý cá nhân hóa", "Phân tích dữ liệu"])

def show_ranking(user_id):
    ranking = get_ranking(user_id)
    for i, rank in enumerate(ranking, 1):
        st.write(f"{i}. {rank}")

def show_ranking_score(user_id):
    data = get_ranking_score(user_id)
    chart = alt.Chart(data).mark_bar().encode(
        x=alt.X('Category:N', axis=alt.Axis(labelAngle=0)),  # Horizontal x-axis labels
        y=alt.Y('Values:Q')
    )
    st.altair_chart(chart, use_container_width=True)

def show_analysis(user_id):
    analysis = get_analysis(user_id)
    st.write(analysis)

def is_user_available(user_id : str, list_user : list = ["test"]) -> bool:
    if user_id in list_user:
        return True

user_id = st.text_input("Enter User ID")
if is_user_available(user_id):
    with st.spinner("waiting..."):
        st.success("User ID found. Processing...")
elif not user_id:
    st.write("Please enter a User ID to see the results.")
elif not is_user_available(user_id):
    st.write("User ID not found.")

# Tab 1: Tổng quan sản phẩm
if page == "Tổng quan sản phẩm":
    show_ranking(user_id)

# Tab 2: Gợi ý cá nhân hóa
elif page == "Gợi ý cá nhân hóa":
    with st.spinner(text="In progress...", show_time=True):
        st.header("Gợi ý cá nhân hóa")
        show_ranking_score(user_id)

# Tab 3: Phân tích dữ liệu
else:
    show_analysis(user_id)
# Footer
st.markdown("---")
st.markdown("© 2025 Techcombank. All rights reserved.")


