from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_contract_assignment_found_result import TnsContractAssignmentFoundResult
    from .tns_personal_computer import TnsPersonalComputer
    from .tns_personal_computer_with_contract_assignments_features import TnsPersonalComputerWithContractAssignments_features
    from .tns_personal_computer_with_details import TnsPersonalComputerWithDetails

from .tns_personal_computer_with_details import TnsPersonalComputerWithDetails

@dataclass
class TnsPersonalComputerWithContractAssignments(TnsPersonalComputerWithDetails, Parsable):
    """
    PC/Server mit Details, Host-/VHost-Infos und optionalen Wartungsvertrags-Zuordnungen
    """
    # The eConfigId property
    e_config_id: Optional[int] = None
    # The eConfigPos property
    e_config_pos: Optional[int] = None
    # The features property
    features: Optional[TnsPersonalComputerWithContractAssignments_features] = None
    # The guaranteeMonth property
    guarantee_month: Optional[int] = None
    # Describes a pc or server
    host_pc: Optional[TnsPersonalComputer] = None
    # nur bei loadContractAssignments=true befüllt
    maintenance_contract_assignments: Optional[list[TnsContractAssignmentFoundResult]] = None
    # The serverEyeContainerId property
    server_eye_container_id: Optional[str] = None
    # virtuelle Hosts, die auf diesem PC laufen
    vhosts: Optional[list[TnsPersonalComputer]] = None
    # The warrantyMonth property
    warranty_month: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsPersonalComputerWithContractAssignments:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsPersonalComputerWithContractAssignments
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsPersonalComputerWithContractAssignments()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_contract_assignment_found_result import TnsContractAssignmentFoundResult
        from .tns_personal_computer import TnsPersonalComputer
        from .tns_personal_computer_with_contract_assignments_features import TnsPersonalComputerWithContractAssignments_features
        from .tns_personal_computer_with_details import TnsPersonalComputerWithDetails

        from .tns_contract_assignment_found_result import TnsContractAssignmentFoundResult
        from .tns_personal_computer import TnsPersonalComputer
        from .tns_personal_computer_with_contract_assignments_features import TnsPersonalComputerWithContractAssignments_features
        from .tns_personal_computer_with_details import TnsPersonalComputerWithDetails

        fields: dict[str, Callable[[Any], None]] = {
            "eConfigId": lambda n : setattr(self, 'e_config_id', n.get_int_value()),
            "eConfigPos": lambda n : setattr(self, 'e_config_pos', n.get_int_value()),
            "features": lambda n : setattr(self, 'features', n.get_object_value(TnsPersonalComputerWithContractAssignments_features)),
            "guaranteeMonth": lambda n : setattr(self, 'guarantee_month', n.get_int_value()),
            "hostPc": lambda n : setattr(self, 'host_pc', n.get_object_value(TnsPersonalComputer)),
            "maintenanceContractAssignments": lambda n : setattr(self, 'maintenance_contract_assignments', n.get_collection_of_object_values(TnsContractAssignmentFoundResult)),
            "serverEyeContainerId": lambda n : setattr(self, 'server_eye_container_id', n.get_str_value()),
            "vhosts": lambda n : setattr(self, 'vhosts', n.get_collection_of_object_values(TnsPersonalComputer)),
            "warrantyMonth": lambda n : setattr(self, 'warranty_month', n.get_int_value()),
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
        writer.write_int_value("eConfigId", self.e_config_id)
        writer.write_int_value("eConfigPos", self.e_config_pos)
        writer.write_object_value("features", self.features)
        writer.write_int_value("guaranteeMonth", self.guarantee_month)
        writer.write_object_value("hostPc", self.host_pc)
        writer.write_collection_of_object_values("maintenanceContractAssignments", self.maintenance_contract_assignments)
        writer.write_str_value("serverEyeContainerId", self.server_eye_container_id)
        writer.write_collection_of_object_values("vhosts", self.vhosts)
        writer.write_int_value("warrantyMonth", self.warranty_month)
    

