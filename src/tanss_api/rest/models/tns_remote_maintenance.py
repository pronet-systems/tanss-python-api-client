from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsRemoteMaintenance(AdditionalDataHolder, Parsable):
    """
    This object represents a remote support
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # (optional) comment of the remote support
    comment: Optional[str] = None
    # id of the company for this remote support
    company_id: Optional[int] = None
    # "Identifier string" or unique name of the device the remote support was executed for. This can be used via a "translation table" toget the company and/or assignment.
    device_id: Optional[str] = None
    # Simply the name of the device the remote support was executed for. This is mainly used for displying issues.
    device_name: Optional[str] = None
    # Id of the technician who has done this remote support (TANSS employee id). This can be omitted if the id is not knownor the "userId" can be "translated"
    employee_id: Optional[int] = None
    # Unix timestamp of the end for this remote support
    end_time: Optional[int] = None
    # The id property
    id: Optional[int] = None
    # LinkId of the assignment (if known)
    link_id: Optional[int] = None
    # LinkTypeId of the assignment (if known)
    link_type_id: Optional[int] = None
    # "Identifier" used by the remote systems to identify this remote support
    remote_maintenance_id: Optional[str] = None
    # Unix timestamp of the begin for this remote support
    start_time: Optional[int] = None
    # "Id" of the external remote support system, which is defined in the TANSS administration ("Externe Fernwartungs-Anbindungen verwalten").This field can't be set, as the Api token was created for a specific "type" and this value is fix.
    type_id: Optional[int] = None
    # "Identifier string" of the technician who has done this remote support. This can be used to "translate" the identifier of the technicianto a TANSS employee id
    user_id: Optional[str] = None
    # name of the technician who has done this remote support, this is mainly used for displaying issues
    user_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsRemoteMaintenance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsRemoteMaintenance
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsRemoteMaintenance()
    
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
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "linkId": lambda n : setattr(self, 'link_id', n.get_int_value()),
            "linkTypeId": lambda n : setattr(self, 'link_type_id', n.get_int_value()),
            "remoteMaintenanceId": lambda n : setattr(self, 'remote_maintenance_id', n.get_str_value()),
            "startTime": lambda n : setattr(self, 'start_time', n.get_int_value()),
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
        writer.write_int_value("linkId", self.link_id)
        writer.write_int_value("linkTypeId", self.link_type_id)
        writer.write_str_value("remoteMaintenanceId", self.remote_maintenance_id)
        writer.write_int_value("startTime", self.start_time)
        writer.write_int_value("typeId", self.type_id)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userName", self.user_name)
        writer.write_additional_data_value(self.additional_data)
    

