from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

def create_retrieval_chain(llm, retriever):
    prompt_template = PromptTemplate(
        input_variables=["context", "question"],
        template="""
        You are an AI assistant with access to the following context:

        {context}

        Question:
        {question}

        Answer:
        """
    )
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs={"prompt": prompt_template}
    )
