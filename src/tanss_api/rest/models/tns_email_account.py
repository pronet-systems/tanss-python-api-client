from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsEmailAccount(AdditionalDataHolder, Parsable):
    """
    describes an email account (mailbox)
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # is this account activated?
    active: Optional[bool] = None
    # list of assigned e-mail addresses
    addresses: Optional[list[str]] = None
    # is this a catch-all-mailbox?
    catch_all_account: Optional[bool] = None
    # mail account is assigned to this company
    company_id: Optional[int] = None
    # will archived mails be sent?
    delete_archived: Optional[bool] = None
    # name of the mailbox / description
    description: Optional[str] = None
    # if the account is assigned to an domain, the id is given here
    domain_id: Optional[int] = None
    # The id property
    id: Optional[int] = None
    # name/address of the incoming mail server
    incoming_server: Optional[str] = None
    # linkId of the assignment for this mail account
    link_id: Optional[int] = None
    # linkType of the assignment for this mail account
    link_type_id: Optional[int] = None
    # login name
    login_name: Optional[str] = None
    # login password
    login_password: Optional[str] = None
    # name/address of the outgoing mail server
    outgoing_server: Optional[str] = None
    # remark for this mail account
    remark: Optional[str] = None
    # are attachments sent?
    send_attachments: Optional[bool] = None
    # shall tracking infos be sent?
    send_tracking_infos: Optional[bool] = None
    # id of the account type
    type_id: Optional[int] = None
    # if no existing type will match the account, you define a name for the type here
    type_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsEmailAccount:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsEmailAccount
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsEmailAccount()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "active": lambda n : setattr(self, 'active', n.get_bool_value()),
            "addresses": lambda n : setattr(self, 'addresses', n.get_collection_of_primitive_values(str)),
            "catchAllAccount": lambda n : setattr(self, 'catch_all_account', n.get_bool_value()),
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "deleteArchived": lambda n : setattr(self, 'delete_archived', n.get_bool_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "domainId": lambda n : setattr(self, 'domain_id', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "incomingServer": lambda n : setattr(self, 'incoming_server', n.get_str_value()),
            "linkId": lambda n : setattr(self, 'link_id', n.get_int_value()),
            "linkTypeId": lambda n : setattr(self, 'link_type_id', n.get_int_value()),
            "loginName": lambda n : setattr(self, 'login_name', n.get_str_value()),
            "loginPassword": lambda n : setattr(self, 'login_password', n.get_str_value()),
            "outgoingServer": lambda n : setattr(self, 'outgoing_server', n.get_str_value()),
            "remark": lambda n : setattr(self, 'remark', n.get_str_value()),
            "sendAttachments": lambda n : setattr(self, 'send_attachments', n.get_bool_value()),
            "sendTrackingInfos": lambda n : setattr(self, 'send_tracking_infos', n.get_bool_value()),
            "typeId": lambda n : setattr(self, 'type_id', n.get_int_value()),
            "typeName": lambda n : setattr(self, 'type_name', n.get_str_value()),
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
        writer.write_collection_of_primitive_values("addresses", self.addresses)
        writer.write_bool_value("catchAllAccount", self.catch_all_account)
        writer.write_int_value("companyId", self.company_id)
        writer.write_bool_value("deleteArchived", self.delete_archived)
        writer.write_str_value("description", self.description)
        writer.write_int_value("domainId", self.domain_id)
        writer.write_str_value("incomingServer", self.incoming_server)
        writer.write_int_value("linkId", self.link_id)
        writer.write_int_value("linkTypeId", self.link_type_id)
        writer.write_str_value("loginName", self.login_name)
        writer.write_str_value("loginPassword", self.login_password)
        writer.write_str_value("outgoingServer", self.outgoing_server)
        writer.write_str_value("remark", self.remark)
        writer.write_bool_value("sendAttachments", self.send_attachments)
        writer.write_bool_value("sendTrackingInfos", self.send_tracking_infos)
        writer.write_int_value("typeId", self.type_id)
        writer.write_str_value("typeName", self.type_name)
        writer.write_additional_data_value(self.additional_data)
    

