from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .client_post_request_body_days import ClientPostRequestBody_days

@dataclass
class ClientPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Working hours per weekday, keyed by day of the week
    days: Optional[ClientPostRequestBody_days] = None
    # Unique identifier of the working hours model
    id: Optional[int] = None
    # Display name of the working hours model
    name: Optional[str] = None
    # Number of companies using this working hours model
    related_companies_count: Optional[int] = None
    # Number of contracts using this working hours model
    related_contracts_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ClientPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ClientPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ClientPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .client_post_request_body_days import ClientPostRequestBody_days

        from .client_post_request_body_days import ClientPostRequestBody_days

        fields: dict[str, Callable[[Any], None]] = {
            "days": lambda n : setattr(self, 'days', n.get_object_value(ClientPostRequestBody_days)),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "relatedCompaniesCount": lambda n : setattr(self, 'related_companies_count', n.get_int_value()),
            "relatedContractsCount": lambda n : setattr(self, 'related_contracts_count', n.get_int_value()),
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
        writer.write_object_value("days", self.days)
        writer.write_str_value("name", self.name)
        writer.write_int_value("relatedCompaniesCount", self.related_companies_count)
        writer.write_int_value("relatedContractsCount", self.related_contracts_count)
        writer.write_additional_data_value(self.additional_data)
    

