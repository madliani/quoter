from wikiquote.config.pages_config import PagesConfig
from wikiquote.scraper.author_scraper import AuthorScraper
from wikiquote.scraper.quote_scraper import QuoteScraper


class WikiquoteScraper:
    def scrape_authors(self):
        author_scraper = AuthorScraper(PagesConfig)
        author_scraper.scrape()

        return author_scraper

    def scrape_quotes(self, page):
        url = f"https://ru.wikiquote.org{page}"
        quote_scraper = QuoteScraper(url)
        quote_scraper.scrape()

        return quote_scraper
