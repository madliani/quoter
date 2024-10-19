import os
from enum import StrEnum


class AppPaths(StrEnum):
    APP_DIR = os.getcwd()
    USER_DIR = os.path.expanduser("~")
