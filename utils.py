from difflib import SequenceMatcher
from PyPDF2 import PdfReader # type: ignore
import docx
from sentence_transformers import SentenceTransformer, util

# Load SBERT model
model = SentenceTransformer('all-MiniLM-L6-v2')

def calculate_exact_similarity(text1, text2):
    """Calculate exact text similarity using SequenceMatcher."""
    similarity = SequenceMatcher(None, text1, text2).ratio()
    return similarity * 100

def calculate_semantic_similarity(text1, text2):
    """Calculate semantic similarity using Sentence-BERT."""
    embeddings1 = model.encode(text1, convert_to_tensor=True)
    embeddings2 = model.encode(text2, convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(embeddings1, embeddings2).item()
    return similarity * 100

def extract_text_from_pdf(uploaded_file):
    """Extract text from a PDF file."""
    pdf_reader = PdfReader(uploaded_file)
    return "".join(page.extract_text() for page in pdf_reader.pages)

def extract_text_from_word(uploaded_file):
    """Extract text from a Word file."""
    doc = docx.Document(uploaded_file)
    return "\n".join(paragraph.text for paragraph in doc.paragraphs)