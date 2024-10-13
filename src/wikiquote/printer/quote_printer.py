class QuotePrinter:
    def __init__(self, page_scraper):
        self.page_scraper = page_scraper

    def print_all(self):
        author = self.page_scraper.get_author()
        quote_count = self.page_scraper.get_count()
        print(f"Список цитат ({author}) ({quote_count}):")
        print()

        for quote in self.page_scraper.get_quotes():
            print(quote)
