# Book Recommendations

## Weaviate Cloud (WCD) and OpenAI

The files contained in ./data-pipeline/openai demonstrate how to use a cluster in Weaviate Cloud (WCD) with OpenAI.

First, you'll need to create a cluster in WCD at https://console.weaviate.cloud/. There are free sandbox tiers that allow you to create a cluster entirely for free.

## Environment Setup

1. You'll need to create an .env file with the following API keys:
    *  WEAVIATE_CLUSTER_URL
    *  WEAVIATE_API_KEY
    *  OPENAI_API_KEY

2. Create a python virtual environment and install dependencies in requirements.txt at the root of this project
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then you can begin executing each step to understand how the BookRecs NextJS project interacts with Weaviate.

## Steps of Execution

```bash
python 1-create_collection.py
```

* This file will create a client in your Weaviate Cloud instance that configures OpenAI for embeddings and inference.

```bash
python 2-populate.py
```

* This script will populate your Weaviate Cloud data with data from the kaggle dataset referenced at the root directory of this project.

```bash
python 3-semantic_search.py
```

* Once executed, the script will make a connection with your Weaviate Cluster. Once complete, you'll be prompted for user input regarding a query you'd like to apply in the semantic search. The script then uses the Weaviate Client to do the semantic search against the dataset. In doing so, Weaviate generates a vector embedding using the configured vectorizer, in this case OpenAI - `text-embedding-3-small`, and then uses the query embedding to find related vectors.

```bash
python 4-generative_search.py
```

* Similar to 3-semantic_search.py, Weaviate applies an additional step where it passes the results over to the configured generative search module to do an inference based on the prompt in `4-generative_search.py`.