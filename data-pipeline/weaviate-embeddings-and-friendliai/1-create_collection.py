import os
import weaviate
from weaviate.classes.init import Auth
import weaviate.classes as wvc
import weaviate.classes.config as wc

WEAVIATE_CLUSTER_URL = os.getenv('WEAVIATE_CLUSTER_URL') or 'REPLACE_WITH_YOUR_CLUSTER_URL_IF_NOT_USING_ENVVAR'
WEAVIATE_API_KEY = os.getenv('WEAVIATE_API_KEY') or 'REPLACE_WITH_YOUR_KEY_IF_NOT_USING_ENVVAR'


client = weaviate.connect_to_weaviate_cloud(
    cluster_url=WEAVIATE_CLUSTER_URL,
    auth_credentials=Auth.api_key(WEAVIATE_API_KEY),
)

client.collections.delete(name="WeaviateEmbeddingBooks")
print(client.is_connected())

questions = client.collections.create(
    name="WeaviateEmbeddingBooks",
    
    vectorizer_config=wvc.config.Configure.Vectorizer.text2vec_weaviate(model="Snowflake/snowflake-arctic-embed-l-v2.0"),
    generative_config=wvc.config.Configure.Generative.friendliai(model="meta-llama-3.3-70b-instruct"),
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