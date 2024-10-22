from enum import StrEnum

from const.app_paths import AppPaths


class AppConfig(StrEnum):
    IMG_PATH = f"{AppPaths.USER_DIR}/Downloads/img.png"
    NLTK_DATA_PATH = f"{AppPaths.APP_DIR}/models"
    TTS_PATH = f"{AppPaths.USER_DIR}/Downloads/tts.wav"
