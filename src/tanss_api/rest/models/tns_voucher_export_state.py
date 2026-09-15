from enum import Enum

class TnsVoucherExportState(str, Enum):
    NONE_ = "NONE",
    WAITING_FOR_VOUCHER_NR = "WAITING_FOR_VOUCHER_NR",
    VOUCHER_NR_WAS_TRANSMITTED = "VOUCHER_NR_WAS_TRANSMITTED",

