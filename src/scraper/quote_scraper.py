from typing import Final, Self

import requests
from bs4 import BeautifulSoup

from config.quote_config import QuoteConfig
from error.title_not_found import TitleNotFoundError


class QuoteScraper:
    def __init__(self: Self, config: QuoteConfig) -> None:
        self.__base_url: Final = config.BASE_URL

    def __fetch(self: Self, url: str):
        response = requests.get(url, timeout=1)
        response.raise_for_status()

        return response.text

    def __parse_title(self: Self, soup: BeautifulSoup):
        title = soup.select_one("span.mw-page-title-main")

        if title is None:
            raise TitleNotFoundError()

        return title.text

    def __parse_quotes(self: Self, soup: BeautifulSoup):
        quote_elements = soup.select("div.poem p")
        quotes = []

        for quote_elem in quote_elements:
            quotes.append(quote_elem.text)

        return quotes

    def __parse(self: Self, html: str):
        soup = BeautifulSoup(html, "lxml")
        author = self.__parse_title(soup)
        quotes = self.__parse_quotes(soup)

        return author, quotes

    def scrape(self: Self, author_link: str):
        url = f"{self.__base_url}{author_link}"
        html = self.__fetch(url)

        return self.__parse(html)
