import streamlit as st
import tiktoken
import html

class GetTiktoken:
    def __init__(self):
        self.model_list = [
            'gpt-4o', 'gpt-4o-mini', 'gpt-4-turbo', 'gpt-4', 'gpt-3.5-turbo',
            'text-embedding-ada-002', 'text-embedding-3-small',
            'text-embedding-3-large'
        ]

    def encode_for_model(self, model, input_text):
        enc = tiktoken.encoding_for_model(model)
        return enc.encode(input_text), enc

# UI Setup
st.set_page_config(page_title="Tiktokenizer", layout="wide")
gt = GetTiktoken()

# Title
st.markdown("<h1 style='font-size: 2.2rem;'>Tiktokenizer</h1>", unsafe_allow_html=True)
col_input, col_output = st.columns([1, 1.2])

with col_input:
    input_text = st.text_area(" ", value="hello world .", height=300, label_visibility="collapsed")

    with st.expander("⚙️ Settings", expanded=True):
        selected_model = st.selectbox("Model", gt.model_list, index=0)
        show_whitespace = st.checkbox("Show whitespace", value=False)

with col_output:
    if input_text.strip():
        tokens, encoder = gt.encode_for_model(selected_model, input_text)
        decoded_tokens = [encoder.decode([tok]) for tok in tokens]

        # Token count
        st.html(f"""<div style='padding:10px 16px;background:#f8f9fa;border-radius:8px;margin-bottom:10px'><b>Token
        count</b><br><span style='font-size:1.4rem'>{len(tokens)}</span></div>""")#, unsafe_allow_html=True)

        # Token display block
        st.markdown("<b>Token Highlight</b>", unsafe_allow_html=True)
        token_html = ""
        color_palette = ["#d0ebff", "#ffe066", "#ffd6d6", "#d3f9d8", "#f1f3f5", "#e9ecef"]

        for i, txt in enumerate(decoded_tokens):
            if show_whitespace:
                txt = txt.replace(" ", "␣").replace("\n", "⏎\n")

            safe_text = html.escape(txt)  # 🔐 sanitize for HTML rendering
            color = color_palette[i % len(color_palette)]

            token_html += f"""
                <span style='background-color: {color}; padding: 4px 6px; margin: 2px;
                border-radius: 6px; font-family: monospace; font-size: 1rem; display: inline-block;'>{safe_text}</span>
            """
        st.html(f"<div style='background:#f8f9fa;padding:10px;border-radius:8px;'>{token_html}</div>")#, unsafe_allow_html=True)

        # Raw token IDs
        st.markdown("<b>Token IDs</b>", unsafe_allow_html=True)
        token_id_str = ", ".join(map(str, tokens))
        #st.markdown(token_id_str)
        st.html(f"<div style='background:#f8f9fa;padding:10px;border-radius:8px;'>{token_id_str}</div>")#, unsafe_allow_html=True)
    else:
        st.info("Start typing to tokenize...")

