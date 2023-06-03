# coding: utf-8

"""
    Nexus Repository Manager REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.42.0-01
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import nexus_sdk
from nexus_sdk.api.product_licensing_api import ProductLicensingApi  # noqa: E501
from nexus_sdk.rest import ApiException


class TestProductLicensingApi(unittest.TestCase):
    """ProductLicensingApi unit test stubs"""

    def setUp(self):
        self.api = ProductLicensingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_license_status(self):
        """Test case for get_license_status

        Get the current license status.  # noqa: E501
        """
        pass

    def test_remove_license(self):
        """Test case for remove_license

        Uninstall license if present.  # noqa: E501
        """
        pass

    def test_set_license(self):
        """Test case for set_license

        Upload a new license file.  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
