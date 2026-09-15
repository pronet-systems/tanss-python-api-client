from enum import Enum

class TnsMailTransportSecurityType(str, Enum):
    NONE_ = "NONE",
    SSL = "SSL",
    TLS = "TLS",

