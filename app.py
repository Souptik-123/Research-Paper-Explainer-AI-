import streamlit as st

from core.loader import load_pdf
from core.splitter import split_text
from core.embeddings import get_embeddings
from core.vectorstore import create_vectorstore, get_retriever

from chains.qa_chain import build_qa_chain
from chains.explain_chain import explain_paper
from chains.diagram_chain import generate_diagram

st.set_page_config(page_title="Research Explainer AI")
st.title(" Research Paper Explainer AI")

# Session state
if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:
    with st.spinner("Processing..."):

        text = load_pdf(uploaded_file)
        docs = split_text(text)

        embeddings = get_embeddings()
        vectorstore = create_vectorstore(docs, embeddings)
        retriever = get_retriever(vectorstore)

        qa_chain = build_qa_chain(retriever)

        st.session_state.qa_chain = qa_chain

    st.success("Paper ready!")

if st.session_state.qa_chain:

    if st.button("📘 Explain Paper"):
        explanation = explain_paper(st.session_state.qa_chain)
        st.write(explanation)

    if st.button("📊 Generate Diagram"):
        diagram = generate_diagram(st.session_state.qa_chain)
        st.code(diagram, language="markdown")


st.subheader("💬 Ask Questions")

query = st.text_input("Ask something...")

if query and st.session_state.qa_chain:
    result = st.session_state.qa_chain({"question": query})
    answer = result["answer"]

    st.session_state.chat_history.append((query, answer))

for q, a in st.session_state.chat_history:
    st.markdown(f"**You:** {q}")
    st.markdown(f"**AI:** {a}")