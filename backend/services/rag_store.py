import os
from typing import List
import chromadb
from chromadb.utils import embedding_functions
from app_settings import settings

COLLECTION_NAME = "stockbase"

class RAGStore:
    def __init__(self):
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection(COLLECTION_NAME)
        self.embedder = embedding_functions.GoogleGenerativeAiEmbeddingFunction(api_key=settings.GEMINI_API_KEY)

    def ingest(self, paths: List[str]):
        for path in paths:
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
            # Simple chunking
            chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
            for idx, chunk in enumerate(chunks):
                doc_id = f"{os.path.basename(path)}_{idx}"
                embedding = self.embedder([chunk])
                self.collection.add(documents=[chunk], embeddings=embedding, ids=[doc_id])

    def query(self, q: str, k=5):
        results = self.collection.query(query_texts=[q], n_results=k)
        return results

rag_store = RAGStore()
