from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.tns_guarantee import TnsGuarantee

@dataclass
class ComponentsPutRequestBody(AdditionalDataHolder, Parsable):
    """
    Beliebige TnsComponent-Felder (JSON-Merge)
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
    # The componentTypeId property
    component_type_id: Optional[int] = None
    # The date property
    date: Optional[int] = None
    # The description property
    description: Optional[str] = None
    # Information of the guarantee or warranty of a device
    guarantee: Optional[TnsGuarantee] = None
    # The hddTypeId property
    hdd_type_id: Optional[int] = None
    # The inventoryNumber property
    inventory_number: Optional[str] = None
    # The mac property
    mac: Optional[str] = None
    # The manufacturerId property
    manufacturer_id: Optional[int] = None
    # The megabytes property
    megabytes: Optional[int] = None
    # The onBoard property
    on_board: Optional[bool] = None
    # The pcId property
    pc_id: Optional[int] = None
    # The peripheryId property
    periphery_id: Optional[int] = None
    # The purchasePrice property
    purchase_price: Optional[float] = None
    # The remark property
    remark: Optional[str] = None
    # The scsiId property
    scsi_id: Optional[str] = None
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ComponentsPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ComponentsPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ComponentsPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ......models.tns_guarantee import TnsGuarantee

        from ......models.tns_guarantee import TnsGuarantee

        fields: dict[str, Callable[[Any], None]] = {
            "active": lambda n : setattr(self, 'active', n.get_bool_value()),
            "articleNumber": lambda n : setattr(self, 'article_number', n.get_str_value()),
            "billingNumber": lambda n : setattr(self, 'billing_number', n.get_str_value()),
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "componentTypeId": lambda n : setattr(self, 'component_type_id', n.get_int_value()),
            "date": lambda n : setattr(self, 'date', n.get_int_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "guarantee": lambda n : setattr(self, 'guarantee', n.get_object_value(TnsGuarantee)),
            "hddTypeId": lambda n : setattr(self, 'hdd_type_id', n.get_int_value()),
            "inventoryNumber": lambda n : setattr(self, 'inventory_number', n.get_str_value()),
            "mac": lambda n : setattr(self, 'mac', n.get_str_value()),
            "manufacturerId": lambda n : setattr(self, 'manufacturer_id', n.get_int_value()),
            "megabytes": lambda n : setattr(self, 'megabytes', n.get_int_value()),
            "onBoard": lambda n : setattr(self, 'on_board', n.get_bool_value()),
            "pcId": lambda n : setattr(self, 'pc_id', n.get_int_value()),
            "peripheryId": lambda n : setattr(self, 'periphery_id', n.get_int_value()),
            "purchasePrice": lambda n : setattr(self, 'purchase_price', n.get_float_value()),
            "remark": lambda n : setattr(self, 'remark', n.get_str_value()),
            "scsiId": lambda n : setattr(self, 'scsi_id', n.get_str_value()),
            "sellingPrice": lambda n : setattr(self, 'selling_price', n.get_float_value()),
            "serialNumber": lambda n : setattr(self, 'serial_number', n.get_str_value()),
            "showRemark": lambda n : setattr(self, 'show_remark', n.get_bool_value()),
            "storageId": lambda n : setattr(self, 'storage_id', n.get_int_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_int_value("componentTypeId", self.component_type_id)
        writer.write_int_value("date", self.date)
        writer.write_str_value("description", self.description)
        writer.write_object_value("guarantee", self.guarantee)
        writer.write_int_value("hddTypeId", self.hdd_type_id)
        writer.write_str_value("inventoryNumber", self.inventory_number)
        writer.write_str_value("mac", self.mac)
        writer.write_int_value("manufacturerId", self.manufacturer_id)
        writer.write_int_value("megabytes", self.megabytes)
        writer.write_bool_value("onBoard", self.on_board)
        writer.write_int_value("pcId", self.pc_id)
        writer.write_int_value("peripheryId", self.periphery_id)
        writer.write_float_value("purchasePrice", self.purchase_price)
        writer.write_str_value("remark", self.remark)
        writer.write_str_value("scsiId", self.scsi_id)
        writer.write_float_value("sellingPrice", self.selling_price)
        writer.write_str_value("serialNumber", self.serial_number)
        writer.write_bool_value("showRemark", self.show_remark)
        writer.write_int_value("storageId", self.storage_id)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

