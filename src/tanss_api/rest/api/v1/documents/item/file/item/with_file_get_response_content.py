from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class WithFileGetResponse_content(AdditionalDataHolder, Parsable):
    """
    object carrying the temporary download URL/token.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The expires property
    expires: Optional[int] = None
    # The token property
    token: Optional[str] = None
    # The url property
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WithFileGetResponse_content:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WithFileGetResponse_content
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WithFileGetResponse_content()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "expires": lambda n : setattr(self, 'expires', n.get_int_value()),
            "token": lambda n : setattr(self, 'token', n.get_str_value()),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
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
        writer.write_int_value("expires", self.expires)
        writer.write_str_value("token", self.token)
        writer.write_str_value("url", self.url)
        writer.write_additional_data_value(self.additional_data)
    

