from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TnsSupportMetaInfos(AdditionalDataHolder, Parsable):
    """
    Optional map of meta information for a support, present only when the support carries such data (e.g. appointments synced from Outlook). Individual keys are omitted when not set.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # comma separated list of participant e-mail addresses
    o_u_t_l_o_o_k_p_a_r_t_i_c_i_p_a_n_t_s: Optional[str] = None
    # status of the synced appointment (e.g. "ACCEPTED", "REQUESTED", "CANCELED")
    s_y_n_c_a_p_p_o_i_n_t_m_e_n_t_s_t_a_t_u_s: Optional[str] = None
    # sync group / correlation id of the appointment
    s_y_n_c_g_r_o_u_p: Optional[str] = None
    # origin of a synced appointment (e.g. "TANSS", "OUTLOOK")
    s_y_n_c_o_r_i_g_i_n: Optional[str] = None
    # Microsoft Teams meeting url of the synced appointment
    t_e_a_m_s_u_r_l: Optional[str] = None
    # "1" if the support text was changed after the sync
    t_e_x_t_w_a_s_c_h_a_n_g_e_d: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TnsSupportMetaInfos:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TnsSupportMetaInfos
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TnsSupportMetaInfos()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "OUTLOOK_PARTICIPANTS": lambda n : setattr(self, 'o_u_t_l_o_o_k_p_a_r_t_i_c_i_p_a_n_t_s', n.get_str_value()),
            "SYNC_APPOINTMENT_STATUS": lambda n : setattr(self, 's_y_n_c_a_p_p_o_i_n_t_m_e_n_t_s_t_a_t_u_s', n.get_str_value()),
            "SYNC_GROUP": lambda n : setattr(self, 's_y_n_c_g_r_o_u_p', n.get_str_value()),
            "SYNC_ORIGIN": lambda n : setattr(self, 's_y_n_c_o_r_i_g_i_n', n.get_str_value()),
            "TEAMS_URL": lambda n : setattr(self, 't_e_a_m_s_u_r_l', n.get_str_value()),
            "TEXT_WAS_CHANGED": lambda n : setattr(self, 't_e_x_t_w_a_s_c_h_a_n_g_e_d', n.get_str_value()),
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
        writer.write_str_value("OUTLOOK_PARTICIPANTS", self.o_u_t_l_o_o_k_p_a_r_t_i_c_i_p_a_n_t_s)
        writer.write_str_value("SYNC_APPOINTMENT_STATUS", self.s_y_n_c_a_p_p_o_i_n_t_m_e_n_t_s_t_a_t_u_s)
        writer.write_str_value("SYNC_GROUP", self.s_y_n_c_g_r_o_u_p)
        writer.write_str_value("SYNC_ORIGIN", self.s_y_n_c_o_r_i_g_i_n)
        writer.write_str_value("TEAMS_URL", self.t_e_a_m_s_u_r_l)
        writer.write_str_value("TEXT_WAS_CHANGED", self.t_e_x_t_w_a_s_c_h_a_n_g_e_d)
        writer.write_additional_data_value(self.additional_data)
    

