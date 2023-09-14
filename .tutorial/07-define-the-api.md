## Setting Up the API Endpoint

In this section, we will take a look at how we set up the API endpoint on our NextJS app that queries Weaviate on our dataset.

### API Directory Structure
In the `./pages` folder, there should be a directory called `api/`. Within it is a `recommendations.ts` file that will be triggered when an HTTP request is sent to `/api/recommendations/`.

### API Endpoint
The `recommendations.ts` endpoint performs the following actions:

1. **Extract Query**: It will extract the `query` from the request body.
   
2. **Query Weaviate**: It then passes the `query` into the `WeaviateClient` as a `nearText` object and queries the Book vectors through GraphQL.
   
3. **Send Result**: The result is then sent back to the client, which we have already set up to be stored in the state of the NextJS application.

---
*Note: The next section of the tutorial will include detailed steps on running the NextJS application and interacting with the user interface.*
