# app.py

import streamlit as st
import requests
from streamlit_float import *
from dotenv import load_dotenv
from helper import navigate_to_page
from streamlit_extras.bottom_container import bottom
import datetime
import sys
import os

# --- PAGE CONFIG ---

st.set_page_config(
    page_title="Financial Dashboard",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded",
)

load_dotenv(dotenv_path="./endpoints.env")
SPEECH_TO_TEXT = os.getenv("SPEECH_TO_TEXT")
ROUTER_MESSAGE = os.getenv("ROUTER_MESSAGE")
TRANSFER_MONEY_EXTRACTION = os.getenv("TRANSFER_MONEY_EXTRACTION")
TRANSFER_MONEY = os.getenv("TRANSFER_MONEY")

# --- TRANSFER DIALOG ---
@st.dialog("transfer money")
def open_transfer_dialog(receiver, amount, note):
    st.write("📤 Nhập thông tin chuyển tiền")

    receiver = st.text_input("👤 Người nhận", key="dialog_receiver_trans", value=receiver)

    amount = st.number_input("💰 Số tiền", key="dialog_amount_trans", value=amount)

    note = st.text_input("📝 Nội dung chuyển khoản", key="dialog_note_trans", value=note)

    if st.button("✅ Xác nhận chuyển tiền", key="dialog_confirm_button_trans"):
        transfer_data = {
            "receiver" : receiver,
            "note" : note,
            "amount" : amount
        }
        response = requests.post(TRANSFER_MONEY, json=transfer_data)
        if response.status_code == 200:
            st.success("✅ Chuyển tiền thành công!")
        else:
            st.markdown("⚠️ Giao dịch không thành công")
        # if receiver and amount >= 1000:
        #     st.session_state.transfer_success = True
        #     st.session_state.transfer_details = {
        #         "receiver": receiver,
        #         "amount": amount,
        #         "note": note,
        #         "time": datetime.strftime("%Y-%m-%d %H:%M:%S"),
        #         "type": "Chuyển tiền (Dialog)"
        #     }
        #     if "new_transactions" not in st.session_state:
        #         st.session_state.new_transactions = []
        #     st.session_state.new_transactions.append({
        #         "Ngày": datetime.now(),
        #         "Loại giao dịch": "Chuyển tiền (Dialog)",
        #         "Số tiền": -amount,
        #         "Mô tả": f"Chuyển đến {receiver} - {note if note else 'Không ghi chú'}"
        #     })
        #     st.rerun()
        # else:
        #     st.warning("⚠️ Vui lòng nhập đầy đủ Người nhận và Số tiền hợp lệ (tối thiểu 1000).")



# --- CUSTOM CSS TO WIDEN THE SIDEBAR ---
# This is a key part of the solution to make the UI look better.
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        width: 400px !important; # Set the width to your desired value
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# --- INITIALIZE SESSION STATE FOR WIDGET RESET ---
if "audio_key" not in st.session_state:
    st.session_state.audio_key = 0
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "How can I help you today?"}
    ]

if "trigger_transfer_dialog" not in st.session_state: # Initialize the flag
    st.session_state.trigger_transfer_dialog = False



# --- SIDEBAR WIDGETS ---
with st.sidebar:

    # 1. AUDIO INPUT (with robust reset logic)
    st.header("Voice Command")

    # We use a dynamic key to force a reset after processing
    with bottom():
        if "last_audio" not in st.session_state:
            st.session_state.last_audio = None
        audio_bytes = st.audio_input(
            "Nhấn để nói chuyện:",
            key=f"audio_input_{st.session_state.audio_key}",
        )

    if audio_bytes:
        # Lấy bytes và so sánh
        audio_bytes_value = audio_bytes.getvalue()
        if audio_bytes_value != st.session_state.last_audio:
            # Cập nhật last_audio
            st.session_state.last_audio = audio_bytes_value
            # Thực sự có input mới -> gọi STT
            res = requests.post(
                SPEECH_TO_TEXT,
                files={"file": ("audio.wav", audio_bytes_value, "audio/wav")}
            )
            transcript = res.json()

            # Đẩy vào history và gọi router
            st.session_state.messages.append({"role": "user", "content": transcript})
            payload = {"user_input": transcript, "history": ""}
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response = requests.post(ROUTER_MESSAGE, json=payload)
                    # navigate_to_page(response.json())
                    st.markdown(response.json())
                    if response.json() in ["card", "home", "loan", "Transaction"]:
                        navigate_to_page(response.json())
                    elif response.json() == "TranferMoney":
                        payload = {"user_input": transcript, "history": ""}
                        response = requests.post(url=TRANSFER_MONEY_EXTRACTION, json=payload)
                        if response.status_code == 200:
                            open_transfer_dialog(response.json()[0], response.json()[1], response.json()[2])

            st.session_state.messages.append({"role": "assistant", "content": response.json()})

        else:
            # Nếu cùng audio, nhảy qua không làm gì thêm
            pass

    st.markdown("---")

    # 2. CHAT BOX
    st.header("Chat")

    if "messages" not in st.session_state:
        st.session_state.messages = []
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    with bottom():
        prompt = st.chat_input("What is up?")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        payload = {"user_input": f"{prompt}", "history": ""}

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = requests.post(url=ROUTER_MESSAGE, json=payload)
                st.markdown(response.json())
                if response.json() in ["card", "home", "loan", "Transaction"]:
                    navigate_to_page(response.json())
                elif response.json() == "TranferMoney":
                    payload = {"user_input": prompt, "history": ""}
                    response = requests.post(url=TRANSFER_MONEY_EXTRACTION, json=payload)
                    if response.status_code == 200:
                        open_transfer_dialog(response.json()[0], response.json()[1], response.json()[2])
                    # navigate_to_page("TranferMoney")
                    # st.rerun()
        st.session_state.messages.append({"role": "assistant", "content": response.json()})

    st.markdown("---")


    # --- NAVIGATION ---
    pg = st.navigation(
        [
            st.Page("UI_navigate/home.py", title="Home", icon="🏠"),
            st.Page("UI_navigate/card.py", title="Credit Cards", icon="💳"),
            st.Page("UI_navigate/loan.py", title="Loans", icon="🏦"),
            st.Page("UI_navigate/transaction.py", title="Transactions", icon="📈"),
        ]
    )

pg.run()
