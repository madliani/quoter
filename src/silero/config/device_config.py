import os
from enum import Enum


class DeviceConfig(Enum):
    DEVICE = "cpu"
    THREAD_NUMBER = os.cpu_count() or 2
