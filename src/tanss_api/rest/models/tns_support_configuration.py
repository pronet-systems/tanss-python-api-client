from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .logic_operator_type import LogicOperatorType
    from .tns_discounted_support_type_filter import TnsDiscountedSupportTypeFilter
    from .tns_internal_support_filter import TnsInternalSupportFilter
    from .tns_open_tickets_filter import TnsOpenTicketsFilter
    from .tns_planning_type import TnsPlanningType
    from .tns_support_icon_type import TnsSupportIconType
    from .tns_support_location import TnsSupportLocation
    from .tns_support_task_filter import TnsSupportTaskFilter
    from .tns_timeframe import TnsTimeframe

@dataclass
class TnsSupportConfiguration(AdditionalDataHolder, Parsable):
    """
    object containing support list query parameters.When querying support with these parameters, you can only use the filter settings you need (You don't have to specify all)
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # show only supports from this companies (ids)
    companies: Optional[list[int]] = None
    # show supports from these company categories (ids)
    company_categories: Optional[list[int]] = None
    # Enum representing the logic linking of certain ids (AND / NOT / OR)
    company_categories_match_type: Optional[LogicOperatorType] = None
    # show supports from these contracts (ids)
    contracts: Optional[list[int]] = None
    # show supports from these departments only
    department_filter: Optional[list[int]] = None
    # determines which filter for "discounted" supports shall be used
    discounted_supports: Optional[TnsDiscountedSupportTypeFilter] = None
    # filter for emmployees (technician) ids
    employees: Optional[list[int]] = None
    # true, if supports from the own company shall be excluded
    exclude_own_company: Optional[bool] = None
    # true if recurrence rules (appointments) shall be fetched as well
    fetch_recurring: Optional[bool] = None
    # show supports from these support "import types" only
    import_types: Optional[list[TnsPlanningType]] = None
    # if true, all sub-ticket supports will be included as well (when displaying support from projects)
    include_sub_tickets: Optional[bool] = None
    # determines which filter for "internal support" shall be used
    internal_support: Optional[TnsInternalSupportFilter] = None
    # filter for a certain invoice (erp) number
    invoice_number: Optional[str] = None
    # show supports from these link types only
    link_types: Optional[list[int]] = None
    # show supports from these "Not charged reasons" only
    not_charged_reasons: Optional[list[int]] = None
    # determines wether supports from open tickets shall be fecthed or not
    open_tickets: Optional[TnsOpenTicketsFilter] = None
    # show supports from these planning types only
    planning_types: Optional[list[TnsPlanningType]] = None
    # show only supports with these support icon types
    support_icon_types: Optional[list[TnsSupportIconType]] = None
    # show only supports from these support locations
    support_locations: Optional[list[TnsSupportLocation]] = None
    # show supports from these support types only
    support_types: Optional[list[int]] = None
    # determines wether supports from tasks shall be fetched as well
    task_filter: Optional[TnsSupportTaskFilter] = None
    # if filtering for support containing a given text, you can specify the text filter here
    text_filter: Optional[str] = None
    # show supports from these ticket phases only
    ticket_phases: Optional[list[int]] = None
    # show supports from these ticket types
    ticket_types: Optional[list[int]] = None
    # show supports from these ticket (ids) only
    tickets: Optional[list[int]] = None
    # Describes a timeframe (from / to)
    timeframe: Optional[TnsTimeframe] = None
    # true if relation supports shall fe fecthed as well (when specifying company filter)
    use_relations: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsSupportConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsSupportConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsSupportConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .logic_operator_type import LogicOperatorType
        from .tns_discounted_support_type_filter import TnsDiscountedSupportTypeFilter
        from .tns_internal_support_filter import TnsInternalSupportFilter
        from .tns_open_tickets_filter import TnsOpenTicketsFilter
        from .tns_planning_type import TnsPlanningType
        from .tns_support_icon_type import TnsSupportIconType
        from .tns_support_location import TnsSupportLocation
        from .tns_support_task_filter import TnsSupportTaskFilter
        from .tns_timeframe import TnsTimeframe

        from .logic_operator_type import LogicOperatorType
        from .tns_discounted_support_type_filter import TnsDiscountedSupportTypeFilter
        from .tns_internal_support_filter import TnsInternalSupportFilter
        from .tns_open_tickets_filter import TnsOpenTicketsFilter
        from .tns_planning_type import TnsPlanningType
        from .tns_support_icon_type import TnsSupportIconType
        from .tns_support_location import TnsSupportLocation
        from .tns_support_task_filter import TnsSupportTaskFilter
        from .tns_timeframe import TnsTimeframe

        fields: dict[str, Callable[[Any], None]] = {
            "companies": lambda n : setattr(self, 'companies', n.get_collection_of_primitive_values(int)),
            "companyCategories": lambda n : setattr(self, 'company_categories', n.get_collection_of_primitive_values(int)),
            "companyCategoriesMatchType": lambda n : setattr(self, 'company_categories_match_type', n.get_enum_value(LogicOperatorType)),
            "contracts": lambda n : setattr(self, 'contracts', n.get_collection_of_primitive_values(int)),
            "departmentFilter": lambda n : setattr(self, 'department_filter', n.get_collection_of_primitive_values(int)),
            "discountedSupports": lambda n : setattr(self, 'discounted_supports', n.get_enum_value(TnsDiscountedSupportTypeFilter)),
            "employees": lambda n : setattr(self, 'employees', n.get_collection_of_primitive_values(int)),
            "excludeOwnCompany": lambda n : setattr(self, 'exclude_own_company', n.get_bool_value()),
            "fetchRecurring": lambda n : setattr(self, 'fetch_recurring', n.get_bool_value()),
            "importTypes": lambda n : setattr(self, 'import_types', n.get_collection_of_enum_values(TnsPlanningType)),
            "includeSubTickets": lambda n : setattr(self, 'include_sub_tickets', n.get_bool_value()),
            "internalSupport": lambda n : setattr(self, 'internal_support', n.get_enum_value(TnsInternalSupportFilter)),
            "invoiceNumber": lambda n : setattr(self, 'invoice_number', n.get_str_value()),
            "linkTypes": lambda n : setattr(self, 'link_types', n.get_collection_of_primitive_values(int)),
            "notChargedReasons": lambda n : setattr(self, 'not_charged_reasons', n.get_collection_of_primitive_values(int)),
            "openTickets": lambda n : setattr(self, 'open_tickets', n.get_enum_value(TnsOpenTicketsFilter)),
            "planningTypes": lambda n : setattr(self, 'planning_types', n.get_collection_of_enum_values(TnsPlanningType)),
            "supportIconTypes": lambda n : setattr(self, 'support_icon_types', n.get_collection_of_enum_values(TnsSupportIconType)),
            "supportLocations": lambda n : setattr(self, 'support_locations', n.get_collection_of_enum_values(TnsSupportLocation)),
            "supportTypes": lambda n : setattr(self, 'support_types', n.get_collection_of_primitive_values(int)),
            "taskFilter": lambda n : setattr(self, 'task_filter', n.get_enum_value(TnsSupportTaskFilter)),
            "textFilter": lambda n : setattr(self, 'text_filter', n.get_str_value()),
            "ticketPhases": lambda n : setattr(self, 'ticket_phases', n.get_collection_of_primitive_values(int)),
            "ticketTypes": lambda n : setattr(self, 'ticket_types', n.get_collection_of_primitive_values(int)),
            "tickets": lambda n : setattr(self, 'tickets', n.get_collection_of_primitive_values(int)),
            "timeframe": lambda n : setattr(self, 'timeframe', n.get_object_value(TnsTimeframe)),
            "useRelations": lambda n : setattr(self, 'use_relations', n.get_bool_value()),
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
        writer.write_collection_of_primitive_values("companies", self.companies)
        writer.write_collection_of_primitive_values("companyCategories", self.company_categories)
        writer.write_enum_value("companyCategoriesMatchType", self.company_categories_match_type)
        writer.write_collection_of_primitive_values("contracts", self.contracts)
        writer.write_collection_of_primitive_values("departmentFilter", self.department_filter)
        writer.write_enum_value("discountedSupports", self.discounted_supports)
        writer.write_collection_of_primitive_values("employees", self.employees)
        writer.write_bool_value("excludeOwnCompany", self.exclude_own_company)
        writer.write_bool_value("fetchRecurring", self.fetch_recurring)
        writer.write_collection_of_enum_values("importTypes", self.import_types)
        writer.write_bool_value("includeSubTickets", self.include_sub_tickets)
        writer.write_enum_value("internalSupport", self.internal_support)
        writer.write_str_value("invoiceNumber", self.invoice_number)
        writer.write_collection_of_primitive_values("linkTypes", self.link_types)
        writer.write_collection_of_primitive_values("notChargedReasons", self.not_charged_reasons)
        writer.write_enum_value("openTickets", self.open_tickets)
        writer.write_collection_of_enum_values("planningTypes", self.planning_types)
        writer.write_collection_of_enum_values("supportIconTypes", self.support_icon_types)
        writer.write_collection_of_enum_values("supportLocations", self.support_locations)
        writer.write_collection_of_primitive_values("supportTypes", self.support_types)
        writer.write_enum_value("taskFilter", self.task_filter)
        writer.write_str_value("textFilter", self.text_filter)
        writer.write_collection_of_primitive_values("ticketPhases", self.ticket_phases)
        writer.write_collection_of_primitive_values("ticketTypes", self.ticket_types)
        writer.write_collection_of_primitive_values("tickets", self.tickets)
        writer.write_object_value("timeframe", self.timeframe)
        writer.write_bool_value("useRelations", self.use_relations)
        writer.write_additional_data_value(self.additional_data)
    

