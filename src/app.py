#!/usr/bin/python

import logging
import random
import sys
import traceback

from silero_tts.silero_tts import SileroTTS

from config.app_config import AppConfig
from config.author_link_config import AuthorLinkConfig
from config.quote_config import QuoteConfig
from config.tts_config import TTSConfig
from const.exit_status import ExitStatus
from scraper.author_link_scraper import AuthorLinkScraper
from scraper.quote_scraper import QuoteScraper


class App:
    def __init__(self):
        self.silero_tts = SileroTTS(
            device=TTSConfig.DEVICE.value,
            language=TTSConfig.LANGUAGE.value,
            model_id=TTSConfig.MODEL.value,
            sample_rate=TTSConfig.SAMPLE_RATE.value,
            speaker=TTSConfig.SPEAKER.value,
        )

    def run(self):
        author_links = AuthorLinkScraper(AuthorLinkConfig).scrape()
        author_link = random.choice(author_links)
        (author, quotes) = QuoteScraper(
            f"{QuoteConfig.BASE_URL}{author_link}"
        ).scrape()
        quote = random.choice(quotes)
        quote_with_author = f"{quote}\n {author}"
        self.silero_tts.tts(quote_with_author, AppConfig.WAV_PATH)
        sys.exit(ExitStatus.SUCCESS)


if __name__ == "__main__":
    try:
        app = App()
        app.run()
    except Exception:
        logging.exception(traceback.format_exc())
        sys.exit(ExitStatus.FAIL)
