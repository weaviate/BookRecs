import os
import weaviate
import weaviate.classes as wvc
import weaviate.classes.config as wc

WEAVIATE_CLUSTER_URL = os.getenv('WEAVIATE_CLUSTER_URL') or 'https://zxzyqcyksbw7ozpm5yowa.c0.us-west2.gcp.weaviate.cloud'
WEAVIATE_API_KEY = os.getenv('WEAVIATE_API_KEY') or 'n6mdfI32xrXF3DH76i8Pwc2IajzLZop2igb6'
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client = weaviate.Client(
    url=WEAVIATE_CLUSTER_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY),
    additional_headers={"X-OpenAI-Api-Key": OPENAI_API_KEY})

client.collections.delete(name="Book")
print(client.is_connected())

questions = client.collections.create(
    name="Book",
    
    vectorizer_config=wvc.config.Configure.Vectorizer.text2vec_openai(model="text-embedding-3-small"),
    generative_config=wvc.config.Configure.Generative.openai(model="gpt-3.5-turbo"),
    properties=[
        wc.Property(name="title", data_type=wc.DataType.TEXT),
        wc.Property(name="isbn10", data_type=wc.DataType.TEXT, skip_vectorization=True),
        wc.Property(name="isbn13", data_type=wc.DataType.TEXT, skip_vectorization=True),
        wc.Property(name="categories", data_type=wc.DataType.TEXT),
        wc.Property(name="thumbnail", data_type=wc.DataType.TEXT, skip_vectorization=True),
        wc.Property(name="description", data_type=wc.DataType.TEXT),
        wc.Property(name="num_pages", data_type=wc.DataType.TEXT, skip_vectorization=True),
        wc.Property(name="average_rating", data_type=wc.DataType.TEXT, skip_vectorization=True),
        wc.Property(name="published_year", data_type=wc.DataType.TEXT, skip_vectorization=True),
        wc.Property(name="authors", data_type=wc.DataType.TEXT, skip_vectorization=True),
    ],
)

client.close()