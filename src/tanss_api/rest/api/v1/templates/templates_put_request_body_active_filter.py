from enum import Enum

class TemplatesPutRequestBody_activeFilter(str, Enum):
    ACTIVE_ONLY = "ACTIVE_ONLY",
    INACTIVE_ONLY = "INACTIVE_ONLY",
    ACTIVE_AND_INACTIVE = "ACTIVE_AND_INACTIVE",

