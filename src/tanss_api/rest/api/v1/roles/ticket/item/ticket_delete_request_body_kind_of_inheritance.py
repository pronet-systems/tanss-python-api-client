from enum import Enum

class TicketDeleteRequestBody_kindOfInheritance(str, Enum):
    DEFAULT = "DEFAULT",
    REVOKED_IN_PROJECT = "REVOKED_IN_PROJECT",
    REVOKED_IN_SUB_TICKET = "REVOKED_IN_SUB_TICKET",
    OVERWRITTEN_IN_SUB_TICKET = "OVERWRITTEN_IN_SUB_TICKET",

