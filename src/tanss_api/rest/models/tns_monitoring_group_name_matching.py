from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsMonitoringGroupNameMatching(AdditionalDataHolder, Parsable):
    """
    This object represents a "translation" between a monitoring group name and a specific company (or device)
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # id of the company for this monitoring group
    company_id: Optional[int] = None
    # name of the monitoring group.* You can use wildcards with a "/*" char, i.e. "Server XY -/*" uses all groups starting with "Server XY -"
    group_name: Optional[str] = None
    # LinkId of the assignment (if known)
    link_id: Optional[int] = None
    # LinkTypeId of the assignment (if known)
    link_type_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsMonitoringGroupNameMatching:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsMonitoringGroupNameMatching
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsMonitoringGroupNameMatching()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "groupName": lambda n : setattr(self, 'group_name', n.get_str_value()),
            "linkId": lambda n : setattr(self, 'link_id', n.get_int_value()),
            "linkTypeId": lambda n : setattr(self, 'link_type_id', n.get_int_value()),
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
        writer.write_str_value("groupName", self.group_name)
        writer.write_int_value("linkId", self.link_id)
        writer.write_int_value("linkTypeId", self.link_type_id)
        writer.write_additional_data_value(self.additional_data)
    

