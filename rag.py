import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

DB_PATH = "my_faiss_index"  

AUTOSTREAM_KNOWLEDGE = [
    "AutoStream Basic Plan costs $29/month. It includes 10 videos/month and 720p resolution.",
    "AutoStream Pro Plan costs $79/month. It includes Unlimited videos, 4K resolution, and AI captions.",
    "AutoStream Refund Policy: No refunds are available after 7 days.",
    "AutoStream Support Policy: 24/7 support is available ONLY on the Pro plan."
]

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

def get_vector_store():
    if os.path.exists(DB_PATH):
        return FAISS.load_local(DB_PATH, embeddings, allow_dangerous_deserialization=True)
    
    documents = [Document(page_content=text) for text in AUTOSTREAM_KNOWLEDGE]
    vector_store = FAISS.from_documents(documents, embeddings)
    
    vector_store.save_local(DB_PATH)
    return vector_store

vector_store = get_vector_store()

def retrieve_info(query: str) -> str:
    results = vector_store.similarity_search(query, k=2)
    return "\n\n".join([doc.page_content for doc in results])

# Test
if __name__ == "__main__":
    print(retrieve_info("price of pro plan"))