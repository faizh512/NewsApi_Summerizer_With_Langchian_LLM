# News Summarizer and Categorizer

## Project Overview

The **News Summarizer and Categorizer** app allows users to input a news topic and retrieve the latest articles on that topic. The app summarizes and categorizes the news articles using **Ollama LLM (Llama3)**. This project was built with **Streamlit** for the web interface, **LangChain** for handling language model prompts, and **NewsAPI** for fetching news data.

## Features

- Fetches the latest news articles based on the user's topic of interest.
- Summarizes the content of the articles.
- Categorizes the news articles into relevant categories based on the content.

## Tech Stack

- **Streamlit**: Front-end web framework for creating a simple user interface.
- **LangChain**: Provides structured handling of prompts and interactions with the language model.
- **Ollama LLM (Llama3)**: Utilized for generating summaries and categorizing articles.
- **NewsAPI**: Used to fetch relevant news articles.
- **dotenv**: Used for securely managing environment variables such as API keys.

## Installation

### Prerequisites

- **Python 3.x** installed on your machine.
- A valid **NewsAPI** key to access the news articles.
- A valid **Ollama LLM** model installed or available for API access.

### Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-repo/news-summarizer-categorizer.git
   cd news-summarizer-categorizer
