from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsTicketSearchResult(AdditionalDataHolder, Parsable):
    """
    object containing a found ticket with all associated infos
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # assigned to department id, name is given in the "linked entities". Note the spelling — that is how the API returns the field.
    assigned_to_dpeartment_id: Optional[int] = None
    # assigned to employee id, name is given in the "linked entities"
    assigned_to_employee_id: Optional[int] = None
    # id of the company, name is given in the "linked entities"
    company_id: Optional[int] = None
    # content of the ticket. This is cut by the number of "previewContentMaxChars" as defined in the dearch config
    content: Optional[str] = None
    # the external ticket id (if given)
    ext_ticket_id: Optional[str] = None
    # id of the ticket
    id: Optional[str] = None
    # status id, name is given in the "linked entities"
    status_id: Optional[int] = None
    # title of the ticket
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsTicketSearchResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsTicketSearchResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsTicketSearchResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "assignedToDpeartmentId": lambda n : setattr(self, 'assigned_to_dpeartment_id', n.get_int_value()),
            "assignedToEmployeeId": lambda n : setattr(self, 'assigned_to_employee_id', n.get_int_value()),
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "extTicketId": lambda n : setattr(self, 'ext_ticket_id', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "statusId": lambda n : setattr(self, 'status_id', n.get_int_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_int_value("assignedToDpeartmentId", self.assigned_to_dpeartment_id)
        writer.write_int_value("assignedToEmployeeId", self.assigned_to_employee_id)
        writer.write_int_value("companyId", self.company_id)
        writer.write_str_value("content", self.content)
        writer.write_str_value("extTicketId", self.ext_ticket_id)
        writer.write_str_value("id", self.id)
        writer.write_int_value("statusId", self.status_id)
        writer.write_str_value("title", self.title)
        writer.write_additional_data_value(self.additional_data)
    

