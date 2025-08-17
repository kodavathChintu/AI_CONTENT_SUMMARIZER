import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from transformers import pipeline

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Hugging Face fallback
hf_summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# 🎨 Custom CSS Styling
st.markdown("""
    <style>
    /* App background */
    .stApp {
        background: linear-gradient(135deg, #f0f8ff, #e6f7ff);
        font-family: 'Segoe UI', sans-serif;
    }

    /* Title styling */
    .title {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(90deg, #4facfe, #00f2fe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 20px;
    }

    /* Textarea styling */
    textarea {
        border-radius: 8px !important;
        border: 1px solid #ccc !important;
        padding: 12px !important;
        font-size: 1rem !important;
        background-color: #ffffffcc !important;
    }

    /* Button styling */
    .stButton>button {
        background: linear-gradient(90deg, #4facfe, #00f2fe);
        color: white;
        font-weight: bold;
        padding: 0.6rem 1.5rem;
        border: none;
        border-radius: 10px;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #00f2fe, #4facfe);
        transform: translateY(-3px);
    }

    /* Summary box */
    .summary-box {
        background: #ffffffcc;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #4facfe;
        margin-top: 20px;
        font-size: 1.1rem;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit UI
st.set_page_config(page_title="AI Content Summarizer", page_icon="📝")
st.markdown("<h1 class='title'>📝 AI Content Summarizer</h1>", unsafe_allow_html=True)
st.write("Paste your text below and get a clean summary in seconds.")

# Text input
user_input = st.text_area("✍️ Enter text here", height=300)

# Functions
def summarize_with_gemini(text):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"Summarize the following text in 3-4 sentences:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text.strip()

def summarize_with_huggingface(text):
    summary_list = hf_summarizer(text, max_length=130, min_length=40, do_sample=False)
    return summary_list[0]['summary_text']

def summarize_text(text):
    try:
        return summarize_with_gemini(text)
    except Exception as e:
        st.warning(f"⚠️ Gemini failed ({str(e)}). Using Hugging Face instead.")
        return summarize_with_huggingface(text)

# Button click
if st.button("✨ Generate Summary"):
    if user_input.strip():
        with st.spinner("Generating summary..."):
            summary = summarize_text(user_input)
        st.markdown(f"<div class='summary-box'>{summary}</div>", unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please enter some text to summarize.")
