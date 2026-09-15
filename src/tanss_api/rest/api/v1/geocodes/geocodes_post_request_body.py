from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class GeocodesPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The accuracy property
    accuracy: Optional[int] = None
    # The companyId property
    company_id: Optional[int] = None
    # The latitude property
    latitude: Optional[float] = None
    # ID of the company or employee.
    link_id: Optional[int] = None
    # 2 = company, 3 = employee. If omitted/0, defaults to the calling user.
    link_type_id: Optional[int] = None
    # The longitude property
    longitude: Optional[float] = None
    # The statusCode property
    status_code: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GeocodesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GeocodesPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GeocodesPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "accuracy": lambda n : setattr(self, 'accuracy', n.get_int_value()),
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "latitude": lambda n : setattr(self, 'latitude', n.get_float_value()),
            "linkId": lambda n : setattr(self, 'link_id', n.get_int_value()),
            "linkTypeId": lambda n : setattr(self, 'link_type_id', n.get_int_value()),
            "longitude": lambda n : setattr(self, 'longitude', n.get_float_value()),
            "statusCode": lambda n : setattr(self, 'status_code', n.get_int_value()),
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
        writer.write_int_value("accuracy", self.accuracy)
        writer.write_int_value("companyId", self.company_id)
        writer.write_float_value("latitude", self.latitude)
        writer.write_int_value("linkId", self.link_id)
        writer.write_int_value("linkTypeId", self.link_type_id)
        writer.write_float_value("longitude", self.longitude)
        writer.write_int_value("statusCode", self.status_code)
        writer.write_additional_data_value(self.additional_data)
    

