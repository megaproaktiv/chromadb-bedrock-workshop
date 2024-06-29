#  Embedding Databases

## ChromaDB

```bash
pip install chromadb
```

```bash
poetry shell
```

## 1) Getting Started

```bash
 poetry shell
 python chromadb-start.py
```

Output:

```bash
/Users/gglawe/.cache/chroma/onnx_models/all-MiniLM-L6-v2/onnx.tar.gz:  35%|█████████████████▎                                | 27.4M/79.3M [00:05<00:11, 4.80MiB/s]
{'ids': [['id1', 'id2']], 'distances': [[1.0403728485107422, 1.2430635690689087]], 'metadatas': [[None, None]], 'embeddings': None, 'documents': [['This is a document about pineapple', 'This is a document about oranges']], 'uris': None, 'data': None, 'included': ['metadatas', 'documents', 'distances']}
```

## 2) Bedrock start

```bash
poetry shell
python bedrock-start.py
```

Output:

```bash
[-0.07963294, 0.022934286, 0.035994086, -0.004260362, 0.005773388, -0.0063308184, 0.031534642, -0.017678512, 0.034082897, 0.024049146, -0.028030794, 0.071669646, 0.026278868, -0.004519169, -0.023252817, 0.057654247, -0.041409127, 0.027234465, 0.03169391, 0.041090596, 0.07740321, 0.025960337, -0.020545298, 0.01951007, -0.04172766, -0.022137957, 4.9770583e-06, 0.01003375, 0.02388988, -0.022297222, 0.038701605, 0.050646547, 0.0033644915, -0.072625235, 0.0793144, 0.110849045, 0.066573136, -0.0055743055, -0.01274127, -0.021341627, 0.012582004, -0.015130258, -0.0033445833, 0.023252817, 0.030260516, 0.048416823, 0.023252817, 0.022934286, 0.07230671, 0.008321642]
1024
```

## 3) ChromaDB with Bedrock langchain

See: [Creating your own embedding function](https://cookbook.chromadb.dev/embeddings/bring-your-own-embeddings/)

Very large

  ```bash
  du -skh  /Users/gglawe/Library/Caches/pypoetry/virtualenvs/py-chroma-ST8gDT65-py3.11/lib/python3.11
  326M	/Users/gglawe/Library/Caches/pypoetry/virtualenvs/py-chroma-ST8gDT65-py3.11/lib/python3.11
  ```

  Without langchain 297M.

  Lambda size limit is 250MB.



## Pyrightconfig

```bash
poetry env list
```

`py-chroma/pyrightconfig.json`

```json
{
  "venv": "py-chroma-ST8gDT65-py3.11",
  "venvPath": "/Users/gglawe/Library/Caches/pypoetry/virtualenvs/"
}
```



## Appendix

### Sources

- [Basic Concepts of Embedding Databases](https://realpython.com/chromadb-vector-database/)
- [chromadb](https://docs.trychroma.com/)
- [Chromadb Bedrock](https://medium.com/@philippkai/building-a-rag-agent-with-langgraph-llama3-70b-and-scaling-with-amazon-bedrock-2be03fb4088b)

### Errors

#### ERROR:root:failed to invoke model: An error occurred (ValidationException) when calling the InvokeModel operation: The provided model identifier is invalid.

Cause:

```py
response = client.invoke_model(
    body=payload_bytes,
    modelId='titanEmbeddingModelID',  # Replace with your actual model ID
    contentType='application/json'
)
```

#### ERROR:root:failed to invoke model: An error occurred (ValidationException) when calling the InvokeModel operation: Malformed input request: 2 schema violations found, please reformat your input and try again.

Cause:

```py
payload = {
    "InputText": input_text,
}
``
