from enum import Enum

class TnsChecklistItemVarType(str, Enum):
    INPUT = "INPUT",
    MULTISELECT = "MULTISELECT",
    PASSWORD = "PASSWORD",
    OUTPUT = "OUTPUT",
    ERP_SELECTION = "ERP_SELECTION",

