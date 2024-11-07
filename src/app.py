#!/usr/bin/python

import logging
import sys
import traceback

from silero_tts.silero_tts import SileroTTS

from config.app_config import AppConfig
from config.tts_config import TTSConfig
from const.exit_status import ExitStatus
from scraper.random_quote_scraper import RandomQuoteScraper


class App:
    def __init__(self):
        self.silero_tts = SileroTTS(
            device=TTSConfig.DEVICE.value,
            language=TTSConfig.LANGUAGE.value,
            model_id=TTSConfig.MODEL.value,
            sample_rate=TTSConfig.SAMPLE_RATE.value,
            speaker=TTSConfig.SPEAKER.value,
        )
        self.quote_scraper = RandomQuoteScraper()

    def run(self):
        quote_with_author = self.quote_scraper.quote_with_author()
        self.silero_tts.tts(quote_with_author, AppConfig.WAV_PATH)


if __name__ == "__main__":
    try:
        app = App()
        app.run()
        sys.exit(ExitStatus.SUCCESS)
    except Exception:
        logging.exception(traceback.format_exc())
        sys.exit(ExitStatus.FAIL)
