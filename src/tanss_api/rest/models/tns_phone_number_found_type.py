from enum import Enum

class TnsPhoneNumberFoundType(str, Enum):
    NONE_ = "NONE",
    TOO_SHORT = "TOO_SHORT",
    COMPANY = "COMPANY",
    EMPLOYEE = "EMPLOYEE",
    EMPLOYEE_INACTIVE = "EMPLOYEE_INACTIVE",

