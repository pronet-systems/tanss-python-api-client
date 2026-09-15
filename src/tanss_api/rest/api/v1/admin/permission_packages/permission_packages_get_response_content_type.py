from enum import Enum

class PermissionPackagesGetResponse_content_type(str, Enum):
    TECHNICIAN = "TECHNICIAN",
    FREELANCER = "FREELANCER",
    RESTRICTED_USER = "RESTRICTED_USER",
    CUSTOMER = "CUSTOMER",

