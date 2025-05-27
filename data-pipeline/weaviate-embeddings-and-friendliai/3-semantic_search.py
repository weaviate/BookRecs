import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.init import AdditionalConfig, Timeout

WEAVIATE_CLUSTER_URL = os.getenv('WEAVIATE_CLUSTER_URL') or 'https://zxzyqcyksbw7ozpm5yowa.c0.us-west2.gcp.weaviate.cloud'
WEAVIATE_API_KEY = os.getenv('WEAVIATE_API_KEY') or 'n6mdfI32xrXF3DH76i8Pwc2IajzLZop2igb6'


client = weaviate.connect_to_weaviate_cloud(
    cluster_url=WEAVIATE_CLUSTER_URL,
    auth_credentials=Auth.api_key(WEAVIATE_API_KEY),
)

print(client.is_connected())

book_collection = client.collections.get(name="WeaviateEmbeddingBooks")

# Semantic Search

response = book_collection.query.near_text(
    query="biology",
    limit=3
)

print()
for book in response.objects:
    print(book.properties['title'])
    print(book.properties['description'])
    print(book.properties['categories'])
    print('---')
