from wikiquote.printer.author_printer import AuthorPrinter
from wikiquote.printer.quote_printer import QuotePrinter


class WikiquotePrinter:
    def print_authors(self, pages_scraper):
        author_printer = AuthorPrinter(pages_scraper)
        author_printer.print_all()

    def pprint_authors(self, pages_scraper):
        author_printer = AuthorPrinter(pages_scraper)
        author_printer.pprint_all()

    def print_quotes(self, page_scraper):
        quote_printer = QuotePrinter(page_scraper)
        quote_printer.print_all()
