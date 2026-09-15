from enum import Enum

class TriggerPutRequestBody_checkMode(str, Enum):
    SHOW = "SHOW",
    SIMULATE = "SIMULATE",
    ESCALATE = "ESCALATE",

