from enum import Enum

class ChecklistPutRequestBody_type(str, Enum):
    CHECKLIST = "CHECKLIST",
    TEMPLATE = "TEMPLATE",
    ADHOC = "ADHOC",

