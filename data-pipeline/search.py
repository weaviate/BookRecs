import os
import csv
import weaviate
import json

client = weaviate.Client(
    url=f"https://{os.environ.get('WEAVIATE_CLUSTER_URL')}",
    auth_client_secret=weaviate.AuthApiKey(api_key=os.environ.get(
        "WEAVIATE_API_KEY")),  # Replace w/ your Weaviate instance API key
    additional_headers={"X-OpenAI-Api-Key": os.environ.get("OPENAI_APIKEY")})

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
