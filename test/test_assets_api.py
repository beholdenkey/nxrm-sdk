# coding: utf-8

"""
    Nexus Repository Manager REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.42.0-01
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import nxrm_sdk
from nxrm_sdk.api.assets_api import AssetsApi  # noqa: E501
from nxrm_sdk.rest import ApiException


class TestAssetsApi(unittest.TestCase):
    """AssetsApi unit test stubs"""

    def setUp(self):
        self.api = AssetsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_asset(self):
        """Test case for delete_asset

        Delete a single asset  # noqa: E501
        """
        pass

    def test_get_asset_by_id(self):
        """Test case for get_asset_by_id

        Get a single asset  # noqa: E501
        """
        pass

    def test_get_assets(self):
        """Test case for get_assets

        List assets  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
