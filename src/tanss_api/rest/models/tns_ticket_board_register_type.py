from enum import Enum

class TnsTicketBoardRegisterType(str, Enum):
    NONE_ = "NONE",
    COMPANY = "COMPANY",
    EMPLOYEE = "EMPLOYEE",
    DEPARTMENT = "DEPARTMENT",
    TAG = "TAG",
    TICKET_TYPE = "TICKET_TYPE",
    TICKET_STATUS = "TICKET_STATUS",
    PROJECT_PHASE = "PROJECT_PHASE",

