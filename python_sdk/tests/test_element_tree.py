import unittest
from python_sdk.globalpayments.api.utils import ElementTree
from python_sdk.globalpayments.api.builders import *


class ElementTreeTests(unittest.TestCase):
    def test_tree_creation(self):
        et = ElementTree()
        builder = AuthorizationBuilder(TransactionType.Auth)
        self.assertIsNotNone(et)
