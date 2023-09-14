## Populating the Vector Database

### Dataset
We will be using a dataset from Kaggle, which includes about 7000 books with details like ISBN number, book description, book cover link, and more. You can find more information about the dataset on Kaggle (link in the description below).

In our repository, there is a folder called `data-pipeline` that contains two scripts and a dataset. The data is stored in a file called “7k-books-Kaggle.csv”. Feel free to look through it for more details.

### Scripts
One of the scripts, `populate.py`, is responsible for creating vectors and storing them in Weaviate. Let's look at `populate.py` in greater detail:

1. We create a weaviate-client object that receives the OpenAI API Key and the Weaviate key.
2. If the script was run before, we delete any pre-existing schema called 'Book' to keep the database “fresh” (Note: This is not recommended in production).
3. We create a schema for our books. The schema contains configuration details for vectorizing the data. We use the “text2vec-openai” vectorizer, and in the module configuration, we use `ada-002` as the foundation model to generate our embeddings.
4. We iterate through each row in our CSV dataset to create vectors for each book. The vectors and their related data objects are then stored in Weaviate.

### Running the Script
Now that you understand how it works, let’s run the script. First, we need to install some dependencies.

1. Set up a python virtual environment for the dependencies.
2. Run `pip install weaviate-client` in the terminal to install the official Weaviate python client.
3. Run `python data-pipeline/populate.py`.

When it finishes, you'll have data in Weaviate, and we can begin doing some fun and interesting searches on it.

---
*Note: The next section of the tutorial will include detailed steps on doing searches on the data.*

