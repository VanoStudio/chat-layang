# primaye - Streamlit AI Chatbot

primaye is a simple chatbot web application built with [Streamlit](https://streamlit.io/) that connects to OpenRouter AI models. It allows users to chat with an AI assistant using their own OpenRouter API key.

---

## Features

- **Chat with AI**: Interact with various OpenRouter-supported models.
- **Session-based Chat History**: Keeps your conversation history during your session.
- **Model Selection**: Choose from multiple AI models.
- **API Key Input**: Securely use your own OpenRouter API key.
- **Clear Chat**: Easily reset your chat history.
- **Terms & Conditions Dialog**: Users must agree to terms before using the app.

---

## Requirements

- Python 3.8+
- [Streamlit](https://streamlit.io/)
- [requests](https://docs.python-requests.org/)

---

## Installation

1. **Clone this repository:**
    ```sh
    git clone https://github.com/yourusername/chat-layang.git
    cd chat-layang
    ```

2. **Install dependencies:**
    ```sh
    pip install streamlit requests
    ```

---

## Usage

1. **Run the app:**
    ```sh
    streamlit run chatbot.py
    ```

2. **Open your browser** to the provided local URL.

3. **Enter your OpenRouter API key** in the sidebar.

4. **Select an AI model**.

5. **Start chatting!**

---

## How It Works

- The app displays a Terms & Conditions dialog on first use.
- Users must enter an OpenRouter API key and select a model in the sidebar.
- Chat messages are sent to the OpenRouter API and responses are displayed in the main area.
- Chat history is stored in the session and can be cleared at any time.

---

## Configuration

- **Supported Models:**  
  - `tngtech/deepseek-r1t2-chimera:free`
  - `mistralai/devstral-small-2505:free`
- **API Endpoint:**  
  - `https://openrouter.ai/api/v1/chat/completions`

---

## Notes

- Your API key is not stored permanently and is only used for the current session.
- The app does not store any personal data.

---

## License

MIT License

---

## Credits

- Built with [Streamlit](https://streamlit.io/)
- Uses
