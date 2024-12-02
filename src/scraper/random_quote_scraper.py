import random
from typing import Final, Self

from config.author_link_config import AuthorLinkConfig
from config.quote_config import QuoteConfig
from scraper.author_link_scraper import AuthorLinkScraper
from scraper.quote_scraper import QuoteScraper


class RandomQuoteScraper:
    def __init__(self: Self) -> None:
        self.__author_link_scraper: Final = AuthorLinkScraper(AuthorLinkConfig)
        self.__quote_scraper: Final = QuoteScraper(QuoteConfig)

    def quote_with_author(self: Self) -> str:
        author_links = self.__author_link_scraper.scrape()
        author_link = random.choice(author_links)
        author, quotes = self.__quote_scraper.scrape(author_link)
        quote = random.choice(quotes)

        return f"{quote}\n {author}"
