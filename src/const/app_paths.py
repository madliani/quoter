import os
from enum import Enum


class AppPaths(Enum):
    APP_DIR = os.getcwd()
    USER_DIR = os.path.expanduser("~")
