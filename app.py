# Importing Required Libraries
import streamlit as st
from PIL import Image
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure genai API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Define a function to load gemini-1.5-flash model
model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    return response.text

# For Image Setup
def input_image_details(uploaded_file):
    if uploaded_file is not None:
        # Read the file into byte data
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get mime type of uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No File Uploaded")

# Streamlit Setup
st.set_page_config(page_title="MultiLanguage Invoice Extractor")
st.markdown("""
    <style>
    body {
        background-color: #2e3b4e;
        color: #f5f5f5;
    }
    .main-header {
        font-size: 3em;
        color: #ff6347;
        text-align: center;
    }
    .sub-header {
        font-size: 1.5em;
        color: #4682b4;
        text-align: center;
    }
    .h2-header {
        font-size: 2em;
        color: #4682b4;
    }
    .custom-input {
        width: 100%;
        padding: 10px;
        margin: 10px 0;
        box-sizing: border-box;
        border: 2px solid #ccc;
        border-radius: 4px;
    }
    .custom-button {
        background-color: #4CAF50;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 16px;
    }
    .response-box {
        background-color: #2e3b4e;
        border: 2px solid #4682b4;
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
        color: #f5f5f5;
    }
    </style>
""", unsafe_allow_html=True)

# Main Header
st.markdown('<h1 class="main-header">🧾 MultiLanguage Invoice Extractor 🌐</h1>', unsafe_allow_html=True)

# Input prompt header
st.markdown('<h2 class="h2-header">📝 Input Prompt:</h2>', unsafe_allow_html=True)
input_prompt = st.text_input("", key="input_prompt", help="Enter the details or question you want to ask about the invoice")

# File uploader header
st.markdown('<h2 class="h2-header">📂 Choose an Image of Invoice...</h2>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png", "jfif"], help="Upload the invoice image in jpg, jpeg, png, or jfif format")

# Display uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='📸 Uploaded Image.', use_column_width=True)

# Submit button
submit = st.button("🔍 Tell me about Invoice", help="Click to analyze the uploaded invoice image")

# Default prompt for the model
default_prompt = """
You are an expert in understanding invoices. You will be given an image of an invoice and a prompt.
You have to answer any question based on uploaded invoice image.
"""

# If submit button is clicked
if submit:
    if uploaded_file is not None:
        image_data = input_image_details(uploaded_file)
        response = get_gemini_response(default_prompt, image_data, input_prompt)
        
        # Display response
        st.markdown('<h2 class="sub-header">🔔 The Response is:</h2>', unsafe_allow_html=True)
        st.markdown(f'<div class="response-box"><p>{response}</p></div>', unsafe_allow_html=True)
    else:
        st.error("🚫 Please upload an invoice image.")
