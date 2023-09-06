import os
import weaviate
import json

from dotenv import load_dotenv

load_dotenv()

WEAVIATE_CLUSTER_URL = os.getenv('WEAVIATE_CLUSTER_URL') or 'https://zxzyqcyksbw7ozpm5yowa.c0.us-west2.gcp.weaviate.cloud'
WEAVIATE_API_KEY = os.getenv('WEAVIATE_API_KEY') or 'n6mdfI32xrXF3DH76i8Pwc2IajzLZop2igb6'
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client = weaviate.Client(
    url=WEAVIATE_CLUSTER_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY),
    additional_headers={"X-OpenAI-Api-Key": OPENAI_API_KEY})

nearText = {
    "concepts":
    ["technology", "data structures and algorithms", "distributed systems"]
}

response = (client.query.get("Book", [
    "title",
    "isbn10",
    "isbn13",
    "categories",
    "thumbnail",
    "description",
    "num_pages",
    "average_rating",
    "published_year",
    "authors",
]).with_near_text(nearText).with_limit(10).do())

print(json.dumps(response, indent=4))
