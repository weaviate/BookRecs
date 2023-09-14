## Running a Semantic Search

### Semantic Search
With data in the vector database, we can run a simple semantic search over our embeddings in Weaviate and understand how the data is sent back to us as a result of the query.

There is a script called `search.py` in the `data-pipeline` directory, which demonstrates a semantic search query.

1. We create a Weaviate client object.
2. We create an object called `nearText` that lists several “concepts” that we want to search against in the vector database. The search will look for semantically related concepts, not exact matches.
3. The query is executed against the Weaviate client object, and the results are printed to the screen.

Feel free to change some of the concepts in `nearText` and run the script several times.

### Running the Search Script
Running the search script is as simple as running `populate.py`.

1. In your shell, run `python ./data-pipeline/search.py`.

The results should include a large object sent back with a list of books deeply nested in the response. These book results should be semantically similar to the `nearText` concepts passed into the query.

### Next Steps
Now that we know how to interact with Weaviate to find semantically similar items, we will see how the NextJS application uses this to surface recommendations to the user in a web interface.

---
*Note: The next section of the tutorial will include detailed steps on using the NextJS application to surface recommendations.*

