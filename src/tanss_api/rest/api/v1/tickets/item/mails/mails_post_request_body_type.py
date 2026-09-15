from enum import Enum

class MailsPostRequestBody_type(str, Enum):
    NORMAL = "NORMAL",
    REPLY = "REPLY",
    SEND_AGAIN = "SEND_AGAIN",
    FORWARD = "FORWARD",
    SEMI_AUTOMATE = "SEMI_AUTOMATE",

