import streamlit as st
from utils import (
    calculate_exact_similarity,
    calculate_semantic_similarity,
    extract_text_from_pdf,
    extract_text_from_word,
)
from chatbot import generate_response

# Page Configuration
st.set_page_config(page_title="Plagiarism & Chatbot", layout="wide")

# Load CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Initialize Session State
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "user_input_buffer" not in st.session_state:
    st.session_state.user_input_buffer = ""

# Functions
def submit_message():
    user_input = st.session_state.user_input_buffer
    if user_input.strip():
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        response = generate_response(user_input)
        st.session_state.chat_history.append({"role": "bot", "content": response})
        st.session_state.user_input_buffer = ""  # Clear the buffer

def extract_text(uploaded_file):
    if uploaded_file:
        if uploaded_file.name.endswith(".pdf"):
            return extract_text_from_pdf(uploaded_file)
        elif uploaded_file.name.endswith(".docx"):
            return extract_text_from_word(uploaded_file)
    return ""

# Layout and Interaction
st.markdown("<h1 class='main-title'>Plagiarism Checker Tool</h1>", unsafe_allow_html=True)

# Introduction Section
st.markdown(
    """
    <div class="intro-section">
        <p class="intro-text">
            Plagiarism refers to the act of presenting someone else's work, ideas, or words as your own without proper acknowledgment. 
            This tool helps in identifying both exact and semantic similarities between texts to ensure originality.
            <br><br>
            <strong>Exact Similarity:</strong> This refers to the direct match of words or phrases between two texts. If two texts are identical or nearly identical, they would have a high exact similarity score.
            <br><br>
            <strong>Semantic Similarity:</strong> Unlike exact similarity, semantic similarity measures how closely the meanings of the texts match. It doesn’t rely on exact wording but instead compares the underlying concepts and ideas. This is particularly useful for detecting paraphrasing or rewording, where the meaning remains the same, but the phrasing is different. Our tool uses advanced models to calculate the semantic similarity to help detect even subtle instances of plagiarism.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Main Layout
col1, col2 = st.columns(2)

with col1:
    uploaded_file1 = st.file_uploader("Upload First File (PDF or Word)", type=["pdf", "docx"], key="file1")
    text1 = extract_text(uploaded_file1)

with col2:
    uploaded_file2 = st.file_uploader("Upload Second File (PDF or Word)", type=["pdf", "docx"], key="file2")
    text2 = extract_text(uploaded_file2)

if st.button("Check Similarity"):
    if text1.strip() and text2.strip():
        exact_similarity = calculate_exact_similarity(text1, text2)
        semantic_similarity = calculate_semantic_similarity(text1, text2)
        
        # Set similarity display class
        if exact_similarity >= 75 or semantic_similarity >= 75:
            similarity_class = "similarity-high"
        else:
            similarity_class = "similarity-low"
        
        st.markdown(
            f"<div class='{similarity_class}'>Exact Similarity: {exact_similarity:.2f}%</div>", 
            unsafe_allow_html=True
        )
        st.markdown(
            f"<div class='{similarity_class}'>Semantic Similarity: {semantic_similarity:.2f}%</div>", 
            unsafe_allow_html=True
        )
    else:
        st.warning("Please provide text in both fields.")


# Sidebar: Chatbot
with st.sidebar:
    st.markdown("### Chatbot 💬")

    for message in st.session_state.chat_history:
        role_class = "chat-message-user" if message["role"] == "user" else "chat-message-bot"
        st.markdown(
            f"<div class='{role_class}'><strong>{message['role'].capitalize()}:</strong> {message['content']}</div>",
            unsafe_allow_html=True,
        )

    if st.button("Clear Chat"):
        st.session_state.chat_history = []

    st.text_input(
        "Type your message and press Enter",
        key="user_input_buffer",
        on_change=submit_message,
        placeholder="Ask the chatbot...",
    )