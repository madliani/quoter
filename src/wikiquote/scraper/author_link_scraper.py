import random

import requests
from bs4 import BeautifulSoup

from wikiquote.const.exception_message import ExceptionMessage


class AuthorLinkScraper:
    def __init__(self, config):
        self._url_ = config.BASE_URL
        self._category_word_ = config.CATEGORY_WORD
        self._author_links_ = []

    def fetch(self):
        response = requests.get(self._url_, timeout=1)
        response.raise_for_status()

        return response.text

    def parse(self, html):
        soup = BeautifulSoup(html, "lxml")
        author_link_elements = soup.select("div.mw-category-group ul li a")

        for author_link_elem in author_link_elements:
            link = author_link_elem.get("href")

            if link and self._category_word_ not in link:
                self._author_links_.append(link)

    def scrape(self):
        html = self.fetch()
        self.parse(html)

    def author_links(self):
        if len(self._author_links_) == 0:
            raise Exception(ExceptionMessage.NO_AUTHORS)

        yield from self._author_links_

    def author_link(self, index):
        if len(self._author_links_) == 0:
            raise Exception(ExceptionMessage.NO_AUTHORS)

        return self._author_links_[index]

    def random_author_link(self):
        if len(self._author_links_) == 0:
            raise Exception(ExceptionMessage.NO_AUTHORS)

        return random.choice(self._author_links_)

    def length(self):
        return len(self._author_links_)
