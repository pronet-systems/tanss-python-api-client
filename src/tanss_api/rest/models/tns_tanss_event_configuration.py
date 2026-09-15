from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_link_type import TnsLinkType
    from .tns_tanss_event_configuration_confirmed_filter import TnsTanssEventConfigurationConfirmedFilter
    from .tns_tanss_event_configuration_seen_filter import TnsTanssEventConfigurationSeenFilter
    from .tns_tanss_event_trigger_type import TnsTanssEventTriggerType

@dataclass
class TnsTanssEventConfiguration(AdditionalDataHolder, Parsable):
    """
    defines the filter for the activity feed items
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # filter for the field "confirmed"
    confirmed_filter: Optional[TnsTanssEventConfigurationConfirmedFilter] = None
    # if true, additional content will be given(i.e. ticket object)
    include_content: Optional[bool] = None
    # link ids that shall be filtered for
    link_ids: Optional[list[int]] = None
    # The linkTypes property
    link_types: Optional[list[TnsLinkType]] = None
    # if given, will only fetch newer activity feed items
    minimum_creation_date: Optional[int] = None
    # if true, will nor mark item as "seen"
    prevent_view_event: Optional[bool] = None
    # filter for the field "seen"
    seen_filter: Optional[TnsTanssEventConfigurationSeenFilter] = None
    # The triggerTypes property
    trigger_types: Optional[list[TnsTanssEventTriggerType]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsTanssEventConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsTanssEventConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsTanssEventConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_link_type import TnsLinkType
        from .tns_tanss_event_configuration_confirmed_filter import TnsTanssEventConfigurationConfirmedFilter
        from .tns_tanss_event_configuration_seen_filter import TnsTanssEventConfigurationSeenFilter
        from .tns_tanss_event_trigger_type import TnsTanssEventTriggerType

        from .tns_link_type import TnsLinkType
        from .tns_tanss_event_configuration_confirmed_filter import TnsTanssEventConfigurationConfirmedFilter
        from .tns_tanss_event_configuration_seen_filter import TnsTanssEventConfigurationSeenFilter
        from .tns_tanss_event_trigger_type import TnsTanssEventTriggerType

        fields: dict[str, Callable[[Any], None]] = {
            "confirmedFilter": lambda n : setattr(self, 'confirmed_filter', n.get_enum_value(TnsTanssEventConfigurationConfirmedFilter)),
            "includeContent": lambda n : setattr(self, 'include_content', n.get_bool_value()),
            "linkIds": lambda n : setattr(self, 'link_ids', n.get_collection_of_primitive_values(int)),
            "linkTypes": lambda n : setattr(self, 'link_types', n.get_collection_of_enum_values(TnsLinkType)),
            "minimumCreationDate": lambda n : setattr(self, 'minimum_creation_date', n.get_int_value()),
            "preventViewEvent": lambda n : setattr(self, 'prevent_view_event', n.get_bool_value()),
            "seenFilter": lambda n : setattr(self, 'seen_filter', n.get_enum_value(TnsTanssEventConfigurationSeenFilter)),
            "triggerTypes": lambda n : setattr(self, 'trigger_types', n.get_collection_of_enum_values(TnsTanssEventTriggerType)),
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
        writer.write_enum_value("confirmedFilter", self.confirmed_filter)
        writer.write_bool_value("includeContent", self.include_content)
        writer.write_collection_of_primitive_values("linkIds", self.link_ids)
        writer.write_collection_of_enum_values("linkTypes", self.link_types)
        writer.write_int_value("minimumCreationDate", self.minimum_creation_date)
        writer.write_bool_value("preventViewEvent", self.prevent_view_event)
        writer.write_enum_value("seenFilter", self.seen_filter)
        writer.write_collection_of_enum_values("triggerTypes", self.trigger_types)
        writer.write_additional_data_value(self.additional_data)
    

