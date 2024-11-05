import random

from config.author_link_config import AuthorLinkConfig
from config.quote_config import QuoteConfig
from scraper.author_link_scraper import AuthorLinkScraper
from scraper.quote_scraper import QuoteScraper


class RandomQuoteScraper:
    def __init__(self):
        self.author_link_scraper = AuthorLinkScraper(AuthorLinkConfig)
        self.quote_scraper = QuoteScraper(QuoteConfig)

    def quote_with_author(self):
        author_links = self.author_link_scraper.scrape()
        author_link = random.choice(author_links)
        (author, quotes) = self.quote_scraper.scrape(author_link)
        quote = random.choice(quotes)

        return f"{quote}\n {author}"
