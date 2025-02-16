# Plagiarism Checker and Chatbot Tool

## Overview
The **Plagiarism Checker and Chatbot Tool** is a web-based application built with **Streamlit** and powered by **Ollama's Gemma2:2b model**. It helps users analyze text for plagiarism by checking both **exact and semantic similarity**, ensuring originality in writing. Additionally, it features an AI chatbot that provides guidance on plagiarism detection and NLP-related topics.

## Features
### ✅ Text Similarity Analysis
- **Exact Similarity**: Uses `SequenceMatcher` to detect direct text matches.
- **Semantic Similarity**: Uses **SBERT (all-MiniLM-L6-v2)** to identify meaning-based similarities.

### ✅ Multi-format File Support
- Supports text extraction and analysis from **PDFs and Word (.docx) files**.

### ✅ Interactive Chatbot
- Offers insights on **plagiarism detection** and **NLP-related plagiarism topics**.
- Ensures **on-topic** responses and avoids unrelated discussions.

### ✅ User-Friendly Interface
- Styled with **custom CSS** for a modern, clean, and professional look.
- Uses **Streamlit components** for **file uploads, chat interactions, and similarity results**.

## Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/mohdazmi03/PlagiarismCheckerAI.git
```

### 2️⃣ Set Up a Virtual Environment (Optional but Recommended)
```bash
python -m venv env
source env/bin/activate  # On macOS/Linux
env\Scripts\activate    # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Install and Set Up Ollama
Make sure **Ollama** is installed and running. If not, install it from [Ollama's official site](https://ollama.ai) and download the **Gemma2:2b** model.
```bash
ollama pull gemma2:2b
```

### 5️⃣ Run the Application
```bash
streamlit run app.py
```

## Usage
1. **Upload a text file (PDF or DOCX)** or enter text manually.
2. **Run the plagiarism check** to see similarity scores.
3. **Chat with the AI** to learn more about plagiarism detection.

## Technologies Used
- **Python** (for backend processing)
- **Streamlit** (for the web interface)
- **Ollama (Gemma2:2b model)** (for chatbot responses)
- **SBERT (all-MiniLM-L6-v2)** (for semantic similarity analysis)
- **NLTK & SequenceMatcher** (for exact text matching)
- **PyMuPDF & python-docx** (for PDF & DOCX text extraction)

## Contributing
Feel free to submit pull requests or open issues for improvements! 🚀

## License
This project is licensed under the **MIT License**.

---
⭐ **Like this project? Give it a star on GitHub!** ⭐

