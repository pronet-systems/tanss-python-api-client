from enum import Enum

class PropertiesPutRequestBody_context(str, Enum):
    TICKET_LIST = "TICKET_LIST",
    OWN_TICKETS = "OWN_TICKETS",
    CREATED_TICKETS = "CREATED_TICKETS",
    PROJECTS = "PROJECTS",

