# 🤖 AI Personality Chatbot

An interactive AI chatbot built with **Python, Streamlit, FastAPI, LangChain, and Ollama**. Choose an AI personality and enjoy conversations with a Funny, Sad, Angry, or Normal AI assistant through a modern web interface with Light and Dark modes.

## ✨ Features

- **Multiple AI Personalities:** Choose between Funny, Sad, Angry, and Normal AI.
- **Interactive Chat Interface:** Chat with the AI through a Streamlit web application.
- **Conversation History:** Maintains the conversation context so the AI can respond based on previous messages.
- **Light and Dark Modes:** Switch between themes for a comfortable viewing experience.
- **REST API:** FastAPI backend handles chat requests and communicates with the language model.
- **LLM Integration:** Uses LangChain and Ollama to generate AI responses.
- **Clear Conversation:** Reset the current chat history whenever needed.
- **Separate Frontend and Backend:** Independent frontend and backend applications make the project easier to maintain and extend.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Frontend and chat interface |
| FastAPI | Backend REST API |
| LangChain | Language model integration and message management |
| Ollama | Language model access |
| Pydantic | API request validation |
| Requests | HTTP communication between frontend and backend |
| uv | Python dependency and project management |

## 🏗️ Project Architecture

```text
AI Personality Chatbot
│
├── frontend/
│   ├── app.py
│   ├── requirements.txt
│   ├── pyproject.toml
│   └── uv.lock
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── pyproject.toml
│   └── uv.lock
│
├── .gitignore
└── README.md
```

### How It Works

1. The user selects an AI personality in the Streamlit interface.
2. The user enters a message.
3. The frontend sends an HTTP POST request to the FastAPI `/chat` endpoint.
4. The backend selects the corresponding personality prompt.
5. LangChain passes the conversation messages to the configured language model.
6. The model generates a response.
7. FastAPI returns the response as JSON.
8. Streamlit displays the response in the chat interface.

```text
User
  |
  v
Streamlit Frontend
  |
  | POST /chat
  v
FastAPI Backend
  |
  v
LangChain
  |
  v
Ollama Language Model
  |
  v
AI Response
  |
  v
Streamlit Chat Interface
```

## 🚀 Getting Started

Follow these steps to run the project locally.

### Prerequisites

Install the following:

- Python
- [uv](https://docs.astral.sh/uv/)
- [Ollama](https://ollama.com/) or access to a supported hosted Ollama model
- Git (optional, for version control)

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-personality-chatbot.git
cd ai-personality-chatbot
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Set Up the Backend

Open a terminal and navigate to the backend directory:

```bash
cd backend
uv sync
```

If you are setting up the dependencies for the first time and have not created the project configuration yet, install the required packages:

```bash
uv add fastapi "uvicorn[standard]" langchain langchain-ollama
```

If using the hosted Ollama API through the OpenAI-compatible integration, install:

```bash
uv add langchain-openai
```

### 3. Configure the Language Model

For local Ollama usage, ensure Ollama is running and the configured model is available.

The backend uses this model configuration by default:

```python
model = init_chat_model(
    model="ollama:gemma4:cloud",
    temperature=0.3,
)
```

If using Ollama Cloud, configure your API key through an environment variable. Never commit API keys or other secrets to GitHub.

### 4. Start the Backend

From the `backend` directory, run:

```bash
uv run python main.py
```

The API should be available at:

- API root: `http://127.0.0.1:8000/`
- Interactive API documentation: `http://127.0.0.1:8000/docs`

### 5. Set Up the Frontend

Open a second terminal and navigate to the frontend directory:

```bash
cd frontend
uv sync
```

If dependencies have not been added yet, install them:

```bash
uv add streamlit requests
```

### 6. Start the Frontend

Run:

```bash
uv run streamlit run app.py
```

Streamlit will display the local URL in the terminal, usually:

`http://localhost:8501`

Open the URL in your browser to start chatting.

## 🔌 API Documentation

### Chat Endpoint

**Endpoint:** `POST /chat`

**Local URL:** `http://127.0.0.1:8000/chat`

#### Request Body

```json
{
  "mode": "funny",
  "history": [],
  "message": "Tell me a joke"
}
```

#### Supported Personality Modes

| Mode | Description |
|---|---|
| `normal` | Helpful and natural responses |
| `funny` | Humorous and playful responses |
| `sad` | Gentle and melancholy responses |
| `angry` | Grumpy and sarcastic responses without abusive language |

#### Example Response

```json
{
  "reply": "Why did the programmer quit his job? Because he didn't get arrays!"
}
```

The actual response depends on the selected model and its generated output.

### Root Endpoint

**Endpoint:** `GET /`

Returns a message confirming that the API is running.

## ☁️ Deployment

The frontend and backend can be deployed independently.

### Frontend — Streamlit Community Cloud

Deploy `frontend/app.py` using [Streamlit Community Cloud](https://share.streamlit.io/).

Configure the following secret with your deployed backend URL:

```toml
BACKEND_URL = "https://your-backend.onrender.com"
```

The frontend must read this value and use it as the base URL for its API requests.

### Backend — Render

Deploy the `backend` directory as a Python web service using [Render](https://render.com/).

**Build command:**

```bash
pip install -r requirements.txt
```

**Start command:**

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

Configure required environment variables, including any API key needed by your selected language model.

> Note: Update the example deployment URLs with your actual service URLs. Deployment also depends on the availability and configuration of the selected model.

## 🔐 Security Notes

- Never hardcode API keys, passwords, or other secrets in source code.
- Store deployment secrets in your hosting provider's environment-variable or secrets settings.
- Do not commit `.env` files or credentials to GitHub.
- Configure appropriate request validation and API access controls before exposing the backend publicly.

## 🔮 Future Improvements

- Streaming AI responses.
- User authentication and individual chat histories.
- Additional AI personalities and customizable system prompts.
- Persistent conversation storage.
- Improved responsive design and accessibility.
- More detailed error handling and API monitoring.

## 👨‍💻 Author

**Mohammad Shahid**

Aspiring Software Developer | Python | FastAPI | LangChain | Generative AI

- GitHub: [Your GitHub Profile](https://github.com/YOUR_USERNAME)
- Live Demo: Add your deployed Streamlit URL here.

---

*Built as a hands-on project to explore LLM integration, REST API development, and AI-powered web applications.*