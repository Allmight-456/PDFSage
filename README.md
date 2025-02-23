# PDFSage

PDFSage is a web application that allows users to upload PDF and TXT files and ask questions about the content. The application uses Google Generative AI and FAISS for vector search and question answering.

## Features

- Upload PDF and TXT files
- Process and extract text from uploaded files
- Generate vector embeddings using Google Generative AI
- Perform similarity search using FAISS
- Answer questions based on the content of the uploaded files

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Backend Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Allmight-456/PDFSage.git
cd pdfsage/backend

```
### 2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup an .env file in backend directory 
```bash
GEMINI_API_KEY= "your_gemini_api_key"
GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-file.json"
```
Replace your_gemini_api_key, your_openai_api_key, and /path/to/your/service-account-file.json with your actual API keys and the path to your Google service account JSON file.

### 5. Run the Application
```bash
streamlit run app.py
```
This will start the Streamlit server and open the application in your default web browser.

## Frontend Setup
The frontend folder is not integrated with the backend. However, the backend can function as a standalone application with its own frontend using Streamlit.

```bash
cd ../frontend
npm install
npm run dev
```

### Notes 
The backend uses Google Generative AI and FAISS for processing and answering questions.
Ensure that your environment variables are set correctly to avoid authentication issues.
The backend can function independently with its own frontend using Streamlit.


