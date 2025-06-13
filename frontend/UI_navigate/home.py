
import streamlit as st
from PIL import Image


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


