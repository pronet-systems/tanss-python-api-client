from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_phone_number_found_item import TnsPhoneNumberFoundItem
    from .tns_phone_number_found_type import TnsPhoneNumberFoundType

@dataclass
class TnsPhoneNumberIdentifyInfos(AdditionalDataHolder, Parsable):
    """
    This object contains methods of how a phone number could be assigned to a company or employee
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Determines how a phone number could be matched
    found_type: Optional[TnsPhoneNumberFoundType] = None
    # all possible matches
    items: Optional[list[TnsPhoneNumberFoundItem]] = None
    # Determines a source of a phone number which could be retrieved from a company or an employee
    result: Optional[TnsPhoneNumberFoundItem] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsPhoneNumberIdentifyInfos:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsPhoneNumberIdentifyInfos
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsPhoneNumberIdentifyInfos()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_phone_number_found_item import TnsPhoneNumberFoundItem
        from .tns_phone_number_found_type import TnsPhoneNumberFoundType

        from .tns_phone_number_found_item import TnsPhoneNumberFoundItem
        from .tns_phone_number_found_type import TnsPhoneNumberFoundType

        fields: dict[str, Callable[[Any], None]] = {
            "foundType": lambda n : setattr(self, 'found_type', n.get_enum_value(TnsPhoneNumberFoundType)),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(TnsPhoneNumberFoundItem)),
            "result": lambda n : setattr(self, 'result', n.get_object_value(TnsPhoneNumberFoundItem)),
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
        writer.write_enum_value("foundType", self.found_type)
        writer.write_collection_of_object_values("items", self.items)
        writer.write_object_value("result", self.result)
        writer.write_additional_data_value(self.additional_data)
    

