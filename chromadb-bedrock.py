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

collection = chroma_client.create_collection(
  name="neo_collection",
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
