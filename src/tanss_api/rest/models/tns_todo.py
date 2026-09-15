from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_todo_list import TnsTodoList

@dataclass
class TnsTodo(AdditionalDataHolder, Parsable):
    """
    ToDo-Wurzelobjekt eines Mitarbeiters.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The choosenListId property
    choosen_list_id: Optional[int] = None
    # The employeeId property
    employee_id: Optional[int] = None
    # The id property
    id: Optional[int] = None
    # The lists property
    lists: Optional[list[TnsTodoList]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsTodo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsTodo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsTodo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_todo_list import TnsTodoList

        from .tns_todo_list import TnsTodoList

        fields: dict[str, Callable[[Any], None]] = {
            "choosenListId": lambda n : setattr(self, 'choosen_list_id', n.get_int_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "lists": lambda n : setattr(self, 'lists', n.get_collection_of_object_values(TnsTodoList)),
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
        writer.write_int_value("choosenListId", self.choosen_list_id)
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_int_value("id", self.id)
        writer.write_collection_of_object_values("lists", self.lists)
        writer.write_additional_data_value(self.additional_data)
    

