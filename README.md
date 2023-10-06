# Streamlit Chatbot Interface.

Streamlit app to interact with a Llama-2 model from a huggingface inference endpoint.
The chat interface uses
LangChain's [memory with summary and buffer](https://python.langchain.com/docs/modules/memory/types/summary_buffer)

## Run it locally

You need to add your secrets to a `secrets.toml` file in the root of the project.
The file should look like this:

```toml
[huggingface]
api_token = <your HF token>
bearer = <your HF inference endpoint token>
endpoint_url = <URL of your HF inference endpoint>

[system]
message = """Your system prompt"""
```

Then run the app with:

```sh
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run Chatbot.py
```
