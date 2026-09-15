from enum import Enum

class PhasesPostRequestBody_clearanceMode(str, Enum):
    DEFAULT = "DEFAULT",
    DONT_CLEAR_SUPPORTS = "DONT_CLEAR_SUPPORTS",
    MAY_CLEAR_SUPPORTS = "MAY_CLEAR_SUPPORTS",

