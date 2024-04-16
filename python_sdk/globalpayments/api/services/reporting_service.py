import python_sdk.globalpayments as gp
from python_sdk.globalpayments.api.entities.enums import ReportType


class ReportingService(object):
    @staticmethod
    def activity():
        return gp.api.builders.TransactionReportBuilder(ReportType.Activity)

    @staticmethod
    def transaction_detail(transaction_id=None):
        return gp.api.builders.TransactionReportBuilder(
            ReportType.TransactionDetail
        ).with_transaction_id(transaction_id)

    @staticmethod
    def find_transactions():
        return gp.api.builders.TransactionReportBuilder(ReportType.FindTransactions)
