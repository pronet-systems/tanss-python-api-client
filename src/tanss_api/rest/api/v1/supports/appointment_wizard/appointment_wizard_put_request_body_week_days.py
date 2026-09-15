from enum import Enum

class AppointmentWizardPutRequestBody_weekDays(str, Enum):
    SUNDAY = "SUNDAY",
    MONDAY = "MONDAY",
    TUESDAY = "TUESDAY",
    WEDNESDAY = "WEDNESDAY",
    THURSDAY = "THURSDAY",
    FRIDAY = "FRIDAY",
    SATURDAY = "SATURDAY",
    EVERYDAY = "EVERYDAY",
    HOLIDAY = "HOLIDAY",
    HOLIDAY_AM = "HOLIDAY_AM",
    HOLIDAY_PM = "HOLIDAY_PM",

