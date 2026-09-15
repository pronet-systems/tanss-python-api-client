from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .check_put_request_body_type import CheckPutRequestBody_type

@dataclass
class CheckPutRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Access token used for the TeamViewer provider.
    access_token: Optional[str] = None
    # Hostname or address of the remote maintenance server.
    host: Optional[str] = None
    # License identifier used for the AnyDesk provider.
    license_id: Optional[str] = None
    # Password for authenticating against the remote maintenance service.
    password: Optional[str] = None
    # Network port used to reach the remote maintenance server.
    port: Optional[int] = None
    # Remote maintenance provider to check against.
    type: Optional[CheckPutRequestBody_type] = None
    # Username for authenticating against the remote maintenance service.
    username: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CheckPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CheckPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CheckPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .check_put_request_body_type import CheckPutRequestBody_type

        from .check_put_request_body_type import CheckPutRequestBody_type

        fields: dict[str, Callable[[Any], None]] = {
            "accessToken": lambda n : setattr(self, 'access_token', n.get_str_value()),
            "host": lambda n : setattr(self, 'host', n.get_str_value()),
            "licenseId": lambda n : setattr(self, 'license_id', n.get_str_value()),
            "password": lambda n : setattr(self, 'password', n.get_str_value()),
            "port": lambda n : setattr(self, 'port', n.get_int_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(CheckPutRequestBody_type)),
            "username": lambda n : setattr(self, 'username', n.get_str_value()),
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
        writer.write_str_value("accessToken", self.access_token)
        writer.write_str_value("host", self.host)
        writer.write_str_value("licenseId", self.license_id)
        writer.write_str_value("password", self.password)
        writer.write_int_value("port", self.port)
        writer.write_enum_value("type", self.type)
        writer.write_str_value("username", self.username)
        writer.write_additional_data_value(self.additional_data)
    

