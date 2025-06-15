
import streamlit as st
from PIL import Image
import requests
import random
import json
import re


if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Xin chào, tôi có thể giúp gì cho bạn?"}]
if "show_chat" not in st.session_state:
    st.session_state.show_chat = False
if 'run_count' not in st.session_state:
    st.session_state.run_count = 0

# Function to toggle chat visibility
def toggle_chat():
    st.session_state.show_chat = not st.session_state.show_chat

# ========== CSS STYLES ==========
# This is where all the magic for positioning and styling happens.
st.markdown("""
    <style>
        /* Main chatbox container */
        .chatbox {
            position: fixed;
            bottom: 100px; /* Position above the floating button */
            right: 20px;
            width: 380px;
            height: 500px;
            background-color: white;
            border-radius: 15px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            z-index: 1000;
            display: flex;
            flex-direction: column;
            border: 1px solid #e0e0e0;
        }

        /* Chatbox Header */
        .chatbox-header {
            padding: 10px 15px;
            background-color: #D40000; /* Techcombank Red */
            color: white;
            font-weight: bold;
            border-top-left-radius: 15px;
            border-top-right-radius: 15px;
        }

        /* Messages Area */
        .messages-container {
            flex-grow: 1;
            padding: 15px;
            overflow-y: auto;
            display: flex;
            flex-direction: column-reverse; /* Newest messages at the bottom */
        }

        /* Input area at the bottom of the chatbox */
        .input-area {
            padding: 10px 15px;
            border-top: 1px solid #e0e0e0;
            display: flex;
            align-items: center; /* Vertically align text input and audio button */
            gap: 10px;
        }

        /* Floating "Try it now!" button container */
        .floating-button-container {
            position: fixed;
            bottom: 20px;
            right: 20px;
            z-index: 1001;
        }
        
        /* Style for the floating button itself */
        .floating-button-container button {
            background-color: #D40000 !important;
            color: white !important;
            border-radius: 50px !important; /* Make it a pill shape */
            font-weight: bold !important;
            padding: 12px 24px !important;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            border: none;
        }

        /* --- STYLING THE AUDIO RECORDER --- */
        /* This is the tricky part to make the audio input a small circle */

        /* Target the specific Streamlit component for audio input */
        [data-testid="stAudioInput"] {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        
        /* Hide the default "Record a clip" label and other visual fluff */
        [data-testid="stAudioInput"] > div:first-child {
            display: none;
        }

        /* Style the actual button element inside the component */
        [data-testid="stAudioInput"] button {
            width: 45px !important;
            height: 45px !important;
            border-radius: 50% !important; /* Make it a circle */
            background-color: #f0f2f6; /* A neutral background */
            border: none;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 0;
        }

        /* Style the microphone icon */
        [data-testid="stAudioInput"] button svg {
            width: 24px;
            height: 24px;
        }

    </style>
""", unsafe_allow_html=True)

# ========== HEADER ==========
col1, col2 = st.columns([1, 6])
with col1:
    # Use a try-except block in case the image is not found
    try:
        logo = Image.open("./static/logo_techcombank.png")
        st.image(logo, width=80)
    except FileNotFoundError:
        st.write("🏦") # Fallback icon
with col2:
    st.markdown(
        """
        <h1 style='color:#D40000; font-size: 36px; margin-bottom: 0;'>Techcombank Buddy</h1>
        <h4 style='color:#444;'>Trợ lý đa tác vụ hỗ trợ công việc ngân hàng</h4>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

# ========== MAIN TEXT ==========
st.markdown(
    """
    <div style='text-align: justify; font-size:18px;'>
        <p>
            Chào mừng bạn đến với <b>Techcombank Buddy</b> – hệ thống trợ lý đa tác vụ hỗ trợ các hoạt động nghiệp vụ ngân hàng.
            Ứng dụng giúp bạn tra cứu, tổng hợp dữ liệu, kiểm tra giao dịch và hỗ trợ ra quyết định nhanh chóng.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# i want image of the product to be random in some way, is there a product image library that i can use
# ========== PRODUCT CARDS ==========
st.markdown(
    """
    <div style='text-align: left; font-size: 24px; margin-bottom: 20px;'>
        <b>Có thể bạn sẽ thích</b>
    </div>
    """,
    unsafe_allow_html=True
)

CUSTOMER_SEG = "http://localhost:8000/customer_segment/"


@st.cache_data
def load_rcm():
    resp = requests.post(url=CUSTOMER_SEG, json={"user_id": "1fce992a-435c-4363-917c-aed958213b43"})
    rcm_data = resp.json()
    return rcm_data
# Load data
st.session_state["rcm_data"] = load_rcm()

# # i have 8 images for products, i want to display them randomly in a grid of 2 rows and 4 columns
# # Randomly shuffle the product images
# product_images = [f"./static/product_{i+1}.png" for i in range(8)]
# random.shuffle(product_images)

# # Display the product images in a grid of 2 rows and 4 columns
# for row in range(2):
#     cols = st.columns(4)
#     for i, col in enumerate(cols):
#         with col:
#             st.image(product_images[row * 4 + i], width=80)
#             st.markdown("**product title**")
#             st.caption("short content")

# Lấy dữ liệu sản phẩm từ API
EIGHT_RCM = "http://localhost:8000/get_explain_for_eight_recommendation/"
  # Thay thành endpoint thực tế của bạn
try:
    resp = requests.post(EIGHT_RCM, json={"data": f"""{st.session_state["rcm_data"]}"""})
    resp.raise_for_status()
    explaination = resp.json()
    if explaination:
    # Nếu raw là chuỗi, loại bỏ markdown fence và parse JSON
        if isinstance(explaination, str):
            m = re.search(r"```json\s*(\[\s*[\s\S]*?\])\s*```", explaination)
            json_str = m.group(1) if m else explaination.strip("` \n")
            try:
                st.session_state["product_explain"] = json.loads(json_str)
            except json.JSONDecodeError as e:
                st.error(f"Lỗi phân tích JSON: {e}")
                # Hiện raw gốc để debug
                st.write(explaination)
except Exception as e:
    st.error(f"Không thể tải danh sách sản phẩm: {e}")
    st.session_state["product_explain"] = []

# Đường dẫn ảnh tĩnh, giả định 1-1 với products
product_images = [f"./static/product_{i+1}.png" for i in range(len(st.session_state["product_explain"]))]

# Hiển thị sản phẩm theo lưới (2 hàng x 4 cột)
cols_per_row = 4
rows = (len(st.session_state["product_explain"]) + cols_per_row - 1) // cols_per_row
idx = 0
for r in range(rows):
    cols = st.columns(cols_per_row)
    for c, col in enumerate(cols):
        if idx < len(st.session_state["product_explain"]):
            product = st.session_state["product_explain"][idx]
            img_path = product_images[idx] if idx < len(product_images) else None
            with col:
                if img_path:
                    st.image(img_path, width=80)
                st.markdown(f"**{product.get('product_category', '')}**")
                st.caption(product.get('explain', ''))
            idx += 1
