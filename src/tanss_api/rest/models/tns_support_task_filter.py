from enum import Enum

class TnsSupportTaskFilter(str, Enum):
    ONLY_TASK_SUPPORTS = "ONLY_TASK_SUPPORTS",
    NO_TASK_SUPPORTS = "NO_TASK_SUPPORTS",

