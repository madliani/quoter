#!/usr/bin/python

import sys

from silero_tts.silero_tts import SileroTTS

from const.app_config import AppConfig
from const.app_paths import AppPaths
from const.exit_status import ExitStatus
from const.tts_config import TTSConfig
from painter.painter import Painter
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

        self.painter = Painter()
        self.silero_tts = SileroTTS(**silero_tts_opts)
        self.wikiquote_scraper = Wikiquote()

    def run(self):
        try:
            author_link_scraper = self.wikiquote_scraper.scrape_authors()
            author_link = author_link_scraper.random_author_link()
            quote_scraper = self.wikiquote_scraper.scrape_quotes(
                author_link)
            quote = quote_scraper.random_quote()
            self.silero_tts.tts(quote, AppPaths.TTS_PATH.value)
            self.painter.write_text(quote)
            self.painter.save(AppConfig.IMG_PATH.value)
            sys.exit(ExitStatus.SUCCESS)
        except Exception as error:
            print(f"An unexpected error occurred: {error}")
            sys.exit(ExitStatus.FAIL)


if __name__ == "__main__":
    app = App()
    app.run()
