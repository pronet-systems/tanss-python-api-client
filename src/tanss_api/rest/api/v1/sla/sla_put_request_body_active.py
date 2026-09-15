from enum import Enum

class SlaPutRequestBody_active(str, Enum):
    ACTIVE_ONLY = "ACTIVE_ONLY",
    INACTIVE_ONLY = "INACTIVE_ONLY",
    ACTIVE_AND_INACTIVE = "ACTIVE_AND_INACTIVE",

