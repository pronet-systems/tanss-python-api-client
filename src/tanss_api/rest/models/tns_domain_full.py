from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_domain import TnsDomain

from .tns_domain import TnsDomain

@dataclass
class TnsDomainFull(TnsDomain, Parsable):
    # url for administration of this domain
    admin_url: Optional[str] = None
    # link id "adminc" (id of company or employee, based on link type)
    adminc: Optional[int] = None
    # link type for "adminc" (company or employee link types possible)
    adminc_link_type_id: Optional[int] = None
    # certificate
    certificate: Optional[str] = None
    # certificate chain
    certificate_ca: Optional[str] = None
    # end time of the contract
    contract_duration_end: Optional[int] = None
    # start time of the contract
    contract_duration_start: Optional[int] = None
    # customer number
    customer_id: Optional[str] = None
    # if this domain is forwarded to another domain, give the id here
    forward_domain_id: Optional[int] = None
    # IP V4 address
    ipv4: Optional[str] = None
    # IP V6 address
    ipv6: Optional[str] = None
    # login name
    login_name: Optional[str] = None
    # login password
    login_password: Optional[str] = None
    # link id "owner" (id of company or employee, based on link type)
    owner: Optional[int] = None
    # link type for "owner" (company or employee link types possible)
    owner_link_type_id: Optional[int] = None
    # Name of the provider
    provider_name: Optional[str] = None
    # purchase price
    purchase_price: Optional[float] = None
    # id of the employee who is responsible for this domain
    responsible_tech_id: Optional[int] = None
    # selling price
    selling_price: Optional[float] = None
    # link id "techc" (id of company or employee, based on link type)
    techc: Optional[int] = None
    # link type for "techc" (company or employee link types possible)
    techc_link_type_id: Optional[int] = None
    # usage for this domain (text)
    utilization: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsDomainFull:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsDomainFull
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsDomainFull()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_domain import TnsDomain

        from .tns_domain import TnsDomain

        fields: dict[str, Callable[[Any], None]] = {
            "adminUrl": lambda n : setattr(self, 'admin_url', n.get_str_value()),
            "adminc": lambda n : setattr(self, 'adminc', n.get_int_value()),
            "admincLinkTypeId": lambda n : setattr(self, 'adminc_link_type_id', n.get_int_value()),
            "certificate": lambda n : setattr(self, 'certificate', n.get_str_value()),
            "certificateCa": lambda n : setattr(self, 'certificate_ca', n.get_str_value()),
            "contractDurationEnd": lambda n : setattr(self, 'contract_duration_end', n.get_int_value()),
            "contractDurationStart": lambda n : setattr(self, 'contract_duration_start', n.get_int_value()),
            "customerId": lambda n : setattr(self, 'customer_id', n.get_str_value()),
            "forwardDomainId": lambda n : setattr(self, 'forward_domain_id', n.get_int_value()),
            "ipv4": lambda n : setattr(self, 'ipv4', n.get_str_value()),
            "ipv6": lambda n : setattr(self, 'ipv6', n.get_str_value()),
            "loginName": lambda n : setattr(self, 'login_name', n.get_str_value()),
            "loginPassword": lambda n : setattr(self, 'login_password', n.get_str_value()),
            "owner": lambda n : setattr(self, 'owner', n.get_int_value()),
            "ownerLinkTypeId": lambda n : setattr(self, 'owner_link_type_id', n.get_int_value()),
            "providerName": lambda n : setattr(self, 'provider_name', n.get_str_value()),
            "purchasePrice": lambda n : setattr(self, 'purchase_price', n.get_float_value()),
            "responsibleTechId": lambda n : setattr(self, 'responsible_tech_id', n.get_int_value()),
            "sellingPrice": lambda n : setattr(self, 'selling_price', n.get_float_value()),
            "techc": lambda n : setattr(self, 'techc', n.get_int_value()),
            "techcLinkTypeId": lambda n : setattr(self, 'techc_link_type_id', n.get_int_value()),
            "utilization": lambda n : setattr(self, 'utilization', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("adminUrl", self.admin_url)
        writer.write_int_value("adminc", self.adminc)
        writer.write_int_value("admincLinkTypeId", self.adminc_link_type_id)
        writer.write_str_value("certificate", self.certificate)
        writer.write_str_value("certificateCa", self.certificate_ca)
        writer.write_int_value("contractDurationEnd", self.contract_duration_end)
        writer.write_int_value("contractDurationStart", self.contract_duration_start)
        writer.write_str_value("customerId", self.customer_id)
        writer.write_int_value("forwardDomainId", self.forward_domain_id)
        writer.write_str_value("ipv4", self.ipv4)
        writer.write_str_value("ipv6", self.ipv6)
        writer.write_str_value("loginName", self.login_name)
        writer.write_str_value("loginPassword", self.login_password)
        writer.write_int_value("owner", self.owner)
        writer.write_int_value("ownerLinkTypeId", self.owner_link_type_id)
        writer.write_str_value("providerName", self.provider_name)
        writer.write_float_value("purchasePrice", self.purchase_price)
        writer.write_int_value("responsibleTechId", self.responsible_tech_id)
        writer.write_float_value("sellingPrice", self.selling_price)
        writer.write_int_value("techc", self.techc)
        writer.write_int_value("techcLinkTypeId", self.techc_link_type_id)
        writer.write_str_value("utilization", self.utilization)
    

