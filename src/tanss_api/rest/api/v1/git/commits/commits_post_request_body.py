from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CommitsPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Request body.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Author of the commit.
    author: Optional[str] = None
    # Branch the commit was made on.
    branch: Optional[str] = None
    # Commit timestamp (epoch seconds).
    date: Optional[int] = None
    # Identifier of the employee linked to the commit.
    employee_id: Optional[int] = None
    # Commit hash.
    hash: Optional[str] = None
    # Unique identifier of the commit record.
    id: Optional[int] = None
    # Commit message.
    message: Optional[str] = None
    # Whether the commit is pinned in the ticket history.
    pinned: Optional[bool] = None
    # Name of the project the commit belongs to.
    project: Optional[str] = None
    # Identifier of the ticket the commit is linked to.
    ticket_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CommitsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CommitsPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CommitsPostRequestBody()
    
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
    

