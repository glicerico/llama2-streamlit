# Streamlit Chatbot Interface.

Streamlit app to interact with a Llama-2 model from a huggingface inference endpoint.
The chat interface uses
LangChain's [memory with summary and buffer](https://python.langchain.com/docs/modules/memory/types/summary_buffer)

## Run it locally

```sh
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run Chatbot.py
```
