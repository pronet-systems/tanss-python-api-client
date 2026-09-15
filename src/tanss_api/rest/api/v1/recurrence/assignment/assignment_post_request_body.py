from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AssignmentPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Request body.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Optional identifier of an exclusion applied to this assignment.
    exclude_id: Optional[int] = None
    # Identifier of the linked entity the recurrence is assigned to.
    link_id: Optional[int] = None
    # Type of the linked entity the recurrence is assigned to.
    link_type_id: Optional[int] = None
    # Identifier of the recurrence rule this assignment belongs to.
    rule_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AssignmentPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AssignmentPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AssignmentPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "excludeId": lambda n : setattr(self, 'exclude_id', n.get_int_value()),
            "linkId": lambda n : setattr(self, 'link_id', n.get_int_value()),
            "linkTypeId": lambda n : setattr(self, 'link_type_id', n.get_int_value()),
            "ruleId": lambda n : setattr(self, 'rule_id', n.get_int_value()),
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
        writer.write_int_value("excludeId", self.exclude_id)
        writer.write_int_value("linkId", self.link_id)
        writer.write_int_value("linkTypeId", self.link_type_id)
        writer.write_int_value("ruleId", self.rule_id)
        writer.write_additional_data_value(self.additional_data)
    

