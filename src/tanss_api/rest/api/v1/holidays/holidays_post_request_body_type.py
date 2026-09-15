from enum import Enum

class HolidaysPostRequestBody_type(str, Enum):
    ALL_DAY = "ALL_DAY",
    FORENOON = "FORENOON",
    AFTERNOON = "AFTERNOON",

