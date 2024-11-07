from typing import Self

import requests
from bs4 import BeautifulSoup

from config.author_link_config import AuthorLinkConfig


class AuthorLinkScraper:
    def __init__(self: Self, config: AuthorLinkConfig) -> None:
        self.__url = config.URL
        self.__category_word = config.CATEGORY_WORD

    def fetch(self: Self) -> str:
        response = requests.get(self.__url, timeout=1)
        response.raise_for_status()

        return response.text

    def parse(self: Self, html: str) -> list[str]:
        soup = BeautifulSoup(html, "lxml")
        author_link_elements = soup.select("div.mw-category-group ul li a")
        author_links = []

        for author_link_elem in author_link_elements:
            author_link = author_link_elem.get("href")

            if author_link and self.__category_word not in author_link:
                author_links.append(author_link)

        return author_links

    def scrape(self: Self) -> str:
        html = self.fetch()

        return self.parse(html)
