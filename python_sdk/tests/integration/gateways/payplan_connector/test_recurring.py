"""
Test Recurring
"""
import datetime
import unittest
from python_sdk.globalpayments.api import ServicesConfig, ServicesContainer


class IntegrationGatewaysPorticoConnectorDebitTests(unittest.TestCase):
    """
    Ensure recurring transactions work
    """

    config = ServicesConfig()
    config.secret_api_key = "skapi_cert_MaePAQBr-1QAqjfckFC8FTbRTT120bVQUlfVOjgCBw"
    config.service_url = "https://cert.api2.heartlandportico.com"

    ServicesContainer.configure(config, "recurring")

    @staticmethod
    def payment_id(payment_type):
        return "{0}-GlobalApi-{1}".format(
            datetime.date.today().isoformat(), payment_type
        )
