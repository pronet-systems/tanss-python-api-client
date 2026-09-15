from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_customer_portal_widget_action import TnsCustomerPortalWidgetAction
    from .tns_customer_portal_widget_details import TnsCustomerPortalWidget_details
    from .tns_customer_portal_widget_selections import TnsCustomerPortalWidget_selections

@dataclass
class TnsCustomerPortalWidget(AdditionalDataHolder, Parsable):
    """
    Widget eines Kundenportal-Wizards
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The actions property
    actions: Optional[list[TnsCustomerPortalWidgetAction]] = None
    # The description property
    description: Optional[str] = None
    # The details property
    details: Optional[TnsCustomerPortalWidget_details] = None
    # The hidden property
    hidden: Optional[bool] = None
    # The icon property
    icon: Optional[str] = None
    # The nextWidgetId property
    next_widget_id: Optional[str] = None
    # The required property
    required: Optional[bool] = None
    # The selected property
    selected: Optional[bool] = None
    # The selections property
    selections: Optional[TnsCustomerPortalWidget_selections] = None
    # The title property
    title: Optional[str] = None
    # Widget-Typ; bekannte Werte u.a. COMPANY_SELECT, SELECTION, CUSTOM_INPUT, CONTACT, OVERVIEW, SELECT_APPOINTMENT (Liste unvollständig)
    type: Optional[str] = None
    # The varName property
    var_name: Optional[str] = None
    # UUID des Widgets
    widget_id: Optional[str] = None
    # untergeordnete Widgets
    widgets: Optional[list[TnsCustomerPortalWidget]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsCustomerPortalWidget:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsCustomerPortalWidget
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsCustomerPortalWidget()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_customer_portal_widget_action import TnsCustomerPortalWidgetAction
        from .tns_customer_portal_widget_details import TnsCustomerPortalWidget_details
        from .tns_customer_portal_widget_selections import TnsCustomerPortalWidget_selections

        from .tns_customer_portal_widget_action import TnsCustomerPortalWidgetAction
        from .tns_customer_portal_widget_details import TnsCustomerPortalWidget_details
        from .tns_customer_portal_widget_selections import TnsCustomerPortalWidget_selections

        fields: dict[str, Callable[[Any], None]] = {
            "actions": lambda n : setattr(self, 'actions', n.get_collection_of_object_values(TnsCustomerPortalWidgetAction)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "details": lambda n : setattr(self, 'details', n.get_object_value(TnsCustomerPortalWidget_details)),
            "hidden": lambda n : setattr(self, 'hidden', n.get_bool_value()),
            "icon": lambda n : setattr(self, 'icon', n.get_str_value()),
            "nextWidgetId": lambda n : setattr(self, 'next_widget_id', n.get_str_value()),
            "required": lambda n : setattr(self, 'required', n.get_bool_value()),
            "selected": lambda n : setattr(self, 'selected', n.get_bool_value()),
            "selections": lambda n : setattr(self, 'selections', n.get_object_value(TnsCustomerPortalWidget_selections)),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "varName": lambda n : setattr(self, 'var_name', n.get_str_value()),
            "widgetId": lambda n : setattr(self, 'widget_id', n.get_str_value()),
            "widgets": lambda n : setattr(self, 'widgets', n.get_collection_of_object_values(TnsCustomerPortalWidget)),
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
        writer.write_collection_of_object_values("actions", self.actions)
        writer.write_str_value("description", self.description)
        writer.write_object_value("details", self.details)
        writer.write_bool_value("hidden", self.hidden)
        writer.write_str_value("icon", self.icon)
        writer.write_str_value("nextWidgetId", self.next_widget_id)
        writer.write_bool_value("required", self.required)
        writer.write_bool_value("selected", self.selected)
        writer.write_object_value("selections", self.selections)
        writer.write_str_value("title", self.title)
        writer.write_str_value("type", self.type)
        writer.write_str_value("varName", self.var_name)
        writer.write_str_value("widgetId", self.widget_id)
        writer.write_collection_of_object_values("widgets", self.widgets)
        writer.write_additional_data_value(self.additional_data)
    

