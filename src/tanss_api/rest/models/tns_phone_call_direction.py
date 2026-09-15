from enum import Enum

class TnsPhoneCallDirection(str, Enum):
    INTERNAL = "INTERNAL",
    INCOMING = "INCOMING",
    OUTGOING = "OUTGOING",

