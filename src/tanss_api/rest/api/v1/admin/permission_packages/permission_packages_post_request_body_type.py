from enum import Enum

class PermissionPackagesPostRequestBody_type(str, Enum):
    TECHNICIAN = "TECHNICIAN",
    FREELANCER = "FREELANCER",
    RESTRICTED_USER = "RESTRICTED_USER",
    CUSTOMER = "CUSTOMER",

