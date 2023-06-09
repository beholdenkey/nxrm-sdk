"""
    Nexus Repository Manager REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.42.0-01

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import unittest

import nxrm_sdk
from nxrm_sdk.api.security_certificates_api import SecurityCertificatesApi  # noqa: E501
from nxrm_sdk.rest import ApiException


class TestSecurityCertificatesApi(unittest.TestCase):
    """SecurityCertificatesApi unit test stubs"""

    def setUp(self):
        self.api = SecurityCertificatesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_certificate(self):
        """Test case for add_certificate

        Add a certificate to the trust store.  # noqa: E501
        """
        pass

    def test_get_trust_store_certificates(self):
        """Test case for get_trust_store_certificates

        Retrieve a list of certificates added to the trust store.  # noqa: E501
        """
        pass

    def test_remove_certificate(self):
        """Test case for remove_certificate

        Remove a certificate in the trust store.  # noqa: E501
        """
        pass

    def test_retrieve_certificate(self):
        """Test case for retrieve_certificate

        Helper method to retrieve certificate details from a remote system.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
