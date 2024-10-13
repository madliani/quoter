import requests
from bs4 import BeautifulSoup


class QuoteScraper:
    def __init__(self, url):
        self.url = url
        self.author = None
        self.quotes = []

    def fetch(self):
        response = requests.get(self.url, timeout=1)
        response.raise_for_status()

        return response.text

    def parse(self, html):
        soup = BeautifulSoup(html, "lxml")
        title = soup.select_one("span.mw-page-title-main")
        quote_paragraphs = soup.select("div.poem p")
        self.author = title.text

        for quote_paragraph in quote_paragraphs:
            self.quotes.append(quote_paragraph.text)

    def scrape(self):
        html = self.fetch()
        self.parse(html)

    def get_quotes(self):
        yield from self.quotes

    def get_quote(self, index):
        if len(self.quotes) > 0:
            return self.quotes[index]

        raise Exception("No quote!")

    def get_author(self):
        return self.author

    def get_count(self):
        return len(self.quotes)
