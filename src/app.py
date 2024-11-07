#!/usr/bin/python

import logging
import sys
import traceback
from typing import Self

from silero_tts.silero_tts import SileroTTS

from config.app_config import AppConfig
from config.tts_config import TTSConfig
from const.exit_status import ExitStatus
from scraper.random_quote_scraper import RandomQuoteScraper


class App:
    def __init__(self: Self) -> None:
        self.__silero_tts = SileroTTS(
            device=TTSConfig.DEVICE.value,
            language=TTSConfig.LANGUAGE.value,
            model_id=TTSConfig.MODEL.value,
            sample_rate=TTSConfig.SAMPLE_RATE.value,
            speaker=TTSConfig.SPEAKER.value,
        )
        self.quote_scraper = RandomQuoteScraper()

    def run(self: Self) -> None:
        quote_with_author = self.quote_scraper.quote_with_author()
        self.__silero_tts.tts(quote_with_author, AppConfig.WAV_PATH)


if __name__ == "__main__":
    try:
        app = App()
        app.run()
        sys.exit(ExitStatus.SUCCESS)
    except Exception:
        logging.exception(traceback.format_exc())
        sys.exit(ExitStatus.FAIL)
