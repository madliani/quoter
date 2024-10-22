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
            "speaker": TTSConfig.SPEAKER.value
        }

        self.silero_tts = SileroTTS(**silero_tts_opts)
        self.wikiquote_scraper = Wikiquote()

    def run(self):
        try:
            author_link_scraper = self.wikiquote_scraper.scrape_authors()
            author_link = author_link_scraper.random_author_link()
            quote_scraper = self.wikiquote_scraper.scrape_quotes(
                author_link)
            quote = quote_scraper.random_quote()
            author = quote_scraper.author()
            quote_with_author = f"{quote}\n {author}"
            self.silero_tts.tts(quote_with_author, AppConfig.TTS_PATH)
        except Exception as exc:
            logging.error(f"An unexpected error occurred: {exc}")
            traceback.print_exc()
            sys.exit(ExitStatus.FAIL)

        sys.exit(ExitStatus.SUCCESS)


if __name__ == "__main__":
    app = App()
    app.run()
