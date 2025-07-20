import streamlit as st
import requests
import tomllib
import os

config_path = os.path.join(os.path.dirname(__file__), '.streamlit', 'secrets.toml')

with open(config_path, "rb") as f:
    config = tomllib.load(f)

api_key = config['OPENROUTER_API_KEY']
MODEL = "tngtech/deepseek-r1t2-chimera:free"
HEADERS = {
    "Authorization": f"Bearer {api_key}",
    "HTTP-Referer": "http://localhost:8501",
    "X-Title": "AI Chatbot Streamlit"
}
API_URL = "https://openrouter.ai/api/v1/chat/completions"

st.title("primaye")
st.markdown(f"Powered by {MODEL} via OpenRouter 🤖")

# ✅ Inisialisasi session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Tampilkan riwayat chat
for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

# Input pengguna
user_input = st.chat_input("Tulis pesan di sini...")
if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    with st.spinner("Mengetik..."):
        payload = {
            "model": MODEL,
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        }
        response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        bot_reply = response.json()['choices'][0]['message']['content']
    else:
        bot_reply = "⚠️ Maaf, gagal mengambil respons dari OpenRouter."

    st.chat_message("assistant").markdown(bot_reply)
    st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})
