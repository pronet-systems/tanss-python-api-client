from enum import Enum

class PutRequestBody_documentType(str, Enum):
    STANDARD = "STANDARD",
    BARCODE = "BARCODE",
    UPLOADED = "UPLOADED",
    KNOWLEDGE_BASE = "KNOWLEDGE_BASE",

