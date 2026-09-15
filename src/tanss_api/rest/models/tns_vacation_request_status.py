from enum import Enum

class TnsVacationRequestStatus(str, Enum):
    NEW = "NEW",
    REQUESTED = "REQUESTED",
    APPROVED = "APPROVED",
    DECLINED = "DECLINED",

