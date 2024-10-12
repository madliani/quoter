from wikiquote.printer.author_printer import AuthorPrinter
from wikiquote.printer.quote_printer import QuotePrinter


class WikiquotePrinter:
    def print_pages(self, pages_scraper):
        author_printer = AuthorPrinter(pages_scraper)
        author_printer.print_quotes()

    def pprint_pages(self, pages_scraper):
        author_printer = AuthorPrinter(pages_scraper)
        author_printer.pprint_quotes()

    def print_quotes(self, page_scraper):
        quote_printer = QuotePrinter(page_scraper)
        quote_printer.print_quotes()
