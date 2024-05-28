## Accounts & Environments

### Register on Weaviate Cloud (WCD)
The first step is to register an account on Weaviate Cloud (WCD). If you already have an account, you can skip ahead to creating a dedicated cluster.

1. Open your browser and go to [Weaviate Cloud](https://console.weaviate.cloud/)
2. Register for an account. (Pause here and sign up for an account if you haven't already)

### Create a New Cluster
Once you have an account, log in and create a new cluster.

1. In the WCD console, click "Create cluster".
2. You can use a “Free sandbox”, or select Standard, Enterprise, or Business Critical for long-term use.
3. Give your cluster a memorable name.
4. Ensure “Enable Authentication” is set to “Yes”.
5. Review the details and click “Create”.

WCD will deploy your cluster and provide an endpoint where you can begin storing your embeddings.

### Note Cluster URL and API Key
While still in WCD, take note of the Cluster URL and the API Key for your Weaviate instance.

1. Click “Details” on the newly created cluster to expand the view.
2. Copy the “Cluster URL” and save it in a text file for later reference.
3. Go back to WCD, click API Keys, and copy the Admin key. Save this in the text file as well.

### Get OpenAI API Key
You will also need an API key from OpenAI to generate embeddings. If you already have a token, you can use it for this project.

1. Register for an account on [OpenAI](https://openai.com).
2. Once logged in, select API.
3. Go to your avatar at the top right, select “View API Keys”, and create a new secret key.
4. Give it a name of your choice and create it.
5. Copy the key and save it in the text file for later reference.

### Set Up Your Environment
Next, set up your environment and insert the values into your environment variables.

- If you are building locally in VSCode, drop the values into a `.env` file and use the following environment variable names as shown on the screen. Source the `.env` file every time you start a new terminal session.
- If you are building in Replit, use the Secrets tool on the bottom left of the screen and insert your environment variables there. You can add the environment variables by editing the JSON and inserting the snippet below, and adding each one manually.


```
{
  "WEAVIATE_API_KEY": "INSERT_API_KEY",
  "WEAVIATE_CLUSTER_URL": "INSERT_CLUSTER_URL",
  "OPENAI_APIKEY": "INSERT_API_KEY"
}
```

### Next Steps
Great! Our environment is set up. Next, we will populate the vector database with our objects and their related embeddings.

---
*Note: The next section of the tutorial will include detailed steps on populating the vector database.*
