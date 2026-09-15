from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .delete_post_request_body_day import DeletePostRequestBody_day

@dataclass
class DeletePostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Identifier of the company the additional charge applies to
    company_id: Optional[int] = None
    # Identifier of the maintenance contract the charge belongs to
    contract_id: Optional[int] = None
    # Weekday or special day the charge applies to
    day: Optional[DeletePostRequestBody_day] = None
    # Identifier of the linked entity the charge is attached to
    link_id: Optional[int] = None
    # Type of the linked entity the charge is attached to
    link_type_id: Optional[int] = None
    # Sequential number of the charge within its group
    number: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeletePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeletePostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeletePostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .delete_post_request_body_day import DeletePostRequestBody_day

        from .delete_post_request_body_day import DeletePostRequestBody_day

        fields: dict[str, Callable[[Any], None]] = {
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "contractId": lambda n : setattr(self, 'contract_id', n.get_int_value()),
            "day": lambda n : setattr(self, 'day', n.get_enum_value(DeletePostRequestBody_day)),
            "linkId": lambda n : setattr(self, 'link_id', n.get_int_value()),
            "linkTypeId": lambda n : setattr(self, 'link_type_id', n.get_int_value()),
            "number": lambda n : setattr(self, 'number', n.get_int_value()),
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
        writer.write_int_value("companyId", self.company_id)
        writer.write_int_value("contractId", self.contract_id)
        writer.write_enum_value("day", self.day)
        writer.write_int_value("linkId", self.link_id)
        writer.write_int_value("linkTypeId", self.link_type_id)
        writer.write_int_value("number", self.number)
        writer.write_additional_data_value(self.additional_data)
    

