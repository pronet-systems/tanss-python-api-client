from enum import Enum

class TnsActiveFilterType(str, Enum):
    ACTIVE_ONLY = "ACTIVE_ONLY",
    INACTIVE_ONLY = "INACTIVE_ONLY",
    ACTIVE_AND_INACTIVE = "ACTIVE_AND_INACTIVE",

