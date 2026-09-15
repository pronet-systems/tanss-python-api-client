from enum import Enum

class PinnedPostRequestBody_type(str, Enum):
    NONE_ = "NONE",
    COMMENT = "COMMENT",
    MAIL = "MAIL",
    SUPPORT = "SUPPORT",
    GIT_COMMIT = "GIT_COMMIT",

