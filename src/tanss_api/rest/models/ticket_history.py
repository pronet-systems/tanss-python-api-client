from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ticket_history_git_commits import TicketHistory_gitCommits
    from .tns_comment import TnsComment
    from .tns_mail import TnsMail
    from .tns_support import TnsSupport

@dataclass
class TicketHistory(AdditionalDataHolder, Parsable):
    """
    object containing the ticket history
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # contains all comments of this ticket
    comments: Optional[list[TnsComment]] = None
    # Git commits linked to this ticket. Only present for technicians/freelancers and onlywhen the `gitCommits` feature is active in the ticket module - otherwise the field isomitted. Same records as `GET /api/v1/git/commits/ticket/{ticketId}`.
    git_commits: Optional[list[TicketHistory_gitCommits]] = None
    # contains all mails of this ticket
    mails: Optional[list[TnsMail]] = None
    # contains all supports of this ticket
    supports: Optional[list[TnsSupport]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TicketHistory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TicketHistory
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TicketHistory()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ticket_history_git_commits import TicketHistory_gitCommits
        from .tns_comment import TnsComment
        from .tns_mail import TnsMail
        from .tns_support import TnsSupport

        from .ticket_history_git_commits import TicketHistory_gitCommits
        from .tns_comment import TnsComment
        from .tns_mail import TnsMail
        from .tns_support import TnsSupport

        fields: dict[str, Callable[[Any], None]] = {
            "comments": lambda n : setattr(self, 'comments', n.get_collection_of_object_values(TnsComment)),
            "gitCommits": lambda n : setattr(self, 'git_commits', n.get_collection_of_object_values(TicketHistory_gitCommits)),
            "mails": lambda n : setattr(self, 'mails', n.get_collection_of_object_values(TnsMail)),
            "supports": lambda n : setattr(self, 'supports', n.get_collection_of_object_values(TnsSupport)),
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
        writer.write_collection_of_object_values("comments", self.comments)
        writer.write_collection_of_object_values("mails", self.mails)
        writer.write_collection_of_object_values("supports", self.supports)
        writer.write_additional_data_value(self.additional_data)
    

