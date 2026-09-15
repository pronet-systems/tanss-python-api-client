from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .contract_workflow_post_request_body_accept_type import ContractWorkflowPostRequestBody_acceptType
    from .contract_workflow_post_request_body_employees import ContractWorkflowPostRequestBody_employees

@dataclass
class ContractWorkflowPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Whether the contract was accepted or declined
    accept_type: Optional[ContractWorkflowPostRequestBody_acceptType] = None
    # Email address of the approving contact person
    approver_email: Optional[str] = None
    # First name of the approving contact person
    approver_first_name: Optional[str] = None
    # Job function or role of the approver
    approver_function: Optional[str] = None
    # Last name of the approving contact person
    approver_last_name: Optional[str] = None
    # Identifier of the approver's salutation
    approver_salutation_id: Optional[int] = None
    # Address of the company
    company_address: Optional[str] = None
    # Name of the company associated with the contract
    company_name: Optional[str] = None
    # Authorized employees related to the contract
    employees: Optional[list[ContractWorkflowPostRequestBody_employees]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ContractWorkflowPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ContractWorkflowPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ContractWorkflowPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .contract_workflow_post_request_body_accept_type import ContractWorkflowPostRequestBody_acceptType
        from .contract_workflow_post_request_body_employees import ContractWorkflowPostRequestBody_employees

        from .contract_workflow_post_request_body_accept_type import ContractWorkflowPostRequestBody_acceptType
        from .contract_workflow_post_request_body_employees import ContractWorkflowPostRequestBody_employees

        fields: dict[str, Callable[[Any], None]] = {
            "acceptType": lambda n : setattr(self, 'accept_type', n.get_enum_value(ContractWorkflowPostRequestBody_acceptType)),
            "approverEmail": lambda n : setattr(self, 'approver_email', n.get_str_value()),
            "approverFirstName": lambda n : setattr(self, 'approver_first_name', n.get_str_value()),
            "approverFunction": lambda n : setattr(self, 'approver_function', n.get_str_value()),
            "approverLastName": lambda n : setattr(self, 'approver_last_name', n.get_str_value()),
            "approverSalutationId": lambda n : setattr(self, 'approver_salutation_id', n.get_int_value()),
            "companyAddress": lambda n : setattr(self, 'company_address', n.get_str_value()),
            "companyName": lambda n : setattr(self, 'company_name', n.get_str_value()),
            "employees": lambda n : setattr(self, 'employees', n.get_collection_of_object_values(ContractWorkflowPostRequestBody_employees)),
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
        writer.write_enum_value("acceptType", self.accept_type)
        writer.write_str_value("approverEmail", self.approver_email)
        writer.write_str_value("approverFirstName", self.approver_first_name)
        writer.write_str_value("approverFunction", self.approver_function)
        writer.write_str_value("approverLastName", self.approver_last_name)
        writer.write_int_value("approverSalutationId", self.approver_salutation_id)
        writer.write_str_value("companyAddress", self.company_address)
        writer.write_str_value("companyName", self.company_name)
        writer.write_collection_of_object_values("employees", self.employees)
        writer.write_additional_data_value(self.additional_data)
    

