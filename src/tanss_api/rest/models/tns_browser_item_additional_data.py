from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsBrowserItemAdditionalData(AdditionalDataHolder, Parsable):
    """
    Zusatzdaten eines Browser-Elements; für SOFTWARELICENSE die Standardwerte der Softwarelizenz-Kategorie (vgl. TnsSoftwarelicenseType).
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The articleNumber property
    article_number: Optional[str] = None
    # The comment property
    comment: Optional[str] = None
    # The manufacturerNumber property
    manufacturer_number: Optional[str] = None
    # The standardMaxNumberOfInstallations property
    standard_max_number_of_installations: Optional[int] = None
    # The standardRenew property
    standard_renew: Optional[bool] = None
    # The standardRunningTime property
    standard_running_time: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsBrowserItemAdditionalData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsBrowserItemAdditionalData
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsBrowserItemAdditionalData()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "articleNumber": lambda n : setattr(self, 'article_number', n.get_str_value()),
            "comment": lambda n : setattr(self, 'comment', n.get_str_value()),
            "manufacturerNumber": lambda n : setattr(self, 'manufacturer_number', n.get_str_value()),
            "standardMaxNumberOfInstallations": lambda n : setattr(self, 'standard_max_number_of_installations', n.get_int_value()),
            "standardRenew": lambda n : setattr(self, 'standard_renew', n.get_bool_value()),
            "standardRunningTime": lambda n : setattr(self, 'standard_running_time', n.get_int_value()),
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
        writer.write_str_value("articleNumber", self.article_number)
        writer.write_str_value("comment", self.comment)
        writer.write_str_value("manufacturerNumber", self.manufacturer_number)
        writer.write_int_value("standardMaxNumberOfInstallations", self.standard_max_number_of_installations)
        writer.write_bool_value("standardRenew", self.standard_renew)
        writer.write_int_value("standardRunningTime", self.standard_running_time)
        writer.write_additional_data_value(self.additional_data)
    

