from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ticket_configuration_modified_within_timeframe import TicketConfiguration_modifiedWithinTimeframe

@dataclass
class TicketConfiguration(AdditionalDataHolder, Parsable):
    """
    query parameters for fetching a custom ticket list
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # fetch only ticket from these companies
    companies: Optional[list[int]] = None
    # fetch only ticket assigned to these departments
    departments: Optional[list[int]] = None
    # fetch only ticket with these ids
    ids: Optional[list[int]] = None
    # by default, only "open" tickets will be fetched. if "done" tickets shall be fetched as well, this has to be given here
    include_done_tickets: Optional[bool] = None
    # if set, will only fetch repair (or no repair) tickets
    is_repair: Optional[bool] = None
    # Number of tickets that shall be fetched (pagination)
    items_per_page: Optional[int] = None
    # fetch only ticket which were modified in given timeframe
    modified_within_timeframe: Optional[TicketConfiguration_modifiedWithinTimeframe] = None
    # don't fetch tickets assigned to these employees
    not_assigned_to_employees: Optional[list[int]] = None
    # Page number (pagination)
    page: Optional[int] = None
    # fetches only tickets of a given phase id
    phase_id: Optional[int] = None
    # fetches only tickets of this project
    project_id: Optional[int] = None
    # if set, will only fetch tickets of this remitter id
    remitter_id: Optional[int] = None
    # fetch only tickets assigned to these employees
    staff: Optional[list[int]] = None
    # fetch only ticket with these state ids
    states: Optional[list[int]] = None
    # fetch only ticket with these type ids
    types: Optional[list[int]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TicketConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TicketConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TicketConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ticket_configuration_modified_within_timeframe import TicketConfiguration_modifiedWithinTimeframe

        from .ticket_configuration_modified_within_timeframe import TicketConfiguration_modifiedWithinTimeframe

        fields: dict[str, Callable[[Any], None]] = {
            "companies": lambda n : setattr(self, 'companies', n.get_collection_of_primitive_values(int)),
            "departments": lambda n : setattr(self, 'departments', n.get_collection_of_primitive_values(int)),
            "ids": lambda n : setattr(self, 'ids', n.get_collection_of_primitive_values(int)),
            "includeDoneTickets": lambda n : setattr(self, 'include_done_tickets', n.get_bool_value()),
            "isRepair": lambda n : setattr(self, 'is_repair', n.get_bool_value()),
            "itemsPerPage": lambda n : setattr(self, 'items_per_page', n.get_int_value()),
            "modifiedWithinTimeframe": lambda n : setattr(self, 'modified_within_timeframe', n.get_object_value(TicketConfiguration_modifiedWithinTimeframe)),
            "notAssignedToEmployees": lambda n : setattr(self, 'not_assigned_to_employees', n.get_collection_of_primitive_values(int)),
            "page": lambda n : setattr(self, 'page', n.get_int_value()),
            "phaseId": lambda n : setattr(self, 'phase_id', n.get_int_value()),
            "projectId": lambda n : setattr(self, 'project_id', n.get_int_value()),
            "remitterId": lambda n : setattr(self, 'remitter_id', n.get_int_value()),
            "staff": lambda n : setattr(self, 'staff', n.get_collection_of_primitive_values(int)),
            "states": lambda n : setattr(self, 'states', n.get_collection_of_primitive_values(int)),
            "types": lambda n : setattr(self, 'types', n.get_collection_of_primitive_values(int)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_primitive_values("companies", self.companies)
        writer.write_collection_of_primitive_values("departments", self.departments)
        writer.write_collection_of_primitive_values("ids", self.ids)
        writer.write_bool_value("includeDoneTickets", self.include_done_tickets)
        writer.write_bool_value("isRepair", self.is_repair)
        writer.write_int_value("itemsPerPage", self.items_per_page)
        writer.write_object_value("modifiedWithinTimeframe", self.modified_within_timeframe)
        writer.write_collection_of_primitive_values("notAssignedToEmployees", self.not_assigned_to_employees)
        writer.write_int_value("page", self.page)
        writer.write_int_value("phaseId", self.phase_id)
        writer.write_int_value("projectId", self.project_id)
        writer.write_int_value("remitterId", self.remitter_id)
        writer.write_collection_of_primitive_values("staff", self.staff)
        writer.write_collection_of_primitive_values("states", self.states)
        writer.write_collection_of_primitive_values("types", self.types)
        writer.write_additional_data_value(self.additional_data)
    

