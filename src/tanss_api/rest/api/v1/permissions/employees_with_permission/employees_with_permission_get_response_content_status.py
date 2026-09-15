from enum import Enum

class EmployeesWithPermissionGetResponse_content_status(str, Enum):
    HAS_PERMISSION = "HAS_PERMISSION",
    INHERITED_FROM_PACKAGE = "INHERITED_FROM_PACKAGE",
    NONE_ = "NONE",

