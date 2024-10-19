#!/usr/bin/python

import sys

from silero_tts.silero_tts import SileroTTS

from const.app_config import AppConfig
from const.app_paths import AppPaths
from const.exit_status import ExitStatus
from painter.painter import Painter
from wikiquote.wikiquote import Wikiquote


class App:
    def __init__(self):
        silero_tts_opts = {
            "device": "cpu",
            "language": "ru",
            "model_id": "v4_ru",
            "sample_rate": 48_000,
            "speaker": "baya"
        }

        self.painter = Painter()
        self.silero_tts = SileroTTS(**silero_tts_opts)
        self.wikiquote_scraper = Wikiquote()

    def run(self):
        try:
            author_link_scraper = self.wikiquote_scraper.scrape_authors()
            random_author = author_link_scraper.random_author_link()
            quote_scraper = self.wikiquote_scraper.scrape_quotes(random_author)
            random_quote = quote_scraper.get_random_quote()
            self.silero_tts.tts(random_quote, AppPaths.TTS_PATH.value)
            self.painter.write_text(random_quote)
            self.painter.save(AppConfig.IMG_PATH.value)
            sys.exit(ExitStatus.SUCCESS)
        except Exception as error:
            print(f"An unexpected error occurred: {error}")
            sys.exit(ExitStatus.FAIL)


if __name__ == "__main__":
    app = App()
    app.run()
