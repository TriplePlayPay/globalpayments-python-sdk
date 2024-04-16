"""
Test Token Management
"""

import unittest
from python_sdk.globalpayments.api import ServicesConfig, ServicesContainer
from python_sdk.globalpayments.api.payment_methods.credit import CreditCardData


class IntegrationGatewaysPorticoConnectorTokenManageTests(unittest.TestCase):
    """
    Ensure token management requests work
    """

    config = ServicesConfig()
    config.secret_api_key = "skapi_cert_MZ97AQBP-EgA5j5Um2fXMdCqcukek6pG6VmVjDg02A"
    config.service_url = "https://cert.api2.heartlandportico.com"
    config.developer_id = "000000"
    config.version_number = "0000"

    ServicesContainer.configure(config)

    card = CreditCardData()
    card.number = "4111111111111111"
    card.exp_month = "12"
    card.exp_year = "2025"
    card.cvn = "123"

