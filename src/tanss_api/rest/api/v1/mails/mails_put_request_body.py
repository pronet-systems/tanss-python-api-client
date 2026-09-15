from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mails_put_request_body_sort_field import MailsPutRequestBody_sortField
    from .mails_put_request_body_sort_order import MailsPutRequestBody_sortOrder

@dataclass
class MailsPutRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Whether access permissions are enforced when listing mails
    check_permissions: Optional[bool] = None
    # Identifier of the company whose mails should be listed
    company_id: Optional[int] = None
    # Whether related ticket information should be loaded alongside each mail
    fetch_ticket_infos: Optional[bool] = None
    # Field the mail list is sorted by
    sort_field: Optional[MailsPutRequestBody_sortField] = None
    # Sort direction of the mail list
    sort_order: Optional[MailsPutRequestBody_sortOrder] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MailsPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MailsPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MailsPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .mails_put_request_body_sort_field import MailsPutRequestBody_sortField
        from .mails_put_request_body_sort_order import MailsPutRequestBody_sortOrder

        from .mails_put_request_body_sort_field import MailsPutRequestBody_sortField
        from .mails_put_request_body_sort_order import MailsPutRequestBody_sortOrder

        fields: dict[str, Callable[[Any], None]] = {
            "checkPermissions": lambda n : setattr(self, 'check_permissions', n.get_bool_value()),
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "fetchTicketInfos": lambda n : setattr(self, 'fetch_ticket_infos', n.get_bool_value()),
            "sortField": lambda n : setattr(self, 'sort_field', n.get_enum_value(MailsPutRequestBody_sortField)),
            "sortOrder": lambda n : setattr(self, 'sort_order', n.get_enum_value(MailsPutRequestBody_sortOrder)),
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
        writer.write_bool_value("checkPermissions", self.check_permissions)
        writer.write_int_value("companyId", self.company_id)
        writer.write_bool_value("fetchTicketInfos", self.fetch_ticket_infos)
        writer.write_enum_value("sortField", self.sort_field)
        writer.write_enum_value("sortOrder", self.sort_order)
        writer.write_additional_data_value(self.additional_data)
    

