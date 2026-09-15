from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .calculate_put_request_body_additional_support_for_calculation import CalculatePutRequestBody_additionalSupportForCalculation

@dataclass
class CalculatePutRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Additional support entries to include in the calculation, e.g. to test whether they fit into the remaining quota.
    additional_support_for_calculation: Optional[list[CalculatePutRequestBody_additionalSupportForCalculation]] = None
    # Whether the calculated quota may go negative.
    allow_negative: Optional[bool] = None
    # Requires showCompleteHistory; if true, recalculates all booked entries from the beginning instead of using stored values.
    calculate_all_over_again: Optional[bool] = None
    # Support entry id to exclude from the calculation.
    exclude_support_id: Optional[int] = None
    # If true, already booked support entries are included; otherwise only unbooked ones are considered.
    show_complete_history: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CalculatePutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CalculatePutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CalculatePutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .calculate_put_request_body_additional_support_for_calculation import CalculatePutRequestBody_additionalSupportForCalculation

        from .calculate_put_request_body_additional_support_for_calculation import CalculatePutRequestBody_additionalSupportForCalculation

        fields: dict[str, Callable[[Any], None]] = {
            "additionalSupportForCalculation": lambda n : setattr(self, 'additional_support_for_calculation', n.get_collection_of_object_values(CalculatePutRequestBody_additionalSupportForCalculation)),
            "allowNegative": lambda n : setattr(self, 'allow_negative', n.get_bool_value()),
            "calculateAllOverAgain": lambda n : setattr(self, 'calculate_all_over_again', n.get_bool_value()),
            "excludeSupportId": lambda n : setattr(self, 'exclude_support_id', n.get_int_value()),
            "showCompleteHistory": lambda n : setattr(self, 'show_complete_history', n.get_bool_value()),
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
        writer.write_collection_of_object_values("additionalSupportForCalculation", self.additional_support_for_calculation)
        writer.write_bool_value("allowNegative", self.allow_negative)
        writer.write_bool_value("calculateAllOverAgain", self.calculate_all_over_again)
        writer.write_int_value("excludeSupportId", self.exclude_support_id)
        writer.write_bool_value("showCompleteHistory", self.show_complete_history)
        writer.write_additional_data_value(self.additional_data)
    

