from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class FiltersPutRequestBody(AdditionalDataHolder, Parsable):
    """
    Request body.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Identifier of the employee who owns this panel filter
    employee_id: Optional[int] = None
    # Whether the panel is hidden
    hidden: Optional[bool] = None
    # Whether completed tickets are included
    include_done_tickets: Optional[bool] = None
    # Whether project tickets are included
    include_projects: Optional[bool] = None
    # Whether sub-tickets are included
    include_sub_tickets: Optional[bool] = None
    # Whether tickets in waiting states are included
    include_waiting_states: Optional[bool] = None
    # Whether to show only overdue tickets
    only_overdue_tickets: Optional[bool] = None
    # Whether to show only the current user's own tickets
    only_own_tickets: Optional[bool] = None
    # Restrict to tickets from this employee identifier
    only_tickets_from_employee: Optional[int] = None
    # Whether to show only tickets matching the user's own roles
    only_tickets_with_own_roles: Optional[bool] = None
    # Identifier of the ticket board panel this filter belongs to
    panel_id: Optional[int] = None
    # Sort order position of the panel
    rank: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FiltersPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FiltersPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FiltersPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "hidden": lambda n : setattr(self, 'hidden', n.get_bool_value()),
            "includeDoneTickets": lambda n : setattr(self, 'include_done_tickets', n.get_bool_value()),
            "includeProjects": lambda n : setattr(self, 'include_projects', n.get_bool_value()),
            "includeSubTickets": lambda n : setattr(self, 'include_sub_tickets', n.get_bool_value()),
            "includeWaitingStates": lambda n : setattr(self, 'include_waiting_states', n.get_bool_value()),
            "onlyOverdueTickets": lambda n : setattr(self, 'only_overdue_tickets', n.get_bool_value()),
            "onlyOwnTickets": lambda n : setattr(self, 'only_own_tickets', n.get_bool_value()),
            "onlyTicketsFromEmployee": lambda n : setattr(self, 'only_tickets_from_employee', n.get_int_value()),
            "onlyTicketsWithOwnRoles": lambda n : setattr(self, 'only_tickets_with_own_roles', n.get_bool_value()),
            "panelId": lambda n : setattr(self, 'panel_id', n.get_int_value()),
            "rank": lambda n : setattr(self, 'rank', n.get_int_value()),
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
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_bool_value("hidden", self.hidden)
        writer.write_bool_value("includeDoneTickets", self.include_done_tickets)
        writer.write_bool_value("includeProjects", self.include_projects)
        writer.write_bool_value("includeSubTickets", self.include_sub_tickets)
        writer.write_bool_value("includeWaitingStates", self.include_waiting_states)
        writer.write_bool_value("onlyOverdueTickets", self.only_overdue_tickets)
        writer.write_bool_value("onlyOwnTickets", self.only_own_tickets)
        writer.write_int_value("onlyTicketsFromEmployee", self.only_tickets_from_employee)
        writer.write_bool_value("onlyTicketsWithOwnRoles", self.only_tickets_with_own_roles)
        writer.write_int_value("panelId", self.panel_id)
        writer.write_int_value("rank", self.rank)
        writer.write_additional_data_value(self.additional_data)
    

