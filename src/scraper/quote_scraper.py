from typing import Final, Self

import requests
from bs4 import BeautifulSoup

from config.quote_config import QuoteConfig

type ParseResult = (str, Final[list[str]])


class QuoteScraper:
    def __init__(self: Self, config: QuoteConfig) -> None:
        self.__base_url: Final = config.BASE_URL

    def __fetch(self: Self, url: str) -> str:
        response: Final = requests.get(url, timeout=1)
        response.raise_for_status()

        return response.text

    def __parse(self: Self, html: str) -> ParseResult:
        soup = BeautifulSoup(html, "lxml")
        title = soup.select_one("span.mw-page-title-main")
        quote_elements = soup.select("div.poem p")
        author = title.text
        quotes = []

        for quote_elem in quote_elements:
            quotes.append(quote_elem.text)

        return (author, quotes)

    def scrape(self: Self, author_link: str) -> ParseResult:
        url = f"{self.__base_url}{author_link}"
        html = self.__fetch(url)

        return self.__parse(html)
