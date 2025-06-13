# app.py

import streamlit as st

# --- PAGE CONFIG ---
# Set the initial state of the sidebar to be expanded
st.set_page_config(
    page_title="Financial Dashboard",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded" 
)

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
    st.session_state.messages = [{"role": "assistant", "content": "How can I help you today?"}]


# --- SIDEBAR WIDGETS ---
with st.sidebar:

    # 1. AUDIO INPUT (with robust reset logic)
    st.header("Voice Command")
    
    # We use a dynamic key to force a reset after processing
    audio_bytes = st.audio_input(
        "Click the microphone to record:", 
        key=f"audio_input_{st.session_state.audio_key}"
    )
    if audio_bytes:
        st.toast("received record!")
        
    st.markdown("---")

    # 2. CHAT BOX (This code is unchanged)
    st.header("Chat")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = f"You asked: '{prompt}'. I'm a demo bot, but I'm here to help!"
                st.markdown(response)
        
        st.session_state.messages.append({"role": "assistant", "content": response})

    st.markdown("---")


# --- NAVIGATION ---
pg = st.navigation([
    st.Page("UI_navigate/home.py", title="Home", icon="🏠"),
    st.Page("UI_navigate/card.py", title="Credit Cards", icon="💳"),
    st.Page("UI_navigate/loan.py", title="Loans", icon="🏦"),
    st.Page("UI_navigate/transaction.py", title="Transactions", icon="📈"),
])

pg.run()