from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class WithCompanyGetResponse_content(AdditionalDataHolder, Parsable):
    """
    object with recommended/unwanted technician ids and their ranking.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The companyId property
    company_id: Optional[int] = None
    # The recommendedEmployeeIds property
    recommended_employee_ids: Optional[list[int]] = None
    # The unwantedEmployeeIds property
    unwanted_employee_ids: Optional[list[int]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WithCompanyGetResponse_content:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WithCompanyGetResponse_content
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WithCompanyGetResponse_content()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "recommendedEmployeeIds": lambda n : setattr(self, 'recommended_employee_ids', n.get_collection_of_primitive_values(int)),
            "unwantedEmployeeIds": lambda n : setattr(self, 'unwanted_employee_ids', n.get_collection_of_primitive_values(int)),
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
        writer.write_collection_of_primitive_values("recommendedEmployeeIds", self.recommended_employee_ids)
        writer.write_collection_of_primitive_values("unwantedEmployeeIds", self.unwanted_employee_ids)
        writer.write_additional_data_value(self.additional_data)
    

