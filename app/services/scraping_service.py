import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # Added a user agent to the header for scraping sites with mod_security turned on
    headers ={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text(separator='\n')
    return text