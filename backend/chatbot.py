# Streamlit chat interface.

from langchain.chat_models import init_chat_model
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage,
)

# Initialize the LLM
model = init_chat_model(
    model="ollama:gemma4:cloud",
    temperature=0.3,
)

# Define AI personalities
AI_MODES = {
    "funny": "You are a funny AI agent. Be humorous and playful.",

    "sad": "You are a sad AI agent. Speak gently and use a melancholy tone.",

    "angry": "You are a grumpy and angry AI agent. Be expressive and sarcastic, but not abusive.",

    "normal": "You are a helpful AI assistant. Answer naturally and clearly.",
}


def generate_response(mode, history, prompt):

    # Select the system prompt
    system_prompt = AI_MODES.get(
        mode,
        AI_MODES["normal"]
    )

    # Start the conversation with the selected personality
    messages = [
        SystemMessage(content=system_prompt)
    ]

    # Add previous conversation messages
    for item in history:

        if item["role"] == "user":
            messages.append(
                HumanMessage(content=item["content"])
            )

        elif item["role"] == "assistant":
            messages.append(
                AIMessage(content=item["content"])
            )

    # Add the latest user message
    messages.append(
        HumanMessage(content=prompt)
    )

    # Call the LLM
    response = model.invoke(messages)

    # Return only the generated text
    return response.content
