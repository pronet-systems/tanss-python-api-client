from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_browser_item_additional_data import TnsBrowserItemAdditionalData

@dataclass
class TnsBrowserItem(AdditionalDataHolder, Parsable):
    """
    Element des Kategorie-Browsers; derzeit nur für Softwarelizenz-Kategorien genutzt.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Zusatzdaten eines Browser-Elements; für SOFTWARELICENSE die Standardwerte der Softwarelizenz-Kategorie (vgl. TnsSoftwarelicenseType).
    additional_data_property: Optional[TnsBrowserItemAdditionalData] = None
    # Anzahl untergeordneter Elemente (bei Einzelabruf 0)
    count: Optional[int] = None
    # ID des Elements (bei POST ignoriert)
    id: Optional[int] = None
    # Typ des Elements (z. B. CATEGORY)
    item_type: Optional[str] = None
    # Untergeordnete Elemente (bei Einzelabruf null)
    items: Optional[list[TnsBrowserItem]] = None
    # Linktyp (bei Einzelabruf null)
    link_type: Optional[str] = None
    # Name des Elements
    name: Optional[str] = None
    # ID der übergeordneten Kategorie
    previous_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsBrowserItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsBrowserItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsBrowserItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_browser_item_additional_data import TnsBrowserItemAdditionalData

        from .tns_browser_item_additional_data import TnsBrowserItemAdditionalData

        fields: dict[str, Callable[[Any], None]] = {
            "additionalData": lambda n : setattr(self, 'additional_data_property', n.get_object_value(TnsBrowserItemAdditionalData)),
            "count": lambda n : setattr(self, 'count', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "itemType": lambda n : setattr(self, 'item_type', n.get_str_value()),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(TnsBrowserItem)),
            "linkType": lambda n : setattr(self, 'link_type', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "previousId": lambda n : setattr(self, 'previous_id', n.get_int_value()),
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
        writer.write_object_value("additionalData", self.additional_data_property)
        writer.write_int_value("count", self.count)
        writer.write_int_value("id", self.id)
        writer.write_str_value("itemType", self.item_type)
        writer.write_collection_of_object_values("items", self.items)
        writer.write_str_value("linkType", self.link_type)
        writer.write_str_value("name", self.name)
        writer.write_int_value("previousId", self.previous_id)
        writer.write_additional_data_value(self.additional_data)
    

