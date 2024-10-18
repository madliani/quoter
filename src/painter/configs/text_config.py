import os
from enum import Enum


class TextConfig(Enum):
    COLOR = "black"
    FONT_PATH = f"{
        os.getcwd()}/assets/fonts/LXGWWenKaiTC-Regular.ttf"
    FONT_SIZE = 15
