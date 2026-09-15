from enum import Enum

class TnsTanssEventConfigurationConfirmedFilter(str, Enum):
    BOTH = "BOTH",
    ONLY_CONFIRMED = "ONLY_CONFIRMED",
    ONLY_UNCONFIRMED = "ONLY_UNCONFIRMED",

