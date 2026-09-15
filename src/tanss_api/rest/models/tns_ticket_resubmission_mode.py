from enum import Enum

class TnsTicketResubmissionMode(str, Enum):
    HIGHLIGHT_TICKET = "HIGHLIGHT_TICKET",
    CLOSE_TICKET = "CLOSE_TICKET",
    SEND_MAIL = "SEND_MAIL",
    SET_STATUS = "SET_STATUS",

