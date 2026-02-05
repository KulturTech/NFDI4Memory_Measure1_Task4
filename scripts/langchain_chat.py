# Install: pip install langchain chromadb sentence-transformers

from langchain.document_loaders import JSONLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import Ollama

# 1. Load your dashboard data
def load_format_data():
    # Parse your HTML file's JSON
    pass

# 2. Create vector store
embeddings = HuggingFaceEmbeddings()
vectordb = Chroma.from_documents(docs, embeddings)

# 3. Query
def ask_question(question):
    docs = vectordb.similarity_search(question, k=3)
    # Feed to LLM with context
    return answer

# Test
print(ask_question("What format is best for archiving PDFs?"))