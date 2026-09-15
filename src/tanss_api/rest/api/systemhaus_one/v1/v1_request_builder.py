from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .companies.companies_request_builder import CompaniesRequestBuilder
    from .company_categories.company_categories_request_builder import CompanyCategoriesRequestBuilder
    from .customers.customers_request_builder import CustomersRequestBuilder
    from .departments.departments_request_builder import DepartmentsRequestBuilder
    from .employees.employees_request_builder import EmployeesRequestBuilder
    from .external_ids.external_ids_request_builder import ExternalIdsRequestBuilder
    from .invoices.invoices_request_builder import InvoicesRequestBuilder
    from .tickets.tickets_request_builder import TicketsRequestBuilder
    from .types.types_request_builder import TypesRequestBuilder

class V1RequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/systemhaus_one/v1
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new V1RequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/systemhaus_one/v1", path_parameters)
    
    @property
    def companies(self) -> CompaniesRequestBuilder:
        """
        The companies property
        """
        from .companies.companies_request_builder import CompaniesRequestBuilder

        return CompaniesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def company_categories(self) -> CompanyCategoriesRequestBuilder:
        """
        The companyCategories property
        """
        from .company_categories.company_categories_request_builder import CompanyCategoriesRequestBuilder

        return CompanyCategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def customers(self) -> CustomersRequestBuilder:
        """
        The customers property
        """
        from .customers.customers_request_builder import CustomersRequestBuilder

        return CustomersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def departments(self) -> DepartmentsRequestBuilder:
        """
        The departments property
        """
        from .departments.departments_request_builder import DepartmentsRequestBuilder

        return DepartmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def employees(self) -> EmployeesRequestBuilder:
        """
        The employees property
        """
        from .employees.employees_request_builder import EmployeesRequestBuilder

        return EmployeesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def external_ids(self) -> ExternalIdsRequestBuilder:
        """
        The externalIds property
        """
        from .external_ids.external_ids_request_builder import ExternalIdsRequestBuilder

        return ExternalIdsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def invoices(self) -> InvoicesRequestBuilder:
        """
        The invoices property
        """
        from .invoices.invoices_request_builder import InvoicesRequestBuilder

        return InvoicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tickets(self) -> TicketsRequestBuilder:
        """
        The tickets property
        """
        from .tickets.tickets_request_builder import TicketsRequestBuilder

        return TicketsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def types(self) -> TypesRequestBuilder:
        """
        The types property
        """
        from .types.types_request_builder import TypesRequestBuilder

        return TypesRequestBuilder(self.request_adapter, self.path_parameters)
    

