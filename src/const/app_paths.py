import os
from enum import Enum


class AppPaths(Enum):
    APP_DIR = os.getcwd()
    USER_DIR = os.path.expanduser("~")
    IMG_PATH = f"{USER_DIR}/Downloads/img.png"
    TTS_PATH = f"{USER_DIR}/Downloads/tts.wav"
