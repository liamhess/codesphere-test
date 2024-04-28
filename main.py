import streamlit as st
import backend_calls

st.set_page_config(
    page_title="Hacker News Aggregator",
    page_icon="💌"
)

st.title("Hacker News Aggregator ✌️")
st.write("Just input a couple of your interests and your mail to get a daily newsletter with the most relevant Hacker News stories for you")

with st.form(key="Form"):
    st.write("Subscribe to your personalized Hacker News Aggregator")
    email: str = st.text_input(label="E-Mail", placeholder="email@domain.com")
    interests: str = st.text_input(label="Interests", placeholder="AI, Cloud, Web Development, DevOps, Cybersecurity, Analytics...")
    submit_button: bool = st.form_submit_button(label="Submit")
        
if submit_button:
    backend_calls.subscribe_user(email, interests)
    st.write("Subscribed!!!")

with st.form(key="Unsubscribe-Form"):
    st.write("Unsubscribe your E-Mail")
    email: str = st.text_input(label="E-Mail", placeholder="email@domain.com")
    submit_button: bool = st.form_submit_button(label="Submit")
        
if submit_button:
    backend_calls.unsubscribe_user(email)
    st.write("Unsubscribed!!!")
