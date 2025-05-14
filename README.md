# 🔍 Tiktokenizer

A simple and elegant Streamlit web app to visualize how OpenAI models tokenize your input using [tiktoken](https://github.com/openai/tiktoken). See your text broken into tokens with color-coded highlights, token IDs, and live updates as you type.

---

## ✨ Features

- 🔤 **Live Tokenization** – See tokenized text as you type
- 🎨 **Color-Coded Token Highlights** – Each token rendered in a separate block
- 🔢 **Token Count & IDs** – Total tokens and token ID list
- 🧠 **Supports Multiple Models** – Works with `gpt-4o`, `gpt-4`, `gpt-3.5-turbo`, and embedding models
- 🔍 **Whitespace Visualization** – Toggle to make spaces/newlines visible
- ⚡ **Fast and lightweight** – Built with Python, Streamlit, and tiktoken

---

## 🚀 Getting Started

### 1. Clone this repo

```bash
git clone https://github.com/iamkamleshrangi/tiktokenizer_streamlit_app
cd tiktokenizer
```

### 2. Install dependencies
You can install them via pip:
```bash
pip install -r requirements.txt
```
Or, manually:
```bash 
pip install streamlit tiktoken

```

### 3. Run the app
``` bash
streamlit run app.py
```
Then visit http://localhost:8501 in your browser.

# 🧠 Supported Models
This app supports the following OpenAI models via the `tiktoken` tokenizer library:
---

### 🔮 GPT Series

- `gpt-4o`
- `gpt-4o-mini`
- `gpt-4-turbo`
- `gpt-4`
- `gpt-3.5-turbo`

These models are commonly used for natural language processing, chatbots, and reasoning tasks.

---

### 🧬 Embedding Models

- `text-embedding-ada-002`
- `text-embedding-3-small`
- `text-embedding-3-large`

These models are optimized for generating vector embeddings for text similarity, clustering, and semantic search.

---

### 📌 Notes
- Tokenizer behavior may vary slightly between models.
- All models are compatible with the `tiktoken.encoding_for_model()` API.
- Some models (like embeddings) may produce more fine-grained tokenization.
