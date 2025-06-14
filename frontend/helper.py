import pandas as pd
import streamlit as st

def get_ranking(user_id: str) -> list:
    if user_id == "test":
        # Placeholder for the actual ranking logic
        return ["Item A", "Item B", "Item C"]


def get_ranking_score(user_id: str) -> dict:
    # Placeholder for the actual ranking score logic
    if user_id == "test":
        score_dict = {"A": 90, "B": 80, "C": 70}
        data = pd.DataFrame(score_dict.items(), columns=["Category", "Values"])
        return data

def get_analysis(user_id: str) -> dict:
    # Placeholder for the actual analysis logic
    if user_id == "test":
        return "Data analysis results for user ID: test"
    
def navigate_to_page(navigation_output: str):
    UI_sample_folder_root = "UI_navigate"
    if navigation_output == "card":
        st.session_state.messages.append({"role": "assistant", "content": "Đang chuyển hướng đến trang thẻ tín dụng..."})
        st.switch_page(f"{UI_sample_folder_root}/card.py")
    elif navigation_output == "home":
        st.session_state.messages.append({"role": "assistant", "content": "Đang chuyển hướng đến trang chính..."})
        st.switch_page(f"{UI_sample_folder_root}/home.py")
    elif navigation_output == "loan":
        st.session_state.messages.append({"role": "assistant", "content": "Đang chuyển hướng đến trang vay vốn..."})
        st.switch_page(f"{UI_sample_folder_root}/loan.py")
    elif navigation_output == "Transaction":
        st.session_state.messages.append({"role": "assistant", "content": "Đang chuyển hướng đến trang giao dịch..."})
        st.switch_page(f"{UI_sample_folder_root}/transaction.py")
    else:
        st.session_state.messages.append({"role": "assistant", "content": "Sorry, I don't understand your request. Please try again."})