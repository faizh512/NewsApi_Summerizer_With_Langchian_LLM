import requests
import streamlit as st
from langchain.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from dotenv import load_dotenv
import os

load_dotenv()

llm = OllamaLLM(model="llama3")

st.title("News Summarizer and Categorizer")
news = st.text_input("Enter the News topic you want to get")

st_btn = st.button("Submit")
if st_btn and news:
    api_key="HERE ENTER YOUR API KEY OF NEWAPI"
    url = f"https://newsapi.org/v2/everything?q={news}&apiKey={api_key}&pageSize=5"
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        if articles:
            for article in articles:
                title = article.get('title', 'No title available')
                description = article.get('description', 'No description available')
                source = article.get('source', {}).get('name', 'No source available')
                if title and description:
                    st.write(f"**Title:** {title}")
                    st.write(f"**Description:** {description}")
                    st.write(f"**Source:** {source}")

                    system_msgs = "You are a helpful assistant. Please summarize the following news article and categorize it."
                    template_str = """Title: "{title}"
                    Description: "{description}"
                    Source: "{source}"
                    Please provide a brief summary of the above news article and categorize it."""
                    prompt = ChatPromptTemplate.from_messages([('system', system_msgs), ('user', template_str)])
                    formatted_prompt = prompt.format(title=title, description=description, source=source)
                    response = llm(formatted_prompt)
                    st.write(f"**Summary:** {response.strip()}")
                    st.write(f"**Category:** {response.strip().split()[-1]}")  # Example to extract category from response
                    st.write("---")
                else:
                    st.write("No sufficient information to summarize.")
        else:
            st.write("No articles found for the given topic.")
    else:
        st.write("Failed to retrieve news articles. Please try again later.")

st_btn = st.button("Submit")
if st_btn and news:
    api_key = '1d3eda3da3c74fbdb46d07db1da14979'
    url = f"https://newsapi.org/v2/everything?q={news}&apiKey={api_key}&pageSize=5"
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        if articles:
            for article in articles:
                title = article.get('title', 'No title available')
                description = article.get('description', 'No description available')
                source = article.get('source', {}).get('name', 'No source available')
                if title and description:
                    st.write(f"**Title:** {title}")
                    st.write(f"**Description:** {description}")
                    st.write(f"**Source:** {source}")

                    # Define system and user messages for summarization
                    system_msgs_summary = "You are a helpful assistant. Please summarize the following news article."
                    template_str_summary = """Title: "{title}"
                    Description: "{description}"
                    Source: "{source}"
                    Please provide a brief summary of the above news article."""

                    # Define system and user messages for categorization
                    system_msgs_category = "You are a helpful assistant. Please categorize the following news article."
                    template_str_category = """Title: "{title}"
                    Description: "{description}"
                    Source: "{source}"
                    Please categorize the above news article into a specific category."""

                    # Create prompts for summarization and categorization
                    prompt_summary = ChatPromptTemplate.from_messages([('system', system_msgs_summary), ('user', template_str_summary)])
                    formatted_prompt_summary = prompt_summary.format(title=title, description=description, source=source)
                    summary_response = llm(formatted_prompt_summary)

                    prompt_category = ChatPromptTemplate.from_messages([('system', system_msgs_category), ('user', template_str_category)])
                    formatted_prompt_category = prompt_category.format(title=title, description=description, source=source)
                    category_response = llm(formatted_prompt_category)

                    # Display the summary and category
                    st.write(f"**Summary:** {summary_response.strip()}")
                    st.write(f"**Category:** {category_response.strip()}")
                    st.write("---")
                else:
                    st.write("No sufficient information to summarize.")
        else:
            st.write("No articles found for the given topic.")
    else:
        st.write("Failed to retrieve news articles. Please try again later.")
