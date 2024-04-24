import streamlit as st

st.title("Hacker News Aggregator ✌️")
st.write("Just input a couple of your interests and your mail to get a daily newsletter with the most relevant Hacker News stories for you")

with st.form(key="Form"):
    st.write("Subscribe to your personalized Hacker News Aggregator")
    email: str = st.text_input(label="E-Mail", placeholder="email@domain.com")
    interests: str = st.text_input(label="Interests", placeholder="Next-Gen Cloud Providers, AI, Cybersecurity, Codesphere")
    submit_button: bool = st.form_submit_button(label="Submit")
	
if submit_button:
	st.write("Subscribed!!!")

with st.form(key="Unsubscribe-Form"):
    st.write("Unsubscribe your E-Mail")
    email: str = st.text_input(label="E-Mail", placeholder="email@domain.com")
    submit_button: bool = st.form_submit_button(label="Submit")
	
if submit_button:
	st.write("Unsubscribed!!!")
