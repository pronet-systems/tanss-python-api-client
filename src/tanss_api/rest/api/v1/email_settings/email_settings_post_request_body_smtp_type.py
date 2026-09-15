from enum import Enum

class EmailSettingsPostRequestBody_smtpType(str, Enum):
    DEFAULT = "DEFAULT",
    GRAPH = "GRAPH",
    GMAIL = "GMAIL",
    AZURE = "AZURE",

