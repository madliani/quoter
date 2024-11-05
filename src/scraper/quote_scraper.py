import requests
from bs4 import BeautifulSoup


class QuoteScraper:
    def __init__(self, config):
        self._base_url_ = config.BASE_URL

    def fetch(self, url):
        response = requests.get(url, timeout=1)
        response.raise_for_status()

        return response.text

    def parse(self, html):
        soup = BeautifulSoup(html, "lxml")
        title = soup.select_one("span.mw-page-title-main")
        quote_elements = soup.select("div.poem p")
        author = title.text
        quotes = []

        for quote_elem in quote_elements:
            quotes.append(quote_elem.text)

        return (author, quotes)

    def scrape(self, author_link):
        url = f"{self._base_url_}{author_link}"
        html = self.fetch(url)

        return self.parse(html)
