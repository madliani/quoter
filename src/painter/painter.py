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

    def write_text(self, text):
        font = ImageFont.truetype(
            FontConfig.PATH.value, FontConfig.SIZE.value)
        width, height = self.__draw__.textsize(text, font)
        x = (ImageConfig.WIDTH.value - width) / 2
        y = (ImageConfig.HEIGHT.value - height) / 2
        self.__draw__.text((x, y), text, TextConfig.COLOR, font)

    def save(self, path):
        self.__image__.save(path)
