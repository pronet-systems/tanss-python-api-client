from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.tns_portal_profile_type import TnsPortalProfileType
    from .profiles_post_request_body_items import ProfilesPostRequestBody_items

@dataclass
class ProfilesPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Portal-Profil (TnsPortalProfile ohne id/employeeId)
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The columns property
    columns: Optional[int] = None
    # The items property
    items: Optional[list[ProfilesPostRequestBody_items]] = None
    # The name property
    name: Optional[str] = None
    # The pos property
    pos: Optional[int] = None
    # The timeline property
    timeline: Optional[bool] = None
    # Typ eines Portal-Profils
    type: Optional[TnsPortalProfileType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProfilesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProfilesPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProfilesPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .....models.tns_portal_profile_type import TnsPortalProfileType
        from .profiles_post_request_body_items import ProfilesPostRequestBody_items

        from .....models.tns_portal_profile_type import TnsPortalProfileType
        from .profiles_post_request_body_items import ProfilesPostRequestBody_items

        fields: dict[str, Callable[[Any], None]] = {
            "columns": lambda n : setattr(self, 'columns', n.get_int_value()),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(ProfilesPostRequestBody_items)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "pos": lambda n : setattr(self, 'pos', n.get_int_value()),
            "timeline": lambda n : setattr(self, 'timeline', n.get_bool_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(TnsPortalProfileType)),
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
        writer.write_int_value("columns", self.columns)
        writer.write_collection_of_object_values("items", self.items)
        writer.write_str_value("name", self.name)
        writer.write_int_value("pos", self.pos)
        writer.write_bool_value("timeline", self.timeline)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

