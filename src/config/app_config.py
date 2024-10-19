from enum import StrEnum

from const.app_paths import AppPaths


class AppConfig(StrEnum):
    IMG_PATH = f"{AppPaths.USER_DIR}/Downloads/img.png"
    TTS_PATH = f"{AppPaths.USER_DIR}/Downloads/tts.wav"
