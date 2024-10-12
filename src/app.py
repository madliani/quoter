#!/usr/bin/python

import sys

from const.exit_status import ExitStatus
from wikiquote.printer.wikiquote_printer import WikiquotePrinter
from wikiquote.scraper.wikiquote_scraper import WikiquoteScraper


class App:
    def run(self):
        try:
            wikiquote_scraper = WikiquoteScraper()
            wikiquote_printer = WikiquotePrinter()
            author_scraper = wikiquote_scraper.scrape_authors()
            random_author = author_scraper.get_random_author()
            quote_scraper = wikiquote_scraper.scrape_quotes(random_author)
            wikiquote_printer.print_quotes(quote_scraper)
            sys.exit(ExitStatus.SUCCESS)
        except Exception as error:
            print(f"An unexpected error occurred: {error}")
            sys.exit(ExitStatus.FAIL)


if __name__ == "__main__":
    app = App()
    app.run()
