from wikiquote.config.author_link_config import AuthorLinkConfig
from wikiquote.scraper.author_link_scraper import AuthorLinkScraper
from wikiquote.scraper.quote_scraper import QuoteScraper


class Wikiquote:
    def scrape_authors(self):
        author_link_scraper = AuthorLinkScraper(AuthorLinkConfig)
        author_link_scraper.scrape()

        return author_link_scraper

    def scrape_quotes(self, page):
        url = f"https://ru.wikiquote.org{page}"
        quote_scraper = QuoteScraper(url)
        quote_scraper.scrape()

        return quote_scraper
