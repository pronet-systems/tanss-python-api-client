from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_ticket_board_panel import TnsTicketBoardPanel

@dataclass
class TnsTicketBoard(AdditionalDataHolder, Parsable):
    """
    Ticket board
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Array of panels
    panels: Optional[list[TnsTicketBoardPanel]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsTicketBoard:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsTicketBoard
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsTicketBoard()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_ticket_board_panel import TnsTicketBoardPanel

        from .tns_ticket_board_panel import TnsTicketBoardPanel

        fields: dict[str, Callable[[Any], None]] = {
            "panels": lambda n : setattr(self, 'panels', n.get_collection_of_object_values(TnsTicketBoardPanel)),
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
        writer.write_collection_of_object_values("panels", self.panels)
        writer.write_additional_data_value(self.additional_data)
    

