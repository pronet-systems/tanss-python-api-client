from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .......models.logic_operator_type import LogicOperatorType
    from .......models.tns_management_dashboard_chart_filter import TnsManagementDashboardChartFilter
    from .......models.tns_management_dashboard_chart_type import TnsManagementDashboardChartType

@dataclass
class ChartsPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Gelesene Keys des neuen Charts
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Filter eines Dashboard-Charts. DOUGHNUT: incomingTags + sortingTags; FUNNEL: incomingTags + stages.Die Elementtypen der Arrays sind nicht dokumentiert (vermutlich Tag-IDs bzw. Stufen-Objekte).
    filter: Optional[TnsManagementDashboardChartFilter] = None
    # Enum representing the logic linking of certain ids (AND / NOT / OR)
    incoming_type: Optional[LogicOperatorType] = None
    # Name (wird getrimmt, max. 100 Zeichen)
    name: Optional[str] = None
    # Typ eines Dashboard-Charts
    type: Optional[TnsManagementDashboardChartType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ChartsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ChartsPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ChartsPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .......models.logic_operator_type import LogicOperatorType
        from .......models.tns_management_dashboard_chart_filter import TnsManagementDashboardChartFilter
        from .......models.tns_management_dashboard_chart_type import TnsManagementDashboardChartType

        from .......models.logic_operator_type import LogicOperatorType
        from .......models.tns_management_dashboard_chart_filter import TnsManagementDashboardChartFilter
        from .......models.tns_management_dashboard_chart_type import TnsManagementDashboardChartType

        fields: dict[str, Callable[[Any], None]] = {
            "filter": lambda n : setattr(self, 'filter', n.get_object_value(TnsManagementDashboardChartFilter)),
            "incomingType": lambda n : setattr(self, 'incoming_type', n.get_enum_value(LogicOperatorType)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(TnsManagementDashboardChartType)),
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
        writer.write_object_value("filter", self.filter)
        writer.write_enum_value("incomingType", self.incoming_type)
        writer.write_str_value("name", self.name)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

