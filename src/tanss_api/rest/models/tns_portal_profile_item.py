from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_portal_profile_item_category import TnsPortalProfileItemCategory
    from .tns_portal_profile_item_state import TnsPortalProfileItemState

@dataclass
class TnsPortalProfileItem(AdditionalDataHolder, Parsable):
    """
    Item (Box) eines Portal-Profils
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Kategorie einer Portal-Box
    category: Optional[TnsPortalProfileItemCategory] = None
    # The column property
    column: Optional[int] = None
    # The id property
    id: Optional[int] = None
    # The pos property
    pos: Optional[int] = None
    # The profileId property
    profile_id: Optional[int] = None
    # Anzeigezustand einer Portal-Box
    state: Optional[TnsPortalProfileItemState] = None
    # Box-Typ; bekannte Werte u.a. OWN_TICKETS, GENERAL_TICKETS, NOT_ASSIGNED_TICKETS, REPAIR_TICKETS, TECHNICIAN_TICKETS, PROJECTS, ROLE_TICKETS, CALLBACKS, APPOINTMENTS, TASKS, TIMERS, LINKS, BIRTHDAYS, COMPANY_TICKETS, SUPPORT_HISTORY, BILLING_INFOS, MAIL_HISTORY, LOCAL_ADMIN_TICKETS (Liste unvollständig)
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsPortalProfileItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsPortalProfileItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsPortalProfileItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_portal_profile_item_category import TnsPortalProfileItemCategory
        from .tns_portal_profile_item_state import TnsPortalProfileItemState

        from .tns_portal_profile_item_category import TnsPortalProfileItemCategory
        from .tns_portal_profile_item_state import TnsPortalProfileItemState

        fields: dict[str, Callable[[Any], None]] = {
            "category": lambda n : setattr(self, 'category', n.get_enum_value(TnsPortalProfileItemCategory)),
            "column": lambda n : setattr(self, 'column', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "pos": lambda n : setattr(self, 'pos', n.get_int_value()),
            "profileId": lambda n : setattr(self, 'profile_id', n.get_int_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(TnsPortalProfileItemState)),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_enum_value("category", self.category)
        writer.write_int_value("column", self.column)
        writer.write_int_value("id", self.id)
        writer.write_int_value("pos", self.pos)
        writer.write_int_value("profileId", self.profile_id)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

