from enum import Enum

class EmailSettingsPostRequestBody_pop3Type(str, Enum):
    DEFAULT = "DEFAULT",
    GRAPH = "GRAPH",
    GMAIL = "GMAIL",
    AZURE = "AZURE",

