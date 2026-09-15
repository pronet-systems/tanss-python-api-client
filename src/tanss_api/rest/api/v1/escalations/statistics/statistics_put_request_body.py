from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .statistics_put_request_body_category_ids import StatisticsPutRequestBody_categoryIds
    from .statistics_put_request_body_company_ids import StatisticsPutRequestBody_companyIds
    from .statistics_put_request_body_esc_triggered_timeframe import StatisticsPutRequestBody_escTriggeredTimeframe
    from .statistics_put_request_body_rule_ids import StatisticsPutRequestBody_ruleIds
    from .statistics_put_request_body_ticket_creation_timeframe import StatisticsPutRequestBody_ticketCreationTimeframe

@dataclass
class StatisticsPutRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # IDs of the ticket categories to filter the statistics by
    category_ids: Optional[list[StatisticsPutRequestBody_categoryIds]] = None
    # IDs of the companies to filter the statistics by
    company_ids: Optional[list[StatisticsPutRequestBody_companyIds]] = None
    # Time range restricting results to escalations triggered within it
    esc_triggered_timeframe: Optional[StatisticsPutRequestBody_escTriggeredTimeframe] = None
    # IDs of the escalation rules to include in the statistics
    rule_ids: Optional[list[StatisticsPutRequestBody_ruleIds]] = None
    # Time range restricting results to tickets created within it
    ticket_creation_timeframe: Optional[StatisticsPutRequestBody_ticketCreationTimeframe] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StatisticsPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StatisticsPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return StatisticsPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .statistics_put_request_body_category_ids import StatisticsPutRequestBody_categoryIds
        from .statistics_put_request_body_company_ids import StatisticsPutRequestBody_companyIds
        from .statistics_put_request_body_esc_triggered_timeframe import StatisticsPutRequestBody_escTriggeredTimeframe
        from .statistics_put_request_body_rule_ids import StatisticsPutRequestBody_ruleIds
        from .statistics_put_request_body_ticket_creation_timeframe import StatisticsPutRequestBody_ticketCreationTimeframe

        from .statistics_put_request_body_category_ids import StatisticsPutRequestBody_categoryIds
        from .statistics_put_request_body_company_ids import StatisticsPutRequestBody_companyIds
        from .statistics_put_request_body_esc_triggered_timeframe import StatisticsPutRequestBody_escTriggeredTimeframe
        from .statistics_put_request_body_rule_ids import StatisticsPutRequestBody_ruleIds
        from .statistics_put_request_body_ticket_creation_timeframe import StatisticsPutRequestBody_ticketCreationTimeframe

        fields: dict[str, Callable[[Any], None]] = {
            "categoryIds": lambda n : setattr(self, 'category_ids', n.get_collection_of_object_values(StatisticsPutRequestBody_categoryIds)),
            "companyIds": lambda n : setattr(self, 'company_ids', n.get_collection_of_object_values(StatisticsPutRequestBody_companyIds)),
            "escTriggeredTimeframe": lambda n : setattr(self, 'esc_triggered_timeframe', n.get_object_value(StatisticsPutRequestBody_escTriggeredTimeframe)),
            "ruleIds": lambda n : setattr(self, 'rule_ids', n.get_collection_of_object_values(StatisticsPutRequestBody_ruleIds)),
            "ticketCreationTimeframe": lambda n : setattr(self, 'ticket_creation_timeframe', n.get_object_value(StatisticsPutRequestBody_ticketCreationTimeframe)),
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
        writer.write_collection_of_object_values("categoryIds", self.category_ids)
        writer.write_collection_of_object_values("companyIds", self.company_ids)
        writer.write_object_value("escTriggeredTimeframe", self.esc_triggered_timeframe)
        writer.write_collection_of_object_values("ruleIds", self.rule_ids)
        writer.write_object_value("ticketCreationTimeframe", self.ticket_creation_timeframe)
        writer.write_additional_data_value(self.additional_data)
    

