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
from nexus_sdk.api.security_management_realms_api import (  # noqa: E501
    SecurityManagementRealmsApi,
)
from nexus_sdk.rest import ApiException


class TestSecurityManagementRealmsApi(unittest.TestCase):
    """SecurityManagementRealmsApi unit test stubs"""

    def setUp(self):
        self.api = SecurityManagementRealmsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_active_realms(self):
        """Test case for get_active_realms

        List the active realm IDs in order  # noqa: E501
        """
        pass

    def test_get_realms(self):
        """Test case for get_realms

        List the available realms  # noqa: E501
        """
        pass

    def test_set_active_realms(self):
        """Test case for set_active_realms

        Set the active security realms in the order they should be used  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
