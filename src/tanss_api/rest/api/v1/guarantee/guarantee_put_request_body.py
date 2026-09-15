from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .guarantee_put_request_body_company_ids import GuaranteePutRequestBody_companyIds
    from .guarantee_put_request_body_link_types import GuaranteePutRequestBody_linkTypes

@dataclass
class GuaranteePutRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Identifiers of the companies to filter guarantee data for.
    company_ids: Optional[list[GuaranteePutRequestBody_companyIds]] = None
    # Identifier of the component type to filter by.
    component_type_id: Optional[int] = None
    # Number of days a guarantee has been expired within which to include entries.
    expired_since_days: Optional[int] = None
    # Number of upcoming days within which an expiring guarantee should be included.
    expires_in_days: Optional[int] = None
    # Whether guarantee information should be fetched.
    fetch_guarantee: Optional[bool] = None
    # Whether warranty information should be fetched.
    fetch_warranty: Optional[bool] = None
    # Device link types to include.
    link_types: Optional[list[GuaranteePutRequestBody_linkTypes]] = None
    # Identifier of the periphery type to filter by.
    periphery_type_id: Optional[int] = None
    # Whether portal-level values should be applied to the query.
    use_portal_values: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GuaranteePutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GuaranteePutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GuaranteePutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .guarantee_put_request_body_company_ids import GuaranteePutRequestBody_companyIds
        from .guarantee_put_request_body_link_types import GuaranteePutRequestBody_linkTypes

        from .guarantee_put_request_body_company_ids import GuaranteePutRequestBody_companyIds
        from .guarantee_put_request_body_link_types import GuaranteePutRequestBody_linkTypes

        fields: dict[str, Callable[[Any], None]] = {
            "companyIds": lambda n : setattr(self, 'company_ids', n.get_collection_of_object_values(GuaranteePutRequestBody_companyIds)),
            "componentTypeId": lambda n : setattr(self, 'component_type_id', n.get_int_value()),
            "expiredSinceDays": lambda n : setattr(self, 'expired_since_days', n.get_int_value()),
            "expiresInDays": lambda n : setattr(self, 'expires_in_days', n.get_int_value()),
            "fetchGuarantee": lambda n : setattr(self, 'fetch_guarantee', n.get_bool_value()),
            "fetchWarranty": lambda n : setattr(self, 'fetch_warranty', n.get_bool_value()),
            "linkTypes": lambda n : setattr(self, 'link_types', n.get_collection_of_object_values(GuaranteePutRequestBody_linkTypes)),
            "peripheryTypeId": lambda n : setattr(self, 'periphery_type_id', n.get_int_value()),
            "usePortalValues": lambda n : setattr(self, 'use_portal_values', n.get_bool_value()),
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
        writer.write_collection_of_object_values("companyIds", self.company_ids)
        writer.write_int_value("componentTypeId", self.component_type_id)
        writer.write_int_value("expiredSinceDays", self.expired_since_days)
        writer.write_int_value("expiresInDays", self.expires_in_days)
        writer.write_bool_value("fetchGuarantee", self.fetch_guarantee)
        writer.write_bool_value("fetchWarranty", self.fetch_warranty)
        writer.write_collection_of_object_values("linkTypes", self.link_types)
        writer.write_int_value("peripheryTypeId", self.periphery_type_id)
        writer.write_bool_value("usePortalValues", self.use_portal_values)
        writer.write_additional_data_value(self.additional_data)
    

