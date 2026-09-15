from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.tns_management_dashboard_visibility import TnsManagementDashboardVisibility
    from ......models.tns_management_dashboard_visibility_type import TnsManagementDashboardVisibilityType

@dataclass
class WithCollectionPutRequestBody(AdditionalDataHolder, Parsable):
    """
    Gelesene Keys der Collection
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Name (wird getrimmt, max. 100 Zeichen)
    name: Optional[str] = None
    # The visibilities property
    visibilities: Optional[list[TnsManagementDashboardVisibility]] = None
    # Sichtbarkeit einer Dashboard-Collection
    visibility_type: Optional[TnsManagementDashboardVisibilityType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WithCollectionPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WithCollectionPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WithCollectionPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ......models.tns_management_dashboard_visibility import TnsManagementDashboardVisibility
        from ......models.tns_management_dashboard_visibility_type import TnsManagementDashboardVisibilityType

        from ......models.tns_management_dashboard_visibility import TnsManagementDashboardVisibility
        from ......models.tns_management_dashboard_visibility_type import TnsManagementDashboardVisibilityType

        fields: dict[str, Callable[[Any], None]] = {
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "visibilities": lambda n : setattr(self, 'visibilities', n.get_collection_of_object_values(TnsManagementDashboardVisibility)),
            "visibilityType": lambda n : setattr(self, 'visibility_type', n.get_enum_value(TnsManagementDashboardVisibilityType)),
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
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("visibilities", self.visibilities)
        writer.write_enum_value("visibilityType", self.visibility_type)
        writer.write_additional_data_value(self.additional_data)
    

