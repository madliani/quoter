from enum import Enum

from const.app_paths import AppPaths


class FontConfig(Enum):
    PATH = f"{AppPaths.APP_DIR.value}/assets/fonts/LXGWWenKaiTC-Regular.ttf"
    SIZE = 15
