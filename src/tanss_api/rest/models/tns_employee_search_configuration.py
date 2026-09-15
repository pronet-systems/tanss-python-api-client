from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_area_search_configuration import TnsAreaSearchConfiguration

from .tns_area_search_configuration import TnsAreaSearchConfiguration

@dataclass
class TnsEmployeeSearchConfiguration(TnsAreaSearchConfiguration, Parsable):
    """
    parameters which specify the employee search
    """
    # if true, expected callbacks will be fetched as well (default = false)
    callbacks: Optional[bool] = None
    # if true, categories will be fetches as well. The names are given in the "linked entities" - "employeeCategories" (default = false)
    categories: Optional[bool] = None
    # if only is to be searched in one company
    company_id: Optional[int] = None
    # if false, inactive users won't be fetched (default = true)
    inactive: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsEmployeeSearchConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsEmployeeSearchConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsEmployeeSearchConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_area_search_configuration import TnsAreaSearchConfiguration

        from .tns_area_search_configuration import TnsAreaSearchConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "callbacks": lambda n : setattr(self, 'callbacks', n.get_bool_value()),
            "categories": lambda n : setattr(self, 'categories', n.get_bool_value()),
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "inactive": lambda n : setattr(self, 'inactive', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_bool_value("callbacks", self.callbacks)
        writer.write_bool_value("categories", self.categories)
        writer.write_int_value("companyId", self.company_id)
        writer.write_bool_value("inactive", self.inactive)
    

