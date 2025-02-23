# This does not require a frontend and runs on streamlit frontend itself
# This is a simple implementation of the conversational chain using the PDF files
# The user can upload the PDF files and ask questions from the PDF files
# The conversational chain will generate the response based on the context of the PDF files
# When vector store is generated, it will be saved as faiss_index in the current directory
# The conversational chain will load the vector store and generate the response based on the user question

import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_text_from_file(file):
    text = ""
    file_type = file.name.split(".")[-1].lower()
    if file_type == "pdf":
        pdf_reader = PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    elif file_type == "txt":
        text = str(file.read(), "utf-8")
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

def get_conversational_chain():
    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """
    model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.3)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)
    chain = get_conversational_chain()
    response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)
    return response["output_text"]

def main():
    st.set_page_config("PDFSage")

    # Custom CSS for the header
    st.markdown(
        """
        <style>
        .centered-header {
            text-align: center;
            color: orange;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<h1 class='centered-header'>PDFSage</h1>", unsafe_allow_html=True)
    st.subheader("Chat with your PDF and TXT documents using Gemini API and FAISS")

    pdf_docs = st.file_uploader("Upload your PDF or TXT Files", accept_multiple_files=True)
    if st.button("Submit & Process"):
        with st.spinner("Processing..."):
            raw_text = ""
            for file in pdf_docs:
                raw_text += get_text_from_file(file)
            text_chunks = get_text_chunks(raw_text)
            get_vector_store(text_chunks)
            st.success("Processing complete!")

    user_question = st.text_input("Ask a Question from the PDF Files", key="user_question")
    
    # Submit question on pressing Enter key
    if user_question:
        with st.spinner("Generating response..."):
            response = user_input(user_question)
            st.write("Reply: ", response)

if __name__ == "__main__":
    main()