from enum import Enum

class TnsDocumentTypeEnum(str, Enum):
    DOCUMENT = "DOCUMENT",
    KNOWLEDGE_BASE_ARTICLE = "KNOWLEDGE_BASE_ARTICLE",
    LINK = "LINK",
    FILE = "FILE",

