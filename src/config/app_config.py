from enum import StrEnum

from const.app_paths import AppPaths


class AppConfig(StrEnum):
    TTS_PATH = f"{AppPaths.USER_DIR}/Downloads/tts.wav"
