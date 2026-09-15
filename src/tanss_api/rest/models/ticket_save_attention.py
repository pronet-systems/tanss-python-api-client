from enum import Enum

class TicketSave_attention(str, Enum):
    NO = "NO",
    YES = "YES",
    RESUBMISSION = "RESUBMISSION",
    MAIL = "MAIL",

