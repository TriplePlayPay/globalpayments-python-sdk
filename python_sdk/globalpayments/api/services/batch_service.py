from python_sdk.globalpayments.api.builders import ManagementBuilder
from python_sdk.globalpayments.api.entities.batch_summary import BatchSummary
from python_sdk.globalpayments.api.entities.enums import TransactionType


class BatchService(object):
    @staticmethod
    def close_batch(config_name="default"):
        _response = ManagementBuilder(
            TransactionType.BatchClose
        ).execute(config_name)
        return True
