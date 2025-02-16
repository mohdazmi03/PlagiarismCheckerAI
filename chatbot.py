import ollama
import streamlit as st

def generate_response(user_input):
    try:
        # Prepare the conversation history for the prompt
        conversation_history = "\n".join(
            [f"{msg['role'].capitalize()}: {msg['content']}" for msg in st.session_state.chat_history]
        )
        
        # Prepare the prompt with conversation history
        prompt = (
            "You are a friendly and helpful chatbot designed to assist users with questions about plagiarism and plagiarism checking in NLP. "
            "Your primary goal is to educate users about plagiarism and plagiarism checking in NLP in a simple and clear manner. "
            "If the user greets you or initiates small talk, respond warmly but quickly steer the conversation back to plagiarism and plagiarism checking in NLP. "
            "If the user's query is related to plagiarism and plagiarism checking in NLP, provide a response to educate them. "
            "If the query is not related to plagiarism and plagiarism checking in NLP, respond with the following exact phrase: "
            "'I'm sorry, I specialize in helping with plagiarism-related topics. Let me know if you have any questions about plagiarism and plagiarism checking in NLP!' "
            "Do not engage in off-topic discussions under any circumstances. "
            "Always maintain a friendly and supportive tone.\n\n"
            "Here is the conversation so far:\n"
            + conversation_history + "\n\n"
            f"User's latest question: {user_input}"
        )
        
        # Generate response with the guiding prompt
        response = ollama.generate(model="gemma2:2b", prompt=prompt)
        return response["response"]
    except Exception as e:
        return f"Error: {e}"
