#!/usr/bin/python

import logging
import sys
import traceback

from silero_tts.silero_tts import SileroTTS

from config.app_config import AppConfig
from config.tts_config import TTSConfig
from const.exit_status import ExitStatus
from wikiquote.wikiquote import Wikiquote


class App:
    def __init__(self):
        silero_tts_opts = {
            "device": TTSConfig.DEVICE.value,
            "language": TTSConfig.LANGUAGE.value,
            "model_id": TTSConfig.MODEL.value,
            "sample_rate": TTSConfig.SAMPLE_RATE.value,
            "speaker": TTSConfig.SPEAKER.value,
        }

        self.silero_tts = SileroTTS(**silero_tts_opts)
        self.wikiquote_scraper = Wikiquote()

    def run(self):
        try:
            author_link_scraper = self.wikiquote_scraper.scrape_authors()
            author_link = author_link_scraper.random_author_link()
            (author, quotes) = self.wikiquote_scraper.scrape_quotes(author_link)
            quote = quotes.random()
            quote_with_author = f"{quote}\n {author}"
            self.silero_tts.tts(quote_with_author, AppConfig.WAV_PATH)
        except Exception:
            logging.exception(traceback.format_exc())
            sys.exit(ExitStatus.FAIL)

        sys.exit(ExitStatus.SUCCESS)


if __name__ == "__main__":
    app = App()
    app.run()
