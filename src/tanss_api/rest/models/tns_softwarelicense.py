from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_assignment import TnsAssignment

@dataclass
class TnsSoftwarelicense(AdditionalDataHolder, Parsable):
    """
    Describes a software license
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # true if the software license is still active
    active: Optional[bool] = None
    # article number of the component
    article_number: Optional[str] = None
    # assignments of this software license to other entities
    assignments: Optional[list[TnsAssignment]] = None
    # company id of the software license
    company_id: Optional[int] = None
    # price which is used in maintenace contracts
    contract_price: Optional[float] = None
    # starting date for this software license
    date: Optional[int] = None
    # id of employee which uses this software license
    employee_id: Optional[int] = None
    # date when the software license will expire
    expiration_date: Optional[int] = None
    # id of the software license
    id: Optional[int] = None
    # internal remarks of the license (can contain passwords), which only is seen by technicians or freelancers with the given permission
    internal_remark: Optional[str] = None
    # inventory number
    inventory_number: Optional[str] = None
    # maximum number of installations
    max_number_of_install: Optional[int] = None
    # number of volumes (i.e. cds)
    number_of_volumes: Optional[int] = None
    # misc. infos of for this software license
    remark: Optional[str] = None
    # if true, the license must be renewed upon expiring and therefore needs further "attention"
    renew: Optional[bool] = None
    # serial number
    serial_number: Optional[str] = None
    # id of the sofware license type
    softwarelicense_type_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsSoftwarelicense:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsSoftwarelicense
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsSoftwarelicense()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_assignment import TnsAssignment

        from .tns_assignment import TnsAssignment

        fields: dict[str, Callable[[Any], None]] = {
            "active": lambda n : setattr(self, 'active', n.get_bool_value()),
            "articleNumber": lambda n : setattr(self, 'article_number', n.get_str_value()),
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(TnsAssignment)),
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "contractPrice": lambda n : setattr(self, 'contract_price', n.get_float_value()),
            "date": lambda n : setattr(self, 'date', n.get_int_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "expirationDate": lambda n : setattr(self, 'expiration_date', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "internalRemark": lambda n : setattr(self, 'internal_remark', n.get_str_value()),
            "inventoryNumber": lambda n : setattr(self, 'inventory_number', n.get_str_value()),
            "maxNumberOfInstall": lambda n : setattr(self, 'max_number_of_install', n.get_int_value()),
            "numberOfVolumes": lambda n : setattr(self, 'number_of_volumes', n.get_int_value()),
            "remark": lambda n : setattr(self, 'remark', n.get_str_value()),
            "renew": lambda n : setattr(self, 'renew', n.get_bool_value()),
            "serialNumber": lambda n : setattr(self, 'serial_number', n.get_str_value()),
            "softwarelicenseTypeId": lambda n : setattr(self, 'softwarelicense_type_id', n.get_int_value()),
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
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_int_value("companyId", self.company_id)
        writer.write_float_value("contractPrice", self.contract_price)
        writer.write_int_value("date", self.date)
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_int_value("expirationDate", self.expiration_date)
        writer.write_str_value("internalRemark", self.internal_remark)
        writer.write_str_value("inventoryNumber", self.inventory_number)
        writer.write_int_value("maxNumberOfInstall", self.max_number_of_install)
        writer.write_int_value("numberOfVolumes", self.number_of_volumes)
        writer.write_str_value("remark", self.remark)
        writer.write_bool_value("renew", self.renew)
        writer.write_str_value("serialNumber", self.serial_number)
        writer.write_int_value("softwarelicenseTypeId", self.softwarelicense_type_id)
        writer.write_additional_data_value(self.additional_data)
    

