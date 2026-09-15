from enum import Enum

class TnsDiscountedSupportTypeFilter(str, Enum):
    ALL = "ALL",
    ONLY_WITH_ADDITION = "ONLY_WITH_ADDITION",
    ONLY_WITH_DISCOUNT = "ONLY_WITH_DISCOUNT",
    ONLY_WITH_ZERO_PERCENT = "ONLY_WITH_ZERO_PERCENT",

