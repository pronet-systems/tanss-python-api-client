from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tasks_put_request_body_company_ids import TasksPutRequestBody_companyIds
    from .tasks_put_request_body_preferred_department_ids import TasksPutRequestBody_preferredDepartmentIds
    from .tasks_put_request_body_preferred_employee_ids import TasksPutRequestBody_preferredEmployeeIds
    from .tasks_put_request_body_task_ids import TasksPutRequestBody_taskIds

@dataclass
class TasksPutRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Restrict results to tasks of these companies
    company_ids: Optional[list[TasksPutRequestBody_companyIds]] = None
    # Identifier of the linked entity to filter by
    link_id: Optional[int] = None
    # Type identifier of the linked entity to filter by
    link_type_id: Optional[int] = None
    # Return only active tasks
    only_active_tasks: Optional[bool] = None
    # Return only expired tasks
    only_expired: Optional[bool] = None
    # Restrict results to tasks preferring these departments
    preferred_department_ids: Optional[list[TasksPutRequestBody_preferredDepartmentIds]] = None
    # Restrict results to tasks preferring these employees
    preferred_employee_ids: Optional[list[TasksPutRequestBody_preferredEmployeeIds]] = None
    # Free-text search term used to filter tasks
    search: Optional[str] = None
    # Restrict results to these task identifiers
    task_ids: Optional[list[TasksPutRequestBody_taskIds]] = None
    # Include contract information in the result
    with_contract: Optional[bool] = None
    # Include next execution information in the result
    with_next_execution: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TasksPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TasksPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TasksPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tasks_put_request_body_company_ids import TasksPutRequestBody_companyIds
        from .tasks_put_request_body_preferred_department_ids import TasksPutRequestBody_preferredDepartmentIds
        from .tasks_put_request_body_preferred_employee_ids import TasksPutRequestBody_preferredEmployeeIds
        from .tasks_put_request_body_task_ids import TasksPutRequestBody_taskIds

        from .tasks_put_request_body_company_ids import TasksPutRequestBody_companyIds
        from .tasks_put_request_body_preferred_department_ids import TasksPutRequestBody_preferredDepartmentIds
        from .tasks_put_request_body_preferred_employee_ids import TasksPutRequestBody_preferredEmployeeIds
        from .tasks_put_request_body_task_ids import TasksPutRequestBody_taskIds

        fields: dict[str, Callable[[Any], None]] = {
            "companyIds": lambda n : setattr(self, 'company_ids', n.get_collection_of_object_values(TasksPutRequestBody_companyIds)),
            "linkId": lambda n : setattr(self, 'link_id', n.get_int_value()),
            "linkTypeId": lambda n : setattr(self, 'link_type_id', n.get_int_value()),
            "onlyActiveTasks": lambda n : setattr(self, 'only_active_tasks', n.get_bool_value()),
            "onlyExpired": lambda n : setattr(self, 'only_expired', n.get_bool_value()),
            "preferredDepartmentIds": lambda n : setattr(self, 'preferred_department_ids', n.get_collection_of_object_values(TasksPutRequestBody_preferredDepartmentIds)),
            "preferredEmployeeIds": lambda n : setattr(self, 'preferred_employee_ids', n.get_collection_of_object_values(TasksPutRequestBody_preferredEmployeeIds)),
            "search": lambda n : setattr(self, 'search', n.get_str_value()),
            "taskIds": lambda n : setattr(self, 'task_ids', n.get_collection_of_object_values(TasksPutRequestBody_taskIds)),
            "withContract": lambda n : setattr(self, 'with_contract', n.get_bool_value()),
            "withNextExecution": lambda n : setattr(self, 'with_next_execution', n.get_bool_value()),
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
        writer.write_collection_of_object_values("companyIds", self.company_ids)
        writer.write_int_value("linkId", self.link_id)
        writer.write_int_value("linkTypeId", self.link_type_id)
        writer.write_bool_value("onlyActiveTasks", self.only_active_tasks)
        writer.write_bool_value("onlyExpired", self.only_expired)
        writer.write_collection_of_object_values("preferredDepartmentIds", self.preferred_department_ids)
        writer.write_collection_of_object_values("preferredEmployeeIds", self.preferred_employee_ids)
        writer.write_str_value("search", self.search)
        writer.write_collection_of_object_values("taskIds", self.task_ids)
        writer.write_bool_value("withContract", self.with_contract)
        writer.write_bool_value("withNextExecution", self.with_next_execution)
        writer.write_additional_data_value(self.additional_data)
    

