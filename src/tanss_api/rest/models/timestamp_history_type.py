from enum import Enum

class TimestampHistoryType(str, Enum):
    CREATED = "CREATED",
    UPDATED = "UPDATED",
    DELETED = "DELETED",

