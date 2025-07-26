import streamlit as st
import requests
import tomllib
import os

if "agreed" not in st.session_state:
    st.session_state.agreed = False
@st.dialog("Terms and Conditions")
def show_terms():
    st.write("""
    **Syarat & Ketentuan:**
    1. Data akan digunakan untuk pengembangan aplikasi.
    2. Aplikasi tidak menyimpan data pribadi secara permanen.
    3. Dengan melanjutkan, kamu setuju mengikuti aturan yang berlaku.
    """)

    if st.button("✅ Saya Setuju"):
        st.session_state.agreed = True
        st.rerun()

if not st.session_state.agreed:
    show_terms()

with st.sidebar:
    MODEL = ["tngtech/deepseek-r1t2-chimera:free", "mistralai/devstral-small-2505:free", ]
    api = st.text_input("Masukkan API OpenRouter","")
    modelai = st.selectbox(
        "Kamu ingin menggunakan model apa ?",MODEL
    )


HEADERS = {
    "Authorization": f"Bearer {api}",
    "HTTP-Referer": "http://localhost:8501",
    "X-Title": "AI Chatbot Streamlit"
}
API_URL = "https://openrouter.ai/api/v1/chat/completions"

st.title("primaye")
st.markdown(f"Powered by {modelai} via OpenRouter 🤖")

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
            "model": modelai,
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        }
        response = requests.post(API_URL, headers=HEADERS, json=payload)


    if response.status_code == 200:
        bot_reply = response.json()['choices'][0]['message']['content']
    elif api == "":
        bot_reply ="‼️ Tolong Masukkan API OpenRouter nya !"
    else:
        bot_reply = "⚠️ Maaf, gagal mengambil respons dari OpenRouter."

    st.chat_message("assistant").markdown(bot_reply)
    st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})
