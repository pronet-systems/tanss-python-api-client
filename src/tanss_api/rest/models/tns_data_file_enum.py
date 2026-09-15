from enum import Enum

class TnsDataFileEnum(str, Enum):
    OK = "OK",
    TOO_BIG = "TOO_BIG",
    ERROR = "ERROR",
    EMPTY = "EMPTY",

