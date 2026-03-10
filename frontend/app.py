import streamlit as st
import requests

st.title("PDF_RAG_Project")
st.subheader("Welcome!!")

# Uploading PDF 
st.write("Upload a PDF and ask questions about it.")
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None:  
    files = {
        "file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")
    }
    response = requests.post(
        "http://127.0.0.1:8000/upload",
        files=files
    )

# Sending Question
question = st.text_input("Ask Something?")

if st.button("Ask"):
    with st.spinner("Thinking..."):
        response = requests.post(
            "http://127.0.0.1:8000/ask",
            json={"question": question}
            )
        answer = response.json()["answer"]
        st.success("Answer Generated Successfully.")
        st.write(answer) 