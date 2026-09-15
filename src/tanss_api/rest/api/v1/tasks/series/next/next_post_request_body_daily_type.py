from enum import Enum

class NextPostRequestBody_dailyType(str, Enum):
    NONE_ = "NONE",
    EVERY_X_DAYS = "EVERY_X_DAYS",
    EVERY_WORKINGDAY = "EVERY_WORKINGDAY",
    EVERY_X_MINUTES_IN_TIMEFRAME = "EVERY_X_MINUTES_IN_TIMEFRAME",

