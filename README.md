# Book Recommendation System (BookRecs)
[![Weaviate](https://img.shields.io/static/v1?label=powered%20by&message=Weaviate%20%E2%9D%A4&color=green&style=flat-square)](https://weaviate.io/) 
[![Demo](https://img.shields.io/badge/Check%20out%20the%20demo!-yellow?&style=flat-square&logo=react&logoColor=white)](https://bookrecs.weaviate.io/)


This project is a book recommendation service that suggests books based on a user's inputted genre and book titles. It's built upon a database of 7000 books retrieved from Kaggle. Using Ada v2 as the large language model, vector embeddings were created with the Kaggle dataset to allow for quick vector search to find semantically similar books through natural language input. The frontend is built using Next.js and styled with TailwindCSS.

![Project Screenshot](/BookRecs.gif)

## 📑 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data Source](#data-source)
- [Tech Stack](#tech-stack)
- [Contributing](#contributing)
- [License](#license)

## 💫 Features

- Input genre and book titles to get book recommendations
- Vector Search on Weaviate Vector database of 7000 books
- Jupyter Notebook workflow to access and store vector embeddings in Weaviate
- Responsive design, thanks to TailwindCSS
- Uses Ollama or OpenAI for vector generation and inference.

## 🛠 Installation

To run the project locally, follow these steps:

Clone the repository
   ```
   git clone https://github.com/weaviate/BookRecs.git
   ```

### The Data Pipeline

The data pipeline shows you how to connect with Weaviate, generate embeddings using integrated modules with Weaviate through OpenAI or Ollama, and then query them using semantic search and vector search. Choose between one of the following options.

#### Data Pipeline Using Ollama (Option1)

If you're using Ollama with this project, follow the instructions found in the [ollama/README.md](./data-pipeline/ollama/README.md) to set up Ollama and Weaviate running locally. 

#### Data Pipeline Using OpenAI (Option2)

If you're using OpenAI with this project, make sure to create a Weaviate Cloud cluster in WCD and get an API key from OpenAI. There are instructions to get an API key from the official [OpenAI Docs](https://platform.openai.com/docs/api-reference/introduction). You'll also need to fund the account.

Once you have the above dependencies sorted out, you can follow the instructions in the [openai/README.md](./data-pipeline/openai/README.md)

### The Web Application

Once you've set up Weaviate and understand how the data pipeline works you can move over to the BookRecs web application written in NextJS. 

**Note**: The web application is configured only to use OpenAI and WCD as an introduction on how to leverage Weaviate. It can be modified to use Ollama and a locally running Weaviate instance, but this project won't do that ouf of the box.

Additionally, this project has access to an existing WCD Cluster with an API Key configured to only allow READing from the public WCD cluster.

Install dependencies
   ```
   cd bookrecs
   npm install
   ```
Run the app
   ```
   npm run dev
   ```
Try out BookRecs in a browser at http://localhost:3000


## 🤝 Configuring Cohere Integration

This project provides book recommendations using a vector database for semantic search. An additional feature is the integration with Cohere through the Weaviate Generative Search module, which provides explainations as to why a user might like a particular book recommendation.

If you would like to enable this feature, you will need to configure the COHERE_API_KEY and NEXT_PUBLIC_COHERE_CONFIGURED environment variables.

Steps
1. Obtain a Cohere API key by signing up on the [Cohere website](https://cohere.com).
2. Once you have your API key, open the .env file in the root directory of the project.
3. Add the following line to the file, replacing 'INSERT_OPEN_API_KEY_HERE' with the API key you obtained from Cohere:
```
COHERE_API_KEY=INSERT_OPENAPI_KEY_HERE
```
4. To enable the Cohere integration, set the NEXT_PUBLIC_COHERE_CONFIGURED environment variable to "1". Add the following line to the .env file:
```
NEXT_PUBLIC_COHERE_CONFIGURED=1
```
5. Save the .env file and restart your development server. The Cohere integration should now be enabled.

Please note that the COHERE_API_KEY should be kept secret and not exposed to the client-side of your application.


## 🧰 Usage

To use the service, simply type in a genre and several book titles in the provided input fields. The system will then generate several book recommendations based on your inputs.

You can try this at https://bookrecs.weaviate.io

You must set at least on OPENAI_API_KEY environment variable. You can also set up your own Weaviate cluster and create embeddings yourself. If you choose not to do this, BookRecs will use a Read Only API key for an existing Weaviate cluster containing the Kaggle dataset. 


## 💾 Data Source

The book data used for this project is sourced from the following Kaggle dataset: [7k books with metadata](https://www.kaggle.com/datasets/dylanjcastillo/7k-books-with-metadata). The dataset has been converted to a vector embedding using the sentence-transformer model for improved natural language processing and stored in a Weaviate clustor for fast vector lookups.

## 💻 Tech Stack

- [NodeJS version 18.12.1 or above](https://nodejs.org/)
- [Next.js](https://nextjs.org/)
- [TailwindCSS](https://tailwindcss.com/)
- [Python Data Pipeline](https://python.org/)
- [Weaviate >1.25](https://weaviate.io/)

## 🕷 Known Issues

- Some book images are inaccessible due to dead links on the original data set

## 💰 Large Language Model (LLM) Costs with OpenAI

BookRecs utilizes OpenAI or Ollama models. For OpenAI -- be advised that the usage costs for these models will be billed to the API access key you provide. Primarily, costs are incurred during data embedding and answer generation processes. The default vectorization engine for this project is `text-embedding-3-small`.

## 💖 Open Source Contribution

Your contributions are always welcome! Feel free to contribute ideas, feedback, or create issues and bug reports if you find any! Visit our [Weaviate Community Forum](https://forum.weaviate.io/) if you need any help!

