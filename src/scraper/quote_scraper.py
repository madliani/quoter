from typing import Self

import requests
from bs4 import BeautifulSoup

from config.quote_config import QuoteConfig


class QuoteScraper:
    def __init__(self: Self, config: QuoteConfig) -> None:
        self._base_url_ = config.BASE_URL

    def fetch(self: Self, url: str) -> str:
        response = requests.get(url, timeout=1)
        response.raise_for_status()

        return response.text

    def parse(self: Self, html: str) -> (str, list[str]):
        soup = BeautifulSoup(html, "lxml")
        title = soup.select_one("span.mw-page-title-main")
        quote_elements = soup.select("div.poem p")
        author = title.text
        quotes = []

        for quote_elem in quote_elements:
            quotes.append(quote_elem.text)

        return (author, quotes)

    def scrape(self: Self, author_link: str) -> str:
        url = f"{self._base_url_}{author_link}"
        html = self.fetch(url)

        return self.parse(html)
