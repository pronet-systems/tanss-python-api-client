from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .with_company_get_response_content_companies import WithCompanyGetResponse_content_companies
    from .with_company_get_response_content_employees import WithCompanyGetResponse_content_employees

@dataclass
class WithCompanyGetResponse_content(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The companies property
    companies: Optional[list[WithCompanyGetResponse_content_companies]] = None
    # The employees property
    employees: Optional[list[WithCompanyGetResponse_content_employees]] = None
    
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
        from .with_company_get_response_content_companies import WithCompanyGetResponse_content_companies
        from .with_company_get_response_content_employees import WithCompanyGetResponse_content_employees

        from .with_company_get_response_content_companies import WithCompanyGetResponse_content_companies
        from .with_company_get_response_content_employees import WithCompanyGetResponse_content_employees

        fields: dict[str, Callable[[Any], None]] = {
            "companies": lambda n : setattr(self, 'companies', n.get_collection_of_object_values(WithCompanyGetResponse_content_companies)),
            "employees": lambda n : setattr(self, 'employees', n.get_collection_of_object_values(WithCompanyGetResponse_content_employees)),
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
        writer.write_collection_of_object_values("companies", self.companies)
        writer.write_collection_of_object_values("employees", self.employees)
        writer.write_additional_data_value(self.additional_data)
    

