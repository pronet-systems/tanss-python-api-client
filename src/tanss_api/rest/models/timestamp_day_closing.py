from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TimestampDayClosing(AdditionalDataHolder, Parsable):
    """
    Describes a day closing of a timestamp statistic. Here, all values are persisted into the database with infosabout working time, vacation, documented supports and the balance for this day.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # returns the effective balance for this account (= totalTime - workingTimeCleaned)
    balance: Optional[int] = None
    # the id of the employee who has approved the day
    completed_by_employee_id: Optional[int] = None
    # the timestamp, when the employee has approved the day closing
    completed_on_date: Optional[int] = None
    # day for this day closing (YYYY-mm-dd)
    date: Optional[datetime.date] = None
    # a ratio between the documented supports to the "WORK" timestamps
    documented_percentage: Optional[int] = None
    # Number of total minutes of all documented supports
    documented_support: Optional[int] = None
    # id of the employee for this day closing
    employee_id: Optional[int] = None
    # Number of total minutes of paid absences (= vacation, illness, overtime and paid absences)
    paid_absences: Optional[int] = None
    # the total balance of all previous days accumulated, plus the balance of the current day
    total_balance: Optional[int] = None
    # the total balance of all previous -not shown- days accumulated
    total_balance_before_timeframe: Optional[int] = None
    # Cumulating the "totalTimestampWorkTime", "paidAbsences" and "unpaidAbsences"
    total_time: Optional[int] = None
    # Number of total minutes of all WORK timestamp periods for this day
    total_timestamp_work_time: Optional[int] = None
    # Number of total minutes of unpaid absences (= unpaid absences)
    unpaid_absences: Optional[int] = None
    # The number of minutes, the employee has to work on this day (based on his working time model)
    working_time: Optional[int] = None
    # Subtracts the "workingTime" with the minutes of "paid absences", thus returning the "effective" working time the employee has to work
    working_time_cleaned: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TimestampDayClosing:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TimestampDayClosing
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TimestampDayClosing()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "balance": lambda n : setattr(self, 'balance', n.get_int_value()),
            "completedByEmployeeId": lambda n : setattr(self, 'completed_by_employee_id', n.get_int_value()),
            "completedOnDate": lambda n : setattr(self, 'completed_on_date', n.get_int_value()),
            "date": lambda n : setattr(self, 'date', n.get_date_value()),
            "documentedPercentage": lambda n : setattr(self, 'documented_percentage', n.get_int_value()),
            "documentedSupport": lambda n : setattr(self, 'documented_support', n.get_int_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_int_value()),
            "paidAbsences": lambda n : setattr(self, 'paid_absences', n.get_int_value()),
            "totalBalance": lambda n : setattr(self, 'total_balance', n.get_int_value()),
            "totalBalanceBeforeTimeframe": lambda n : setattr(self, 'total_balance_before_timeframe', n.get_int_value()),
            "totalTime": lambda n : setattr(self, 'total_time', n.get_int_value()),
            "totalTimestampWorkTime": lambda n : setattr(self, 'total_timestamp_work_time', n.get_int_value()),
            "unpaidAbsences": lambda n : setattr(self, 'unpaid_absences', n.get_int_value()),
            "workingTime": lambda n : setattr(self, 'working_time', n.get_int_value()),
            "workingTimeCleaned": lambda n : setattr(self, 'working_time_cleaned', n.get_int_value()),
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
        writer.write_int_value("balance", self.balance)
        writer.write_int_value("completedByEmployeeId", self.completed_by_employee_id)
        writer.write_int_value("completedOnDate", self.completed_on_date)
        writer.write_date_value("date", self.date)
        writer.write_int_value("documentedPercentage", self.documented_percentage)
        writer.write_int_value("documentedSupport", self.documented_support)
        writer.write_int_value("employeeId", self.employee_id)
        writer.write_int_value("paidAbsences", self.paid_absences)
        writer.write_int_value("totalBalance", self.total_balance)
        writer.write_int_value("totalBalanceBeforeTimeframe", self.total_balance_before_timeframe)
        writer.write_int_value("totalTime", self.total_time)
        writer.write_int_value("totalTimestampWorkTime", self.total_timestamp_work_time)
        writer.write_int_value("unpaidAbsences", self.unpaid_absences)
        writer.write_int_value("workingTime", self.working_time)
        writer.write_int_value("workingTimeCleaned", self.working_time_cleaned)
        writer.write_additional_data_value(self.additional_data)
    

