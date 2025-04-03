import streamlit as st
from api import query_groq

# Define Personalities
personalities = {
    "Bunty - The Humorous Companion": "You are Bunty, the ultimate funny, lighthearted AI. You crack jokes, make puns, and ensure every conversation is playful. You speak like a stand-up comedian, using sarcasm, witty comebacks, and a touch of randomness. You often start with ‘Yo buddy!’ and love making people laugh.",
}

# Streamlit UI
st.title("😂 Bunty - The Funny AI Chatbot")
st.sidebar.title("🎭 Choose a Personality")
selected_personality = st.sidebar.radio("Select:", list(personalities.keys()))

st.write(f"💬 **{selected_personality} says:** {personalities[selected_personality]}")

user_input = st.text_input("You: ", "")

if st.button("Send"):
    if user_input.strip():
        response = query_groq(user_input, personalities[selected_personality])
        st.write(f"🤖 **{selected_personality}:** {response}")
