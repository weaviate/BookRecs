import os
import csv
import weaviate

client = weaviate.Client(
    url=f"https://{os.environ.get('WEAVIATE_CLUSTER_URL')}",
    auth_client_secret=weaviate.AuthApiKey(api_key=os.environ.get(
        "WEAVIATE_API_KEY")),  # Replace w/ your Weaviate instance API key
    additional_headers={"X-OpenAI-Api-Key": os.environ.get("OPENAI_APIKEY")})

client.schema.delete_class("Book")

class_obj = {
    "class": "Book",
    "vectorizer": "text2vec-openai",
    "moduleConfig": {
        "text2vec-openai": {
            "model": "ada",
            "modelVersion": "002",
            "type": "text"
        }
    }
}

client.schema.create_class(class_obj)
# client.batch.configure(batch_size=100)  # Configure batch
f = open("./data-workflow/7k-books-kaggle.csv", "r")
current_book = None
try:
  with client.batch as batch:  # Initialize a batch process
    batch.batch_size = 100
    reader = csv.reader(f)
    # Iterate through each row of data
    for book in reader:
      current_book = book
      # 0 - isbn13
      # 1 - isbn10
      # 2 - title
      # 3 - subtitle
      # 4 - authors
      # 5 - categories
      # 6 - thumbnail
      # 7 - description
      # 8 - published_year
      # 9 - average_rating
      # 10 - num_pages
      # 11 - ratings_count

      properties = {
          "isbn13": book[0],
          "isbn10": book[1],
          "title": book[2],
          "subtitle": book[3],
          "authors": book[4],
          "categories": book[5],
          "thumbnail": book[6],
          "description": book[7],
          "published_year": book[8],
          "average_rating": book[9],
          "num_pages": book[10],
          "ratings_count": book[11],
      }

      batch.add_data_object(data_object=properties, class_name="Book")
      # print(f"{book[2]}: {uuid}", end='\n')
except Exception as e:
  print(f"something happened {e}. Failure at {current_book}")

f.close()
