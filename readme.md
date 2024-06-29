#  Embedding Databases

This workshop shows the usage of an embedding database, which uses a local db file.
This way it could be included in lambda.
As documents, we use a part of the tecRacer AWS FAQs, stored in `tecracer-faq.txt`.

## 0 Install

```bash
poetry install
```

## 1) Getting Started with Chromadb

ChromaDB is a vector database that allows you to store and query embeddings.

Here you see the first steps.


```bash
poetry shell
python chromadb-start.py
```

What happens?
A model is downloaded locally.


## 2) Bedrock start

This is an example of how Bedrock is used to get embeddings from a model.

You see the numerical representation of the text "This is a content of the document".

```bash
poetry shell
python bedrock-start.py
```

Output:

```bash
[-0.07963294, 0.022934286, 0.035994086, -0.004260362, 0.005773388, -0.0063308184, 0.031534642, -0.017678512, 0.034082897, 0.024049146, -0.028030794, 0.071669646, 0.026278868, -0.004519169, -0.023252817, 0.057654247, -0.041409127, 0.027234465, 0.03169391, 0.041090596, 0.07740321, 0.025960337, -0.020545298, 0.01951007, -0.04172766, -0.022137957, 4.9770583e-06, 0.01003375, 0.02388988, -0.022297222, 0.038701605, 0.050646547, 0.0033644915, -0.072625235, 0.0793144, 0.110849045, 0.066573136, -0.0055743055, -0.01274127, -0.021341627, 0.012582004, -0.015130258, -0.0033445833, 0.023252817, 0.030260516, 0.048416823, 0.023252817, 0.022934286, 0.07230671, 0.008321642]
1024
```

## 3) ChromaDB with Bedrock

Now we combine the two examples above.
For that, a own embedding function is used.

See [embedding.py](bedrock/embedding.py)

The texts are send to the bedrockruntime AWS API.
The responses include the embedding vectors:

```py
resp.get('embedding', [])]
```

All embeddings are stored in a local SQLite database file:

```bash
db/chroma.sqlite3
```

If you start this a second time, you will see that the embeddings are already stored in the database.
With "task reset" you can delete the database and start from scratch.

## 4) ChromaDB with Bedrock and local database

```bash
poetry shell
python chromadb-persisted.py
```

As we have created a local database in the previous step, we can now use this database to get the embeddings.

So the "import" step is not necessary anymore.


## Pyrightconfig

If you use pyright, with poetry, you may have to configure the path to the virtual environment.


```bash
poetry env list
```

`py-chroma/pyrightconfig.json`

```json
{
  "venv": "py-chroma-ST8gDT65-py3.11",
  "venvPath": "/Users/******/Library/Caches/pypoetry/virtualenvs/"
}
```



## Appendix

### Sources

- [Basic Concepts of Embedding Databases](https://realpython.com/chromadb-vector-database/)
- [chromadb](https://docs.trychroma.com/)

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
