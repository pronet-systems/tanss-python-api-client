from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ticket_workflow_post_request_body_vars import TicketWorkflowPostRequestBody_vars

@dataclass
class TicketWorkflowPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Identifier of the selected multi-select option for the workflow landing page.
    multi_select_id: Optional[int] = None
    # Free-text remark associated with the landing page selection.
    remark: Optional[str] = None
    # Optional service cap value applied to the workflow.
    service_cap: Optional[float] = None
    # Map of additional key/value variables for the landing page.
    vars: Optional[TicketWorkflowPostRequestBody_vars] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TicketWorkflowPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TicketWorkflowPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TicketWorkflowPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ticket_workflow_post_request_body_vars import TicketWorkflowPostRequestBody_vars

        from .ticket_workflow_post_request_body_vars import TicketWorkflowPostRequestBody_vars

        fields: dict[str, Callable[[Any], None]] = {
            "multiSelectId": lambda n : setattr(self, 'multi_select_id', n.get_int_value()),
            "remark": lambda n : setattr(self, 'remark', n.get_str_value()),
            "serviceCap": lambda n : setattr(self, 'service_cap', n.get_float_value()),
            "vars": lambda n : setattr(self, 'vars', n.get_object_value(TicketWorkflowPostRequestBody_vars)),
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
        writer.write_int_value("multiSelectId", self.multi_select_id)
        writer.write_str_value("remark", self.remark)
        writer.write_float_value("serviceCap", self.service_cap)
        writer.write_object_value("vars", self.vars)
        writer.write_additional_data_value(self.additional_data)
    

