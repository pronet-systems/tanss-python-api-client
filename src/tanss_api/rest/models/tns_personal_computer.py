from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_device_ownage_type import TnsDeviceOwnageType

@dataclass
class TnsPersonalComputer(AdditionalDataHolder, Parsable):
    """
    Describes a pc or server
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # is this pc active or not ?
    active: Optional[bool] = None
    # AnyDesk id
    anydesk_id: Optional[str] = None
    # AnyDesk password
    anydesk_password: Optional[str] = None
    # article number of the pc
    article_number: Optional[str] = None
    # infos about the billing number which this pc was purchased
    billing_number: Optional[str] = None
    # infos about the bios
    bios: Optional[str] = None
    # release infos of the bios
    bios_release: Optional[str] = None
    # id of the company which this pc is assigned to
    company_id: Optional[int] = None
    # frequency of the cpu (in MHz)
    cpu_frequency: Optional[int] = None
    # id of the cpu manufacturer
    cpu_manufacturer_id: Optional[int] = None
    # number of cpus
    cpu_number: Optional[int] = None
    # id of the cpu type
    cpu_type_id: Optional[int] = None
    # date when this pc was purchased
    date: Optional[int] = None
    # misc. description infos for this pc
    description: Optional[str] = None
    # id of employee, which this pc is assigned to
    employee_id: Optional[int] = None
    # if this pc is a virtual host, then here the id of the host is given
    host_id: Optional[int] = None
    # id of the pc / server
    id: Optional[int] = None
    # internal remarks of the pc (can contain passwords), which only is seen by technicians or freelancers with the given permission
    internal_remark: Optional[str] = None
    # inventory number
    inventory_number: Optional[str] = None
    # serial number of the keyboard
    keyboad_serial_number: Optional[str] = None
    # location / room of this pc
    location: Optional[str] = None
    # id of the mainboard manufacturer
    mainboard_manufacturer_id: Optional[int] = None
    # revision of the mainboard
    mainboard_revision: Optional[str] = None
    # serial number of the mainboard
    mainboard_serial_number: Optional[str] = None
    # id of the manufacturer of this pc
    manufacturer_id: Optional[int] = None
    # manufacturer number of this pc
    manufacturer_number: Optional[str] = None
    # describes the "model" of the pc. This field often is used to describe the pc (mostly in lists)
    model: Optional[str] = None
    # serial number of the mouse
    mouse_serial_number: Optional[str] = None
    # hostname
    name: Optional[str] = None
    # id of the operating system
    os_id: Optional[int] = None
    # describes who "owns" this pc
    ownage_type: Optional[TnsDeviceOwnageType] = None
    # purchase price of this pc
    purchase_price: Optional[float] = None
    # a text field which contains misc. infos / remarks about this pc
    remark: Optional[str] = None
    # reserved cpu capacity reserved for this virtual host
    reserved_cpu: Optional[float] = None
    # reserved hard disk space reserved for this virtual host
    reserved_hard_disk: Optional[float] = None
    # reserved ram for this virtual host
    reserved_ram: Optional[float] = None
    # selling price of this pc
    selling_price: Optional[float] = None
    # serial number
    serial_number: Optional[str] = None
    # true if this pc is a server
    server: Optional[bool] = None
    # id of the responsible service technician
    service_technician_id: Optional[int] = None
    # if true, the remark will be shown as popup when this pc is selected in a support/ticket mask and the employee has the permission
    show_remark: Optional[bool] = None
    # a text field which contains infos about installed software
    software: Optional[str] = None
    # id of the storage, the pc is contained in
    storage_id: Optional[int] = None
    # TeamViewer id
    teamviewer_id: Optional[str] = None
    # TeamViewer password
    teamviewer_password: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsPersonalComputer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsPersonalComputer
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsPersonalComputer()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_device_ownage_type import TnsDeviceOwnageType

        from .tns_device_ownage_type import TnsDeviceOwnageType

        fields: dict[str, Callable[[Any], None]] = {
            "active": lambda n : setattr(self, 'active', n.get_bool_value()),
            "anydeskId": lambda n : setattr(self, 'anydesk_id', n.get_str_value()),
            "anydeskPassword": lambda n : setattr(self, 'anydesk_password', n.get_str_value()),
            "articleNumber": lambda n : setattr(self, 'article_number', n.get_str_value()),
            "billingNumber": lambda n : setattr(self, 'billing_number', n.get_str_value()),
            "bios": lambda n : setattr(self, 'bios', n.get_str_value()),
            "biosRelease": lambda n : setattr(self, 'bios_release', n.get_str_value()),
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "cpuFrequency": lambda n : setattr(self, 'cpu_frequency', n.get_int_value()),
            "cpuManufacturerId": lambda n : setattr(self, 'cpu_manufacturer_id', n.get_int_value()),
            "cpuNumber": lambda n : setattr(self, 'cpu_number', n.get_int_value()),
            "cpuTypeId": lambda n : setattr(self, 'cpu_type_id', n.get_int_value()),
            "date": lambda n : setattr(self, 'date', n.get_int_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "hostId": lambda n : setattr(self, 'host_id', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "internalRemark": lambda n : setattr(self, 'internal_remark', n.get_str_value()),
            "inventoryNumber": lambda n : setattr(self, 'inventory_number', n.get_str_value()),
            "keyboadSerialNumber": lambda n : setattr(self, 'keyboad_serial_number', n.get_str_value()),
            "location": lambda n : setattr(self, 'location', n.get_str_value()),
            "mainboardManufacturerId": lambda n : setattr(self, 'mainboard_manufacturer_id', n.get_int_value()),
            "mainboardRevision": lambda n : setattr(self, 'mainboard_revision', n.get_str_value()),
            "mainboardSerialNumber": lambda n : setattr(self, 'mainboard_serial_number', n.get_str_value()),
            "manufacturerId": lambda n : setattr(self, 'manufacturer_id', n.get_int_value()),
            "manufacturerNumber": lambda n : setattr(self, 'manufacturer_number', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "mouseSerialNumber": lambda n : setattr(self, 'mouse_serial_number', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "osId": lambda n : setattr(self, 'os_id', n.get_int_value()),
            "ownageType": lambda n : setattr(self, 'ownage_type', n.get_enum_value(TnsDeviceOwnageType)),
            "purchasePrice": lambda n : setattr(self, 'purchase_price', n.get_float_value()),
            "remark": lambda n : setattr(self, 'remark', n.get_str_value()),
            "reservedCpu": lambda n : setattr(self, 'reserved_cpu', n.get_float_value()),
            "reservedHardDisk": lambda n : setattr(self, 'reserved_hard_disk', n.get_float_value()),
            "reservedRam": lambda n : setattr(self, 'reserved_ram', n.get_float_value()),
            "sellingPrice": lambda n : setattr(self, 'selling_price', n.get_float_value()),
            "serialNumber": lambda n : setattr(self, 'serial_number', n.get_str_value()),
            "server": lambda n : setattr(self, 'server', n.get_bool_value()),
            "serviceTechnicianId": lambda n : setattr(self, 'service_technician_id', n.get_int_value()),
            "showRemark": lambda n : setattr(self, 'show_remark', n.get_bool_value()),
            "software": lambda n : setattr(self, 'software', n.get_str_value()),
            "storageId": lambda n : setattr(self, 'storage_id', n.get_int_value()),
            "teamviewerId": lambda n : setattr(self, 'teamviewer_id', n.get_str_value()),
            "teamviewerPassword": lambda n : setattr(self, 'teamviewer_password', n.get_str_value()),
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
        writer.write_str_value("anydeskId", self.anydesk_id)
        writer.write_str_value("anydeskPassword", self.anydesk_password)
        writer.write_str_value("articleNumber", self.article_number)
        writer.write_str_value("billingNumber", self.billing_number)
        writer.write_str_value("bios", self.bios)
        writer.write_str_value("biosRelease", self.bios_release)
        writer.write_int_value("companyId", self.company_id)
        writer.write_int_value("cpuFrequency", self.cpu_frequency)
        writer.write_int_value("cpuManufacturerId", self.cpu_manufacturer_id)
        writer.write_int_value("cpuNumber", self.cpu_number)
        writer.write_int_value("cpuTypeId", self.cpu_type_id)
        writer.write_int_value("date", self.date)
        writer.write_str_value("description", self.description)
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_int_value("hostId", self.host_id)
        writer.write_str_value("internalRemark", self.internal_remark)
        writer.write_str_value("inventoryNumber", self.inventory_number)
        writer.write_str_value("keyboadSerialNumber", self.keyboad_serial_number)
        writer.write_str_value("location", self.location)
        writer.write_int_value("mainboardManufacturerId", self.mainboard_manufacturer_id)
        writer.write_str_value("mainboardRevision", self.mainboard_revision)
        writer.write_str_value("mainboardSerialNumber", self.mainboard_serial_number)
        writer.write_int_value("manufacturerId", self.manufacturer_id)
        writer.write_str_value("manufacturerNumber", self.manufacturer_number)
        writer.write_str_value("model", self.model)
        writer.write_str_value("mouseSerialNumber", self.mouse_serial_number)
        writer.write_str_value("name", self.name)
        writer.write_int_value("osId", self.os_id)
        writer.write_enum_value("ownageType", self.ownage_type)
        writer.write_float_value("purchasePrice", self.purchase_price)
        writer.write_str_value("remark", self.remark)
        writer.write_float_value("reservedCpu", self.reserved_cpu)
        writer.write_float_value("reservedHardDisk", self.reserved_hard_disk)
        writer.write_float_value("reservedRam", self.reserved_ram)
        writer.write_float_value("sellingPrice", self.selling_price)
        writer.write_str_value("serialNumber", self.serial_number)
        writer.write_bool_value("server", self.server)
        writer.write_int_value("serviceTechnicianId", self.service_technician_id)
        writer.write_bool_value("showRemark", self.show_remark)
        writer.write_str_value("software", self.software)
        writer.write_int_value("storageId", self.storage_id)
        writer.write_str_value("teamviewerId", self.teamviewer_id)
        writer.write_str_value("teamviewerPassword", self.teamviewer_password)
        writer.write_additional_data_value(self.additional_data)
    

