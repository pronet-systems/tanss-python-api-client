from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .with_company_post_request_body_assignments import WithCompanyPostRequestBody_assignments

@dataclass
class WithCompanyPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # For ASSIGNMENT-type entries.
    assignments: Optional[list[WithCompanyPostRequestBody_assignments]] = None
    # Definition id this entry belongs to.
    id: Optional[int] = None
    # The name property
    name: Optional[str] = None
    # DEFAULT, ASSIGNMENT, ASSIGNMENT_SERVICE, ASSIGNMENT_SERVICE_PASSWORD, ...
    type: Optional[str] = None
    # For value-type entries.
    value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WithCompanyPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WithCompanyPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WithCompanyPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .with_company_post_request_body_assignments import WithCompanyPostRequestBody_assignments

        from .with_company_post_request_body_assignments import WithCompanyPostRequestBody_assignments

        fields: dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(WithCompanyPostRequestBody_assignments)),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
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
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_str_value("name", self.name)
        writer.write_str_value("type", self.type)
        writer.write_str_value("value", self.value)
        writer.write_additional_data_value(self.additional_data)
    

