#                                 FAQ-Module-Interactive-ChatBox

## Link of the app : https://faq-module-app-khc53mwoxe4p7n4pqkaeqk.streamlit.app/

# Overview
The FAQ Search System is an interactive web application built using Streamlit and Sentence Transformers. It allows users to ask questions and receive relevant answers from a dataset of frequently asked questions (FAQs). The application employs natural language processing (NLP) techniques to enhance the search experience by understanding the semantics of user queries.

## Features
### 1. Interactive search interface for querying FAQs
### 2. Utilizes sentence embeddings for semantic similarity
### 3. Retrieves the most relevant answers based on user input
### 4. Customizable user interface through external CSS styling

## Technologies Used
### 1. Streamlit: A framework for building interactive web applications in Python.
### 2. Sentence Transformers: A library for generating sentence embeddings and calculating similarity.
### 3. JSON: A format for storing and managing FAQ data.

## Application Structure
This is the main application file where the following components are defined:

### Loading FAQ Data: The application reads and processes the FAQ data from the faqs.json file.
### Embedding FAQs: It utilizes the Sentence Transformers model to convert FAQ questions into embeddings for semantic comparison.
### Search Functionality: The application provides a search function that computes the cosine similarity between user queries and FAQ embeddings to find the most relevant FAQs.
### User Interface: The Streamlit framework is used to create an interactive interface that includes a text input for queries and a display area for results.
local_css(file_name)
This function loads an external CSS file to style the application, enhancing the user interface.

## User Guide
The FAQ Search System is deployed and can be accessed directly using the following link:

Access the FAQ Search System(https://faq-module-app-khc53mwoxe4p7n4pqkaeqk.streamlit.app/)

### 1. Open the link in a web browser.
### 2. In the input field labeled "Ask your question here...", enter your query and click the "Search" button.
### 3. The application will display the most relevant answers based on the entered query. If no matches are found, an appropriate message will be shown.

# Acknowledgments
Thank you to the developers of Streamlit and Sentence Transformers for creating powerful tools that facilitate the development of this application.
