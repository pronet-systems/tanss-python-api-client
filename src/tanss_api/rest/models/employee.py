from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class Employee(AdditionalDataHolder, Parsable):
    """
    object representing an employee
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # id of the accounting type for this employee
    accounting_type_id: Optional[int] = None
    # true if the employee is active
    active: Optional[bool] = None
    # birthday in the format "YYYY-MM-DD"
    birthday: Optional[str] = None
    # if this employee is assigned to a specific car, the id goes here
    car_id: Optional[int] = None
    # id of the department which tis employee is assigned to
    department_id: Optional[int] = None
    # e-Mail address
    email_address: Optional[str] = None
    # The erpNumber property
    erp_number: Optional[str] = None
    # first name of the employee
    first_name: Optional[str] = None
    # The id property
    id: Optional[int] = None
    # initials for this employee
    initials: Optional[str] = None
    # language which this employee uses
    language: Optional[str] = None
    # last name of the employee
    last_name: Optional[str] = None
    # second mobile telephone number
    mobile_number_two: Optional[str] = None
    # mobile telephone number
    mobile_phone: Optional[str] = None
    # full name of the employee
    name: Optional[str] = None
    # fax number
    personal_fax_number: Optional[str] = None
    # private telephone number
    private_phone_number: Optional[str] = None
    # true, if the user has a "restricted" user license (if he/she is from the own company). restricted user licenses won't use a user license
    restricted_user_license: Optional[bool] = None
    # role for this employee
    role: Optional[str] = None
    # location / room of the employee
    room: Optional[str] = None
    # id of the salutation for this employee
    salutation_id: Optional[int] = None
    # main telephone number
    telephone_number: Optional[str] = None
    # second telephone number
    telephone_number_two: Optional[str] = None
    # if the employee uses a title, the id goes here
    title_id: Optional[int] = None
    # working hour model for this employee
    working_hour_model_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Employee:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Employee
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Employee()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "accountingTypeId": lambda n : setattr(self, 'accounting_type_id', n.get_int_value()),
            "active": lambda n : setattr(self, 'active', n.get_bool_value()),
            "birthday": lambda n : setattr(self, 'birthday', n.get_str_value()),
            "carId": lambda n : setattr(self, 'car_id', n.get_int_value()),
            "departmentId": lambda n : setattr(self, 'department_id', n.get_int_value()),
            "emailAddress": lambda n : setattr(self, 'email_address', n.get_str_value()),
            "erpNumber": lambda n : setattr(self, 'erp_number', n.get_str_value()),
            "firstName": lambda n : setattr(self, 'first_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "initials": lambda n : setattr(self, 'initials', n.get_str_value()),
            "language": lambda n : setattr(self, 'language', n.get_str_value()),
            "lastName": lambda n : setattr(self, 'last_name', n.get_str_value()),
            "mobileNumberTwo": lambda n : setattr(self, 'mobile_number_two', n.get_str_value()),
            "mobilePhone": lambda n : setattr(self, 'mobile_phone', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "personalFaxNumber": lambda n : setattr(self, 'personal_fax_number', n.get_str_value()),
            "privatePhoneNumber": lambda n : setattr(self, 'private_phone_number', n.get_str_value()),
            "restrictedUserLicense": lambda n : setattr(self, 'restricted_user_license', n.get_bool_value()),
            "role": lambda n : setattr(self, 'role', n.get_str_value()),
            "room": lambda n : setattr(self, 'room', n.get_str_value()),
            "salutationId": lambda n : setattr(self, 'salutation_id', n.get_int_value()),
            "telephoneNumber": lambda n : setattr(self, 'telephone_number', n.get_str_value()),
            "telephoneNumberTwo": lambda n : setattr(self, 'telephone_number_two', n.get_str_value()),
            "titleId": lambda n : setattr(self, 'title_id', n.get_int_value()),
            "workingHourModelId": lambda n : setattr(self, 'working_hour_model_id', n.get_int_value()),
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
        writer.write_int_value("accountingTypeId", self.accounting_type_id)
        writer.write_bool_value("active", self.active)
        writer.write_str_value("birthday", self.birthday)
        writer.write_int_value("carId", self.car_id)
        writer.write_int_value("departmentId", self.department_id)
        writer.write_str_value("emailAddress", self.email_address)
        writer.write_str_value("erpNumber", self.erp_number)
        writer.write_str_value("firstName", self.first_name)
        writer.write_str_value("initials", self.initials)
        writer.write_str_value("language", self.language)
        writer.write_str_value("lastName", self.last_name)
        writer.write_str_value("mobileNumberTwo", self.mobile_number_two)
        writer.write_str_value("mobilePhone", self.mobile_phone)
        writer.write_str_value("name", self.name)
        writer.write_str_value("personalFaxNumber", self.personal_fax_number)
        writer.write_str_value("privatePhoneNumber", self.private_phone_number)
        writer.write_bool_value("restrictedUserLicense", self.restricted_user_license)
        writer.write_str_value("role", self.role)
        writer.write_str_value("room", self.room)
        writer.write_int_value("salutationId", self.salutation_id)
        writer.write_str_value("telephoneNumber", self.telephone_number)
        writer.write_str_value("telephoneNumberTwo", self.telephone_number_two)
        writer.write_int_value("titleId", self.title_id)
        writer.write_int_value("workingHourModelId", self.working_hour_model_id)
        writer.write_additional_data_value(self.additional_data)
    

