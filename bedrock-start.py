import boto3
import json, re
from langchain_community.embeddings import BedrockEmbeddings

# Create a bedrock runtime client in us-west-2
bedrock_rt = boto3.client("bedrock-runtime",
                          region_name="eu-central-1"
)



# Choose from a set of embedding models hosted on Amazon Bedrock
# Provider  | Model Name                        | Model ID
# -------------------------------------------------------------------------------
# Amazon    | Titan Embeddings G1 - Text 1.x   | amazon.titan-embed-text-v1
# Amazon    | Titan Embedding Text v2 1.x       | amazon.titan-embed-text-v2:0
# Cohere    | Embed English 3.x                 | cohere.embed-english-v3
# Cohere   | Embed Multilingual 3.x           | cohere.embed-multilingual-v3
embedding_model_id = "amazon.titan-embed-text-v2:0"
embeddings = BedrockEmbeddings(client=bedrock_rt, model_id=embedding_model_id)
vector = embeddings.embed_documents(
    ["This is a content of the document", "This is another document"]
)

print(vector[0][:50])
print(len(vector[0]))
