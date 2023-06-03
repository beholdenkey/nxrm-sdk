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
from nexus_sdk.api.security_management_ldap_api import SecurityManagementLDAPApi  # noqa: E501
from nexus_sdk.rest import ApiException


class TestSecurityManagementLDAPApi(unittest.TestCase):
    """SecurityManagementLDAPApi unit test stubs"""

    def setUp(self):
        self.api = SecurityManagementLDAPApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_change_order(self):
        """Test case for change_order

        Change LDAP server order  # noqa: E501
        """
        pass

    def test_create_ldap_server(self):
        """Test case for create_ldap_server

        Create LDAP server  # noqa: E501
        """
        pass

    def test_delete_ldap_server(self):
        """Test case for delete_ldap_server

        Delete LDAP server  # noqa: E501
        """
        pass

    def test_get_ldap_server(self):
        """Test case for get_ldap_server

        Get LDAP server  # noqa: E501
        """
        pass

    def test_get_ldap_servers(self):
        """Test case for get_ldap_servers

        List LDAP servers  # noqa: E501
        """
        pass

    def test_update_ldap_server(self):
        """Test case for update_ldap_server

        Update LDAP server  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
