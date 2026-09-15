from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class RemoteSupportsPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The comment property
    comment: Optional[str] = None
    # The companyId property
    company_id: Optional[int] = None
    # The deviceId property
    device_id: Optional[str] = None
    # The deviceName property
    device_name: Optional[str] = None
    # The employeeId property
    employee_id: Optional[int] = None
    # The endTime property
    end_time: Optional[int] = None
    # The fee property
    fee: Optional[float] = None
    # The linkId property
    link_id: Optional[int] = None
    # The linkTypeId property
    link_type_id: Optional[int] = None
    # The remoteMaintenanceId property
    remote_maintenance_id: Optional[str] = None
    # The startTime property
    start_time: Optional[int] = None
    # The ticketId property
    ticket_id: Optional[int] = None
    # >= 1000, muss ein Eintrag aus /remoteSupports/systems sein
    type_id: Optional[int] = None
    # The userId property
    user_id: Optional[str] = None
    # The userName property
    user_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RemoteSupportsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RemoteSupportsPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RemoteSupportsPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "comment": lambda n : setattr(self, 'comment', n.get_str_value()),
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "endTime": lambda n : setattr(self, 'end_time', n.get_int_value()),
            "fee": lambda n : setattr(self, 'fee', n.get_float_value()),
            "linkId": lambda n : setattr(self, 'link_id', n.get_int_value()),
            "linkTypeId": lambda n : setattr(self, 'link_type_id', n.get_int_value()),
            "remoteMaintenanceId": lambda n : setattr(self, 'remote_maintenance_id', n.get_str_value()),
            "startTime": lambda n : setattr(self, 'start_time', n.get_int_value()),
            "ticketId": lambda n : setattr(self, 'ticket_id', n.get_int_value()),
            "typeId": lambda n : setattr(self, 'type_id', n.get_int_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_int_value("companyId", self.company_id)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_int_value("endTime", self.end_time)
        writer.write_float_value("fee", self.fee)
        writer.write_int_value("linkId", self.link_id)
        writer.write_int_value("linkTypeId", self.link_type_id)
        writer.write_str_value("remoteMaintenanceId", self.remote_maintenance_id)
        writer.write_int_value("startTime", self.start_time)
        writer.write_int_value("ticketId", self.ticket_id)
        writer.write_int_value("typeId", self.type_id)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userName", self.user_name)
        writer.write_additional_data_value(self.additional_data)
    

