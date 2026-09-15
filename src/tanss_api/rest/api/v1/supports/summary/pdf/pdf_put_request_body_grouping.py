from enum import Enum

class PdfPutRequestBody_grouping(str, Enum):
    DONT_GROUP = "DONT_GROUP",
    GROUP_BY_TICKETS = "GROUP_BY_TICKETS",
    GROUP_BY_COST_CENTER = "GROUP_BY_COST_CENTER",
    GROUP_BY_DEPARTMENT = "GROUP_BY_DEPARTMENT",

