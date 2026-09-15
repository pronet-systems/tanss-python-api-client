from enum import Enum

class TimestampState(str, Enum):
    ON = "ON",
    OFF = "OFF",
    PAUSE_START = "PAUSE_START",
    PAUSE_END = "PAUSE_END",

