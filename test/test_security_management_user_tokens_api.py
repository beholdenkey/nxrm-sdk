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
from nexus_sdk.api.security_management_user_tokens_api import (  # noqa: E501
    SecurityManagementUserTokensApi,
)
from nexus_sdk.rest import ApiException


class TestSecurityManagementUserTokensApi(unittest.TestCase):
    """SecurityManagementUserTokensApi unit test stubs"""

    def setUp(self):
        self.api = SecurityManagementUserTokensApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_reset_all_user_tokens(self):
        """Test case for reset_all_user_tokens

        Invalidate all existing user tokens.  # noqa: E501
        """
        pass

    def test_service_status(self):
        """Test case for service_status

        Show if the user token capability is enabled or not  # noqa: E501
        """
        pass

    def test_set_service_status(self):
        """Test case for set_service_status

        Enable/Disable the user token capability  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
