from enum import Enum

class TnsMailStatus(str, Enum):
    UNSENT = "UNSENT",
    SENT = "SENT",
    ERROR = "ERROR",
    RECEIVED = "RECEIVED",

