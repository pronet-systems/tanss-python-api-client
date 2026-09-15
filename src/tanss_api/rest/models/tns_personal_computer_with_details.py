from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_component import TnsComponent
    from .tns_periphery import TnsPeriphery
    from .tns_personal_computer_with_ip_guarantee import TnsPersonalComputerWithIpGuarantee
    from .tns_service_icon import TnsServiceIcon
    from .tns_softwarelicense import TnsSoftwarelicense

from .tns_personal_computer_with_ip_guarantee import TnsPersonalComputerWithIpGuarantee

@dataclass
class TnsPersonalComputerWithDetails(TnsPersonalComputerWithIpGuarantee, Parsable):
    """
    Describes a pc or server with all "attached" infos
    """
    # infos about components which are built into this pc
    components: Optional[list[TnsComponent]] = None
    # infos about peripheries which are linked to this pc
    peripheries: Optional[list[TnsPeriphery]] = None
    # The serviceIcons property
    service_icons: Optional[list[TnsServiceIcon]] = None
    # infos about software licenses which are used by this pc
    softwarelicenses: Optional[list[TnsSoftwarelicense]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsPersonalComputerWithDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsPersonalComputerWithDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsPersonalComputerWithDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_component import TnsComponent
        from .tns_periphery import TnsPeriphery
        from .tns_personal_computer_with_ip_guarantee import TnsPersonalComputerWithIpGuarantee
        from .tns_service_icon import TnsServiceIcon
        from .tns_softwarelicense import TnsSoftwarelicense

        from .tns_component import TnsComponent
        from .tns_periphery import TnsPeriphery
        from .tns_personal_computer_with_ip_guarantee import TnsPersonalComputerWithIpGuarantee
        from .tns_service_icon import TnsServiceIcon
        from .tns_softwarelicense import TnsSoftwarelicense

        fields: dict[str, Callable[[Any], None]] = {
            "components": lambda n : setattr(self, 'components', n.get_collection_of_object_values(TnsComponent)),
            "peripheries": lambda n : setattr(self, 'peripheries', n.get_collection_of_object_values(TnsPeriphery)),
            "serviceIcons": lambda n : setattr(self, 'service_icons', n.get_collection_of_object_values(TnsServiceIcon)),
            "softwarelicenses": lambda n : setattr(self, 'softwarelicenses', n.get_collection_of_object_values(TnsSoftwarelicense)),
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
        writer.write_collection_of_object_values("components", self.components)
        writer.write_collection_of_object_values("peripheries", self.peripheries)
        writer.write_collection_of_object_values("serviceIcons", self.service_icons)
        writer.write_collection_of_object_values("softwarelicenses", self.softwarelicenses)
    

