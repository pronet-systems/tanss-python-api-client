from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_company_search_result import TnsCompanySearchResult
    from .tns_employee_search_result import TnsEmployeeSearchResult
    from .tns_ticket_search_result import TnsTicketSearchResult

@dataclass
class TnsSearchResult(AdditionalDataHolder, Parsable):
    """
    object representing the search results
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The companies property
    companies: Optional[list[TnsCompanySearchResult]] = None
    # The employees property
    employees: Optional[list[TnsEmployeeSearchResult]] = None
    # The tickets property
    tickets: Optional[list[TnsTicketSearchResult]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsSearchResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsSearchResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsSearchResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_company_search_result import TnsCompanySearchResult
        from .tns_employee_search_result import TnsEmployeeSearchResult
        from .tns_ticket_search_result import TnsTicketSearchResult

        from .tns_company_search_result import TnsCompanySearchResult
        from .tns_employee_search_result import TnsEmployeeSearchResult
        from .tns_ticket_search_result import TnsTicketSearchResult

        fields: dict[str, Callable[[Any], None]] = {
            "companies": lambda n : setattr(self, 'companies', n.get_collection_of_object_values(TnsCompanySearchResult)),
            "employees": lambda n : setattr(self, 'employees', n.get_collection_of_object_values(TnsEmployeeSearchResult)),
            "tickets": lambda n : setattr(self, 'tickets', n.get_collection_of_object_values(TnsTicketSearchResult)),
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
        writer.write_collection_of_object_values("tickets", self.tickets)
        writer.write_additional_data_value(self.additional_data)
    

