from enum import Enum

class TnsDeviceOwnageType(str, Enum):
    OWN = "OWN",
    FOREIGN = "FOREIGN",
    OWN_RENT = "OWN_RENT",
    FOREIGN_RENT = "FOREIGN_RENT",

