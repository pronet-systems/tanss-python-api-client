from enum import Enum

class TnsTanssEventConfigurationSeenFilter(str, Enum):
    BOTH = "BOTH",
    ONLY_SEEN = "ONLY_SEEN",
    ONLY_UNSEEN = "ONLY_UNSEEN",

