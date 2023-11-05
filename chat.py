import os
import sys
import requests
from bs4 import BeautifulSoup
import constants
from urllib.parse import urljoin
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = constants.APIKEY

base_url = 'https://www.gonzaga.edu/'

def download_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        text_data = soup.get_text()
        return text_data
    else:
        print(f'Failed to fetch the web page: {url}')
        return None
    
def process_data(text_data):
    file_path = 'scraped_data.txt'

    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(text_data + '\n')


loader = DirectoryLoader(".", glob="*.txt")
index = VectorstoreIndexCreator().from_loaders([loader])

visited_urls = set()
to_visit = [base_url]

def find_links(url, html_content):
    links = []
    soup = BeautifulSoup(html_content, 'html.parser')

    for link in soup.find_all('a', href=True):
        href = link.get('href')
        full_url = urljoin(url, href)
        if is_valid_link(full_url):
            links.append(full_url)
    
    return links

while to_visit:
    url = to_visit.pop()
    if url not in visited_urls:
        text_data = download_data(url)
        if text_data:
            process_data(text_data)
        visited_urls.add(url)
        links = find_links

def is_valid_link(link):
    return link.startswith('https://www.gonzaga.edu')

query = sys.argv[1]

print(index.query(query, llm=ChatOpenAI()))