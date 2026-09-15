from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_timeframe import TnsTimeframe

@dataclass
class TnsTokenLogConfiguration(AdditionalDataHolder, Parsable):
    """
    Filter für das API-Token-Protokoll (TnsTokenLogConfiguration).
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Describes a timeframe (from / to)
    creation_timeframe: Optional[TnsTimeframe] = None
    # Describes a timeframe (from / to)
    expiration_timeframe: Optional[TnsTimeframe] = None
    # Externes Programm (Enum TnsExtPrograms; NONE = kein Filter).
    ext_program_filter: Optional[str] = None
    # The includeExpired property
    include_expired: Optional[bool] = None
    # The itemsPerPage property
    items_per_page: Optional[int] = None
    # The omitTotalCount property
    omit_total_count: Optional[bool] = None
    # The page property
    page: Optional[int] = None
    # The searchText property
    search_text: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsTokenLogConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsTokenLogConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsTokenLogConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_timeframe import TnsTimeframe

        from .tns_timeframe import TnsTimeframe

        fields: dict[str, Callable[[Any], None]] = {
            "creationTimeframe": lambda n : setattr(self, 'creation_timeframe', n.get_object_value(TnsTimeframe)),
            "expirationTimeframe": lambda n : setattr(self, 'expiration_timeframe', n.get_object_value(TnsTimeframe)),
            "extProgramFilter": lambda n : setattr(self, 'ext_program_filter', n.get_str_value()),
            "includeExpired": lambda n : setattr(self, 'include_expired', n.get_bool_value()),
            "itemsPerPage": lambda n : setattr(self, 'items_per_page', n.get_int_value()),
            "omitTotalCount": lambda n : setattr(self, 'omit_total_count', n.get_bool_value()),
            "page": lambda n : setattr(self, 'page', n.get_int_value()),
            "searchText": lambda n : setattr(self, 'search_text', n.get_str_value()),
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
        writer.write_object_value("creationTimeframe", self.creation_timeframe)
        writer.write_object_value("expirationTimeframe", self.expiration_timeframe)
        writer.write_str_value("extProgramFilter", self.ext_program_filter)
        writer.write_bool_value("includeExpired", self.include_expired)
        writer.write_int_value("itemsPerPage", self.items_per_page)
        writer.write_bool_value("omitTotalCount", self.omit_total_count)
        writer.write_int_value("page", self.page)
        writer.write_str_value("searchText", self.search_text)
        writer.write_additional_data_value(self.additional_data)
    

