#!/usr/bin/python

import logging
import sys
import traceback
from typing import Final, Self

from const.exit_status import ExitStatus
from scraper.random_quote_scraper import RandomQuoteScraper


class App:
    def __init__(self: Self) -> None:
        self.__quote_scraper: Final = RandomQuoteScraper()

    def run(self: Self) -> None:
        quote_with_author = self.__quote_scraper.quote_with_author()
        print(quote_with_author)


if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR)

    try:
        app: Final = App()
        app.run()
    except Exception:
        logging.exception(traceback.format_exc())
        sys.exit(ExitStatus.FAIL)

    sys.exit(ExitStatus.SUCCESS)
