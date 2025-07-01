from langchain.chat_models import ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA

llm = ChatOpenAI(model="gpt-4")
embeddings = OpenAIEmbeddings()
vectordb = Chroma(persist_directory="marketing_docs", embedding_function=embeddings)
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectordb.as_retriever())

def vector_search(state):
    result = qa_chain.run(state["user_query"])
    state["retrieval_result"] = result
    return state
