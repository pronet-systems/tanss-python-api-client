from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tns_branch_filter_type import TnsBranchFilterType
    from .tns_document_type_enum import TnsDocumentTypeEnum

@dataclass
class TnsDocumentConfiguration(AdditionalDataHolder, Parsable):
    """
    filter object for fetching a document list
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # filter settings for branches
    branch_filter: Optional[TnsBranchFilterType] = None
    # if given, will only show documents of this company
    company_id: Optional[int] = None
    # show only documents for this assignment (linkId)
    link_id: Optional[int] = None
    # show only documents for this assignment (linkTypeId)
    link_type_id: Optional[int] = None
    # text filter for documents
    text_filter: Optional[str] = None
    # The types property
    types: Optional[list[TnsDocumentTypeEnum]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsDocumentConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsDocumentConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsDocumentConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tns_branch_filter_type import TnsBranchFilterType
        from .tns_document_type_enum import TnsDocumentTypeEnum

        from .tns_branch_filter_type import TnsBranchFilterType
        from .tns_document_type_enum import TnsDocumentTypeEnum

        fields: dict[str, Callable[[Any], None]] = {
            "branchFilter": lambda n : setattr(self, 'branch_filter', n.get_enum_value(TnsBranchFilterType)),
            "companyId": lambda n : setattr(self, 'company_id', n.get_int_value()),
            "linkId": lambda n : setattr(self, 'link_id', n.get_int_value()),
            "linkTypeId": lambda n : setattr(self, 'link_type_id', n.get_int_value()),
            "textFilter": lambda n : setattr(self, 'text_filter', n.get_str_value()),
            "types": lambda n : setattr(self, 'types', n.get_collection_of_enum_values(TnsDocumentTypeEnum)),
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
        writer.write_enum_value("branchFilter", self.branch_filter)
        writer.write_int_value("companyId", self.company_id)
        writer.write_int_value("linkId", self.link_id)
        writer.write_int_value("linkTypeId", self.link_type_id)
        writer.write_str_value("textFilter", self.text_filter)
        writer.write_collection_of_enum_values("types", self.types)
        writer.write_additional_data_value(self.additional_data)
    

