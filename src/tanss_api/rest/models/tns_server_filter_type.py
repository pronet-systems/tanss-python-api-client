from enum import Enum

class TnsServerFilterType(str, Enum):
    PCS_ONLY = "PCS_ONLY",
    SERVERS_ONLY = "SERVERS_ONLY",
    SERVERS_AND_PCS = "SERVERS_AND_PCS",

