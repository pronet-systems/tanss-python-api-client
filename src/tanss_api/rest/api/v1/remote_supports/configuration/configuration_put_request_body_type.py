from enum import Enum

class ConfigurationPutRequestBody_type(str, Enum):
    TEAMVIEWER = "TEAMVIEWER",
    FASTVIEWER = "FASTVIEWER",
    PCVISIT = "PCVISIT",
    GO2ASSIST = "GO2ASSIST",
    REMOTEDESKTOPMANAGER = "REMOTEDESKTOPMANAGER",
    ANYDESK = "ANYDESK",
    ISL = "ISL",

