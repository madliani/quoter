import random

import requests
from bs4 import BeautifulSoup

from wikiquote.const.exception_message import ExceptionMessage


class AuthorLinkScraper:
    def __init__(self, config):
        self.__url__ = config.BASE_URL
        self.__category_word__ = config.CATEGORY_WORD
        self.__author_links__ = []

    def fetch(self):
        response = requests.get(self.__url__, timeout=1)
        response.raise_for_status()

        return response.text

    def parse(self, html):
        soup = BeautifulSoup(html, "lxml")
        author_link_elements = soup.select("div.mw-category-group ul li a")

        for author_link_elem in author_link_elements:
            link = author_link_elem.get("href")

            if link and self.__category_word__ not in link:
                self.__author_links__.append(link)

    def scrape(self):
        html = self.fetch()
        self.parse(html)

    def author_links(self):
        if len(self.__author_links__) == 0:
            raise Exception(ExceptionMessage.NO_AUTHORS)

        yield from self.__author_links__

    def author_link(self, index):
        if len(self.__author_links__) == 0:
            raise Exception(ExceptionMessage.NO_AUTHORS)

        return self.__author_links__[index]

    def random_author_link(self):
        if len(self.__author_links__) == 0:
            raise Exception(ExceptionMessage.NO_AUTHORS)

        return random.choice(self.__author_links__)

    def length(self):
        return len(self.__author_links__)
