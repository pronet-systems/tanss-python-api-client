from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_callback_state import TnsCallbackState
    from .tns_timeframe import TnsTimeframe

@dataclass
class TnsCallbackConfiguration(AdditionalDataHolder, Parsable):
    """
    filter settings for retrieving callbacks
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # filters only callbacks for these (customer) companies (ids given here)
    company_ids: Optional[list[int]] = None
    # filters only callbacks for these (customer) employees (ids given here)
    employee_ids: Optional[list[int]] = None
    # filters only callbacks which were created by this employee (technician)
    from_employee_id: Optional[int] = None
    # if pagination shall be used, give here the items per page
    items_per_page: Optional[int] = None
    # if true, "linked entities" will be loaded as well (given in the responses "meta" section)
    load_linked_entites: Optional[bool] = None
    # if pagination shall be used, the page number is given here
    page: Optional[int] = None
    # Describes a current "state" of a callback
    state: Optional[TnsCallbackState] = None
    # if multiple states have to be filtered, give an array here
    states: Optional[list[TnsCallbackState]] = None
    # Describes a timeframe (from / to)
    timeframe: Optional[TnsTimeframe] = None
    # if "toEmployeeId" is given, also retrieves all callbacks which the user has access to
    to_all_employees_with_access_to: Optional[bool] = None
    # filters only callbacks for these departments
    to_department_ids: Optional[list[int]] = None
    # filters only callbacks to this employee (techncian)
    to_employee_id: Optional[int] = None
    # if true, will also load all state logs of the retrieved callbacks
    with_log: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsCallbackConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsCallbackConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsCallbackConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_callback_state import TnsCallbackState
        from .tns_timeframe import TnsTimeframe

        from .tns_callback_state import TnsCallbackState
        from .tns_timeframe import TnsTimeframe

        fields: dict[str, Callable[[Any], None]] = {
            "companyIds": lambda n : setattr(self, 'company_ids', n.get_collection_of_primitive_values(int)),
            "employeeIds": lambda n : setattr(self, 'employee_ids', n.get_collection_of_primitive_values(int)),
            "fromEmployeeId": lambda n : setattr(self, 'from_employee_id', n.get_int_value()),
            "itemsPerPage": lambda n : setattr(self, 'items_per_page', n.get_int_value()),
            "loadLinkedEntites": lambda n : setattr(self, 'load_linked_entites', n.get_bool_value()),
            "page": lambda n : setattr(self, 'page', n.get_int_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(TnsCallbackState)),
            "states": lambda n : setattr(self, 'states', n.get_collection_of_enum_values(TnsCallbackState)),
            "timeframe": lambda n : setattr(self, 'timeframe', n.get_object_value(TnsTimeframe)),
            "toAllEmployeesWithAccessTo": lambda n : setattr(self, 'to_all_employees_with_access_to', n.get_bool_value()),
            "toDepartmentIds": lambda n : setattr(self, 'to_department_ids', n.get_collection_of_primitive_values(int)),
            "toEmployeeId": lambda n : setattr(self, 'to_employee_id', n.get_int_value()),
            "withLog": lambda n : setattr(self, 'with_log', n.get_bool_value()),
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
        writer.write_collection_of_primitive_values("companyIds", self.company_ids)
        writer.write_collection_of_primitive_values("employeeIds", self.employee_ids)
        writer.write_int_value("fromEmployeeId", self.from_employee_id)
        writer.write_int_value("itemsPerPage", self.items_per_page)
        writer.write_bool_value("loadLinkedEntites", self.load_linked_entites)
        writer.write_int_value("page", self.page)
        writer.write_enum_value("state", self.state)
        writer.write_collection_of_enum_values("states", self.states)
        writer.write_object_value("timeframe", self.timeframe)
        writer.write_bool_value("toAllEmployeesWithAccessTo", self.to_all_employees_with_access_to)
        writer.write_collection_of_primitive_values("toDepartmentIds", self.to_department_ids)
        writer.write_int_value("toEmployeeId", self.to_employee_id)
        writer.write_bool_value("withLog", self.with_log)
        writer.write_additional_data_value(self.additional_data)
    

