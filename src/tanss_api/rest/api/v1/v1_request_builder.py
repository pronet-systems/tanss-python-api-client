from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .accounting_types.accounting_types_request_builder import AccountingTypesRequestBuilder
    from .additional_charges.additional_charges_request_builder import AdditionalChargesRequestBuilder
    from .admin.admin_request_builder import AdminRequestBuilder
    from .ai.ai_request_builder import AiRequestBuilder
    from .assignments.assignments_request_builder import AssignmentsRequestBuilder
    from .availability.availability_request_builder import AvailabilityRequestBuilder
    from .bankaccounts.bankaccounts_request_builder import BankaccountsRequestBuilder
    from .browser.browser_request_builder import BrowserRequestBuilder
    from .cache.cache_request_builder import CacheRequestBuilder
    from .callbacks.callbacks_request_builder import CallbacksRequestBuilder
    from .cars.cars_request_builder import CarsRequestBuilder
    from .chats.chats_request_builder import ChatsRequestBuilder
    from .checklists.checklists_request_builder import ChecklistsRequestBuilder
    from .checklist_events.checklist_events_request_builder import ChecklistEventsRequestBuilder
    from .checklist_items.checklist_items_request_builder import ChecklistItemsRequestBuilder
    from .cloud.cloud_request_builder import CloudRequestBuilder
    from .companies.companies_request_builder import CompaniesRequestBuilder
    from .company_categories.company_categories_request_builder import CompanyCategoriesRequestBuilder
    from .components.components_request_builder import ComponentsRequestBuilder
    from .config_values.config_values_request_builder import ConfigValuesRequestBuilder
    from .contracts.contracts_request_builder import ContractsRequestBuilder
    from .cpus.cpus_request_builder import CpusRequestBuilder
    from .currencies.currencies_request_builder import CurrenciesRequestBuilder
    from .customer_notifications.customer_notifications_request_builder import CustomerNotificationsRequestBuilder
    from .customer_portal_wizards.customer_portal_wizards_request_builder import CustomerPortalWizardsRequestBuilder
    from .documents.documents_request_builder import DocumentsRequestBuilder
    from .domains.domains_request_builder import DomainsRequestBuilder
    from .email_accounts.email_accounts_request_builder import EmailAccountsRequestBuilder
    from .email_settings.email_settings_request_builder import EmailSettingsRequestBuilder
    from .employees.employees_request_builder import EmployeesRequestBuilder
    from .entity_files.entity_files_request_builder import EntityFilesRequestBuilder
    from .erp.erp_request_builder import ErpRequestBuilder
    from .escalations.escalations_request_builder import EscalationsRequestBuilder
    from .ev.ev_request_builder import EvRequestBuilder
    from .externals.externals_request_builder import ExternalsRequestBuilder
    from .favorites.favorites_request_builder import FavoritesRequestBuilder
    from .files_and_links.files_and_links_request_builder import FilesAndLinksRequestBuilder
    from .files_and_links_media.files_and_links_media_request_builder import FilesAndLinksMediaRequestBuilder
    from .files_and_links_url.files_and_links_url_request_builder import FilesAndLinksUrlRequestBuilder
    from .generic_assignments.generic_assignments_request_builder import GenericAssignmentsRequestBuilder
    from .geocodes.geocodes_request_builder import GeocodesRequestBuilder
    from .git.git_request_builder import GitRequestBuilder
    from .guarantee.guarantee_request_builder import GuaranteeRequestBuilder
    from .hdd_types.hdd_types_request_builder import HddTypesRequestBuilder
    from .holidays.holidays_request_builder import HolidaysRequestBuilder
    from .ical.ical_request_builder import IcalRequestBuilder
    from .identify.identify_request_builder import IdentifyRequestBuilder
    from .ips.ips_request_builder import IpsRequestBuilder
    from .jwts.jwts_request_builder import JwtsRequestBuilder
    from .knowledge_base.knowledge_base_request_builder import KnowledgeBaseRequestBuilder
    from .landing_page.landing_page_request_builder import LandingPageRequestBuilder
    from .log.log_request_builder import LogRequestBuilder
    from .login.login_request_builder import LoginRequestBuilder
    from .logo.logo_request_builder import LogoRequestBuilder
    from .mails.mails_request_builder import MailsRequestBuilder
    from .mail_robot.mail_robot_request_builder import MailRobotRequestBuilder
    from .management_dashboard.management_dashboard_request_builder import ManagementDashboardRequestBuilder
    from .manufacturers.manufacturers_request_builder import ManufacturersRequestBuilder
    from .mass.mass_request_builder import MassRequestBuilder
    from .mention.mention_request_builder import MentionRequestBuilder
    from .offer.offer_request_builder import OfferRequestBuilder
    from .offers.offers_request_builder import OffersRequestBuilder
    from .os.os_request_builder import OsRequestBuilder
    from .overtime.overtime_request_builder import OvertimeRequestBuilder
    from .own_daily_services.own_daily_services_request_builder import OwnDailyServicesRequestBuilder
    from .passkey.passkey_request_builder import PasskeyRequestBuilder
    from .passwords.passwords_request_builder import PasswordsRequestBuilder
    from .payment_methods.payment_methods_request_builder import PaymentMethodsRequestBuilder
    from .pcs.pcs_request_builder import PcsRequestBuilder
    from .peripheries.peripheries_request_builder import PeripheriesRequestBuilder
    from .permissions.permissions_request_builder import PermissionsRequestBuilder
    from .phone_calls.phone_calls_request_builder import PhoneCallsRequestBuilder
    from .planning.planning_request_builder import PlanningRequestBuilder
    from .pop_up_notifications.pop_up_notifications_request_builder import PopUpNotificationsRequestBuilder
    from .portal.portal_request_builder import PortalRequestBuilder
    from .priorities.priorities_request_builder import PrioritiesRequestBuilder
    from .projects.projects_request_builder import ProjectsRequestBuilder
    from .push.push_request_builder import PushRequestBuilder
    from .qr.qr_request_builder import QrRequestBuilder
    from .recurrence.recurrence_request_builder import RecurrenceRequestBuilder
    from .remote_supports.remote_supports_request_builder import RemoteSupportsRequestBuilder
    from .roles.roles_request_builder import RolesRequestBuilder
    from .round.round_request_builder import RoundRequestBuilder
    from .sales_target.sales_target_request_builder import SalesTargetRequestBuilder
    from .search.search_request_builder import SearchRequestBuilder
    from .sentry.sentry_request_builder import SentryRequestBuilder
    from .services.services_request_builder import ServicesRequestBuilder
    from .sla.sla_request_builder import SlaRequestBuilder
    from .softwarelicenses.softwarelicenses_request_builder import SoftwarelicensesRequestBuilder
    from .starface.starface_request_builder import StarfaceRequestBuilder
    from .supports.supports_request_builder import SupportsRequestBuilder
    from .support_profile_categories.support_profile_categories_request_builder import SupportProfileCategoriesRequestBuilder
    from .support_rules.support_rules_request_builder import SupportRulesRequestBuilder
    from .support_types.support_types_request_builder import SupportTypesRequestBuilder
    from .systemhaus_one.systemhaus_one_request_builder import Systemhaus_oneRequestBuilder
    from .sys_tasks.sys_tasks_request_builder import SysTasksRequestBuilder
    from .tags.tags_request_builder import TagsRequestBuilder
    from .tanss_events.tanss_events_request_builder import TanssEventsRequestBuilder
    from .tanss_licenses.tanss_licenses_request_builder import TanssLicensesRequestBuilder
    from .tasks.tasks_request_builder import TasksRequestBuilder
    from .telephone_systems.telephone_systems_request_builder import TelephoneSystemsRequestBuilder
    from .templates.templates_request_builder import TemplatesRequestBuilder
    from .temp_cache.temp_cache_request_builder import TempCacheRequestBuilder
    from .text_modules.text_modules_request_builder import TextModulesRequestBuilder
    from .tickets.tickets_request_builder import TicketsRequestBuilder
    from .ticket_board.ticket_board_request_builder import TicketBoardRequestBuilder
    from .ticket_workflows.ticket_workflows_request_builder import TicketWorkflowsRequestBuilder
    from .timeline.timeline_request_builder import TimelineRequestBuilder
    from .timers.timers_request_builder import TimersRequestBuilder
    from .timestamps.timestamps_request_builder import TimestampsRequestBuilder
    from .tmp_file_uploads.tmp_file_uploads_request_builder import TmpFileUploadsRequestBuilder
    from .todos.todos_request_builder import TodosRequestBuilder
    from .util.util_request_builder import UtilRequestBuilder
    from .vacation_requests.vacation_requests_request_builder import VacationRequestsRequestBuilder
    from .vouchers.vouchers_request_builder import VouchersRequestBuilder
    from .workflow_contracts.workflow_contracts_request_builder import WorkflowContractsRequestBuilder
    from .working_hours.working_hours_request_builder import WorkingHoursRequestBuilder

class V1RequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new V1RequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1", path_parameters)
    
    @property
    def accounting_types(self) -> AccountingTypesRequestBuilder:
        """
        The accountingTypes property
        """
        from .accounting_types.accounting_types_request_builder import AccountingTypesRequestBuilder

        return AccountingTypesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def additional_charges(self) -> AdditionalChargesRequestBuilder:
        """
        The additionalCharges property
        """
        from .additional_charges.additional_charges_request_builder import AdditionalChargesRequestBuilder

        return AdditionalChargesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def admin(self) -> AdminRequestBuilder:
        """
        The admin property
        """
        from .admin.admin_request_builder import AdminRequestBuilder

        return AdminRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ai(self) -> AiRequestBuilder:
        """
        The ai property
        """
        from .ai.ai_request_builder import AiRequestBuilder

        return AiRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignments(self) -> AssignmentsRequestBuilder:
        """
        The assignments property
        """
        from .assignments.assignments_request_builder import AssignmentsRequestBuilder

        return AssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def availability(self) -> AvailabilityRequestBuilder:
        """
        The availability property
        """
        from .availability.availability_request_builder import AvailabilityRequestBuilder

        return AvailabilityRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bankaccounts(self) -> BankaccountsRequestBuilder:
        """
        The bankaccounts property
        """
        from .bankaccounts.bankaccounts_request_builder import BankaccountsRequestBuilder

        return BankaccountsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def browser(self) -> BrowserRequestBuilder:
        """
        The browser property
        """
        from .browser.browser_request_builder import BrowserRequestBuilder

        return BrowserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cache(self) -> CacheRequestBuilder:
        """
        The cache property
        """
        from .cache.cache_request_builder import CacheRequestBuilder

        return CacheRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def callbacks(self) -> CallbacksRequestBuilder:
        """
        The callbacks property
        """
        from .callbacks.callbacks_request_builder import CallbacksRequestBuilder

        return CallbacksRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cars(self) -> CarsRequestBuilder:
        """
        The cars property
        """
        from .cars.cars_request_builder import CarsRequestBuilder

        return CarsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def chats(self) -> ChatsRequestBuilder:
        """
        The chats property
        """
        from .chats.chats_request_builder import ChatsRequestBuilder

        return ChatsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def checklist_events(self) -> ChecklistEventsRequestBuilder:
        """
        The checklistEvents property
        """
        from .checklist_events.checklist_events_request_builder import ChecklistEventsRequestBuilder

        return ChecklistEventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def checklist_items(self) -> ChecklistItemsRequestBuilder:
        """
        The checklistItems property
        """
        from .checklist_items.checklist_items_request_builder import ChecklistItemsRequestBuilder

        return ChecklistItemsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def checklists(self) -> ChecklistsRequestBuilder:
        """
        The checklists property
        """
        from .checklists.checklists_request_builder import ChecklistsRequestBuilder

        return ChecklistsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cloud(self) -> CloudRequestBuilder:
        """
        The cloud property
        """
        from .cloud.cloud_request_builder import CloudRequestBuilder

        return CloudRequestBuilder(self.request_adapter, self.path_parameters)
    
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
    def components(self) -> ComponentsRequestBuilder:
        """
        The components property
        """
        from .components.components_request_builder import ComponentsRequestBuilder

        return ComponentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def config_values(self) -> ConfigValuesRequestBuilder:
        """
        The configValues property
        """
        from .config_values.config_values_request_builder import ConfigValuesRequestBuilder

        return ConfigValuesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def contracts(self) -> ContractsRequestBuilder:
        """
        The contracts property
        """
        from .contracts.contracts_request_builder import ContractsRequestBuilder

        return ContractsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cpus(self) -> CpusRequestBuilder:
        """
        The cpus property
        """
        from .cpus.cpus_request_builder import CpusRequestBuilder

        return CpusRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def currencies(self) -> CurrenciesRequestBuilder:
        """
        The currencies property
        """
        from .currencies.currencies_request_builder import CurrenciesRequestBuilder

        return CurrenciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def customer_notifications(self) -> CustomerNotificationsRequestBuilder:
        """
        The customerNotifications property
        """
        from .customer_notifications.customer_notifications_request_builder import CustomerNotificationsRequestBuilder

        return CustomerNotificationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def customer_portal_wizards(self) -> CustomerPortalWizardsRequestBuilder:
        """
        The customerPortalWizards property
        """
        from .customer_portal_wizards.customer_portal_wizards_request_builder import CustomerPortalWizardsRequestBuilder

        return CustomerPortalWizardsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def documents(self) -> DocumentsRequestBuilder:
        """
        The documents property
        """
        from .documents.documents_request_builder import DocumentsRequestBuilder

        return DocumentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def domains(self) -> DomainsRequestBuilder:
        """
        The domains property
        """
        from .domains.domains_request_builder import DomainsRequestBuilder

        return DomainsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def email_accounts(self) -> EmailAccountsRequestBuilder:
        """
        The emailAccounts property
        """
        from .email_accounts.email_accounts_request_builder import EmailAccountsRequestBuilder

        return EmailAccountsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def email_settings(self) -> EmailSettingsRequestBuilder:
        """
        The emailSettings property
        """
        from .email_settings.email_settings_request_builder import EmailSettingsRequestBuilder

        return EmailSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def employees(self) -> EmployeesRequestBuilder:
        """
        The employees property
        """
        from .employees.employees_request_builder import EmployeesRequestBuilder

        return EmployeesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def entity_files(self) -> EntityFilesRequestBuilder:
        """
        The entityFiles property
        """
        from .entity_files.entity_files_request_builder import EntityFilesRequestBuilder

        return EntityFilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def erp(self) -> ErpRequestBuilder:
        """
        The erp property
        """
        from .erp.erp_request_builder import ErpRequestBuilder

        return ErpRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def escalations(self) -> EscalationsRequestBuilder:
        """
        The escalations property
        """
        from .escalations.escalations_request_builder import EscalationsRequestBuilder

        return EscalationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ev(self) -> EvRequestBuilder:
        """
        The ev property
        """
        from .ev.ev_request_builder import EvRequestBuilder

        return EvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def externals(self) -> ExternalsRequestBuilder:
        """
        The externals property
        """
        from .externals.externals_request_builder import ExternalsRequestBuilder

        return ExternalsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def favorites(self) -> FavoritesRequestBuilder:
        """
        The favorites property
        """
        from .favorites.favorites_request_builder import FavoritesRequestBuilder

        return FavoritesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def files_and_links(self) -> FilesAndLinksRequestBuilder:
        """
        The filesAndLinks property
        """
        from .files_and_links.files_and_links_request_builder import FilesAndLinksRequestBuilder

        return FilesAndLinksRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def files_and_links_media(self) -> FilesAndLinksMediaRequestBuilder:
        """
        The filesAndLinksMedia property
        """
        from .files_and_links_media.files_and_links_media_request_builder import FilesAndLinksMediaRequestBuilder

        return FilesAndLinksMediaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def files_and_links_url(self) -> FilesAndLinksUrlRequestBuilder:
        """
        The filesAndLinksUrl property
        """
        from .files_and_links_url.files_and_links_url_request_builder import FilesAndLinksUrlRequestBuilder

        return FilesAndLinksUrlRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def generic_assignments(self) -> GenericAssignmentsRequestBuilder:
        """
        The genericAssignments property
        """
        from .generic_assignments.generic_assignments_request_builder import GenericAssignmentsRequestBuilder

        return GenericAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def geocodes(self) -> GeocodesRequestBuilder:
        """
        The geocodes property
        """
        from .geocodes.geocodes_request_builder import GeocodesRequestBuilder

        return GeocodesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def git(self) -> GitRequestBuilder:
        """
        The git property
        """
        from .git.git_request_builder import GitRequestBuilder

        return GitRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def guarantee(self) -> GuaranteeRequestBuilder:
        """
        The guarantee property
        """
        from .guarantee.guarantee_request_builder import GuaranteeRequestBuilder

        return GuaranteeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def hdd_types(self) -> HddTypesRequestBuilder:
        """
        The hddTypes property
        """
        from .hdd_types.hdd_types_request_builder import HddTypesRequestBuilder

        return HddTypesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def holidays(self) -> HolidaysRequestBuilder:
        """
        The holidays property
        """
        from .holidays.holidays_request_builder import HolidaysRequestBuilder

        return HolidaysRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ical(self) -> IcalRequestBuilder:
        """
        The ical property
        """
        from .ical.ical_request_builder import IcalRequestBuilder

        return IcalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def identify(self) -> IdentifyRequestBuilder:
        """
        The identify property
        """
        from .identify.identify_request_builder import IdentifyRequestBuilder

        return IdentifyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ips(self) -> IpsRequestBuilder:
        """
        The ips property
        """
        from .ips.ips_request_builder import IpsRequestBuilder

        return IpsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def jwts(self) -> JwtsRequestBuilder:
        """
        The jwts property
        """
        from .jwts.jwts_request_builder import JwtsRequestBuilder

        return JwtsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def knowledge_base(self) -> KnowledgeBaseRequestBuilder:
        """
        The knowledgeBase property
        """
        from .knowledge_base.knowledge_base_request_builder import KnowledgeBaseRequestBuilder

        return KnowledgeBaseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def landing_page(self) -> LandingPageRequestBuilder:
        """
        The landingPage property
        """
        from .landing_page.landing_page_request_builder import LandingPageRequestBuilder

        return LandingPageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def log(self) -> LogRequestBuilder:
        """
        The log property
        """
        from .log.log_request_builder import LogRequestBuilder

        return LogRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def login(self) -> LoginRequestBuilder:
        """
        The login property
        """
        from .login.login_request_builder import LoginRequestBuilder

        return LoginRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def logo(self) -> LogoRequestBuilder:
        """
        The logo property
        """
        from .logo.logo_request_builder import LogoRequestBuilder

        return LogoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mail_robot(self) -> MailRobotRequestBuilder:
        """
        The mailRobot property
        """
        from .mail_robot.mail_robot_request_builder import MailRobotRequestBuilder

        return MailRobotRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mails(self) -> MailsRequestBuilder:
        """
        The mails property
        """
        from .mails.mails_request_builder import MailsRequestBuilder

        return MailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def management_dashboard(self) -> ManagementDashboardRequestBuilder:
        """
        The managementDashboard property
        """
        from .management_dashboard.management_dashboard_request_builder import ManagementDashboardRequestBuilder

        return ManagementDashboardRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def manufacturers(self) -> ManufacturersRequestBuilder:
        """
        The manufacturers property
        """
        from .manufacturers.manufacturers_request_builder import ManufacturersRequestBuilder

        return ManufacturersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mass(self) -> MassRequestBuilder:
        """
        The mass property
        """
        from .mass.mass_request_builder import MassRequestBuilder

        return MassRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mention(self) -> MentionRequestBuilder:
        """
        The mention property
        """
        from .mention.mention_request_builder import MentionRequestBuilder

        return MentionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def offer(self) -> OfferRequestBuilder:
        """
        The offer property
        """
        from .offer.offer_request_builder import OfferRequestBuilder

        return OfferRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def offers(self) -> OffersRequestBuilder:
        """
        The offers property
        """
        from .offers.offers_request_builder import OffersRequestBuilder

        return OffersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def os(self) -> OsRequestBuilder:
        """
        The os property
        """
        from .os.os_request_builder import OsRequestBuilder

        return OsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def overtime(self) -> OvertimeRequestBuilder:
        """
        The overtime property
        """
        from .overtime.overtime_request_builder import OvertimeRequestBuilder

        return OvertimeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def own_daily_services(self) -> OwnDailyServicesRequestBuilder:
        """
        The ownDailyServices property
        """
        from .own_daily_services.own_daily_services_request_builder import OwnDailyServicesRequestBuilder

        return OwnDailyServicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def passkey(self) -> PasskeyRequestBuilder:
        """
        The passkey property
        """
        from .passkey.passkey_request_builder import PasskeyRequestBuilder

        return PasskeyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def passwords(self) -> PasswordsRequestBuilder:
        """
        The passwords property
        """
        from .passwords.passwords_request_builder import PasswordsRequestBuilder

        return PasswordsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def payment_methods(self) -> PaymentMethodsRequestBuilder:
        """
        The paymentMethods property
        """
        from .payment_methods.payment_methods_request_builder import PaymentMethodsRequestBuilder

        return PaymentMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pcs(self) -> PcsRequestBuilder:
        """
        The pcs property
        """
        from .pcs.pcs_request_builder import PcsRequestBuilder

        return PcsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def peripheries(self) -> PeripheriesRequestBuilder:
        """
        The peripheries property
        """
        from .peripheries.peripheries_request_builder import PeripheriesRequestBuilder

        return PeripheriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def permissions(self) -> PermissionsRequestBuilder:
        """
        The permissions property
        """
        from .permissions.permissions_request_builder import PermissionsRequestBuilder

        return PermissionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def phone_calls(self) -> PhoneCallsRequestBuilder:
        """
        The phoneCalls property
        """
        from .phone_calls.phone_calls_request_builder import PhoneCallsRequestBuilder

        return PhoneCallsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def planning(self) -> PlanningRequestBuilder:
        """
        The planning property
        """
        from .planning.planning_request_builder import PlanningRequestBuilder

        return PlanningRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pop_up_notifications(self) -> PopUpNotificationsRequestBuilder:
        """
        The popUpNotifications property
        """
        from .pop_up_notifications.pop_up_notifications_request_builder import PopUpNotificationsRequestBuilder

        return PopUpNotificationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def portal(self) -> PortalRequestBuilder:
        """
        The portal property
        """
        from .portal.portal_request_builder import PortalRequestBuilder

        return PortalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def priorities(self) -> PrioritiesRequestBuilder:
        """
        The priorities property
        """
        from .priorities.priorities_request_builder import PrioritiesRequestBuilder

        return PrioritiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def projects(self) -> ProjectsRequestBuilder:
        """
        The projects property
        """
        from .projects.projects_request_builder import ProjectsRequestBuilder

        return ProjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def push(self) -> PushRequestBuilder:
        """
        The push property
        """
        from .push.push_request_builder import PushRequestBuilder

        return PushRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def qr(self) -> QrRequestBuilder:
        """
        The qr property
        """
        from .qr.qr_request_builder import QrRequestBuilder

        return QrRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def recurrence(self) -> RecurrenceRequestBuilder:
        """
        The recurrence property
        """
        from .recurrence.recurrence_request_builder import RecurrenceRequestBuilder

        return RecurrenceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remote_supports(self) -> RemoteSupportsRequestBuilder:
        """
        The remoteSupports property
        """
        from .remote_supports.remote_supports_request_builder import RemoteSupportsRequestBuilder

        return RemoteSupportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def roles(self) -> RolesRequestBuilder:
        """
        The roles property
        """
        from .roles.roles_request_builder import RolesRequestBuilder

        return RolesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def round(self) -> RoundRequestBuilder:
        """
        The round property
        """
        from .round.round_request_builder import RoundRequestBuilder

        return RoundRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sales_target(self) -> SalesTargetRequestBuilder:
        """
        The salesTarget property
        """
        from .sales_target.sales_target_request_builder import SalesTargetRequestBuilder

        return SalesTargetRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def search(self) -> SearchRequestBuilder:
        """
        The search property
        """
        from .search.search_request_builder import SearchRequestBuilder

        return SearchRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sentry(self) -> SentryRequestBuilder:
        """
        The sentry property
        """
        from .sentry.sentry_request_builder import SentryRequestBuilder

        return SentryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def services(self) -> ServicesRequestBuilder:
        """
        The services property
        """
        from .services.services_request_builder import ServicesRequestBuilder

        return ServicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sla(self) -> SlaRequestBuilder:
        """
        The sla property
        """
        from .sla.sla_request_builder import SlaRequestBuilder

        return SlaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def softwarelicenses(self) -> SoftwarelicensesRequestBuilder:
        """
        The softwarelicenses property
        """
        from .softwarelicenses.softwarelicenses_request_builder import SoftwarelicensesRequestBuilder

        return SoftwarelicensesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def starface(self) -> StarfaceRequestBuilder:
        """
        The starface property
        """
        from .starface.starface_request_builder import StarfaceRequestBuilder

        return StarfaceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def support_profile_categories(self) -> SupportProfileCategoriesRequestBuilder:
        """
        The supportProfileCategories property
        """
        from .support_profile_categories.support_profile_categories_request_builder import SupportProfileCategoriesRequestBuilder

        return SupportProfileCategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def support_rules(self) -> SupportRulesRequestBuilder:
        """
        The supportRules property
        """
        from .support_rules.support_rules_request_builder import SupportRulesRequestBuilder

        return SupportRulesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def support_types(self) -> SupportTypesRequestBuilder:
        """
        The supportTypes property
        """
        from .support_types.support_types_request_builder import SupportTypesRequestBuilder

        return SupportTypesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def supports(self) -> SupportsRequestBuilder:
        """
        The supports property
        """
        from .supports.supports_request_builder import SupportsRequestBuilder

        return SupportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sys_tasks(self) -> SysTasksRequestBuilder:
        """
        The sysTasks property
        """
        from .sys_tasks.sys_tasks_request_builder import SysTasksRequestBuilder

        return SysTasksRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def systemhaus_one(self) -> Systemhaus_oneRequestBuilder:
        """
        The systemhaus_one property
        """
        from .systemhaus_one.systemhaus_one_request_builder import Systemhaus_oneRequestBuilder

        return Systemhaus_oneRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tags(self) -> TagsRequestBuilder:
        """
        The tags property
        """
        from .tags.tags_request_builder import TagsRequestBuilder

        return TagsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tanss_events(self) -> TanssEventsRequestBuilder:
        """
        The tanssEvents property
        """
        from .tanss_events.tanss_events_request_builder import TanssEventsRequestBuilder

        return TanssEventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tanss_licenses(self) -> TanssLicensesRequestBuilder:
        """
        The tanssLicenses property
        """
        from .tanss_licenses.tanss_licenses_request_builder import TanssLicensesRequestBuilder

        return TanssLicensesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tasks(self) -> TasksRequestBuilder:
        """
        The tasks property
        """
        from .tasks.tasks_request_builder import TasksRequestBuilder

        return TasksRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def telephone_systems(self) -> TelephoneSystemsRequestBuilder:
        """
        The telephoneSystems property
        """
        from .telephone_systems.telephone_systems_request_builder import TelephoneSystemsRequestBuilder

        return TelephoneSystemsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def temp_cache(self) -> TempCacheRequestBuilder:
        """
        The tempCache property
        """
        from .temp_cache.temp_cache_request_builder import TempCacheRequestBuilder

        return TempCacheRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def templates(self) -> TemplatesRequestBuilder:
        """
        The templates property
        """
        from .templates.templates_request_builder import TemplatesRequestBuilder

        return TemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def text_modules(self) -> TextModulesRequestBuilder:
        """
        The textModules property
        """
        from .text_modules.text_modules_request_builder import TextModulesRequestBuilder

        return TextModulesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ticket_board(self) -> TicketBoardRequestBuilder:
        """
        The ticketBoard property
        """
        from .ticket_board.ticket_board_request_builder import TicketBoardRequestBuilder

        return TicketBoardRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ticket_workflows(self) -> TicketWorkflowsRequestBuilder:
        """
        The ticketWorkflows property
        """
        from .ticket_workflows.ticket_workflows_request_builder import TicketWorkflowsRequestBuilder

        return TicketWorkflowsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tickets(self) -> TicketsRequestBuilder:
        """
        The tickets property
        """
        from .tickets.tickets_request_builder import TicketsRequestBuilder

        return TicketsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def timeline(self) -> TimelineRequestBuilder:
        """
        The timeline property
        """
        from .timeline.timeline_request_builder import TimelineRequestBuilder

        return TimelineRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def timers(self) -> TimersRequestBuilder:
        """
        The timers property
        """
        from .timers.timers_request_builder import TimersRequestBuilder

        return TimersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def timestamps(self) -> TimestampsRequestBuilder:
        """
        The timestamps property
        """
        from .timestamps.timestamps_request_builder import TimestampsRequestBuilder

        return TimestampsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tmp_file_uploads(self) -> TmpFileUploadsRequestBuilder:
        """
        The tmpFileUploads property
        """
        from .tmp_file_uploads.tmp_file_uploads_request_builder import TmpFileUploadsRequestBuilder

        return TmpFileUploadsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def todos(self) -> TodosRequestBuilder:
        """
        The todos property
        """
        from .todos.todos_request_builder import TodosRequestBuilder

        return TodosRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def util(self) -> UtilRequestBuilder:
        """
        The util property
        """
        from .util.util_request_builder import UtilRequestBuilder

        return UtilRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def vacation_requests(self) -> VacationRequestsRequestBuilder:
        """
        The vacationRequests property
        """
        from .vacation_requests.vacation_requests_request_builder import VacationRequestsRequestBuilder

        return VacationRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def vouchers(self) -> VouchersRequestBuilder:
        """
        The vouchers property
        """
        from .vouchers.vouchers_request_builder import VouchersRequestBuilder

        return VouchersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def workflow_contracts(self) -> WorkflowContractsRequestBuilder:
        """
        The workflowContracts property
        """
        from .workflow_contracts.workflow_contracts_request_builder import WorkflowContractsRequestBuilder

        return WorkflowContractsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def working_hours(self) -> WorkingHoursRequestBuilder:
        """
        The workingHours property
        """
        from .working_hours.working_hours_request_builder import WorkingHoursRequestBuilder

        return WorkingHoursRequestBuilder(self.request_adapter, self.path_parameters)
    

