from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.tns_device_ownage_type import TnsDeviceOwnageType
    from ......models.tns_guarantee import TnsGuarantee
    from ......models.tns_ip_mac import TnsIpMac
    from ......models.tns_periphery_field_info import TnsPeripheryFieldInfo

@dataclass
class PeripheriesPutRequestBody(AdditionalDataHolder, Parsable):
    """
    Beliebige TnsPeriphery-Felder (JSON-Merge)
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The active property
    active: Optional[bool] = None
    # The articleNumber property
    article_number: Optional[str] = None
    # The billingNumber property
    billing_number: Optional[str] = None
    # The companyId property
    company_id: Optional[int] = None
    # The description property
    description: Optional[str] = None
    # The employeeId property
    employee_id: Optional[int] = None
    # The fields property
    fields: Optional[list[TnsPeripheryFieldInfo]] = None
    # Information of the guarantee or warranty of a device
    guarantee: Optional[TnsGuarantee] = None
    # The internalRemark property
    internal_remark: Optional[str] = None
    # The inventoryNumber property
    inventory_number: Optional[str] = None
    # The ip property
    ip: Optional[str] = None
    # The ips property
    ips: Optional[list[TnsIpMac]] = None
    # The isdn property
    isdn: Optional[str] = None
    # The location property
    location: Optional[str] = None
    # The loginName property
    login_name: Optional[str] = None
    # The loginPassword property
    login_password: Optional[str] = None
    # The mac property
    mac: Optional[str] = None
    # The manufacturerId property
    manufacturer_id: Optional[int] = None
    # The manufacturerNumber property
    manufacturer_number: Optional[str] = None
    # The name property
    name: Optional[str] = None
    # describes who "owns" this pc
    ownage_type: Optional[TnsDeviceOwnageType] = None
    # The pcId property
    pc_id: Optional[int] = None
    # The peripheryTypeId property
    periphery_type_id: Optional[int] = None
    # The purchasePrice property
    purchase_price: Optional[float] = None
    # The remark property
    remark: Optional[str] = None
    # The sellingPrice property
    selling_price: Optional[float] = None
    # The serialNumber property
    serial_number: Optional[str] = None
    # The showRemark property
    show_remark: Optional[bool] = None
    # The storageId property
    storage_id: Optional[int] = None
    # The type property
    type: Optional[str] = None
    # The version property
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PeripheriesPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PeripheriesPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PeripheriesPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ......models.tns_device_ownage_type import TnsDeviceOwnageType
        from ......models.tns_guarantee import TnsGuarantee
        from ......models.tns_ip_mac import TnsIpMac
        from ......models.tns_periphery_field_info import TnsPeripheryFieldInfo

        from ......models.tns_device_ownage_type import TnsDeviceOwnageType
        from ......models.tns_guarantee import TnsGuarantee
        from ......models.tns_ip_mac import TnsIpMac
        from ......models.tns_periphery_field_info import TnsPeripheryFieldInfo

        fields: dict[str, Callable[[Any], None]] = {
            "active": lambda n : setattr(self, 'active', n.get_bool_value()),
            "articleNumber": lambda n : setattr(self, 'article_number', n.get_str_value()),
            "billingNumber": lambda n : setattr(self, 'billing_number', n.get_str_value()),
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "fields": lambda n : setattr(self, 'fields', n.get_collection_of_object_values(TnsPeripheryFieldInfo)),
            "guarantee": lambda n : setattr(self, 'guarantee', n.get_object_value(TnsGuarantee)),
            "internalRemark": lambda n : setattr(self, 'internal_remark', n.get_str_value()),
            "inventoryNumber": lambda n : setattr(self, 'inventory_number', n.get_str_value()),
            "ip": lambda n : setattr(self, 'ip', n.get_str_value()),
            "ips": lambda n : setattr(self, 'ips', n.get_collection_of_object_values(TnsIpMac)),
            "isdn": lambda n : setattr(self, 'isdn', n.get_str_value()),
            "location": lambda n : setattr(self, 'location', n.get_str_value()),
            "loginName": lambda n : setattr(self, 'login_name', n.get_str_value()),
            "loginPassword": lambda n : setattr(self, 'login_password', n.get_str_value()),
            "mac": lambda n : setattr(self, 'mac', n.get_str_value()),
            "manufacturerId": lambda n : setattr(self, 'manufacturer_id', n.get_int_value()),
            "manufacturerNumber": lambda n : setattr(self, 'manufacturer_number', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "ownageType": lambda n : setattr(self, 'ownage_type', n.get_enum_value(TnsDeviceOwnageType)),
            "pcId": lambda n : setattr(self, 'pc_id', n.get_int_value()),
            "peripheryTypeId": lambda n : setattr(self, 'periphery_type_id', n.get_int_value()),
            "purchasePrice": lambda n : setattr(self, 'purchase_price', n.get_float_value()),
            "remark": lambda n : setattr(self, 'remark', n.get_str_value()),
            "sellingPrice": lambda n : setattr(self, 'selling_price', n.get_float_value()),
            "serialNumber": lambda n : setattr(self, 'serial_number', n.get_str_value()),
            "showRemark": lambda n : setattr(self, 'show_remark', n.get_bool_value()),
            "storageId": lambda n : setattr(self, 'storage_id', n.get_int_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_bool_value("active", self.active)
        writer.write_str_value("articleNumber", self.article_number)
        writer.write_str_value("billingNumber", self.billing_number)
        writer.write_int_value("companyId", self.company_id)
        writer.write_str_value("description", self.description)
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_collection_of_object_values("fields", self.fields)
        writer.write_object_value("guarantee", self.guarantee)
        writer.write_str_value("internalRemark", self.internal_remark)
        writer.write_str_value("inventoryNumber", self.inventory_number)
        writer.write_str_value("ip", self.ip)
        writer.write_collection_of_object_values("ips", self.ips)
        writer.write_str_value("isdn", self.isdn)
        writer.write_str_value("location", self.location)
        writer.write_str_value("loginName", self.login_name)
        writer.write_str_value("loginPassword", self.login_password)
        writer.write_str_value("mac", self.mac)
        writer.write_int_value("manufacturerId", self.manufacturer_id)
        writer.write_str_value("manufacturerNumber", self.manufacturer_number)
        writer.write_str_value("name", self.name)
        writer.write_enum_value("ownageType", self.ownage_type)
        writer.write_int_value("pcId", self.pc_id)
        writer.write_int_value("peripheryTypeId", self.periphery_type_id)
        writer.write_float_value("purchasePrice", self.purchase_price)
        writer.write_str_value("remark", self.remark)
        writer.write_float_value("sellingPrice", self.selling_price)
        writer.write_str_value("serialNumber", self.serial_number)
        writer.write_bool_value("showRemark", self.show_remark)
        writer.write_int_value("storageId", self.storage_id)
        writer.write_str_value("type", self.type)
        writer.write_str_value("version", self.version)
        writer.write_additional_data_value(self.additional_data)
    

