from enum import Enum

class PdfExportPostRequestBody_fileNameType(str, Enum):
    CUSTOMER_FIRST = "CUSTOMER_FIRST",
    INVOICE_FIRST = "INVOICE_FIRST",

