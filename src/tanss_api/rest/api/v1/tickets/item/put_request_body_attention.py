from enum import Enum

class PutRequestBody_attention(str, Enum):
    NO = "NO",
    YES = "YES",
    RESUBMISSION = "RESUBMISSION",
    MAIL = "MAIL",

