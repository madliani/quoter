import requests
from bs4 import BeautifulSoup


class QuoteScraper:
    def __init__(self, url):
        self._url_ = url

    def fetch(self):
        response = requests.get(self._url_, timeout=1)
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

    def scrape(self):
        html = self.fetch()

        return self.parse(html)
