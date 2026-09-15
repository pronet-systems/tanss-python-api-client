from enum import Enum

class NextPostRequestBody_seriesType(str, Enum):
    DAILY = "DAILY",
    WEEKLY = "WEEKLY",
    MONTHLY = "MONTHLY",
    YEARLY = "YEARLY",
    INDIVIDUALLY = "INDIVIDUALLY",

