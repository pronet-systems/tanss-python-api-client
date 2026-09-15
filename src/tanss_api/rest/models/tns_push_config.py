from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_push_device_type import TnsPushDeviceType

@dataclass
class TnsPushConfig(AdditionalDataHolder, Parsable):
    """
    Push-Konfiguration (Gerätetoken) eines Benutzers
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The apnsToken property
    apns_token: Optional[str] = None
    # The appVersion property
    app_version: Optional[str] = None
    # The deviceType property
    device_type: Optional[TnsPushDeviceType] = None
    # The fcmToken property
    fcm_token: Optional[str] = None
    # The id property
    id: Optional[int] = None
    # The lastResponse property
    last_response: Optional[int] = None
    # The userId property
    user_id: Optional[int] = None
    # Geräte-UUID (Pflicht beim Anlegen)
    uuid: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsPushConfig:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsPushConfig
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsPushConfig()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_push_device_type import TnsPushDeviceType

        from .tns_push_device_type import TnsPushDeviceType

        fields: dict[str, Callable[[Any], None]] = {
            "apnsToken": lambda n : setattr(self, 'apns_token', n.get_str_value()),
            "appVersion": lambda n : setattr(self, 'app_version', n.get_str_value()),
            "deviceType": lambda n : setattr(self, 'device_type', n.get_enum_value(TnsPushDeviceType)),
            "fcmToken": lambda n : setattr(self, 'fcm_token', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "lastResponse": lambda n : setattr(self, 'last_response', n.get_int_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_int_value()),
            "uuid": lambda n : setattr(self, 'uuid', n.get_str_value()),
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
        writer.write_str_value("apnsToken", self.apns_token)
        writer.write_str_value("appVersion", self.app_version)
        writer.write_enum_value("deviceType", self.device_type)
        writer.write_str_value("fcmToken", self.fcm_token)
        writer.write_int_value("id", self.id)
        writer.write_int_value("lastResponse", self.last_response)
        writer.write_int_value("userId", self.user_id)
        writer.write_str_value("uuid", self.uuid)
        writer.write_additional_data_value(self.additional_data)
    

