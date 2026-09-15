from enum import Enum

class TnsMailReceiverMethod(str, Enum):
    TO = "TO",
    CC = "CC",
    BCC = "BCC",

