from enum import Enum

class EscalationsPostRequestBody_triggerLogicOperator(str, Enum):
    AND_ = "AND",
    OR_ = "OR",
    NOT_ = "NOT",
    NOT_AND = "NOT_AND",
    GREATER_THAN = "GREATER_THAN",
    GREATER_OR_EQUAL = "GREATER_OR_EQUAL",
    LESS_THAN = "LESS_THAN",
    LESS_OR_EQUAL = "LESS_OR_EQUAL",
    EQUALS = "EQUALS",

