from enum import Enum

class NextPostRequestBody_monthlyType(str, Enum):
    NONE_ = "NONE",
    ON_DAY_EVERY_X_MONTH = "ON_DAY_EVERY_X_MONTH",
    ON_COUNTED_WEEKDAY_EVERY_X_MONTH = "ON_COUNTED_WEEKDAY_EVERY_X_MONTH",

