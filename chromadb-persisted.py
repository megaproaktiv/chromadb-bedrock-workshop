import boto3
import json, re
from chromadb import EmbeddingFunction, Embeddings, Client
from bedrock.embedding import fetch_embedding, BedrockEmbeddingFunction
import chromadb
from chromadb.config import DEFAULT_TENANT, DEFAULT_DATABASE, Settings


chroma_client = chromadb.PersistentClient(
    path="db",
    settings=Settings(),
    tenant=DEFAULT_TENANT,
    database=DEFAULT_DATABASE,
)

collection = chroma_client.get_collection(
  name="neo_collection",
  embedding_function=BedrockEmbeddingFunction()
)

results = collection.query(
    query_texts=["Is my data secure"], # Chroma will embed this for you
    n_results=3 # how many results to return
)
print(results)

results = collection.query(
    query_texts=["How can I scale"], # Chroma will embed this for you
    n_results=3 # how many results to return
)
print(results)
