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
from nexus_sdk.api.formats_api import FormatsApi  # noqa: E501
from nexus_sdk.rest import ApiException


class TestFormatsApi(unittest.TestCase):
    """FormatsApi unit test stubs"""

    def setUp(self):
        self.api = FormatsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get1(self):
        """Test case for get1

        Get upload field requirements for the desired format  # noqa: E501
        """
        pass

    def test_get2(self):
        """Test case for get2

        Get upload field requirements for each supported format  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
