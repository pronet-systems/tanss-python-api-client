from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_workflow_contract_token_type import TnsWorkflowContractTokenType

@dataclass
class TnsWorkflowContractToken(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # date, when the token was generated
    date: Optional[int] = None
    # date, when the token will expire
    expire: Optional[int] = None
    # id of this token
    id: Optional[int] = None
    # describes the type of a token
    type: Optional[TnsWorkflowContractTokenType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsWorkflowContractToken:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsWorkflowContractToken
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsWorkflowContractToken()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_workflow_contract_token_type import TnsWorkflowContractTokenType

        from .tns_workflow_contract_token_type import TnsWorkflowContractTokenType

        fields: dict[str, Callable[[Any], None]] = {
            "date": lambda n : setattr(self, 'date', n.get_int_value()),
            "expire": lambda n : setattr(self, 'expire', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(TnsWorkflowContractTokenType)),
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
        writer.write_int_value("date", self.date)
        writer.write_int_value("expire", self.expire)
        writer.write_int_value("id", self.id)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

