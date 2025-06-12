import streamlit as st
import altair as alt
from helper import get_ranking, get_ranking_score, get_analysis

st.title('Techcombank Buddy')


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
    st.subheader("Product Ranking")
    show_ranking(user_id)

    st.subheader("Data Visualization")
    show_ranking_score(user_id)

    st.subheader("Data Analysis")
    show_analysis(user_id)
elif not user_id:
    st.write("Please enter a User ID to see the results.")
elif not is_user_available(user_id):
    st.write("User ID not found.")
