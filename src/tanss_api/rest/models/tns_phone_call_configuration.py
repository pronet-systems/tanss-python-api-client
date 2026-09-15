from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_phone_call_direction import TnsPhoneCallDirection
    from .tns_timeframe import TnsTimeframe

@dataclass
class TnsPhoneCallConfiguration(AdditionalDataHolder, Parsable):
    """
    This object is used to get phone calls based on this filter settings
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # only shows phone calls of this company
    company_id: Optional[int] = None
    # fetches for example only incoming or outgoing calls
    directions: Optional[list[TnsPhoneCallDirection]] = None
    # only shows phone calls of a certain employee
    employee_id: Optional[int] = None
    # one or more telephone number filters to be applied to the list
    number_filters: Optional[list[str]] = None
    # if true, then the fields "fromPhoneNrInfos" and "toPhoneNrInfos" will be determined for the calls
    number_infos: Optional[bool] = None
    # if true, will show "tries" as well, meaning phone calls which didn't have an established connection
    show_trys_as_well: Optional[bool] = None
    # Describes a timeframe (from / to)
    timeframe: Optional[TnsTimeframe] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsPhoneCallConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsPhoneCallConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsPhoneCallConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_phone_call_direction import TnsPhoneCallDirection
        from .tns_timeframe import TnsTimeframe

        from .tns_phone_call_direction import TnsPhoneCallDirection
        from .tns_timeframe import TnsTimeframe

        fields: dict[str, Callable[[Any], None]] = {
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "directions": lambda n : setattr(self, 'directions', n.get_collection_of_enum_values(TnsPhoneCallDirection)),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "numberFilters": lambda n : setattr(self, 'number_filters', n.get_collection_of_primitive_values(str)),
            "numberInfos": lambda n : setattr(self, 'number_infos', n.get_bool_value()),
            "showTrysAsWell": lambda n : setattr(self, 'show_trys_as_well', n.get_bool_value()),
            "timeframe": lambda n : setattr(self, 'timeframe', n.get_object_value(TnsTimeframe)),
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
        writer.write_collection_of_enum_values("directions", self.directions)
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_collection_of_primitive_values("numberFilters", self.number_filters)
        writer.write_bool_value("numberInfos", self.number_infos)
        writer.write_bool_value("showTrysAsWell", self.show_trys_as_well)
        writer.write_object_value("timeframe", self.timeframe)
        writer.write_additional_data_value(self.additional_data)
    

