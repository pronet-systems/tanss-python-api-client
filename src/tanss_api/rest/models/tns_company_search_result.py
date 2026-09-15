from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_anticipated_callback_search_result import TnsAnticipatedCallbackSearchResult
    from .tns_company_central_type import TnsCompanyCentralType
    from .tns_company_type import TnsCompanyType

@dataclass
class TnsCompanySearchResult(AdditionalDataHolder, Parsable):
    """
    object containing a found company with all associated infos
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The anticipatedCallbacks property
    anticipated_callbacks: Optional[list[TnsAnticipatedCallbackSearchResult]] = None
    # defines, if a company is a central, or a branch (or none of it)
    central_type: Optional[TnsCompanyCentralType] = None
    # city of the company
    city: Optional[str] = None
    # country of the company
    country: Optional[str] = None
    # display if (customer nr.)
    display_id: Optional[str] = None
    # e-Mail of the company
    email: Optional[str] = None
    # fax number
    fax_number: Optional[str] = None
    # id fo the company
    id: Optional[int] = None
    # if the company is incative, info is given here
    inactive: Optional[bool] = None
    # defines, if the company is locked (n service may be entered)
    lockout: Optional[bool] = None
    # mobile phone number (only if its a private customer)
    mobile_number: Optional[str] = None
    # name of the company
    name: Optional[str] = None
    # defines if the company is a "private customer"
    personal_customer: Optional[bool] = None
    # phone number
    phone_number: Optional[str] = None
    # postal code of the company
    post_code: Optional[str] = None
    # private phone number (only if its a private customer)
    private_number: Optional[str] = None
    # street of the company
    street: Optional[str] = None
    # The types property
    types: Optional[list[TnsCompanyType]] = None
    # website of the company
    website: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsCompanySearchResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsCompanySearchResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsCompanySearchResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_anticipated_callback_search_result import TnsAnticipatedCallbackSearchResult
        from .tns_company_central_type import TnsCompanyCentralType
        from .tns_company_type import TnsCompanyType

        from .tns_anticipated_callback_search_result import TnsAnticipatedCallbackSearchResult
        from .tns_company_central_type import TnsCompanyCentralType
        from .tns_company_type import TnsCompanyType

        fields: dict[str, Callable[[Any], None]] = {
            "anticipatedCallbacks": lambda n : setattr(self, 'anticipated_callbacks', n.get_collection_of_object_values(TnsAnticipatedCallbackSearchResult)),
            "centralType": lambda n : setattr(self, 'central_type', n.get_enum_value(TnsCompanyCentralType)),
            "city": lambda n : setattr(self, 'city', n.get_str_value()),
            "country": lambda n : setattr(self, 'country', n.get_str_value()),
            "displayId": lambda n : setattr(self, 'display_id', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "faxNumber": lambda n : setattr(self, 'fax_number', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "inactive": lambda n : setattr(self, 'inactive', n.get_bool_value()),
            "lockout": lambda n : setattr(self, 'lockout', n.get_bool_value()),
            "mobileNumber": lambda n : setattr(self, 'mobile_number', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "personalCustomer": lambda n : setattr(self, 'personal_customer', n.get_bool_value()),
            "phoneNumber": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "postCode": lambda n : setattr(self, 'post_code', n.get_str_value()),
            "privateNumber": lambda n : setattr(self, 'private_number', n.get_str_value()),
            "street": lambda n : setattr(self, 'street', n.get_str_value()),
            "types": lambda n : setattr(self, 'types', n.get_collection_of_object_values(TnsCompanyType)),
            "website": lambda n : setattr(self, 'website', n.get_str_value()),
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
        writer.write_collection_of_object_values("anticipatedCallbacks", self.anticipated_callbacks)
        writer.write_enum_value("centralType", self.central_type)
        writer.write_str_value("city", self.city)
        writer.write_str_value("country", self.country)
        writer.write_str_value("displayId", self.display_id)
        writer.write_str_value("email", self.email)
        writer.write_str_value("faxNumber", self.fax_number)
        writer.write_int_value("id", self.id)
        writer.write_bool_value("inactive", self.inactive)
        writer.write_bool_value("lockout", self.lockout)
        writer.write_str_value("mobileNumber", self.mobile_number)
        writer.write_str_value("name", self.name)
        writer.write_bool_value("personalCustomer", self.personal_customer)
        writer.write_str_value("phoneNumber", self.phone_number)
        writer.write_str_value("postCode", self.post_code)
        writer.write_str_value("privateNumber", self.private_number)
        writer.write_str_value("street", self.street)
        writer.write_collection_of_object_values("types", self.types)
        writer.write_str_value("website", self.website)
        writer.write_additional_data_value(self.additional_data)
    

