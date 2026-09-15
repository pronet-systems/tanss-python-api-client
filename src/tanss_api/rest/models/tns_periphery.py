from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_device_ownage_type import TnsDeviceOwnageType
    from .tns_periphery_field_info import TnsPeripheryFieldInfo

@dataclass
class TnsPeriphery(AdditionalDataHolder, Parsable):
    """
    Describes a periphery
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # true, if the device is active
    active: Optional[bool] = None
    # article number of the component
    article_number: Optional[str] = None
    # infos about the billing number which this component was purchased
    billing_number: Optional[str] = None
    # id of the assigned company
    company_id: Optional[int] = None
    # date when the device was purchased (or entered into the system)
    date: Optional[int] = None
    # misc. description infos for this device
    description: Optional[str] = None
    # id of the assigned employee
    employee_id: Optional[int] = None
    # The fields property
    fields: Optional[list[TnsPeripheryFieldInfo]] = None
    # id of the periphery
    id: Optional[int] = None
    # internal remarks of the device (can contain passwords), which only is seen by technicians or freelancers with the given permission
    internal_remark: Optional[str] = None
    # inventory number of this device
    inventory_number: Optional[str] = None
    # location / room of this device
    location: Optional[str] = None
    # id of the device manufacturer
    manufacturer_id: Optional[int] = None
    # manufacturer number of this device
    manufacturer_number: Optional[str] = None
    # hostname
    name: Optional[str] = None
    # describes who "owns" this pc
    ownage_type: Optional[TnsDeviceOwnageType] = None
    # if the device is built into this pc, a pc id is given here
    pc_id: Optional[int] = None
    # id of the periphery type
    periphery_type_id: Optional[int] = None
    # purchase price of this component
    purchase_price: Optional[float] = None
    # remarks for this component
    remark: Optional[str] = None
    # selling price of this device
    selling_price: Optional[float] = None
    # serial number of the device
    serial_number: Optional[str] = None
    # id of the storage, the component is contained in
    storage_id: Optional[int] = None
    # type of the periphery. This is mostly used to "describe" the periphery in lists
    type: Optional[str] = None
    # infos of the version of this device
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsPeriphery:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsPeriphery
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsPeriphery()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_device_ownage_type import TnsDeviceOwnageType
        from .tns_periphery_field_info import TnsPeripheryFieldInfo

        from .tns_device_ownage_type import TnsDeviceOwnageType
        from .tns_periphery_field_info import TnsPeripheryFieldInfo

        fields: dict[str, Callable[[Any], None]] = {
            "active": lambda n : setattr(self, 'active', n.get_bool_value()),
            "articleNumber": lambda n : setattr(self, 'article_number', n.get_str_value()),
            "billingNumber": lambda n : setattr(self, 'billing_number', n.get_str_value()),
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "date": lambda n : setattr(self, 'date', n.get_int_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "fields": lambda n : setattr(self, 'fields', n.get_collection_of_object_values(TnsPeripheryFieldInfo)),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "internalRemark": lambda n : setattr(self, 'internal_remark', n.get_str_value()),
            "inventoryNumber": lambda n : setattr(self, 'inventory_number', n.get_str_value()),
            "location": lambda n : setattr(self, 'location', n.get_str_value()),
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
        writer.write_int_value("date", self.date)
        writer.write_str_value("description", self.description)
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_collection_of_object_values("fields", self.fields)
        writer.write_str_value("internalRemark", self.internal_remark)
        writer.write_str_value("inventoryNumber", self.inventory_number)
        writer.write_str_value("location", self.location)
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
        writer.write_int_value("storageId", self.storage_id)
        writer.write_str_value("type", self.type)
        writer.write_str_value("version", self.version)
        writer.write_additional_data_value(self.additional_data)
    

