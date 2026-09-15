from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .templates_put_request_body_active_filter import TemplatesPutRequestBody_activeFilter
    from .templates_put_request_body_type import TemplatesPutRequestBody_type

@dataclass
class TemplatesPutRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Filter for including active, inactive, or all templates
    active_filter: Optional[TemplatesPutRequestBody_activeFilter] = None
    # Identifier of the company the templates are scoped to
    company_id: Optional[int] = None
    # Identifier of the customer contact the templates are scoped to
    customer_employee_id: Optional[int] = None
    # Identifier of the employee the templates are scoped to
    employee_id: Optional[int] = None
    # Whether the full template contents are loaded
    load_templates: Optional[bool] = None
    # Name filter for matching templates
    name: Optional[str] = None
    # Identifier of the ticket the templates relate to
    ticket_id: Optional[int] = None
    # Type of object the templates apply to
    type: Optional[TemplatesPutRequestBody_type] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TemplatesPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TemplatesPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TemplatesPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .templates_put_request_body_active_filter import TemplatesPutRequestBody_activeFilter
        from .templates_put_request_body_type import TemplatesPutRequestBody_type

        from .templates_put_request_body_active_filter import TemplatesPutRequestBody_activeFilter
        from .templates_put_request_body_type import TemplatesPutRequestBody_type

        fields: dict[str, Callable[[Any], None]] = {
            "activeFilter": lambda n : setattr(self, 'active_filter', n.get_enum_value(TemplatesPutRequestBody_activeFilter)),
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "customerEmployeeId": lambda n : setattr(self, 'customer_employee_id', n.get_int_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "loadTemplates": lambda n : setattr(self, 'load_templates', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "ticketId": lambda n : setattr(self, 'ticket_id', n.get_int_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(TemplatesPutRequestBody_type)),
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
        writer.write_enum_value("activeFilter", self.active_filter)
        writer.write_int_value("companyId", self.company_id)
        writer.write_int_value("customerEmployeeId", self.customer_employee_id)
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_bool_value("loadTemplates", self.load_templates)
        writer.write_str_value("name", self.name)
        writer.write_int_value("ticketId", self.ticket_id)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

