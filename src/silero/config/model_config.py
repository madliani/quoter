import os
from enum import Enum


class ModelConfig(Enum):
    FILE = f"{os.path.expanduser("~")}/Models/model.pt"
    URL = "https://models.silero.ai/models/tts/ru/v4_ru.pt"
