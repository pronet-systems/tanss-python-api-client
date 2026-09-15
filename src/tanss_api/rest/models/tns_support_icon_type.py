from enum import Enum

class TnsSupportIconType(str, Enum):
    STANDARD = "STANDARD",
    REMOTE = "REMOTE",
    NOT_CHARGED = "NOT_CHARGED",
    ERP = "ERP",
    INSTALLATION_FEE = "INSTALLATION_FEE",
    FULLSERVICE = "FULLSERVICE",
    CONTRACT = "CONTRACT",
    PREPAID = "PREPAID",

