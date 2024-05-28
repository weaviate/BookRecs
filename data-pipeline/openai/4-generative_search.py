import os
import weaviate
from weaviate.classes.init import AdditionalConfig, Timeout

from dotenv import load_dotenv

load_dotenv()

WEAVIATE_CLUSTER_URL = os.getenv('WEAVIATE_CLUSTER_URL') or 'https://zxzyqcyksbw7ozpm5yowa.c0.us-west2.gcp.weaviate.cloud'
WEAVIATE_API_KEY = os.getenv('WEAVIATE_API_KEY') or 'n6mdfI32xrXF3DH76i8Pwc2IajzLZop2igb6'
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client = weaviate.Client(
    url=WEAVIATE_CLUSTER_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY),
    additional_headers={"X-OpenAI-Api-Key": OPENAI_API_KEY})

print(client.is_connected())

book_collection = client.collections.get(name="Book")

# Generative Search

response = book_collection.generate.near_text(
    query="technology, data structures and algorithms, distributed systems",
    limit=2,
    single_prompt="Explain why this book might be interesting to someone who likes playing the violin, rock climbing, and doing yoga. the book's title is {title}, with a description: {description}, and is in the genre: {categories}."
)


print(response.objects[0].generated)  # Inspect the first object
