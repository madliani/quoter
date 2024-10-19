#!/usr/bin/python

import os
import sys

from silero_tts.silero_tts import SileroTTS

from const.exit_status import ExitStatus
from painter.painter import Painter
from wikiquote.wikiquote import Wikiquote


class App:
    def run(self):
        silero_tts_opt = {
            "model_id": 'v4_ru',
            "language": 'ru',
            "speaker": 'baya',
            "sample_rate": 48_000,
            "device": 'cpu'
        }

        try:
            wikiquote_scraper = Wikiquote()
            silero_tts = SileroTTS(**silero_tts_opt)
            painter = Painter()
            author_scraper = wikiquote_scraper.scrape_authors()
            random_author = author_scraper.get_random_author()
            quote_scraper = wikiquote_scraper.scrape_quotes(random_author)
            random_quote = quote_scraper.get_random_quote()
            silero_tts.tts(random_quote, f"{
                           os.path.expanduser("~")}/Downloads/tts.wav")
            painter.write_text(random_quote)
            painter.save(f"{os.path.expanduser("~")}/Downloads/img.png")
            sys.exit(ExitStatus.SUCCESS)
        except Exception as error:
            print(f"An unexpected error occurred: {error}")
            sys.exit(ExitStatus.FAIL)


if __name__ == "__main__":
    app = App()
    app.run()
