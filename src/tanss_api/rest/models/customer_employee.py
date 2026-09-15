from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .assigned_customers import AssignedCustomers
    from .customer_employee_preferred_customer import CustomerEmployee_preferred_customer

@dataclass
class CustomerEmployee(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The active property
    active: Optional[bool] = None
    # The assigned_to_customers property
    assigned_to_customers: Optional[list[AssignedCustomers]] = None
    # The email property
    email: Optional[str] = None
    # The external_id property
    external_id: Optional[str] = None
    # The fax_number property
    fax_number: Optional[str] = None
    # The first_name property
    first_name: Optional[str] = None
    # The function property
    function: Optional[str] = None
    # The id property
    id: Optional[int] = None
    # The initials property
    initials: Optional[str] = None
    # The last_name property
    last_name: Optional[str] = None
    # The mobile_number_1 property
    mobile_number_1: Optional[str] = None
    # The mobile_number_2 property
    mobile_number_2: Optional[str] = None
    # Unix timestamp of the last change to the employee. Matched against the `modified` request parameter.
    modified: Optional[int] = None
    # The name property
    name: Optional[str] = None
    # The phone_number_1 property
    phone_number_1: Optional[str] = None
    # The phone_number_2 property
    phone_number_2: Optional[str] = None
    # Preferred company of the employee. Only present when the request was sent without`preferredCustomers=false`. `id` is `0` and `customer_number` empty when no preferredcompany is set; `external_id` is only filled when one is.
    preferred_customer: Optional[CustomerEmployee_preferred_customer] = None
    # The room property
    room: Optional[str] = None
    # The salutation property
    salutation: Optional[str] = None
    # The title property
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomerEmployee:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomerEmployee
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomerEmployee()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .assigned_customers import AssignedCustomers
        from .customer_employee_preferred_customer import CustomerEmployee_preferred_customer

        from .assigned_customers import AssignedCustomers
        from .customer_employee_preferred_customer import CustomerEmployee_preferred_customer

        fields: dict[str, Callable[[Any], None]] = {
            "active": lambda n : setattr(self, 'active', n.get_bool_value()),
            "assigned_to_customers": lambda n : setattr(self, 'assigned_to_customers', n.get_collection_of_object_values(AssignedCustomers)),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "external_id": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "fax_number": lambda n : setattr(self, 'fax_number', n.get_str_value()),
            "first_name": lambda n : setattr(self, 'first_name', n.get_str_value()),
            "function": lambda n : setattr(self, 'function', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "initials": lambda n : setattr(self, 'initials', n.get_str_value()),
            "last_name": lambda n : setattr(self, 'last_name', n.get_str_value()),
            "mobile_number_1": lambda n : setattr(self, 'mobile_number_1', n.get_str_value()),
            "mobile_number_2": lambda n : setattr(self, 'mobile_number_2', n.get_str_value()),
            "modified": lambda n : setattr(self, 'modified', n.get_int_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "phone_number_1": lambda n : setattr(self, 'phone_number_1', n.get_str_value()),
            "phone_number_2": lambda n : setattr(self, 'phone_number_2', n.get_str_value()),
            "preferred_customer": lambda n : setattr(self, 'preferred_customer', n.get_object_value(CustomerEmployee_preferred_customer)),
            "room": lambda n : setattr(self, 'room', n.get_str_value()),
            "salutation": lambda n : setattr(self, 'salutation', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_collection_of_object_values("assigned_to_customers", self.assigned_to_customers)
        writer.write_str_value("email", self.email)
        writer.write_str_value("external_id", self.external_id)
        writer.write_str_value("fax_number", self.fax_number)
        writer.write_str_value("first_name", self.first_name)
        writer.write_str_value("function", self.function)
        writer.write_int_value("id", self.id)
        writer.write_str_value("initials", self.initials)
        writer.write_str_value("last_name", self.last_name)
        writer.write_str_value("mobile_number_1", self.mobile_number_1)
        writer.write_str_value("mobile_number_2", self.mobile_number_2)
        writer.write_int_value("modified", self.modified)
        writer.write_str_value("name", self.name)
        writer.write_str_value("phone_number_1", self.phone_number_1)
        writer.write_str_value("phone_number_2", self.phone_number_2)
        writer.write_object_value("preferred_customer", self.preferred_customer)
        writer.write_str_value("room", self.room)
        writer.write_str_value("salutation", self.salutation)
        writer.write_str_value("title", self.title)
        writer.write_additional_data_value(self.additional_data)
    

