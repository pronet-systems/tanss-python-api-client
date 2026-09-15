from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_tanss_license_fetched_item import TnsTanssLicenseFetchedItem

@dataclass
class TnsTanssLicenseFetchResponse(AdditionalDataHolder, Parsable):
    """
    Ergebnis des Lizenzabgleichs (TnsTanssLicenseFetchResponse).
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The added property
    added: Optional[list[int]] = None
    # The fetched property
    fetched: Optional[list[TnsTanssLicenseFetchedItem]] = None
    # The removed property
    removed: Optional[list[int]] = None
    # The updated property
    updated: Optional[list[int]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsTanssLicenseFetchResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsTanssLicenseFetchResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsTanssLicenseFetchResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_tanss_license_fetched_item import TnsTanssLicenseFetchedItem

        from .tns_tanss_license_fetched_item import TnsTanssLicenseFetchedItem

        fields: dict[str, Callable[[Any], None]] = {
            "added": lambda n : setattr(self, 'added', n.get_collection_of_primitive_values(int)),
            "fetched": lambda n : setattr(self, 'fetched', n.get_collection_of_object_values(TnsTanssLicenseFetchedItem)),
            "removed": lambda n : setattr(self, 'removed', n.get_collection_of_primitive_values(int)),
            "updated": lambda n : setattr(self, 'updated', n.get_collection_of_primitive_values(int)),
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
        writer.write_collection_of_primitive_values("added", self.added)
        writer.write_collection_of_object_values("fetched", self.fetched)
        writer.write_collection_of_primitive_values("removed", self.removed)
        writer.write_collection_of_primitive_values("updated", self.updated)
        writer.write_additional_data_value(self.additional_data)
    

