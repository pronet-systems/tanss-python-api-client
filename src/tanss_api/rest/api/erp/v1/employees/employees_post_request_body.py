from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class EmployeesPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Request body.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Whether the employee account is active.
    active: Optional[bool] = None
    # Identifier of the department the employee belongs to.
    department_id: Optional[int] = None
    # Business email address of the employee.
    email_address: Optional[str] = None
    # First name of the employee.
    first_name: Optional[str] = None
    # Unique identifier of the employee.
    id: Optional[int] = None
    # Preferred interface language code of the employee.
    language: Optional[str] = None
    # Last name of the employee.
    last_name: Optional[str] = None
    # Login user name of the employee.
    login: Optional[str] = None
    # Mobile phone number of the employee.
    mobile_phone: Optional[str] = None
    # Display name of the employee.
    name: Optional[str] = None
    # Primary telephone number of the employee.
    telephone_number: Optional[str] = None
    # Identifier of the employee's title.
    title_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EmployeesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EmployeesPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EmployeesPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "active": lambda n : setattr(self, 'active', n.get_bool_value()),
            "departmentId": lambda n : setattr(self, 'department_id', n.get_int_value()),
            "emailAddress": lambda n : setattr(self, 'email_address', n.get_str_value()),
            "firstName": lambda n : setattr(self, 'first_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "language": lambda n : setattr(self, 'language', n.get_str_value()),
            "lastName": lambda n : setattr(self, 'last_name', n.get_str_value()),
            "login": lambda n : setattr(self, 'login', n.get_str_value()),
            "mobilePhone": lambda n : setattr(self, 'mobile_phone', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "telephoneNumber": lambda n : setattr(self, 'telephone_number', n.get_str_value()),
            "titleId": lambda n : setattr(self, 'title_id', n.get_int_value()),
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
        writer.write_int_value("departmentId", self.department_id)
        writer.write_str_value("emailAddress", self.email_address)
        writer.write_str_value("firstName", self.first_name)
        writer.write_str_value("language", self.language)
        writer.write_str_value("lastName", self.last_name)
        writer.write_str_value("login", self.login)
        writer.write_str_value("mobilePhone", self.mobile_phone)
        writer.write_str_value("name", self.name)
        writer.write_str_value("telephoneNumber", self.telephone_number)
        writer.write_int_value("titleId", self.title_id)
        writer.write_additional_data_value(self.additional_data)
    

