from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .parameters_put_request_body_strategy import ParametersPutRequestBody_strategy

@dataclass
class ParametersPutRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Identifier of the company the contract lookup applies to.
    company_id: Optional[int] = None
    # Reference timestamp for which the applicable contract is queried.
    date: Optional[int] = None
    # Identifier of the employee associated with the query.
    employee_id: Optional[int] = None
    # Whether an installation fee applies.
    installation_fee: Optional[bool] = None
    # Identifier of the linked entity.
    link_id: Optional[int] = None
    # Type identifier of the linked entity.
    link_type_id: Optional[int] = None
    # Identifier of the priority.
    priority_id: Optional[int] = None
    # Query strategy determining how matching contracts are resolved.
    strategy: Optional[ParametersPutRequestBody_strategy] = None
    # Identifier of the support location (e.g. on-site or remote).
    support_location_id: Optional[int] = None
    # Identifier of the support type.
    support_type_id: Optional[int] = None
    # Identifier of the ticket type.
    ticket_type_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ParametersPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ParametersPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ParametersPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .parameters_put_request_body_strategy import ParametersPutRequestBody_strategy

        from .parameters_put_request_body_strategy import ParametersPutRequestBody_strategy

        fields: dict[str, Callable[[Any], None]] = {
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "date": lambda n : setattr(self, 'date', n.get_int_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "installationFee": lambda n : setattr(self, 'installation_fee', n.get_bool_value()),
            "linkId": lambda n : setattr(self, 'link_id', n.get_int_value()),
            "linkTypeId": lambda n : setattr(self, 'link_type_id', n.get_int_value()),
            "priorityId": lambda n : setattr(self, 'priority_id', n.get_int_value()),
            "strategy": lambda n : setattr(self, 'strategy', n.get_enum_value(ParametersPutRequestBody_strategy)),
            "supportLocationId": lambda n : setattr(self, 'support_location_id', n.get_int_value()),
            "supportTypeId": lambda n : setattr(self, 'support_type_id', n.get_int_value()),
            "ticketTypeId": lambda n : setattr(self, 'ticket_type_id', n.get_int_value()),
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
        writer.write_int_value("date", self.date)
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_bool_value("installationFee", self.installation_fee)
        writer.write_int_value("linkId", self.link_id)
        writer.write_int_value("linkTypeId", self.link_type_id)
        writer.write_int_value("priorityId", self.priority_id)
        writer.write_enum_value("strategy", self.strategy)
        writer.write_int_value("supportLocationId", self.support_location_id)
        writer.write_int_value("supportTypeId", self.support_type_id)
        writer.write_int_value("ticketTypeId", self.ticket_type_id)
        writer.write_additional_data_value(self.additional_data)
    

