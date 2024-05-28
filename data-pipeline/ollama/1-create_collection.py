import weaviate
import weaviate.classes as wvc
import weaviate.classes.config as wc

client = weaviate.connect_to_local()
client.collections.delete(name="Book")
print(client.is_connected())

questions = client.collections.create(
    name="Book",
    
    vectorizer_config=wvc.config.Configure.Vectorizer.text2vec_ollama(model="snowflake-arctic-embed:latest", api_endpoint="http://host.docker.internal:11434"),
    generative_config=wvc.config.Configure.Generative.ollama(api_endpoint="http://host.docker.internal:11434", model="llama3:latest"),
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