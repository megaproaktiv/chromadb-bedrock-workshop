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
    #self.model = "amazon.titan-embed-text-v1"
    self.model = "amazon.titan-embed-text-v2:0"

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
        """Where are my data stored with Amazon AWS?
        Currently, there are eight Amazon data centers (AWS Regions) in different parts of the world.""",
        """
        How secure are my data with Amazon AWS?
        Customer data is stored in a highly secured infrastructure.
        """,
        """Security measures include:

        - Protection against DDoS attacks (Distributed Denial of Service)
        - Defense against brute-force attacks on AWS accounts
        - Secure access: Access is established over SSL.
        - Firewall: Ingress and egress to AWS data can be controlled.
        - Encrypted data storage: Data can be encrypted with Advanced Encryption Standard (AES) 256.
        - Certifications: Regular security reviews through independent certifications that AWS undergoes.
        """,
        """
        If your chosen resources do not provide enough performance, you can easily grant more CPU power to the resources with just a few clicks. You don't need to install anything new; you only need to restart your virtual machine or virtual database instance.""",
        """
        Amazon AWS offers you external and internal load balancers.

        External load balancers connect to the Internet and distribute the load across web servers. Internal load balancers can also be used to distribute the load across different backend servers. As part of AutoScaling, you can define a configuration that automatically starts or stops additional resources (virtual computers) based on defined metrics. You only pay for the resources you use.
        """
    ],
    ids=["storage", "security", "security-measures", "performace", "load-balancers"]
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
