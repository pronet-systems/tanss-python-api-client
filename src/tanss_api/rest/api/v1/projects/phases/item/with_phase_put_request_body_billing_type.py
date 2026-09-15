from enum import Enum

class WithPhasePutRequestBody_billingType(str, Enum):
    DEFAULT = "DEFAULT",
    TICKET_MUST_BE_CLOSED = "TICKET_MUST_BE_CLOSED",
    ALL_TICKETS_MUST_BE_CLOSED = "ALL_TICKETS_MUST_BE_CLOSED",

