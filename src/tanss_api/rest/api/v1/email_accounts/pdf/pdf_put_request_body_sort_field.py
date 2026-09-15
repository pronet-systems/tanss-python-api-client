from enum import Enum

class PdfPutRequestBody_sortField(str, Enum):
    TYPE_NAME = "TYPE_NAME",
    DESCRIPTION = "DESCRIPTION",
    ASSIGNEE = "ASSIGNEE",
    LOGIN_NAME = "LOGIN_NAME",
    LOGIN_PASSWORD = "LOGIN_PASSWORD",
    EMAIL_ACCOUNTS = "EMAIL_ACCOUNTS",

