from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_anticipated_callback_search_result import TnsAnticipatedCallbackSearchResult

@dataclass
class TnsEmployeeSearchResult(AdditionalDataHolder, Parsable):
    """
    object containing a found employee with all associated infos
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # determines wether an employee is active or not
    active: Optional[bool] = None
    # The anticipatedCallbacks property
    anticipated_callbacks: Optional[list[TnsAnticipatedCallbackSearchResult]] = None
    # ids of all employee categories (if defined in the employee search configuration). The names are given in the "linked entities" - "employeeCategories"
    categories: Optional[list[int]] = None
    # shows assigned companies of this user, the name is given in the "linked entities"
    companies: Optional[list[int]] = None
    # department id of the employee, the name is given in the "linked entities"
    department_id: Optional[str] = None
    # email
    email: Optional[str] = None
    # first name
    first_name: Optional[str] = None
    # id of the employee
    id: Optional[str] = None
    # last name
    last_name: Optional[str] = None
    # mobile phone number
    mobile_nr: Optional[str] = None
    # mobile phone number
    mobile_nr2: Optional[str] = None
    # full (displayed) name
    name: Optional[str] = None
    # phone number
    phone_nr: Optional[str] = None
    # phone number
    phone_nr2: Optional[str] = None
    # private phone number
    private_nr: Optional[str] = None
    # role of the employee
    role: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsEmployeeSearchResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsEmployeeSearchResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsEmployeeSearchResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_anticipated_callback_search_result import TnsAnticipatedCallbackSearchResult

        from .tns_anticipated_callback_search_result import TnsAnticipatedCallbackSearchResult

        fields: dict[str, Callable[[Any], None]] = {
            "active": lambda n : setattr(self, 'active', n.get_bool_value()),
            "anticipatedCallbacks": lambda n : setattr(self, 'anticipated_callbacks', n.get_collection_of_object_values(TnsAnticipatedCallbackSearchResult)),
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_primitive_values(int)),
            "companies": lambda n : setattr(self, 'companies', n.get_collection_of_primitive_values(int)),
            "departmentId": lambda n : setattr(self, 'department_id', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "firstName": lambda n : setattr(self, 'first_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "lastName": lambda n : setattr(self, 'last_name', n.get_str_value()),
            "mobileNr": lambda n : setattr(self, 'mobile_nr', n.get_str_value()),
            "mobileNr2": lambda n : setattr(self, 'mobile_nr2', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "phoneNr": lambda n : setattr(self, 'phone_nr', n.get_str_value()),
            "phoneNr2": lambda n : setattr(self, 'phone_nr2', n.get_str_value()),
            "privateNr": lambda n : setattr(self, 'private_nr', n.get_str_value()),
            "role": lambda n : setattr(self, 'role', n.get_str_value()),
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
        writer.write_bool_value("active", self.active)
        writer.write_collection_of_object_values("anticipatedCallbacks", self.anticipated_callbacks)
        writer.write_collection_of_primitive_values("categories", self.categories)
        writer.write_collection_of_primitive_values("companies", self.companies)
        writer.write_str_value("departmentId", self.department_id)
        writer.write_str_value("email", self.email)
        writer.write_str_value("firstName", self.first_name)
        writer.write_str_value("id", self.id)
        writer.write_str_value("lastName", self.last_name)
        writer.write_str_value("mobileNr", self.mobile_nr)
        writer.write_str_value("mobileNr2", self.mobile_nr2)
        writer.write_str_value("name", self.name)
        writer.write_str_value("phoneNr", self.phone_nr)
        writer.write_str_value("phoneNr2", self.phone_nr2)
        writer.write_str_value("privateNr", self.private_nr)
        writer.write_str_value("role", self.role)
        writer.write_additional_data_value(self.additional_data)
    

