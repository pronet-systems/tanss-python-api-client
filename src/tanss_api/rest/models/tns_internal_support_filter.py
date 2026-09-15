from enum import Enum

class TnsInternalSupportFilter(str, Enum):
    ALL = "ALL",
    ONLY_INTERNAL = "ONLY_INTERNAL",
    ONLY_EXTERNAL = "ONLY_EXTERNAL",

