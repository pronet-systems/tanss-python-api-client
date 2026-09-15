from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mail_post_request_body_mail_receivers import MailPostRequestBody_mailReceivers
    from .mail_post_request_body_supplement_sheet import MailPostRequestBody_supplementSheet

@dataclass
class MailPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # List of mail recipients the generated PDF is sent to
    mail_receivers: Optional[list[MailPostRequestBody_mailReceivers]] = None
    # Whether prices are shown in the generated PDF
    prices: Optional[bool] = None
    # Whether a signature field is included in the generated PDF
    signature_field: Optional[bool] = None
    # Type of supplement sheet appended to the PDF
    supplement_sheet: Optional[MailPostRequestBody_supplementSheet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MailPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MailPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MailPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .mail_post_request_body_mail_receivers import MailPostRequestBody_mailReceivers
        from .mail_post_request_body_supplement_sheet import MailPostRequestBody_supplementSheet

        from .mail_post_request_body_mail_receivers import MailPostRequestBody_mailReceivers
        from .mail_post_request_body_supplement_sheet import MailPostRequestBody_supplementSheet

        fields: dict[str, Callable[[Any], None]] = {
            "mailReceivers": lambda n : setattr(self, 'mail_receivers', n.get_collection_of_object_values(MailPostRequestBody_mailReceivers)),
            "prices": lambda n : setattr(self, 'prices', n.get_bool_value()),
            "signatureField": lambda n : setattr(self, 'signature_field', n.get_bool_value()),
            "supplementSheet": lambda n : setattr(self, 'supplement_sheet', n.get_enum_value(MailPostRequestBody_supplementSheet)),
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
        writer.write_collection_of_object_values("mailReceivers", self.mail_receivers)
        writer.write_bool_value("prices", self.prices)
        writer.write_bool_value("signatureField", self.signature_field)
        writer.write_enum_value("supplementSheet", self.supplement_sheet)
        writer.write_additional_data_value(self.additional_data)
    

