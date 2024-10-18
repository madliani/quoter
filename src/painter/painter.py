from PIL import Image, ImageDraw, ImageFont

from painter.configs.image_config import ImageConfig
from painter.configs.text_config import TextConfig


class Painter:
    def __init__(self):
        size = (ImageConfig.WIDTH.value, ImageConfig.HEIGHT.value)
        self.image = Image.new(ImageConfig.MODE.value,
                               size, ImageConfig.COLOR.value)
        self.draw = ImageDraw.Draw(self.image)

    def write_text(self, text):
        font = ImageFont.truetype(
            TextConfig.FONT_PATH.value, TextConfig.FONT_SIZE.value)
        width, height = self.draw.textsize(text, font)
        x = (ImageConfig.WIDTH.value - width) / 2
        y = (ImageConfig.HEIGHT.value - height) / 2
        self.draw.text((x, y), text,
                       TextConfig.COLOR.value, font)

    def save(self, path):
        self.image.save(path)
