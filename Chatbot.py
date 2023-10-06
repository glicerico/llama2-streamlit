"""
Streamlit Chatbot Interface.

This module provides a Streamlit interface for interacting with an LLM model.
"""

import streamlit as st
import toml

from llm_api import reset_memory, continue_conversation, num_tokens_from_string, MAX_SYS_TOKENS

# Load secrets from toml file
DEFAULT_SYS_MESS = st.secrets.get("system", {}).get("message", "You are a helpful, respectful and honest assistant")

# Reset the LLM memory
reset_memory()

st.title("💬 Chatbot")
st.caption("🚀 A streamlit chatbot powered by Llama-2 derived models")

# Sidebar for system message and temperature input
system_message = st.sidebar.text_area("System Message:", value=DEFAULT_SYS_MESS)
tokens = num_tokens_from_string(system_message, encoding_name='cl100k_base')
st.sidebar.markdown(f"**Tokens used:** {tokens}/{MAX_SYS_TOKENS}")
if tokens > MAX_SYS_TOKENS:
    st.warning(f"Exceeded max token limit! You have {tokens} tokens, but the limit is {MAX_SYS_TOKENS}.")
temperature = st.sidebar.number_input("Model Temperature:", min_value=0.0, max_value=2.0, value=0.7, step=0.1)

# Reset conversation button
if st.sidebar.button("Reset Conversation"):
    st.session_state.clear()
    st.experimental_rerun()
    reset_memory()  # Reset the LLM memory
    st.success("Conversation reset successfully!")

# Initialize or retrieve message history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display message history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Get user input and continue conversation
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    response = continue_conversation(st.session_state.messages, system_message=system_message, max_new_tokens=256,
                                     temperature=temperature)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)
