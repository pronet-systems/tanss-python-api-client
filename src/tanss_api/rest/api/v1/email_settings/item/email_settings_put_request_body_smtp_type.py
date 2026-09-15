from enum import Enum

class EmailSettingsPutRequestBody_smtpType(str, Enum):
    DEFAULT = "DEFAULT",
    GRAPH = "GRAPH",
    GMAIL = "GMAIL",
    AZURE = "AZURE",

