import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API Key Securely
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # Fetch from environment
genai.configure(api_key=GEMINI_API_KEY, api_version="v1")  # Use the correct API version

# Function to call Gemini API
def generate_response(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.0-pro")  # Use the correct model name
        response = model.generate_content(prompt)
        if hasattr(response, "text"):
            return response.text.strip()
        else:
            return "Error: No valid response from Gemini API."
    except Exception as e:
        return f"Error: {e}"

# Truncate text to fit API limits
MAX_LENGTH = 4000  # Adjust based on model limits

def truncate_text(text, max_length=MAX_LENGTH):
    return text[:max_length] if len(text) > max_length else text

# Streamlit UI
st.title("📜 Legal Document Analyzer")
uploaded_file = st.file_uploader("Upload a .txt file", type="txt")

if uploaded_file:
    text = uploaded_file.read().decode("utf-8")
    truncated_text = truncate_text(text)

    st.subheader("Original Text (First 500 chars)")
    st.write(text[:500] + "..." if len(text) > 500 else text)

    # Choose functionality
    option = st.radio("Choose an action:", [
        "Summarize", "Extract Key Points", "Simplify Legal Terms",
        "Generate FAQs", "Translate Summary", "List Important People/Parties & Places"
    ])

    # Execute based on user choice
    if st.button("Generate Result"):
        if option == "Summarize":
            prompt = f"Summarize the following legal text in simple terms:\n\n{truncated_text}"
        elif option == "Extract Key Points":
            prompt = f"List the key points from the following legal document:\n\n{truncated_text}"
        elif option == "Simplify Legal Terms":
            prompt = f"Convert the following legal document into plain language:\n\n{truncated_text}"
        elif option == "Generate FAQs":
            prompt = f"Generate common FAQs based on the following legal document:\n\n{truncated_text}"
        elif option == "Translate Summary":
            prompt = f"Translate the following summary into Hindi and French:\n\n{truncated_text}"
        elif option == "List Important People/Parties & Places":
            prompt = f"Extract names of involved parties, people, and places mentioned in this legal document:\n\n{truncated_text}"

        # Get result from API
        result = generate_response(prompt)
        st.subheader(f"Result: {option}")
        st.write(result)