from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_timeframe import TnsTimeframe

@dataclass
class TnsRemoteMaintenanceConfiguration(AdditionalDataHolder, Parsable):
    """
    This object is used to get remote supports based on filter settings
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # only shows remote supports of this company
    company_id: Optional[int] = None
    # only shows remote supports of a certain employee
    employee_id: Optional[int] = None
    # text filter for remote supports
    text: Optional[str] = None
    # Describes a timeframe (from / to)
    timeframe: Optional[TnsTimeframe] = None
    # If set, only shows remote supports of this type
    type_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsRemoteMaintenanceConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsRemoteMaintenanceConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsRemoteMaintenanceConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_timeframe import TnsTimeframe

        from .tns_timeframe import TnsTimeframe

        fields: dict[str, Callable[[Any], None]] = {
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
            "timeframe": lambda n : setattr(self, 'timeframe', n.get_object_value(TnsTimeframe)),
            "typeId": lambda n : setattr(self, 'type_id', n.get_int_value()),
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
        writer.write_int_value("companyId", self.company_id)
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_str_value("text", self.text)
        writer.write_object_value("timeframe", self.timeframe)
        writer.write_int_value("typeId", self.type_id)
        writer.write_additional_data_value(self.additional_data)
    

