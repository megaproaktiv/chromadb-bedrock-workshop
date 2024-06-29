import json
import logging
import boto3
import sys
from typing import Sequence, List, Union

from chromadb import  EmbeddingFunction, Embeddings
from chromadb.api.models.CollectionCommon import Embedding

Vector = Union[Sequence[float], Sequence[int]]


def fetch_embedding(input_texts, model)-> Embeddings:
    # See https://github.com/build-on-aws/amazon-bedrock-go-sdk-examples/blob/main/titan-text-embedding/main.go

    # Define the payload
    embeddings: List[Embedding] = []
    for input_text in input_texts:
      payload = {
        "inputText": input_text,
        "dimensions": 512,
        "normalize": True
      }

      # Serialize the payload to JSON
      try:
          payload_bytes = json.dumps(payload)
      except json.JSONDecodeError as err:
          logging.error(err)
          sys.exit(1)

      # Initialize the boto3 client
      client = boto3.client('bedrock-runtime')

      # Invoke the model
      # See: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime/client/invoke_model.html
      try:
          response = client.invoke_model(
              body=payload_bytes,
              modelId=model,  # Replace with your actual model ID
              contentType='application/json'
          )
      except client.exceptions.ClientError as err:
          logging.error(f"failed to invoke model: {err}")
          sys.exit(1)

      # Deserialize the response body
      try:
          resp =json.loads(response.get('body').read())
      except json.JSONDecodeError as err:
          logging.error(f"failed to unmarshal: {err}")
          sys.exit(1)

      # Extract embeddings
      #    embeddings: List[Embedding] = [Vector(item) for item in resp.get('Embedding', [])]

      embedding = [float(item) for item in resp.get('embedding', [])]
      embeddings.append(embedding)
      # Print vector length
      print("generated vector length -", len(embeddings))


    return embeddings
