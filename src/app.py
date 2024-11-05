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
        self.silero_tts = SileroTTS(
            device=TTSConfig.DEVICE.value,
            language=TTSConfig.LANGUAGE.value,
            model_id=TTSConfig.MODEL.value,
            sample_rate=TTSConfig.SAMPLE_RATE.value,
            speaker=TTSConfig.SPEAKER.value,
        )

        self.wikiquote = Wikiquote()

    def run(self):
        author_links = self.wikiquote.scrape_authors()
        author_link = author_links.random()
        (author, quotes) = self.wikiquote.scrape_quotes(author_link)
        quote = quotes.random()
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
