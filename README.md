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

## 🛠 Installation

To run the project locally, follow these steps:

1. Clone the repository
   ```
   git clone https://github.com/weaviate/BookRecs.git
   ```

2. Optionally, create a Weaviate Cluster using the [Weaviate Console](https://console.weaviate.cloud/) and make note of the cluster URL and the API Key. The project is already configured to read from an existing Weaviate Cluster. If you choose not to create a new Weaviate Cluster, you can rely on the default cluster we've already created for you. It's configured in both the NextJS app and the Python data pipeline. 

3. Create a OpenAI account and create API Key.

4. Set up environment variables in .env
   ```
   cp env.example .env
   ```
   `OPENAI_API_KEY` is required. If you don't choose not to create the Weaviate Cluster, remove `WEAVIATE_CLUSTER_URL` and `WEAVIATE_API_KEY` from the `.env`.

5. Set up a Python virtualenv to populate your vector database and to experiment with semantic search. 
   ```
   python3 -m venv venv 
   source venv/bin/activate
   pip install -r requirements.txt
   python data-pipeline/populate.py # Will only work if you create your own cluster
   python data-pipeline/search.py
   ```

6. Install dependencies
   ```
   cd bookrecs
   npm install
   ```
7. Run the app
   ```
   npm run dev
   ```
8. Try out BookRecs in a browser at http://localhost:3000


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

## 🕷 Known Issues

- Some book images are inaccessible due to dead links on the original data set

## 💰 Large Language Model (LLM) Costs

BookRecs exclusively utilizes OpenAI models. Be advised that the usage costs for these models will be billed to the API access key you provide. Primarily, costs are incurred during data embedding and answer generation processes. The default vectorization engine for this project is `Ada v2`.

## 💖 Open Source Contribution

Your contributions are always welcome! Feel free to contribute ideas, feedback, or create issues and bug reports if you find any! Visit our [Weaviate Community Forum](https://forum.weaviate.io/) if you need any help!

