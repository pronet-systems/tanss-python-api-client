from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TicketHistory_gitCommits(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # author as reported by git
    author: Optional[str] = None
    # branch the commit was pushed to
    branch: Optional[str] = None
    # commit date as unix timestamp
    date: Optional[int] = None
    # id of the TANSS employee the author could be matched to (0 if none).Name is stored in the "linked entities" - "employees"
    employee_id: Optional[int] = None
    # commit hash
    hash: Optional[str] = None
    # The id property
    id: Optional[int] = None
    # commit message
    message: Optional[str] = None
    # whether the commit was pinned to the ticket
    pinned: Optional[bool] = None
    # name of the git project the commit belongs to
    project: Optional[str] = None
    # id of the ticket the commit is linked to
    ticket_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TicketHistory_gitCommits:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TicketHistory_gitCommits
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TicketHistory_gitCommits()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "author": lambda n : setattr(self, 'author', n.get_str_value()),
            "branch": lambda n : setattr(self, 'branch', n.get_str_value()),
            "date": lambda n : setattr(self, 'date', n.get_int_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "hash": lambda n : setattr(self, 'hash', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "pinned": lambda n : setattr(self, 'pinned', n.get_bool_value()),
            "project": lambda n : setattr(self, 'project', n.get_str_value()),
            "ticketId": lambda n : setattr(self, 'ticket_id', n.get_int_value()),
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
        writer.write_str_value("author", self.author)
        writer.write_str_value("branch", self.branch)
        writer.write_int_value("date", self.date)
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_str_value("hash", self.hash)
        writer.write_str_value("message", self.message)
        writer.write_bool_value("pinned", self.pinned)
        writer.write_str_value("project", self.project)
        writer.write_int_value("ticketId", self.ticket_id)
        writer.write_additional_data_value(self.additional_data)
    

