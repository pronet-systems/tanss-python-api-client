from enum import Enum

class TnsLLMProvider(str, Enum):
    OPEN_AI = "OPEN_AI",
    GEMINI = "GEMINI",
    TANSS_AI = "TANSS_AI",

