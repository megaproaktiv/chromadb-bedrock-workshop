import boto3
import json, re
from chromadb import Documents, EmbeddingFunction, Embeddings, Client
from titan.embedding import fetch_embedding
import chromadb
from chromadb.config import DEFAULT_TENANT, DEFAULT_DATABASE, Settings

# See https://cookbook.chromadb.dev/embeddings/bring-your-own-embeddings/#example-implementation
# https://github.com/neo-con/chromadb-tutorial/blob/main/7.%20Using%20Embedding%20Functions/2.%20Custom%20Embedding%20Functions/custom_emb_func.py
# https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-titan-embed-text.html
class BedrockEmbeddingFunction(EmbeddingFunction):
  def __init__(self):
    self.model = "amazon.titan-embed-text-v1"

  def __call__(self, input: Documents) -> Embeddings:
        """Embed the input documents."""
        return  fetch_embedding(input, self.model)

chroma_client = chromadb.PersistentClient(
    path="db",
    settings=Settings(),
    tenant=DEFAULT_TENANT,
    database=DEFAULT_DATABASE,
)
# Delete all collections
# Remove this line if you want to keep your collections

collection = chroma_client.create_collection(
  name="neo_collection",
  # embedding_function=BedrockEmbeddingFunction(model_name="amazon.titan-embed-text-v2:0")
  embedding_function=BedrockEmbeddingFunction()
)

collection.add(
    documents=[
        "This is a document about pineapple",
        "This is a document about oranges"
    ],
    ids=["id1", "id2"]
)

results = collection.query(
    query_texts=["This is a query document about hawaii"], # Chroma will embed this for you
    n_results=2 # how many results to return
)
print(results)
