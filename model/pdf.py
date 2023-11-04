import streamlit as st
from config import PALM_API_KEY
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.indexes import VectorstoreIndexCreator
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.chains import RetrievalQA
from langchain.vectorstores import chroma
from langchain.embeddings import GooglePalmEmbeddings
from langchain.llms import GooglePalm
import os , glob



st.header("Chat with PDF 💬")

files_path = "data.pdf"
loaders = [UnstructuredPDFLoader(files_path)]

# if "index" not in st.session:
index = VectorstoreIndexCreator(
    embedding=GooglePalmEmbeddings(google_api_key=PALM_API_KEY),
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=0),
).from_loaders(loaders)

llm = GooglePalm(temperature=0.1,google_api_key=PALM_API_KEY)
chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=index.vectorstore.as_retriever(),
    # input_key="question",
    return_source_documents=True,
)

# st.session.index = index

# Accept user questions/query
query = st.text_input("Ask questions about your PDF file:")
# st.write(query)
if query:
    response = chain(query)
    st.write(response["result"])
    with st.expander("Returned Chunks"):
        for doc in response["source_documents"]:
            st.write(f"{doc.metadata['source']} \n {doc.page_content}")
