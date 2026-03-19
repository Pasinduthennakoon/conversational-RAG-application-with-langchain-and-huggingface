from langchain_core.prompts import PromptTemplate

template = """
Answer this question using the provided context only.if you don't know answer form the context, say you don't know. Don't try to make up an answer.

{question}

Context:
{context}

Answer:
"""

prompt = PromptTemplate.from_template(template)