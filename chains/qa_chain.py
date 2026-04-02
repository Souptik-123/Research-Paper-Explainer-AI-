from langchain_openai import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from config import OPENAI_MODEL, TEMPERATURE
from dotenv import load_dotenv

load_dotenv()
def build_qa_chain(retriever):
    llm = ChatOpenAI(
        model=OPENAI_MODEL,
        temperature=TEMPERATURE
    )

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory
    )