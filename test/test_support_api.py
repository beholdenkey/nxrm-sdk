"""
    Nexus Repository Manager REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.42.0-01

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import unittest

import nxrm_sdk
from nxrm_sdk.api.support_api import SupportApi  # noqa: E501
from nxrm_sdk.rest import ApiException


class TestSupportApi(unittest.TestCase):
    """SupportApi unit test stubs"""

    def setUp(self):
        self.api = SupportApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_supportzip(self):
        """Test case for supportzip

        Creates and downloads a support zip  # noqa: E501
        """
        pass

    def test_supportzippath(self):
        """Test case for supportzippath

        Creates a support zip and returns the path  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
