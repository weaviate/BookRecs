import weaviate
from weaviate.classes.init import AdditionalConfig, Timeout

client = weaviate.connect_to_local(additional_config=AdditionalConfig(
    timeout=Timeout(init=2, query=200, insert=120)  # Values in seconds
))

print(client.is_connected())

book_collection = client.collections.get(name="Book")

# Generative Search

user_input = input("What query do you have for book recommendations? ")


response = book_collection.generate.near_text(
    query=user_input,
    limit=2,
    single_prompt="Explain why this book might be interesting to read. The book's title is {title}, with a description: {description}, and is in the genre: {categories}."
)


print(f"Here are the recommended books for you based on your interest in {user_input}:")
for book in response.objects:
    print(f"Book Title: {book.properties['title']}")
    print(f"Book Description: {book.properties['description']}")
    print('---\n\n\n')

client.close()
