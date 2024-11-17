from data_loader import load_excel_files
from chromadb_manager import initialize_chromadb, create_collection
from model_initializer import initialize_model
from retrieval_qa import create_retrieval_chain
from langchain import HuggingFacePipeline
from transformers import pipeline

if __name__ == "__main__":
    # Step 1: Load data
    data_directory = "data"
    df = load_excel_files(data_directory)

    # Step 2: Initialize ChromaDB
    client = initialize_chromadb()
    collection = create_collection(client, "sales_data", None)

    # Step 3: Add documents in batches (see earlier implementation for batching)

    # Step 4: Initialize GPT-J model
    model, tokenizer = initialize_model()
    generator = pipeline("text-generation", model=model, tokenizer=tokenizer, device=0)
    gpt_llm = HuggingFacePipeline(pipeline=generator)

    # Step 5: Create retrieval QA chain
    retriever = collection.as_retriever()
    qa = create_retrieval_chain(gpt_llm, retriever)

    # Step 6: Chat with the bot
    while True:
        user_query = input("Ask a question about the sales data: ")
        if user_query.lower() in ["exit", "quit"]:
            break
        response = qa({"query": user_query})
        print(f"Answer: {response.get('result', 'No answer found.')}")
