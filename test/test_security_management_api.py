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
from nexus_sdk.api.security_management_api import SecurityManagementApi  # noqa: E501
from nexus_sdk.rest import ApiException


class TestSecurityManagementApi(unittest.TestCase):
    """SecurityManagementApi unit test stubs"""

    def setUp(self):
        self.api = SecurityManagementApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_user_sources(self):
        """Test case for get_user_sources

        Retrieve a list of the available user sources.  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
