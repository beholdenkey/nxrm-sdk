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
from nexus_sdk.api.read_only_api import ReadOnlyApi  # noqa: E501
from nexus_sdk.rest import ApiException


class TestReadOnlyApi(unittest.TestCase):
    """ReadOnlyApi unit test stubs"""

    def setUp(self):
        self.api = ReadOnlyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_force_release(self):
        """Test case for force_release

        Forcibly release read-only  # noqa: E501
        """
        pass

    def test_freeze(self):
        """Test case for freeze

        Enable read-only  # noqa: E501
        """
        pass

    def test_get(self):
        """Test case for get

        Get read-only state  # noqa: E501
        """
        pass

    def test_release(self):
        """Test case for release

        Release read-only  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
