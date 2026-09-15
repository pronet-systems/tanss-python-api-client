from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsManagementDashboardVisibility(AdditionalDataHolder, Parsable):
    """
    Sichtbarkeit einer Collection für einen Mitarbeiter oder eine Abteilung
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # ID der Collection
    collection_id: Optional[int] = None
    # ID des Mitarbeiters bzw. der Abteilung
    link_id: Optional[int] = None
    # Verknüpfungstyp (3 = Mitarbeiter, 34 = Abteilung)
    link_type_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsManagementDashboardVisibility:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsManagementDashboardVisibility
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsManagementDashboardVisibility()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "collectionId": lambda n : setattr(self, 'collection_id', n.get_int_value()),
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
        writer.write_int_value("collectionId", self.collection_id)
        writer.write_int_value("linkId", self.link_id)
        writer.write_int_value("linkTypeId", self.link_type_id)
        writer.write_additional_data_value(self.additional_data)
    

