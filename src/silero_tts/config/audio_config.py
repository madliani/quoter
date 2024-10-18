import os
from enum import Enum


class AudioConfig(Enum):
    FILENAME = f"{os.path.expanduser("~")}/Downloads/tts.wav"
