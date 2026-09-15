from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .from_post_request_body_phase_ids import FromPostRequestBody_phaseIds

@dataclass
class FromPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Name of the mass ticket to create
    name: Optional[str] = None
    # Whether an already existing mass ticket for the project is overwritten
    overwrite_existing: Optional[bool] = None
    # Identifier of a specific existing mass ticket to overwrite
    overwrite_mass_ticket_id: Optional[int] = None
    # Identifiers of the project phases included in the mass ticket
    phase_ids: Optional[list[FromPostRequestBody_phaseIds]] = None
    # Identifier of the project the mass ticket belongs to
    project_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FromPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FromPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FromPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .from_post_request_body_phase_ids import FromPostRequestBody_phaseIds

        from .from_post_request_body_phase_ids import FromPostRequestBody_phaseIds

        fields: dict[str, Callable[[Any], None]] = {
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "overwriteExisting": lambda n : setattr(self, 'overwrite_existing', n.get_bool_value()),
            "overwriteMassTicketId": lambda n : setattr(self, 'overwrite_mass_ticket_id', n.get_int_value()),
            "phaseIds": lambda n : setattr(self, 'phase_ids', n.get_collection_of_object_values(FromPostRequestBody_phaseIds)),
            "projectId": lambda n : setattr(self, 'project_id', n.get_int_value()),
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
        writer.write_str_value("name", self.name)
        writer.write_bool_value("overwriteExisting", self.overwrite_existing)
        writer.write_int_value("overwriteMassTicketId", self.overwrite_mass_ticket_id)
        writer.write_collection_of_object_values("phaseIds", self.phase_ids)
        writer.write_int_value("projectId", self.project_id)
        writer.write_additional_data_value(self.additional_data)
    

