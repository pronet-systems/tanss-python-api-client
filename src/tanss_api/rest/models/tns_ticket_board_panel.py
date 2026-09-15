from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_ticket_board_panel_company import TnsTicketBoardPanelCompany
    from .tns_ticket_board_panel_department import TnsTicketBoardPanelDepartment
    from .tns_ticket_board_panel_employee import TnsTicketBoardPanelEmployee
    from .tns_ticket_board_panel_filter import TnsTicketBoardPanelFilter
    from .tns_ticket_board_panel_tag import TnsTicketBoardPanelTag
    from .tns_ticket_board_panel_ticket_status import TnsTicketBoardPanelTicketStatus
    from .tns_ticket_board_panel_ticket_type import TnsTicketBoardPanelTicketType
    from .tns_ticket_board_panel_type import TnsTicketBoardPanelType
    from .tns_ticket_board_panel_visibility import TnsTicketBoardPanelVisibility
    from .tns_ticket_board_register_type import TnsTicketBoardRegisterType

@dataclass
class TnsTicketBoardPanel(AdditionalDataHolder, Parsable):
    """
    Ticket board panel
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Array of panel companies
    companies: Optional[list[TnsTicketBoardPanelCompany]] = None
    # Array of panel departments
    departments: Optional[list[TnsTicketBoardPanelDepartment]] = None
    # Panel employee id
    employee_id: Optional[int] = None
    # Array of panel employees
    employees: Optional[list[TnsTicketBoardPanelEmployee]] = None
    # Per-employee filter of a ticket board panel. The include/only flags live here, not on thepanel itself.
    filter: Optional[TnsTicketBoardPanelFilter] = None
    # Panel id
    id: Optional[int] = None
    # Panel name
    name: Optional[str] = None
    # Panel type
    panel_type: Optional[TnsTicketBoardPanelType] = None
    # Panel project id
    project_id: Optional[int] = None
    # Register type
    register_type: Optional[TnsTicketBoardRegisterType] = None
    # Array of panel tags
    tags: Optional[list[TnsTicketBoardPanelTag]] = None
    # Array of panel ticket status
    ticket_status: Optional[list[TnsTicketBoardPanelTicketStatus]] = None
    # Array of panel ticket types
    ticket_types: Optional[list[TnsTicketBoardPanelTicketType]] = None
    # Panel visibility
    visibility: Optional[TnsTicketBoardPanelVisibility] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsTicketBoardPanel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsTicketBoardPanel
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsTicketBoardPanel()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_ticket_board_panel_company import TnsTicketBoardPanelCompany
        from .tns_ticket_board_panel_department import TnsTicketBoardPanelDepartment
        from .tns_ticket_board_panel_employee import TnsTicketBoardPanelEmployee
        from .tns_ticket_board_panel_filter import TnsTicketBoardPanelFilter
        from .tns_ticket_board_panel_tag import TnsTicketBoardPanelTag
        from .tns_ticket_board_panel_ticket_status import TnsTicketBoardPanelTicketStatus
        from .tns_ticket_board_panel_ticket_type import TnsTicketBoardPanelTicketType
        from .tns_ticket_board_panel_type import TnsTicketBoardPanelType
        from .tns_ticket_board_panel_visibility import TnsTicketBoardPanelVisibility
        from .tns_ticket_board_register_type import TnsTicketBoardRegisterType

        from .tns_ticket_board_panel_company import TnsTicketBoardPanelCompany
        from .tns_ticket_board_panel_department import TnsTicketBoardPanelDepartment
        from .tns_ticket_board_panel_employee import TnsTicketBoardPanelEmployee
        from .tns_ticket_board_panel_filter import TnsTicketBoardPanelFilter
        from .tns_ticket_board_panel_tag import TnsTicketBoardPanelTag
        from .tns_ticket_board_panel_ticket_status import TnsTicketBoardPanelTicketStatus
        from .tns_ticket_board_panel_ticket_type import TnsTicketBoardPanelTicketType
        from .tns_ticket_board_panel_type import TnsTicketBoardPanelType
        from .tns_ticket_board_panel_visibility import TnsTicketBoardPanelVisibility
        from .tns_ticket_board_register_type import TnsTicketBoardRegisterType

        fields: dict[str, Callable[[Any], None]] = {
            "companies": lambda n : setattr(self, 'companies', n.get_collection_of_object_values(TnsTicketBoardPanelCompany)),
            "departments": lambda n : setattr(self, 'departments', n.get_collection_of_object_values(TnsTicketBoardPanelDepartment)),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "employees": lambda n : setattr(self, 'employees', n.get_collection_of_object_values(TnsTicketBoardPanelEmployee)),
            "filter": lambda n : setattr(self, 'filter', n.get_object_value(TnsTicketBoardPanelFilter)),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "panelType": lambda n : setattr(self, 'panel_type', n.get_enum_value(TnsTicketBoardPanelType)),
            "projectId": lambda n : setattr(self, 'project_id', n.get_int_value()),
            "registerType": lambda n : setattr(self, 'register_type', n.get_enum_value(TnsTicketBoardRegisterType)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_object_values(TnsTicketBoardPanelTag)),
            "ticketStatus": lambda n : setattr(self, 'ticket_status', n.get_collection_of_object_values(TnsTicketBoardPanelTicketStatus)),
            "ticketTypes": lambda n : setattr(self, 'ticket_types', n.get_collection_of_object_values(TnsTicketBoardPanelTicketType)),
            "visibility": lambda n : setattr(self, 'visibility', n.get_enum_value(TnsTicketBoardPanelVisibility)),
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
        writer.write_collection_of_object_values("companies", self.companies)
        writer.write_collection_of_object_values("departments", self.departments)
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_collection_of_object_values("employees", self.employees)
        writer.write_object_value("filter", self.filter)
        writer.write_str_value("name", self.name)
        writer.write_enum_value("panelType", self.panel_type)
        writer.write_int_value("projectId", self.project_id)
        writer.write_enum_value("registerType", self.register_type)
        writer.write_collection_of_object_values("tags", self.tags)
        writer.write_collection_of_object_values("ticketStatus", self.ticket_status)
        writer.write_collection_of_object_values("ticketTypes", self.ticket_types)
        writer.write_enum_value("visibility", self.visibility)
        writer.write_additional_data_value(self.additional_data)
    

