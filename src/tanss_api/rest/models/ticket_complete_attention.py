from enum import Enum

class TicketComplete_attention(str, Enum):
    NO = "NO",
    YES = "YES",
    RESUBMISSION = "RESUBMISSION",
    MAIL = "MAIL",

