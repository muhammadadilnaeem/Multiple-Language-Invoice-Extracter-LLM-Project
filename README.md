

---

# **🧾 MultiLanguage Invoice Extractor 🌐**

Welcome to the **MultiLanguage Invoice Extractor** project! This Streamlit application utilizes advanced language models to analyze invoice images and answer questions about their content.

## **🚀 Overview**

This application is designed to extract information from uploaded invoice images and provide detailed responses based on user prompts. It leverages the **Google Gemini-1.5-flash** model for generating content and analyzing the invoice data.

https://github.com/user-attachments/assets/6df3fbf4-49cd-4ebb-9816-da6d7bdafb05

## **📦 Requirements**

- **Streamlit**: For creating the web interface
- **Pillow (PIL)**: For handling image files
- **Google Generative AI**: For using the Gemini-1.5-flash model
- **python-dotenv**: For loading environment variables

You can install the required libraries using the following command:

```bash
pip install -r requirements.txt
```

## **📁 Installation**

1. Clone the repository:

    ```bash
    git clone https://github.com/muhammadadilnaeem/Multiple-Language-Invoice-Extracter-LLM-Project.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Multiple-Language-Invoice-Extracter-LLM-Project
    ```

3. Create a `.env` file in the project root directory and add your Google API key:

    ```plaintext
    GOOGLE_API_KEY=your_google_api_key_here
    ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

## **🖼️ Features**

- **Upload Invoice Image**: Supports jpg, jpeg, png, and jfif formats.
- **Input Prompt**: Enter a question or details about the invoice.
- **Generate Response**: Click the button to analyze the invoice and get the response.

## **📸 How to Use**

1. **Upload an Invoice Image**: Click the "Choose an Image of Invoice" button to upload your invoice image.
2. **Enter a Prompt**: Provide any details or questions you have regarding the invoice in the input field.
3. **Analyze the Invoice**: Click "Tell me about Invoice" to get a detailed response based on the invoice content.


## **🛠️ Error Handling**

The application will notify you if no invoice image is uploaded when you try to submit the form.

## **🎨 Customization**

The app features a custom style including colors and layout, optimized for both light and dark themes.

---
