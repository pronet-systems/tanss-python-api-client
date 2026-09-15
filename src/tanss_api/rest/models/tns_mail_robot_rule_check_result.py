from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .company_detail import CompanyDetail
    from .employee import Employee
    from .ticket_standard import TicketStandard
    from .tns_callback import TnsCallback
    from .tns_document import TnsDocument
    from .tns_mail import TnsMail
    from .tns_support import TnsSupport

@dataclass
class TnsMailRobotRuleCheckResult(AdditionalDataHolder, Parsable):
    """
    Ergebnis-Collector eines Mailroboter-Regellaufs. Die JSON-Schlüssel sind im Bytecode obfuskiert; die Feldnamen hier sind aus dem Inhalt abgeleitet und unsicher.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The callbacks property
    callbacks: Optional[list[TnsCallback]] = None
    # The companies property
    companies: Optional[list[CompanyDetail]] = None
    # The documents property
    documents: Optional[list[TnsDocument]] = None
    # The employees property
    employees: Optional[list[Employee]] = None
    # The log property
    log: Optional[list[str]] = None
    # The mails property
    mails: Optional[list[TnsMail]] = None
    # The supports property
    supports: Optional[list[TnsSupport]] = None
    # The tickets property
    tickets: Optional[list[TicketStandard]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsMailRobotRuleCheckResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsMailRobotRuleCheckResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsMailRobotRuleCheckResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .company_detail import CompanyDetail
        from .employee import Employee
        from .ticket_standard import TicketStandard
        from .tns_callback import TnsCallback
        from .tns_document import TnsDocument
        from .tns_mail import TnsMail
        from .tns_support import TnsSupport

        from .company_detail import CompanyDetail
        from .employee import Employee
        from .ticket_standard import TicketStandard
        from .tns_callback import TnsCallback
        from .tns_document import TnsDocument
        from .tns_mail import TnsMail
        from .tns_support import TnsSupport

        fields: dict[str, Callable[[Any], None]] = {
            "callbacks": lambda n : setattr(self, 'callbacks', n.get_collection_of_object_values(TnsCallback)),
            "companies": lambda n : setattr(self, 'companies', n.get_collection_of_object_values(CompanyDetail)),
            "documents": lambda n : setattr(self, 'documents', n.get_collection_of_object_values(TnsDocument)),
            "employees": lambda n : setattr(self, 'employees', n.get_collection_of_object_values(Employee)),
            "log": lambda n : setattr(self, 'log', n.get_collection_of_primitive_values(str)),
            "mails": lambda n : setattr(self, 'mails', n.get_collection_of_object_values(TnsMail)),
            "supports": lambda n : setattr(self, 'supports', n.get_collection_of_object_values(TnsSupport)),
            "tickets": lambda n : setattr(self, 'tickets', n.get_collection_of_object_values(TicketStandard)),
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
        writer.write_collection_of_object_values("callbacks", self.callbacks)
        writer.write_collection_of_object_values("companies", self.companies)
        writer.write_collection_of_object_values("documents", self.documents)
        writer.write_collection_of_object_values("employees", self.employees)
        writer.write_collection_of_primitive_values("log", self.log)
        writer.write_collection_of_object_values("mails", self.mails)
        writer.write_collection_of_object_values("supports", self.supports)
        writer.write_collection_of_object_values("tickets", self.tickets)
        writer.write_additional_data_value(self.additional_data)
    

