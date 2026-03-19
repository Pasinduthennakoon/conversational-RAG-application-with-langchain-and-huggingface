from langchain_classic.chains import create_history_aware_retriever
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.prompts import ChatPromptTemplate
from .retriever import retriever
from .model import llm

# Define the contextualize system prompt
contextualize_system_prompt = (
    "using chat history and latest user question, just reformulate question if needed and otherwise return it as is"
)

# Create the contextualize prompt template
contextualize_prompt = ChatPromptTemplate.from_messages(
    [
      ("system", contextualize_system_prompt),
      MessagesPlaceholder(variable_name="chat_history"),
      ("human", "{input}")
    ]
)

# Create the history aware-retriever
history_aware_retriever = create_history_aware_retriever(
    llm,
    retriever,
    contextualize_prompt
)