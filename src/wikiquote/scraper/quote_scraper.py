import random

import requests
from bs4 import BeautifulSoup

from wikiquote.const.exception_message import ExceptionMessage


class QuoteScraper:
    def __init__(self, url):
        self.__url__ = url
        self.__author__ = None
        self.__quotes__ = []

    def fetch(self):
        response = requests.get(self.__url__, timeout=1)
        response.raise_for_status()

        return response.text

    def parse(self, html):
        soup = BeautifulSoup(html, "lxml")
        title = soup.select_one("span.mw-page-title-main")
        quote_elements = soup.select("div.poem p")
        self.__author__ = title.text

        for quote_elem in quote_elements:
            self.__quotes__.append(quote_elem.text)

    def scrape(self):
        html = self.fetch()
        self.parse(html)

    def quotes(self):
        if len(self.__quotes__) == 0:
            raise Exception(ExceptionMessage.NO_QUOTES)

        yield from self.__quotes__

    def quote(self, index):
        if len(self.__quotes__) == 0:
            raise Exception(ExceptionMessage.NO_QUOTES)

        return self.__quotes__[index]

    def author(self):
        return self.__author__

    def random_quote(self):
        if len(self.__quotes__) == 0:
            raise Exception(ExceptionMessage.NO_QUOTES)

        return random.choice(self.__quotes__)

    def length(self):
        return len(self.__quotes__)
