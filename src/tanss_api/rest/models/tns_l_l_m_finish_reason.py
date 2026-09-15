from enum import Enum

class TnsLLMFinishReason(str, Enum):
    STOP = "STOP",
    MAX_TOKENS_EXCEEDED = "MAX_TOKENS_EXCEEDED",
    OTHER = "OTHER",

