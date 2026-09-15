from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .passwords_put_request_body_link_type import PasswordsPutRequestBody_linkType

@dataclass
class PasswordsPutRequestBody(AdditionalDataHolder, Parsable):
    """
    Request body.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Free-text comment for the password entry
    comment: Optional[str] = None
    # Unique identifier of the stored password entry
    id: Optional[int] = None
    # Identifier of the linked entity the password belongs to
    link_id: Optional[int] = None
    # Type of entity the password entry is linked to
    link_type: Optional[PasswordsPutRequestBody_linkType] = None
    # The stored password value
    password: Optional[str] = None
    # Identifier of the password type/category
    password_type_id: Optional[int] = None
    # User name associated with the password entry
    user_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PasswordsPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PasswordsPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PasswordsPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .passwords_put_request_body_link_type import PasswordsPutRequestBody_linkType

        from .passwords_put_request_body_link_type import PasswordsPutRequestBody_linkType

        fields: dict[str, Callable[[Any], None]] = {
            "comment": lambda n : setattr(self, 'comment', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "linkId": lambda n : setattr(self, 'link_id', n.get_int_value()),
            "linkType": lambda n : setattr(self, 'link_type', n.get_enum_value(PasswordsPutRequestBody_linkType)),
            "password": lambda n : setattr(self, 'password', n.get_str_value()),
            "passwordTypeId": lambda n : setattr(self, 'password_type_id', n.get_int_value()),
            "userName": lambda n : setattr(self, 'user_name', n.get_str_value()),
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
        writer.write_str_value("comment", self.comment)
        writer.write_int_value("linkId", self.link_id)
        writer.write_enum_value("linkType", self.link_type)
        writer.write_str_value("password", self.password)
        writer.write_int_value("passwordTypeId", self.password_type_id)
        writer.write_str_value("userName", self.user_name)
        writer.write_additional_data_value(self.additional_data)
    

