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
2. Install dependencies
   ```
   cd bookrecs
   npm install
   ```
3. Create a Weaviate Instance and make note of the cluster URL and the API Key
4. Create a OpenAI account and create API Key (Also referred to as Access Token)

5.  Set up environment variables in .env.local
   ```
   cp env.example .env.local
   ```
6. Run the app, then access the app in a browser at http://localhost:3000
   ```
   npm run dev
   ```
7. Run the Jupyter Notebook to learn how wo create vector embeddings and store them on Weaviate
   ```
   python3 -m venv venv 
   pip install -r requirements.txt
   jupyter notebook
   ```
8. Access the Jupyter Notebook in a browser at http://localhost:8000

## 🧰 Usage

To use the service, simply type in a genre and several book titles in the provided input fields. The system will then generate several book recommendations based on your inputs.

You can try this at https://bookrecs.weaviate.io

You must set at least on OPENAI_APIKEY environment variable. You can also set up your own Weaviate cluster and create embeddings yourself. If you choose not to do this, BookRecs will use a Read Only API key for an existing Weaviate cluster containing the Kaggle dataset. 


## 💾 Data Source

The book data used for this project is sourced from the following Kaggle dataset: [7k books with metadata](https://www.kaggle.com/datasets/dylanjcastillo/7k-books-with-metadata). The dataset has been converted to a vector embedding using the sentence-transformer model for improved natural language processing and stored in a Weaviate clustor for fast vector lookups.

## 💻 Tech Stack

- [NodeJS version 18.12.1 or above](https://nodejs.org/)
- [Next.js](https://nextjs.org/)
- [TailwindCSS](https://tailwindcss.com/)
- [Python Data Pipeline](https://python.org/)

## 🕷 Known Issues

- Book recommendation cards may by different heights due to overflowing book titles
- Some book images are inaccessible due to dead links on the original data set

## 💰 Large Language Model (LLM) Costs

BookRecs exclusively utilizes OpenAI models. Be advised that the usage costs for these models will be billed to the API access key you provide. Primarily, costs are incurred during data embedding and answer generation processes. The default vectorization engine for this project is `Ada v2`.

## 💖 Open Source Contribution

Your contributions are always welcome! Feel free to contribute ideas, feedback, or create issues and bug reports if you find any! Visit our [Weaviate Community Forum](https://forum.weaviate.io/) if you need any help!

