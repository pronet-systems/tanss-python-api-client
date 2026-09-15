from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsJwtJwk(AdditionalDataHolder, Parsable):
    """
    Öffentlicher RSA-Schlüssel im JWK-Format.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The alg property
    alg: Optional[str] = None
    # The e property
    e: Optional[str] = None
    # The kid property
    kid: Optional[str] = None
    # The kty property
    kty: Optional[str] = None
    # The n property
    n: Optional[str] = None
    # The use property
    use: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsJwtJwk:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsJwtJwk
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsJwtJwk()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "alg": lambda n : setattr(self, 'alg', n.get_str_value()),
            "e": lambda n : setattr(self, 'e', n.get_str_value()),
            "kid": lambda n : setattr(self, 'kid', n.get_str_value()),
            "kty": lambda n : setattr(self, 'kty', n.get_str_value()),
            "n": lambda n : setattr(self, 'n', n.get_str_value()),
            "use": lambda n : setattr(self, 'use', n.get_str_value()),
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
        writer.write_str_value("alg", self.alg)
        writer.write_str_value("e", self.e)
        writer.write_str_value("kid", self.kid)
        writer.write_str_value("kty", self.kty)
        writer.write_str_value("n", self.n)
        writer.write_str_value("use", self.use)
        writer.write_additional_data_value(self.additional_data)
    

