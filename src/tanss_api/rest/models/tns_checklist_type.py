from enum import Enum

class TnsChecklistType(str, Enum):
    CHECKLIST = "CHECKLIST",
    TEMPLATE = "TEMPLATE",
    ADHOC = "ADHOC",

