from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .assignment.assignment_request_builder import AssignmentRequestBuilder
    from .files.files_request_builder import FilesRequestBuilder
    from .graph.graph_request_builder import GraphRequestBuilder
    from .languages.languages_request_builder import LanguagesRequestBuilder
    from .mailpicker.mailpicker_request_builder import MailpickerRequestBuilder
    from .pref.pref_request_builder import PrefRequestBuilder
    from .reimport_solr.reimport_solr_request_builder import ReimportSolrRequestBuilder
    from .reset_solr.reset_solr_request_builder import ResetSolrRequestBuilder
    from .spref.spref_request_builder import SprefRequestBuilder
    from .test_solr.test_solr_request_builder import TestSolrRequestBuilder
    from .textmodule.textmodule_request_builder import TextmoduleRequestBuilder
    from .textmodules.textmodules_request_builder import TextmodulesRequestBuilder
    from .textvariables.textvariables_request_builder import TextvariablesRequestBuilder
    from .ws.ws_request_builder import WsRequestBuilder

class UtilRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/util
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new UtilRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/util", path_parameters)
    
    @property
    def assignment(self) -> AssignmentRequestBuilder:
        """
        The assignment property
        """
        from .assignment.assignment_request_builder import AssignmentRequestBuilder

        return AssignmentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def files(self) -> FilesRequestBuilder:
        """
        The files property
        """
        from .files.files_request_builder import FilesRequestBuilder

        return FilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph(self) -> GraphRequestBuilder:
        """
        The graph property
        """
        from .graph.graph_request_builder import GraphRequestBuilder

        return GraphRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def languages(self) -> LanguagesRequestBuilder:
        """
        The languages property
        """
        from .languages.languages_request_builder import LanguagesRequestBuilder

        return LanguagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mailpicker(self) -> MailpickerRequestBuilder:
        """
        The mailpicker property
        """
        from .mailpicker.mailpicker_request_builder import MailpickerRequestBuilder

        return MailpickerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pref(self) -> PrefRequestBuilder:
        """
        The pref property
        """
        from .pref.pref_request_builder import PrefRequestBuilder

        return PrefRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reimport_solr(self) -> ReimportSolrRequestBuilder:
        """
        The reimportSolr property
        """
        from .reimport_solr.reimport_solr_request_builder import ReimportSolrRequestBuilder

        return ReimportSolrRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reset_solr(self) -> ResetSolrRequestBuilder:
        """
        The resetSolr property
        """
        from .reset_solr.reset_solr_request_builder import ResetSolrRequestBuilder

        return ResetSolrRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def spref(self) -> SprefRequestBuilder:
        """
        The spref property
        """
        from .spref.spref_request_builder import SprefRequestBuilder

        return SprefRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def test_solr(self) -> TestSolrRequestBuilder:
        """
        The testSolr property
        """
        from .test_solr.test_solr_request_builder import TestSolrRequestBuilder

        return TestSolrRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def textmodule(self) -> TextmoduleRequestBuilder:
        """
        The textmodule property
        """
        from .textmodule.textmodule_request_builder import TextmoduleRequestBuilder

        return TextmoduleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def textmodules(self) -> TextmodulesRequestBuilder:
        """
        The textmodules property
        """
        from .textmodules.textmodules_request_builder import TextmodulesRequestBuilder

        return TextmodulesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def textvariables(self) -> TextvariablesRequestBuilder:
        """
        The textvariables property
        """
        from .textvariables.textvariables_request_builder import TextvariablesRequestBuilder

        return TextvariablesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ws(self) -> WsRequestBuilder:
        """
        The ws property
        """
        from .ws.ws_request_builder import WsRequestBuilder

        return WsRequestBuilder(self.request_adapter, self.path_parameters)
    

