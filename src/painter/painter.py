import nltk
from PIL import Image, ImageDraw, ImageFont

from painter.configs.font_config import FontConfig
from painter.configs.image_config import ImageConfig
from painter.configs.text_config import TextConfig


class Painter:
    def __init__(self):
        size = (ImageConfig.WIDTH.value, ImageConfig.HEIGHT.value)
        self.__image__ = Image.new(ImageConfig.MODE.value,
                                   size, ImageConfig.COLOR.value)
        self.__draw__ = ImageDraw.Draw(self.__image__)

    def __wrap_text__(self, text, count):
        tokens = nltk.word_tokenize(text)
        splitted_tokens = []
        wrapped_tokens = []

        for i in range(0, len(tokens), count):
            splitted_tokens.append(tokens[i:i + count])

        for splitted_token in splitted_tokens:
            wrapped_tokens.extend(splitted_token)
            wrapped_tokens.append("\n")

        return " ".join(wrapped_tokens)

    def write_text(self, text):
        texts = self.__wrap_text__(text, 5)
        font = ImageFont.truetype(FontConfig.PATH.value, FontConfig.SIZE.value)

        for i, text in enumerate(texts):
            width, height = self.__draw__.textsize(text, font)
            x = (ImageConfig.WIDTH.value - width) / 2
            y = (ImageConfig.HEIGHT.value - height) / 2 + i * 10
            self.__draw__.text((x, y), text, TextConfig.COLOR, font)

    def save(self, path):
        self.__image__.save(path)
