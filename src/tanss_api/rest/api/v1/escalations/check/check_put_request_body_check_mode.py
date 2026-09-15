from enum import Enum

class CheckPutRequestBody_checkMode(str, Enum):
    SHOW = "SHOW",
    SIMULATE = "SIMULATE",
    ESCALATE = "ESCALATE",

