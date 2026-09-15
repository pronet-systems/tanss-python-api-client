from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_management_dashboard_chart_filter_incoming_tags import TnsManagementDashboardChartFilter_incomingTags
    from .tns_management_dashboard_chart_filter_sorting_tags import TnsManagementDashboardChartFilter_sortingTags
    from .tns_management_dashboard_chart_filter_stages import TnsManagementDashboardChartFilter_stages

@dataclass
class TnsManagementDashboardChartFilter(AdditionalDataHolder, Parsable):
    """
    Filter eines Dashboard-Charts. DOUGHNUT: incomingTags + sortingTags; FUNNEL: incomingTags + stages.Die Elementtypen der Arrays sind nicht dokumentiert (vermutlich Tag-IDs bzw. Stufen-Objekte).
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Eingangs-Tags
    incoming_tags: Optional[list[TnsManagementDashboardChartFilter_incomingTags]] = None
    # Sortier-Tags (nur DOUGHNUT)
    sorting_tags: Optional[list[TnsManagementDashboardChartFilter_sortingTags]] = None
    # Stufen (nur FUNNEL)
    stages: Optional[list[TnsManagementDashboardChartFilter_stages]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsManagementDashboardChartFilter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsManagementDashboardChartFilter
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsManagementDashboardChartFilter()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_management_dashboard_chart_filter_incoming_tags import TnsManagementDashboardChartFilter_incomingTags
        from .tns_management_dashboard_chart_filter_sorting_tags import TnsManagementDashboardChartFilter_sortingTags
        from .tns_management_dashboard_chart_filter_stages import TnsManagementDashboardChartFilter_stages

        from .tns_management_dashboard_chart_filter_incoming_tags import TnsManagementDashboardChartFilter_incomingTags
        from .tns_management_dashboard_chart_filter_sorting_tags import TnsManagementDashboardChartFilter_sortingTags
        from .tns_management_dashboard_chart_filter_stages import TnsManagementDashboardChartFilter_stages

        fields: dict[str, Callable[[Any], None]] = {
            "incomingTags": lambda n : setattr(self, 'incoming_tags', n.get_collection_of_object_values(TnsManagementDashboardChartFilter_incomingTags)),
            "sortingTags": lambda n : setattr(self, 'sorting_tags', n.get_collection_of_object_values(TnsManagementDashboardChartFilter_sortingTags)),
            "stages": lambda n : setattr(self, 'stages', n.get_collection_of_object_values(TnsManagementDashboardChartFilter_stages)),
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
        writer.write_collection_of_object_values("incomingTags", self.incoming_tags)
        writer.write_collection_of_object_values("sortingTags", self.sorting_tags)
        writer.write_collection_of_object_values("stages", self.stages)
        writer.write_additional_data_value(self.additional_data)
    

