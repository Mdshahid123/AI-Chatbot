
import requests
import streamlit as st


# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="AI Personality Chatbot",
    page_icon="🤖",
    layout="centered",
)


# -----------------------------
# Initialize session state
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "theme" not in st.session_state:
    st.session_state.theme = "Light"


# -----------------------------
# Sidebar settings
# -----------------------------
with st.sidebar:
    st.title("🤖 Chat Settings")
    st.caption("Customize your chatbot experience.")

    theme = st.selectbox(
        "Appearance",
        options=["Light", "Dark"],
        index=0 if st.session_state.theme == "Light" else 1,
        key="theme_selector",
    )

    st.session_state.theme = theme

    personality = st.selectbox(
        "AI Personality",
        options=["Normal", "Funny", "Sad", "Angry"],
        index=0,
        key="personality_selector",
    )

    st.divider()

    st.write("**Selected personality**")
    st.info(f"{personality} AI")

    if st.button("🗑️ Clear conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# -----------------------------
# Theme colors
# -----------------------------
if st.session_state.theme == "Dark":
    colors = {
        "background": "#0e1117",
        "sidebar": "#161b26",
        "surface": "#1c2333",
        "input": "#20293a",
        "text": "#f1f5f9",
        "muted": "#b0bbcc",
        "border": "#354158",
        "accent": "#7c9cff",
        "user_message": "#263958",
        "assistant_message": "#1c2333",

        # Dropdown fixes
        "dropdown-bg": "#20293a",
        "dropdown-border": "#354158",
        "dropdown-text": "#f1f5f9",
        "dropdown-hover": "#354158",

        # Chat input container fixes
        "input-container-bg": "#161b26",
        "placeholder-color": "#b0bbcc",
    }

else:
    colors = {
        "background": "#f5f7fb",
        "sidebar": "#eaf0f8",
        "surface": "#ffffff",
        "input": "#ffffff",
        "text": "#172033",
        "muted": "#596579",
        "border": "#d9e1ec",
        "accent": "#315efb",
        "user_message": "#e8efff",
        "assistant_message": "#ffffff",

        # Dropdown fixes
        "dropdown-bg": "#ffffff",
        "dropdown-border": "#d9e1ec",
        "dropdown-text": "#172033",
        "dropdown-hover": "#e8efff",

        # Chat input container fixes
        "input-container-bg": "#f5f7fb",
        "placeholder-color": "#596579",
    }


# -----------------------------
# Custom CSS
# -----------------------------
st.markdown(
    f"""
    <style>
    /* Main application */
    .stApp {{
        background-color: {colors["background"]};
        color: {colors["text"]};
    }}

    [data-testid="stHeader"] {{
        background-color: {colors["background"]};
    }}

    [data-testid="stMain"] {{
        background-color: {colors["background"]};
    }}

    .block-container {{
        max-width: 850px;
        padding-top: 2rem;
        padding-bottom: 7rem;
    }}

    /* Text and headings */
    h1, h2, h3, h4, p, label,
    [data-testid="stMarkdownContainer"],
    [data-testid="stCaptionContainer"] {{
        color: {colors["text"]};
    }}

    [data-testid="stCaptionContainer"] {{
        color: {colors["muted"]};
    }}

    /* Sidebar */
    [data-testid="stSidebar"],
    [data-testid="stSidebar"] > div {{
        background-color: {colors["sidebar"]};
        color: {colors["text"]};
    }}

    [data-testid="stSidebar"] * {{
        color: {colors["text"]};
    }}

    /* Dropdown control */
    div[data-baseweb="select"] > div {{
        background-color: {colors["dropdown-bg"]} !important;
        border: 1px solid {colors["dropdown-border"]} !important;
        color: {colors["dropdown-text"]} !important;
    }}

    div[data-baseweb="select"] input {{
        color: {colors["dropdown-text"]} !important;
        -webkit-text-fill-color: {colors["dropdown-text"]} !important;
    }}

    div[data-baseweb="select"] svg {{
        fill: {colors["dropdown-text"]} !important;
        color: {colors["dropdown-text"]} !important;
    }}

    /* Open dropdown menu */
    div[data-baseweb="popover"],
    div[data-baseweb="popover"] > div,
    div[data-baseweb="menu"],
    ul[role="listbox"] {{
        background-color: {colors["dropdown-bg"]} !important;
        border-color: {colors["dropdown-border"]} !important;
        color: {colors["dropdown-text"]} !important;
    }}

    /* Dropdown options */
    li[role="option"],
    li[role="option"] div,
    li[role="option"] span {{
        background-color: {colors["dropdown-bg"]} !important;
        color: {colors["dropdown-text"]} !important;
    }}

    li[role="option"]:hover,
    li[role="option"][aria-selected="true"] {{
        background-color: {colors["dropdown-hover"]} !important;
        color: {colors["dropdown-text"]} !important;
    }}

    /* Streamlit BaseWeb option hover */
    [data-baseweb="menu"] [role="option"]:hover,
    [data-baseweb="menu"] [aria-selected="true"] {{
        background-color: {colors["dropdown-hover"]} !important;
        color: {colors["dropdown-text"]} !important;
    }}

    /* Chat message cards */
    [data-testid="stChatMessage"] {{
        background-color: {colors["assistant_message"]};
        border: 1px solid {colors["border"]};
        border-radius: 16px;
        padding: 14px;
        margin-bottom: 12px;
    }}

    [data-testid="stChatMessage"] p,
    [data-testid="stChatMessage"] li,
    [data-testid="stChatMessage"] span {{
        color: {colors["text"]};
    }}

    /* Entire bottom input area */
    [data-testid="stBottom"],
    [data-testid="stBottom"] > div,
    [data-testid="stBottom"] > div > div,
    [data-testid="stBottom"] [data-testid="stBottomBlockContainer"] {{
        background-color: {colors["background"]} !important;
    }}

    /* Chat input outer container */
    [data-testid="stChatInput"],
    [data-testid="stChatInput"] > div,
    [data-testid="stChatInput"] > div > div {{
        background-color: {colors["input-container-bg"]} !important;
        border-color: {colors["dropdown-border"]} !important;
    }}

    [data-testid="stChatInput"] > div {{
        border: 1px solid {colors["dropdown-border"]} !important;
        border-radius: 16px !important;
        box-shadow: none !important;
    }}

    /* Chat input text */
    [data-testid="stChatInput"] textarea {{
        background-color: {colors["input-container-bg"]} !important;
        color: {colors["dropdown-text"]} !important;
        -webkit-text-fill-color: {colors["dropdown-text"]} !important;
        caret-color: {colors["accent"]} !important;
        border: none !important;
        box-shadow: none !important;
    }}

    [data-testid="stChatInput"] textarea::placeholder {{
        color: {colors["placeholder-color"]} !important;
        -webkit-text-fill-color: {colors["placeholder-color"]} !important;
        opacity: 1 !important;
    }}

    [data-testid="stChatInput"] button {{
        background-color: transparent !important;
        color: {colors["accent"]} !important;
    }}

    /* Other inputs */
    input, textarea {{
        color: {colors["dropdown-text"]} !important;
        caret-color: {colors["accent"]} !important;
    }}

    /* Buttons */
    .stButton > button {{
        background-color: {colors["surface"]} !important;
        color: {colors["text"]} !important;
        border: 1px solid {colors["border"]} !important;
        border-radius: 10px;
        min-height: 42px;
        transition: border-color 0.2s ease;
    }}

    .stButton > button:hover {{
        border-color: {colors["accent"]} !important;
        color: {colors["accent"]} !important;
    }}

    /* Info messages */
    [data-testid="stAlert"] {{
        background-color: {colors["surface"]} !important;
        border: 1px solid {colors["border"]} !important;
        border-radius: 12px;
    }}

    [data-testid="stAlert"] p,
    [data-testid="stAlert"] svg {{
        color: {colors["text"]} !important;
    }}

    /* Dividers */
    hr {{
        border-color: {colors["border"]} !important;
    }}

    /* Scrollbar */
    * {{
        scrollbar-color: {colors["border"]} {colors["background"]};
    }}
    </style>
    """,
    unsafe_allow_html=True,
)


# -----------------------------
# Main interface
# -----------------------------
st.title("AI Personality Chatbot")

st.write(
    f"Chat with your own AI assistant. "
    f"Current personality: **{personality}**."
)

st.caption(
    f"{'🌙 Dark' if theme == 'Dark' else '☀️ Light'} Mode · "
    "Powered by Streamlit, FastAPI, LangChain and Ollama"
)


# -----------------------------
# Display chat history
# -----------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# -----------------------------
# Chat input and API request
# -----------------------------
prompt = st.chat_input("Type your message here...")

if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    request_data = {
        "mode": personality.lower(),
        "history": st.session_state.messages[:-1],
        "message": prompt,
    }

    with st.chat_message("assistant"):
        with st.spinner("AI is thinking..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/chat",
                    json=request_data,
                    timeout=180,
                )

                response.raise_for_status()
                answer = response.json()["reply"]

                st.markdown(answer)

                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )

            except requests.exceptions.ConnectionError:
                st.error(
                    "Cannot connect to the backend. "
                    "Please start your FastAPI server first."
                )

            except requests.exceptions.Timeout:
                st.error(
                    "The AI took too long to respond. Please try again."
                )

            except requests.exceptions.RequestException as exc:
                st.error(f"API request failed: {exc}")

            except (ValueError, KeyError):
                st.error("The backend returned an unexpected response.")
