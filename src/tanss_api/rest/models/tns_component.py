from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsComponent(AdditionalDataHolder, Parsable):
    """
    Describes a pc component
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # true, if the component is active
    active: Optional[bool] = None
    # article number of the component
    article_number: Optional[str] = None
    # infos about the billing number which this component was purchased
    billing_number: Optional[str] = None
    # id of the company, which this component is assigned to. Only relevant if the component is not built into a pc!
    company_id: Optional[int] = None
    # id of the component type
    component_type_id: Optional[int] = None
    # date when the component was purchased (or entered into the system)
    date: Optional[int] = None
    # misc. description infos for this component
    description: Optional[str] = None
    # id of the HDD type
    hdd_type_id: Optional[int] = None
    # id of the pc / server
    id: Optional[int] = None
    # inventory number of this component
    inventory_number: Optional[str] = None
    # id of the components manufacturer
    manufacturer_id: Optional[int] = None
    # capcity (in megbytes), which is used to determine the size of ram or HDDs
    megabytes: Optional[int] = None
    # if true, the component is "onboard"
    on_board: Optional[bool] = None
    # the component is built into this pc (0 if the component ist not attached to a pc)
    pc_id: Optional[int] = None
    # if the component is built into a periphery, here the id is given
    periphery_id: Optional[int] = None
    # purchase price of this component
    purchase_price: Optional[float] = None
    # remarks for this component
    remark: Optional[str] = None
    # SCSI id
    scsi_id: Optional[str] = None
    # selling price of this component
    selling_price: Optional[float] = None
    # serial number of the component
    serial_number: Optional[str] = None
    # id of the storage, the component is contained in
    storage_id: Optional[int] = None
    # type of the component. This is mostly used to "describe" the component in lists
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsComponent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsComponent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsComponent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "active": lambda n : setattr(self, 'active', n.get_bool_value()),
            "articleNumber": lambda n : setattr(self, 'article_number', n.get_str_value()),
            "billingNumber": lambda n : setattr(self, 'billing_number', n.get_str_value()),
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "componentTypeId": lambda n : setattr(self, 'component_type_id', n.get_int_value()),
            "date": lambda n : setattr(self, 'date', n.get_int_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "hddTypeId": lambda n : setattr(self, 'hdd_type_id', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "inventoryNumber": lambda n : setattr(self, 'inventory_number', n.get_str_value()),
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
        writer.write_int_value("hddTypeId", self.hdd_type_id)
        writer.write_str_value("inventoryNumber", self.inventory_number)
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
        writer.write_int_value("storageId", self.storage_id)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

