import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("api_key")

client = OpenAI(api_key = api_key)

st.image("images.png")
st.title("AI Advisor Bot :robot_face:")

with st.chat_message("ai"):
    st.write("How may I adviced you today?")

user_input = st.chat_input("Please write your query")

if "coversation_history" not in st.session_state:
    st.session_state["coversation_history"] = []

conv_hist = st.session_state["coversation_history"]
if user_input is not None:
    conv_hist.append({"sender":"user","message": user_input})
    response = client.chat.completions.create(model = "gpt-3.5-turbo", messages = [{"role":"user","content": user_input}])
    ai_response = response.choices[0].message.content
    conv_hist.append({"sender":"ai","message":ai_response})
for d in conv_hist: #list of dictionary and when we looping on dictionary it return keys
    with st.chat_message(d["sender"]):
        st.write(d["message"])
if st.sidebar.button("Clear History"):
    st.session_state["coversation_history"] = []

# #
