from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ticket_standard import TicketStandard

@dataclass
class TnsCustomerPortalCompleteWizardResult(AdditionalDataHolder, Parsable):
    """
    Ergebnis des Wizard-Abschlusses
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The createdTicket property
    created_ticket: Optional[TicketStandard] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsCustomerPortalCompleteWizardResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsCustomerPortalCompleteWizardResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsCustomerPortalCompleteWizardResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ticket_standard import TicketStandard

        from .ticket_standard import TicketStandard

        fields: dict[str, Callable[[Any], None]] = {
            "createdTicket": lambda n : setattr(self, 'created_ticket', n.get_object_value(TicketStandard)),
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
        writer.write_object_value("createdTicket", self.created_ticket)
        writer.write_additional_data_value(self.additional_data)
    

