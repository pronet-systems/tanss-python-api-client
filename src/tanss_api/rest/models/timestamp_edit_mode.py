from enum import Enum

class TimestampEditMode(str, Enum):
    NONE_ = "NONE",
    MAY_REQUEST = "MAY_REQUEST",
    DIRECT_ACCESS = "DIRECT_ACCESS",

