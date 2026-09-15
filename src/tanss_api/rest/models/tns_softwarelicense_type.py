from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsSoftwarelicenseType(AdditionalDataHolder, Parsable):
    """
    Describes a software license type including default values and pricing information.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates whether the software license type is active.
    active: Optional[bool] = None
    # Internal article number.
    article_number: Optional[str] = None
    # Comment or description of the software license type.
    comment: Optional[str] = None
    # Unique identifier of the software license type.
    id: Optional[int] = None
    # Manufacturer article number.
    manufacturer_number: Optional[str] = None
    # Name of the software license type.
    name: Optional[str] = None
    # Hierarchical path of the software license type.
    path: Optional[list[str]] = None
    # Reference to a previous software license type.
    previous_id: Optional[int] = None
    # Default maximum number of installations.
    standard_max_number_of_installations: Optional[int] = None
    # Indicates whether the license is renewed by default.
    standard_renew: Optional[bool] = None
    # Default running time of the license (e.g. in months).
    standard_running_time: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsSoftwarelicenseType:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsSoftwarelicenseType
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsSoftwarelicenseType()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "active": lambda n : setattr(self, 'active', n.get_bool_value()),
            "articleNumber": lambda n : setattr(self, 'article_number', n.get_str_value()),
            "comment": lambda n : setattr(self, 'comment', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "manufacturerNumber": lambda n : setattr(self, 'manufacturer_number', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "path": lambda n : setattr(self, 'path', n.get_collection_of_primitive_values(str)),
            "previousId": lambda n : setattr(self, 'previous_id', n.get_int_value()),
            "standardMaxNumberOfInstallations": lambda n : setattr(self, 'standard_max_number_of_installations', n.get_int_value()),
            "standardRenew": lambda n : setattr(self, 'standard_renew', n.get_bool_value()),
            "standardRunningTime": lambda n : setattr(self, 'standard_running_time', n.get_int_value()),
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
        writer.write_str_value("comment", self.comment)
        writer.write_str_value("manufacturerNumber", self.manufacturer_number)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_primitive_values("path", self.path)
        writer.write_int_value("previousId", self.previous_id)
        writer.write_int_value("standardMaxNumberOfInstallations", self.standard_max_number_of_installations)
        writer.write_bool_value("standardRenew", self.standard_renew)
        writer.write_int_value("standardRunningTime", self.standard_running_time)
        writer.write_additional_data_value(self.additional_data)
    

