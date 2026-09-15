from enum import Enum

class PropertiesPostRequestBody_status(str, Enum):
    NEW = "NEW",
    REQUESTED = "REQUESTED",
    APPROVED = "APPROVED",
    DECLINED = "DECLINED",

