from enum import Enum

from const.app_paths import AppPaths


class AppConfig(Enum):
    IMG_PATH = f"{AppPaths.USER_DIR.value}/Downloads/img.png"
    TTS_PATH = f"{AppPaths.USER_DIR.value}/Downloads/tts.wav"
