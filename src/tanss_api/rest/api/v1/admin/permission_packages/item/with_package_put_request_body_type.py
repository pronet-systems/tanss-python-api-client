from enum import Enum

class WithPackagePutRequestBody_type(str, Enum):
    TECHNICIAN = "TECHNICIAN",
    FREELANCER = "FREELANCER",
    RESTRICTED_USER = "RESTRICTED_USER",
    CUSTOMER = "CUSTOMER",

