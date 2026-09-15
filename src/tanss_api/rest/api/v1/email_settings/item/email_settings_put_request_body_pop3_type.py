from enum import Enum

class EmailSettingsPutRequestBody_pop3Type(str, Enum):
    DEFAULT = "DEFAULT",
    GRAPH = "GRAPH",
    GMAIL = "GMAIL",
    AZURE = "AZURE",

