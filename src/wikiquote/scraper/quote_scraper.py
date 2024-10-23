import random

import requests
from bs4 import BeautifulSoup

from wikiquote.const.exception_message import ExceptionMessage


class QuoteScraper:
    def __init__(self, url):
        self._url_ = url
        self._author_ = None
        self._quotes_ = []

    def fetch(self):
        response = requests.get(self._url_, timeout=1)
        response.raise_for_status()

        return response.text

    def parse(self, html):
        soup = BeautifulSoup(html, "lxml")
        title = soup.select_one("span.mw-page-title-main")
        quote_elements = soup.select("div.poem p")
        self._author_ = title.text

        for quote_elem in quote_elements:
            self._quotes_.append(quote_elem.text)

    def scrape(self):
        html = self.fetch()
        self.parse(html)

    def quotes(self):
        if len(self._quotes_) == 0:
            raise Exception(ExceptionMessage.NO_QUOTES)

        yield from self._quotes_

    def quote(self, index):
        if len(self._quotes_) == 0:
            raise Exception(ExceptionMessage.NO_QUOTES)

        return self._quotes_[index]

    def author(self):
        if self._author_ is None:
            raise Exception(ExceptionMessage.NO_AUTHOR)

        return self._author_

    def random_quote(self):
        if len(self._quotes_) == 0:
            raise Exception(ExceptionMessage.NO_QUOTES)

        return random.choice(self._quotes_)

    def length(self):
        return len(self._quotes_)
