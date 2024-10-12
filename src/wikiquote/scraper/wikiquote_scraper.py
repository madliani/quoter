import os
from concurrent.futures import ThreadPoolExecutor

from wikiquote.config.pages_config import PagesConfig
from wikiquote.scraper.author_scraper import AuthorScraper
from wikiquote.scraper.quote_scraper import QuoteScraper


class WikiquoteScraper:
    def scrape_authors(self):
        cpu_count = os.cpu_count()
        author_scraper = AuthorScraper(PagesConfig)

        with ThreadPoolExecutor(max_workers=cpu_count) as thread_pool:
            scrape_future = thread_pool.submit(author_scraper.scrape)
            scrape_future.result()

        return author_scraper

    def scrape_quotes(self, page):
        url = f"https://ru.wikiquote.org{page}"
        quote_scraper = QuoteScraper(url)
        quote_scraper.scrape()

        return quote_scraper
