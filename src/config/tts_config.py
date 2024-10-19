from enum import Enum


class TTSConfig(Enum):
    DEVICE = "cpu"
    LANGUAGE = "ru"
    MODEL = "v4_ru"
    SAMPLE_RATE = 48_000
    SPEAKER = "baya"
