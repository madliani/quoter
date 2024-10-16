#!/usr/bin/python

import sys

from const.exit_status import ExitStatus
from silero_tts.silero_tts import SileroTTS
from wikiquote.wikiquote import Wikiquote


class App:
    def run(self):
        try:
            wikiquote_scraper = Wikiquote()
            silero_tts = SileroTTS()
            author_scraper = wikiquote_scraper.scrape_authors()
            random_author = author_scraper.get_random_author()
            quote_scraper = wikiquote_scraper.scrape_quotes(random_author)
            silero_tts.tts(quote_scraper.get_random_quote())
            sys.exit(ExitStatus.SUCCESS)
        except Exception as error:
            print(f"An unexpected error occurred: {error}")
            sys.exit(ExitStatus.FAIL)


if __name__ == "__main__":
    app = App()
    app.run()
