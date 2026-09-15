from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.tns_planning_type import TnsPlanningType
    from ......models.tns_support import TnsSupport
    from .with_support_put_request_body_grouped_exceptions import WithSupportPutRequestBody_groupedExceptions

from ......models.tns_support import TnsSupport

@dataclass
class WithSupportPutRequestBody(TnsSupport, Parsable):
    """
    Steuer-Keys, die der Support-Service zusaetzlich liest
    """
    # The automaticallyResolveConflicts property
    automatically_resolve_conflicts: Optional[bool] = None
    # The checkForUserInput property
    check_for_user_input: Optional[bool] = None
    # The contractNotCharged property
    contract_not_charged: Optional[bool] = None
    # The planning type defines if a support is actually a support, appointment (or some other type)
    created_with_planning_type: Optional[TnsPlanningType] = None
    # The dateExport property
    date_export: Optional[int] = None
    # The discardOnSupport property
    discard_on_support: Optional[bool] = None
    # The fullservice property
    fullservice: Optional[bool] = None
    # The groupId property
    group_id: Optional[int] = None
    # The groupedExceptions property
    grouped_exceptions: Optional[WithSupportPutRequestBody_groupedExceptions] = None
    # The mainId property
    main_id: Optional[int] = None
    # The prevId property
    prev_id: Optional[int] = None
    # The preventNotification property
    prevent_notification: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WithSupportPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WithSupportPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WithSupportPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ......models.tns_planning_type import TnsPlanningType
        from ......models.tns_support import TnsSupport
        from .with_support_put_request_body_grouped_exceptions import WithSupportPutRequestBody_groupedExceptions

        from ......models.tns_planning_type import TnsPlanningType
        from ......models.tns_support import TnsSupport
        from .with_support_put_request_body_grouped_exceptions import WithSupportPutRequestBody_groupedExceptions

        fields: dict[str, Callable[[Any], None]] = {
            "automaticallyResolveConflicts": lambda n : setattr(self, 'automatically_resolve_conflicts', n.get_bool_value()),
            "checkForUserInput": lambda n : setattr(self, 'check_for_user_input', n.get_bool_value()),
            "contractNotCharged": lambda n : setattr(self, 'contract_not_charged', n.get_bool_value()),
            "createdWithPlanningType": lambda n : setattr(self, 'created_with_planning_type', n.get_enum_value(TnsPlanningType)),
            "dateExport": lambda n : setattr(self, 'date_export', n.get_int_value()),
            "discardOnSupport": lambda n : setattr(self, 'discard_on_support', n.get_bool_value()),
            "fullservice": lambda n : setattr(self, 'fullservice', n.get_bool_value()),
            "groupId": lambda n : setattr(self, 'group_id', n.get_int_value()),
            "groupedExceptions": lambda n : setattr(self, 'grouped_exceptions', n.get_object_value(WithSupportPutRequestBody_groupedExceptions)),
            "mainId": lambda n : setattr(self, 'main_id', n.get_int_value()),
            "prevId": lambda n : setattr(self, 'prev_id', n.get_int_value()),
            "preventNotification": lambda n : setattr(self, 'prevent_notification', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_bool_value("automaticallyResolveConflicts", self.automatically_resolve_conflicts)
        writer.write_bool_value("checkForUserInput", self.check_for_user_input)
        writer.write_bool_value("contractNotCharged", self.contract_not_charged)
        writer.write_enum_value("createdWithPlanningType", self.created_with_planning_type)
        writer.write_int_value("dateExport", self.date_export)
        writer.write_bool_value("discardOnSupport", self.discard_on_support)
        writer.write_bool_value("fullservice", self.fullservice)
        writer.write_int_value("groupId", self.group_id)
        writer.write_object_value("groupedExceptions", self.grouped_exceptions)
        writer.write_int_value("mainId", self.main_id)
        writer.write_int_value("prevId", self.prev_id)
        writer.write_bool_value("preventNotification", self.prevent_notification)
    

