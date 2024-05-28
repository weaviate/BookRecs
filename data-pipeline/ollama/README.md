# Book Recommendations

## Weaviate Local and Ollama

The files contained in `./data-pipeline/ollama` demonstrate how to run Weaviate locally using Docker and configuring Ollama to create vector embeddings and inference.

## Environment Setup

First, you'll need to run Weaviate locally through docker and configure the text2vec_ollama and generative_ollama modules for Weaviate. You can use the docker-compose.yml in this folder. 

```bash
docker-compose -f ./data-pipeline/ollama/docker-compose.yml up -d
```

**NOTE**: The docker compose file above only has Ollama modules enabled. If you want to use another vectorizer configuration, you'll need to extend the docker-compose.yml configuration. Details can be found in our [developer docs for using Weaviate with Docker](https://weaviate.io/developers/weaviate/installation/docker-compose). 

You'll also need to install ollama locally and pull two models. Go to [Ollama](https://ollama.com) and download ollama for your operating system. Then pull two models - `llama3:latest` for inference, `snowflake-arctic-embed:latest` for embeddings.

```
ollama pull snowflake-arctic-embed:latest
ollama pull llama3:latest
```

Create a python virtual environment and install dependencies in requirements.txt at the root of this project
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

* This file will create a client in your locally running Weaviate instance that configures Ollama for embeddings and inference.

```bash
python 2-populate.py
```

* This script will populate your Weaviate Cloud data with data from the kaggle dataset referenced at the root directory of this project.

```bash
python 3-semantic_search.py
```

* Once executed, the script will make a connection with your Weaviate Cluster. Once complete, you'll be prompted for user input regarding a query you'd like to apply in the semantic search. The script then uses the Weaviate Client to do the semantic search against the dataset. In doing so, Weaviate generates a vector embedding using the configured vectorizer, in this case Ollama - `snowflake-arctic-embed:latest`, and then uses the query embedding to find related vectors.

```bash
python 4-generative_search.py
```

* Similar to 3-semantic_search.py, Weaviate applies an additional step where it passes the results over to the configured generative search module to do an inference based on the prompt in `4-generative_search.py`.