from langchain_core.runnables import RunnablePassthrough
from langchain_classic.chains import create_history_aware_retriever
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains import create_retrieval_chain
from .retriever import retriever
from .prompts import prompt
from .model import llm
from .output import output_parser
from .history_aware_retriever import history_aware_retriever

system_prompt = (
    "You are an intelligent chatbot.Use the following context to answer the questions. If you don't know the answer, just say that you don't know, don't try to make up an answer."
    "\n\n"
    "{context}"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}")
    ]
)

qa_chain = create_stuff_documents_chain(
    llm,
    prompt
) | output_parser

rag_chain = create_retrieval_chain(
    history_aware_retriever,
    qa_chain
)