from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.employee import Employee
    from .....models.tns_employee_list_type import TnsEmployeeListType

@dataclass
class OwnStateGetResponse_content(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The apiVersion property
    api_version: Optional[str] = None
    # The companyAccess property
    company_access: Optional[list[int]] = None
    # object representing an employee
    logged_in_user: Optional[Employee] = None
    # The ownCompanyId property
    own_company_id: Optional[int] = None
    # The rights property
    rights: Optional[list[int]] = None
    # The unseenEvents property
    unseen_events: Optional[int] = None
    # informtation about the "type" of the employee (this info is not always given)
    user_type: Optional[TnsEmployeeListType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OwnStateGetResponse_content:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OwnStateGetResponse_content
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OwnStateGetResponse_content()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .....models.employee import Employee
        from .....models.tns_employee_list_type import TnsEmployeeListType

        from .....models.employee import Employee
        from .....models.tns_employee_list_type import TnsEmployeeListType

        fields: dict[str, Callable[[Any], None]] = {
            "apiVersion": lambda n : setattr(self, 'api_version', n.get_str_value()),
            "companyAccess": lambda n : setattr(self, 'company_access', n.get_collection_of_primitive_values(int)),
            "loggedInUser": lambda n : setattr(self, 'logged_in_user', n.get_object_value(Employee)),
            "ownCompanyId": lambda n : setattr(self, 'own_company_id', n.get_int_value()),
            "rights": lambda n : setattr(self, 'rights', n.get_collection_of_primitive_values(int)),
            "unseenEvents": lambda n : setattr(self, 'unseen_events', n.get_int_value()),
            "userType": lambda n : setattr(self, 'user_type', n.get_enum_value(TnsEmployeeListType)),
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
        writer.write_str_value("apiVersion", self.api_version)
        writer.write_collection_of_primitive_values("companyAccess", self.company_access)
        writer.write_object_value("loggedInUser", self.logged_in_user)
        writer.write_int_value("ownCompanyId", self.own_company_id)
        writer.write_collection_of_primitive_values("rights", self.rights)
        writer.write_int_value("unseenEvents", self.unseen_events)
        writer.write_enum_value("userType", self.user_type)
        writer.write_additional_data_value(self.additional_data)
    

