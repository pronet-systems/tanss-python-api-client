from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .remote_supports_put_request_body_employee_ids import RemoteSupportsPutRequestBody_employeeIds
    from .remote_supports_put_request_body_timeframe import RemoteSupportsPutRequestBody_timeframe

@dataclass
class RemoteSupportsPutRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Identifier of the company to filter by.
    company_id: Optional[int] = None
    # Identifier of a single employee to filter by.
    employee_id: Optional[int] = None
    # Identifiers of multiple employees to filter by.
    employee_ids: Optional[list[RemoteSupportsPutRequestBody_employeeIds]] = None
    # Whether to include only externally allowed remote maintenance entries.
    only_external_allowed: Optional[bool] = None
    # Whether permission checks are applied to the query.
    permission_checks: Optional[bool] = None
    # Free-text search term used to filter results.
    text: Optional[str] = None
    # Time range used to constrain the remote maintenance query.
    timeframe: Optional[RemoteSupportsPutRequestBody_timeframe] = None
    # Identifier of the remote maintenance type to filter by.
    type_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RemoteSupportsPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RemoteSupportsPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RemoteSupportsPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .remote_supports_put_request_body_employee_ids import RemoteSupportsPutRequestBody_employeeIds
        from .remote_supports_put_request_body_timeframe import RemoteSupportsPutRequestBody_timeframe

        from .remote_supports_put_request_body_employee_ids import RemoteSupportsPutRequestBody_employeeIds
        from .remote_supports_put_request_body_timeframe import RemoteSupportsPutRequestBody_timeframe

        fields: dict[str, Callable[[Any], None]] = {
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "employeeIds": lambda n : setattr(self, 'employee_ids', n.get_collection_of_object_values(RemoteSupportsPutRequestBody_employeeIds)),
            "onlyExternalAllowed": lambda n : setattr(self, 'only_external_allowed', n.get_bool_value()),
            "permissionChecks": lambda n : setattr(self, 'permission_checks', n.get_bool_value()),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
            "timeframe": lambda n : setattr(self, 'timeframe', n.get_object_value(RemoteSupportsPutRequestBody_timeframe)),
            "typeId": lambda n : setattr(self, 'type_id', n.get_int_value()),
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
        writer.write_int_value("companyId", self.company_id)
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_collection_of_object_values("employeeIds", self.employee_ids)
        writer.write_bool_value("onlyExternalAllowed", self.only_external_allowed)
        writer.write_bool_value("permissionChecks", self.permission_checks)
        writer.write_str_value("text", self.text)
        writer.write_object_value("timeframe", self.timeframe)
        writer.write_int_value("typeId", self.type_id)
        writer.write_additional_data_value(self.additional_data)
    

