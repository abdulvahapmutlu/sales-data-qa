from chromadb.config import Settings
import chromadb

def initialize_chromadb():
    client = chromadb.Client(Settings(persist_directory="chroma_store"))
    print("ChromaDB client initialized.")
    return client

def create_collection(client, collection_name, embedding_function):
    try:
        collection = client.create_collection(name=collection_name, embedding_function=embedding_function)
        print(f"ChromaDB collection '{collection_name}' created.")
    except Exception as e:
        collection = client.get_collection(name=collection_name)
        print(f"ChromaDB collection '{collection_name}' retrieved.")
    return collection
