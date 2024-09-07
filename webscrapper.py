import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        titles = soup.find_all('h2')

        print("Article Titles:")
        for idx, title in enumerate(titles, start=1):
            print(f"{idx}. {title.get_text()}")
    else:
        print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")

website_url = 'https://www.youtube.com'

scrape_website(website_url)
