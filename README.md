# Sales Data Question-Answering with GPT-J and ChromaDB

This project demonstrates a retrieval-augmented question-answering (QA) system for sales data stored in Excel files. The system combines ChromaDB for efficient document retrieval, HuggingFace embeddings for text encoding, and GPT-J-6B for natural language responses. This setup allows users to query sales data in plain English and receive accurate, context-aware answers.

---

## Features
- Load and preprocess Excel files for sales data analysis.
- Create a vector store using ChromaDB for fast document retrieval.
- Generate human-like responses with GPT-J-6B.
- Modular and scalable Python architecture.
- Example interactions to demonstrate capabilities.

---
## Getting Started

### 1. Clone the Repository
```
git clone https://github.com/abdulvahapmutlu/sales-data-qa.git
cd sales-data-qa
```

### 2. Install Dependencies
Ensure you have Python 3.8+ installed. Then, install the required libraries:
```
pip install -r requirements.txt
```

### 3. Add Your Sales Data
Place your Excel files in the `data/` directory.

---

## Usage

### Run the Application
Execute the following command to start the application:
```
python src/app.py
```

### Ask Questions
You can interact with the chatbot by asking questions about your sales data, such as:
- "What is the total sales in the sales data?"
- "Can you provide a breakdown of sales by region?"

---

## Components

### Data Preprocessing
- The `data_loader.py` script loads and preprocesses Excel files to create a unified text column for retrieval.

### ChromaDB Integration
- `chromadb_manager.py` manages the creation of vector stores and the addition of documents in batches.

### Language Model Initialization
- `model_initializer.py` initializes the GPT-J-6B model for generating responses.

### Retrieval QA
- `retrieval_qa.py` defines the question-answering chain using LangChain components.

### Main Application
- `app.py` orchestrates all components and provides a user-friendly interface.

---

## License

This project is licensed under the MIT License.

---

## Contributing

Feel free to submit pull requests or open issues for any suggestions or improvements.

---

## Acknowledgments
- ChromaDB: For vector storage.
- HuggingFace: For providing state-of-the-art language models.
- LangChain: For seamless integration of retrieval-augmented generation pipelines.
