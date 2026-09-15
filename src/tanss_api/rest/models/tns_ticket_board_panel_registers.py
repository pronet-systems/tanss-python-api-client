from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_ticket_board_panel_register import TnsTicketBoardPanelRegister

@dataclass
class TnsTicketBoardPanelRegisters(AdditionalDataHolder, Parsable):
    """
    Ticket board panel registers
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Array of panel registers
    registers: Optional[list[TnsTicketBoardPanelRegister]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsTicketBoardPanelRegisters:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsTicketBoardPanelRegisters
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsTicketBoardPanelRegisters()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_ticket_board_panel_register import TnsTicketBoardPanelRegister

        from .tns_ticket_board_panel_register import TnsTicketBoardPanelRegister

        fields: dict[str, Callable[[Any], None]] = {
            "registers": lambda n : setattr(self, 'registers', n.get_collection_of_object_values(TnsTicketBoardPanelRegister)),
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
        writer.write_collection_of_object_values("registers", self.registers)
        writer.write_additional_data_value(self.additional_data)
    

