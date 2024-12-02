from typing import Final, Self

import requests
from bs4 import BeautifulSoup

from config.author_link_config import AuthorLinkConfig


class AuthorLinkScraper:
    def __init__(self: Self, config: type[AuthorLinkConfig]) -> None:
        self.__url: Final = config.URL
        self.__category_word: Final = config.CATEGORY_WORD

    def __fetch(self: Self):
        response = requests.get(self.__url, timeout=1)
        response.raise_for_status()

        return response.text

    def __parse(self: Self, html: str):
        soup = BeautifulSoup(html, "lxml")
        author_link_elements = soup.select("div.mw-category-group ul li a")
        author_links = []

        for author_link_elem in author_link_elements:
            author_link = author_link_elem.get("href")

            if author_link and self.__category_word not in author_link:
                author_links.append(author_link)

        return author_links

    def scrape(self: Self):
        html = self.__fetch()

        return self.__parse(html)
