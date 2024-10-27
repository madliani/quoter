from wikiquote.collections.quote_list import QuoteList
from wikiquote.config.author_link_config import AuthorLinkConfig
from wikiquote.config.wikiquote_config import WikiquoteConfig
from wikiquote.scraper.author_link_scraper import AuthorLinkScraper
from wikiquote.scraper.quote_scraper import QuoteScraper


class Wikiquote:
    def scrape_authors(self):
        author_link_scraper = AuthorLinkScraper(AuthorLinkConfig)
        author_link_scraper.scrape()

        return author_link_scraper

    def scrape_quotes(self, page):
        url = f"{WikiquoteConfig.BASE_URL}{page}"
        quote_scraper = QuoteScraper(url)
        (author, quotes) = quote_scraper.scrape()
        quote_list = QuoteList(quotes)

        return (author, quote_list)
