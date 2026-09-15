from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_active_filter_type import TnsActiveFilterType
    from .tns_branch_filter_type import TnsBranchFilterType

@dataclass
class TnsDeviceBaseConfiguration(AdditionalDataHolder, Parsable):
    """
    Parameters which are used to query for pcs when displaying a list of pcs/servers
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # filter settings for "active" state of the device
    active: Optional[TnsActiveFilterType] = None
    # filter settings for branches
    branches: Optional[TnsBranchFilterType] = None
    # show only entries of this company
    company_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsDeviceBaseConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsDeviceBaseConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsDeviceBaseConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_active_filter_type import TnsActiveFilterType
        from .tns_branch_filter_type import TnsBranchFilterType

        from .tns_active_filter_type import TnsActiveFilterType
        from .tns_branch_filter_type import TnsBranchFilterType

        fields: dict[str, Callable[[Any], None]] = {
            "active": lambda n : setattr(self, 'active', n.get_enum_value(TnsActiveFilterType)),
            "branches": lambda n : setattr(self, 'branches', n.get_enum_value(TnsBranchFilterType)),
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
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
        writer.write_enum_value("active", self.active)
        writer.write_enum_value("branches", self.branches)
        writer.write_int_value("companyId", self.company_id)
        writer.write_additional_data_value(self.additional_data)
    

