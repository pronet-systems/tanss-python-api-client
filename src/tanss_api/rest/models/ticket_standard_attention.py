from enum import Enum

class TicketStandard_attention(str, Enum):
    NO = "NO",
    YES = "YES",
    RESUBMISSION = "RESUBMISSION",
    MAIL = "MAIL",

