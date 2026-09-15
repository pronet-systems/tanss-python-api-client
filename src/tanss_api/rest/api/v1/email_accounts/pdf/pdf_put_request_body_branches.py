from enum import Enum

class PdfPutRequestBody_branches(str, Enum):
    COMPANY_ONLY = "COMPANY_ONLY",
    BRANCHES_ONLY = "BRANCHES_ONLY",
    COMPANY_AND_BRANCHES = "COMPANY_AND_BRANCHES",
    SPECIFIC_BRANCH = "SPECIFIC_BRANCH",

