# coding: utf-8

"""
    Nexus Repository Manager REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.42.0-01
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class CreateLdapServerXo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        "name": "str",
        "protocol": "str",
        "use_trust_store": "bool",
        "host": "str",
        "port": "int",
        "search_base": "str",
        "auth_scheme": "str",
        "auth_realm": "str",
        "auth_username": "str",
        "connection_timeout_seconds": "int",
        "connection_retry_delay_seconds": "int",
        "max_incidents_count": "int",
        "user_base_dn": "str",
        "user_subtree": "bool",
        "user_object_class": "str",
        "user_ldap_filter": "str",
        "user_id_attribute": "str",
        "user_real_name_attribute": "str",
        "user_email_address_attribute": "str",
        "user_password_attribute": "str",
        "ldap_groups_as_roles": "bool",
        "group_type": "str",
        "group_base_dn": "str",
        "group_subtree": "bool",
        "group_object_class": "str",
        "group_id_attribute": "str",
        "group_member_attribute": "str",
        "group_member_format": "str",
        "user_member_of_attribute": "str",
        "auth_password": "str",
    }

    attribute_map = {
        "name": "name",
        "protocol": "protocol",
        "use_trust_store": "useTrustStore",
        "host": "host",
        "port": "port",
        "search_base": "searchBase",
        "auth_scheme": "authScheme",
        "auth_realm": "authRealm",
        "auth_username": "authUsername",
        "connection_timeout_seconds": "connectionTimeoutSeconds",
        "connection_retry_delay_seconds": "connectionRetryDelaySeconds",
        "max_incidents_count": "maxIncidentsCount",
        "user_base_dn": "userBaseDn",
        "user_subtree": "userSubtree",
        "user_object_class": "userObjectClass",
        "user_ldap_filter": "userLdapFilter",
        "user_id_attribute": "userIdAttribute",
        "user_real_name_attribute": "userRealNameAttribute",
        "user_email_address_attribute": "userEmailAddressAttribute",
        "user_password_attribute": "userPasswordAttribute",
        "ldap_groups_as_roles": "ldapGroupsAsRoles",
        "group_type": "groupType",
        "group_base_dn": "groupBaseDn",
        "group_subtree": "groupSubtree",
        "group_object_class": "groupObjectClass",
        "group_id_attribute": "groupIdAttribute",
        "group_member_attribute": "groupMemberAttribute",
        "group_member_format": "groupMemberFormat",
        "user_member_of_attribute": "userMemberOfAttribute",
        "auth_password": "authPassword",
    }

    def __init__(
        self,
        name=None,
        protocol=None,
        use_trust_store=None,
        host=None,
        port=None,
        search_base=None,
        auth_scheme=None,
        auth_realm=None,
        auth_username=None,
        connection_timeout_seconds=None,
        connection_retry_delay_seconds=None,
        max_incidents_count=None,
        user_base_dn=None,
        user_subtree=None,
        user_object_class=None,
        user_ldap_filter=None,
        user_id_attribute=None,
        user_real_name_attribute=None,
        user_email_address_attribute=None,
        user_password_attribute=None,
        ldap_groups_as_roles=None,
        group_type=None,
        group_base_dn=None,
        group_subtree=None,
        group_object_class=None,
        group_id_attribute=None,
        group_member_attribute=None,
        group_member_format=None,
        user_member_of_attribute=None,
        auth_password=None,
    ):  # noqa: E501
        """CreateLdapServerXo - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._protocol = None
        self._use_trust_store = None
        self._host = None
        self._port = None
        self._search_base = None
        self._auth_scheme = None
        self._auth_realm = None
        self._auth_username = None
        self._connection_timeout_seconds = None
        self._connection_retry_delay_seconds = None
        self._max_incidents_count = None
        self._user_base_dn = None
        self._user_subtree = None
        self._user_object_class = None
        self._user_ldap_filter = None
        self._user_id_attribute = None
        self._user_real_name_attribute = None
        self._user_email_address_attribute = None
        self._user_password_attribute = None
        self._ldap_groups_as_roles = None
        self._group_type = None
        self._group_base_dn = None
        self._group_subtree = None
        self._group_object_class = None
        self._group_id_attribute = None
        self._group_member_attribute = None
        self._group_member_format = None
        self._user_member_of_attribute = None
        self._auth_password = None
        self.discriminator = None
        self.name = name
        self.protocol = protocol
        if use_trust_store is not None:
            self.use_trust_store = use_trust_store
        self.host = host
        self.port = port
        self.search_base = search_base
        self.auth_scheme = auth_scheme
        if auth_realm is not None:
            self.auth_realm = auth_realm
        if auth_username is not None:
            self.auth_username = auth_username
        self.connection_timeout_seconds = connection_timeout_seconds
        self.connection_retry_delay_seconds = connection_retry_delay_seconds
        self.max_incidents_count = max_incidents_count
        if user_base_dn is not None:
            self.user_base_dn = user_base_dn
        if user_subtree is not None:
            self.user_subtree = user_subtree
        if user_object_class is not None:
            self.user_object_class = user_object_class
        if user_ldap_filter is not None:
            self.user_ldap_filter = user_ldap_filter
        if user_id_attribute is not None:
            self.user_id_attribute = user_id_attribute
        if user_real_name_attribute is not None:
            self.user_real_name_attribute = user_real_name_attribute
        if user_email_address_attribute is not None:
            self.user_email_address_attribute = user_email_address_attribute
        if user_password_attribute is not None:
            self.user_password_attribute = user_password_attribute
        if ldap_groups_as_roles is not None:
            self.ldap_groups_as_roles = ldap_groups_as_roles
        self.group_type = group_type
        if group_base_dn is not None:
            self.group_base_dn = group_base_dn
        if group_subtree is not None:
            self.group_subtree = group_subtree
        if group_object_class is not None:
            self.group_object_class = group_object_class
        if group_id_attribute is not None:
            self.group_id_attribute = group_id_attribute
        if group_member_attribute is not None:
            self.group_member_attribute = group_member_attribute
        if group_member_format is not None:
            self.group_member_format = group_member_format
        if user_member_of_attribute is not None:
            self.user_member_of_attribute = user_member_of_attribute
        self.auth_password = auth_password

    @property
    def name(self):
        """Gets the name of this CreateLdapServerXo.  # noqa: E501

        LDAP server name  # noqa: E501

        :return: The name of this CreateLdapServerXo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateLdapServerXo.

        LDAP server name  # noqa: E501

        :param name: The name of this CreateLdapServerXo.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError(
                "Invalid value for `name`, must not be `None`"
            )  # noqa: E501

        self._name = name

    @property
    def protocol(self):
        """Gets the protocol of this CreateLdapServerXo.  # noqa: E501

        LDAP server connection Protocol to use  # noqa: E501

        :return: The protocol of this CreateLdapServerXo.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this CreateLdapServerXo.

        LDAP server connection Protocol to use  # noqa: E501

        :param protocol: The protocol of this CreateLdapServerXo.  # noqa: E501
        :type: str
        """
        if protocol is None:
            raise ValueError(
                "Invalid value for `protocol`, must not be `None`"
            )  # noqa: E501
        allowed_values = ["ldap", "ldaps"]  # noqa: E501
        if protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `protocol` ({0}), must be one of {1}".format(  # noqa: E501
                    protocol, allowed_values
                )
            )

        self._protocol = protocol

    @property
    def use_trust_store(self):
        """Gets the use_trust_store of this CreateLdapServerXo.  # noqa: E501

        Whether to use certificates stored in Nexus Repository Manager's truststore  # noqa: E501

        :return: The use_trust_store of this CreateLdapServerXo.  # noqa: E501
        :rtype: bool
        """
        return self._use_trust_store

    @use_trust_store.setter
    def use_trust_store(self, use_trust_store):
        """Sets the use_trust_store of this CreateLdapServerXo.

        Whether to use certificates stored in Nexus Repository Manager's truststore  # noqa: E501

        :param use_trust_store: The use_trust_store of this CreateLdapServerXo.  # noqa: E501
        :type: bool
        """

        self._use_trust_store = use_trust_store

    @property
    def host(self):
        """Gets the host of this CreateLdapServerXo.  # noqa: E501

        LDAP server connection hostname  # noqa: E501

        :return: The host of this CreateLdapServerXo.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this CreateLdapServerXo.

        LDAP server connection hostname  # noqa: E501

        :param host: The host of this CreateLdapServerXo.  # noqa: E501
        :type: str
        """
        if host is None:
            raise ValueError(
                "Invalid value for `host`, must not be `None`"
            )  # noqa: E501

        self._host = host

    @property
    def port(self):
        """Gets the port of this CreateLdapServerXo.  # noqa: E501

        LDAP server connection port to use  # noqa: E501

        :return: The port of this CreateLdapServerXo.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this CreateLdapServerXo.

        LDAP server connection port to use  # noqa: E501

        :param port: The port of this CreateLdapServerXo.  # noqa: E501
        :type: int
        """
        if port is None:
            raise ValueError(
                "Invalid value for `port`, must not be `None`"
            )  # noqa: E501

        self._port = port

    @property
    def search_base(self):
        """Gets the search_base of this CreateLdapServerXo.  # noqa: E501

        LDAP location to be added to the connection URL  # noqa: E501

        :return: The search_base of this CreateLdapServerXo.  # noqa: E501
        :rtype: str
        """
        return self._search_base

    @search_base.setter
    def search_base(self, search_base):
        """Sets the search_base of this CreateLdapServerXo.

        LDAP location to be added to the connection URL  # noqa: E501

        :param search_base: The search_base of this CreateLdapServerXo.  # noqa: E501
        :type: str
        """
        if search_base is None:
            raise ValueError(
                "Invalid value for `search_base`, must not be `None`"
            )  # noqa: E501

        self._search_base = search_base

    @property
    def auth_scheme(self):
        """Gets the auth_scheme of this CreateLdapServerXo.  # noqa: E501

        Authentication scheme used for connecting to LDAP server  # noqa: E501

        :return: The auth_scheme of this CreateLdapServerXo.  # noqa: E501
        :rtype: str
        """
        return self._auth_scheme

    @auth_scheme.setter
    def auth_scheme(self, auth_scheme):
        """Sets the auth_scheme of this CreateLdapServerXo.

        Authentication scheme used for connecting to LDAP server  # noqa: E501

        :param auth_scheme: The auth_scheme of this CreateLdapServerXo.  # noqa: E501
        :type: str
        """
        if auth_scheme is None:
            raise ValueError(
                "Invalid value for `auth_scheme`, must not be `None`"
            )  # noqa: E501
        allowed_values = ["NONE", "SIMPLE", "DIGEST_MD5", "CRAM_MD5"]  # noqa: E501
        if auth_scheme not in allowed_values:
            raise ValueError(
                "Invalid value for `auth_scheme` ({0}), must be one of {1}".format(  # noqa: E501
                    auth_scheme, allowed_values
                )
            )

        self._auth_scheme = auth_scheme

    @property
    def auth_realm(self):
        """Gets the auth_realm of this CreateLdapServerXo.  # noqa: E501

        The SASL realm to bind to. Required if authScheme is CRAM_MD5 or DIGEST_MD5  # noqa: E501

        :return: The auth_realm of this CreateLdapServerXo.  # noqa: E501
        :rtype: str
        """
        return self._auth_realm

    @auth_realm.setter
    def auth_realm(self, auth_realm):
        """Sets the auth_realm of this CreateLdapServerXo.

        The SASL realm to bind to. Required if authScheme is CRAM_MD5 or DIGEST_MD5  # noqa: E501

        :param auth_realm: The auth_realm of this CreateLdapServerXo.  # noqa: E501
        :type: str
        """

        self._auth_realm = auth_realm

    @property
    def auth_username(self):
        """Gets the auth_username of this CreateLdapServerXo.  # noqa: E501

        This must be a fully qualified username if simple authentication is used. Required if authScheme other than none.  # noqa: E501

        :return: The auth_username of this CreateLdapServerXo.  # noqa: E501
        :rtype: str
        """
        return self._auth_username

    @auth_username.setter
    def auth_username(self, auth_username):
        """Sets the auth_username of this CreateLdapServerXo.

        This must be a fully qualified username if simple authentication is used. Required if authScheme other than none.  # noqa: E501

        :param auth_username: The auth_username of this CreateLdapServerXo.  # noqa: E501
        :type: str
        """

        self._auth_username = auth_username

    @property
    def connection_timeout_seconds(self):
        """Gets the connection_timeout_seconds of this CreateLdapServerXo.  # noqa: E501

        How long to wait before timeout  # noqa: E501

        :return: The connection_timeout_seconds of this CreateLdapServerXo.  # noqa: E501
        :rtype: int
        """
        return self._connection_timeout_seconds

    @connection_timeout_seconds.setter
    def connection_timeout_seconds(self, connection_timeout_seconds):
        """Sets the connection_timeout_seconds of this CreateLdapServerXo.

        How long to wait before timeout  # noqa: E501

        :param connection_timeout_seconds: The connection_timeout_seconds of this CreateLdapServerXo.  # noqa: E501
        :type: int
        """
        if connection_timeout_seconds is None:
            raise ValueError(
                "Invalid value for `connection_timeout_seconds`, must not be `None`"
            )  # noqa: E501

        self._connection_timeout_seconds = connection_timeout_seconds

    @property
    def connection_retry_delay_seconds(self):
        """Gets the connection_retry_delay_seconds of this CreateLdapServerXo.  # noqa: E501

        How long to wait before retrying  # noqa: E501

        :return: The connection_retry_delay_seconds of this CreateLdapServerXo.  # noqa: E501
        :rtype: int
        """
        return self._connection_retry_delay_seconds

    @connection_retry_delay_seconds.setter
    def connection_retry_delay_seconds(self, connection_retry_delay_seconds):
        """Sets the connection_retry_delay_seconds of this CreateLdapServerXo.

        How long to wait before retrying  # noqa: E501

        :param connection_retry_delay_seconds: The connection_retry_delay_seconds of this CreateLdapServerXo.  # noqa: E501
        :type: int
        """
        if connection_retry_delay_seconds is None:
            raise ValueError(
                "Invalid value for `connection_retry_delay_seconds`, must not be `None`"
            )  # noqa: E501

        self._connection_retry_delay_seconds = connection_retry_delay_seconds

    @property
    def max_incidents_count(self):
        """Gets the max_incidents_count of this CreateLdapServerXo.  # noqa: E501

        How many retry attempts  # noqa: E501

        :return: The max_incidents_count of this CreateLdapServerXo.  # noqa: E501
        :rtype: int
        """
        return self._max_incidents_count

    @max_incidents_count.setter
    def max_incidents_count(self, max_incidents_count):
        """Sets the max_incidents_count of this CreateLdapServerXo.

        How many retry attempts  # noqa: E501

        :param max_incidents_count: The max_incidents_count of this CreateLdapServerXo.  # noqa: E501
        :type: int
        """
        if max_incidents_count is None:
            raise ValueError(
                "Invalid value for `max_incidents_count`, must not be `None`"
            )  # noqa: E501

        self._max_incidents_count = max_incidents_count

    @property
    def user_base_dn(self):
        """Gets the user_base_dn of this CreateLdapServerXo.  # noqa: E501

        The relative DN where user objects are found (e.g. ou=people). This value will have the Search base DN value appended to form the full User search base DN.  # noqa: E501

        :return: The user_base_dn of this CreateLdapServerXo.  # noqa: E501
        :rtype: str
        """
        return self._user_base_dn

    @user_base_dn.setter
    def user_base_dn(self, user_base_dn):
        """Sets the user_base_dn of this CreateLdapServerXo.

        The relative DN where user objects are found (e.g. ou=people). This value will have the Search base DN value appended to form the full User search base DN.  # noqa: E501

        :param user_base_dn: The user_base_dn of this CreateLdapServerXo.  # noqa: E501
        :type: str
        """

        self._user_base_dn = user_base_dn

    @property
    def user_subtree(self):
        """Gets the user_subtree of this CreateLdapServerXo.  # noqa: E501

        Are users located in structures below the user base DN?  # noqa: E501

        :return: The user_subtree of this CreateLdapServerXo.  # noqa: E501
        :rtype: bool
        """
        return self._user_subtree

    @user_subtree.setter
    def user_subtree(self, user_subtree):
        """Sets the user_subtree of this CreateLdapServerXo.

        Are users located in structures below the user base DN?  # noqa: E501

        :param user_subtree: The user_subtree of this CreateLdapServerXo.  # noqa: E501
        :type: bool
        """

        self._user_subtree = user_subtree

    @property
    def user_object_class(self):
        """Gets the user_object_class of this CreateLdapServerXo.  # noqa: E501

        LDAP class for user objects  # noqa: E501

        :return: The user_object_class of this CreateLdapServerXo.  # noqa: E501
        :rtype: str
        """
        return self._user_object_class

    @user_object_class.setter
    def user_object_class(self, user_object_class):
        """Sets the user_object_class of this CreateLdapServerXo.

        LDAP class for user objects  # noqa: E501

        :param user_object_class: The user_object_class of this CreateLdapServerXo.  # noqa: E501
        :type: str
        """

        self._user_object_class = user_object_class

    @property
    def user_ldap_filter(self):
        """Gets the user_ldap_filter of this CreateLdapServerXo.  # noqa: E501

        LDAP search filter to limit user search  # noqa: E501

        :return: The user_ldap_filter of this CreateLdapServerXo.  # noqa: E501
        :rtype: str
        """
        return self._user_ldap_filter

    @user_ldap_filter.setter
    def user_ldap_filter(self, user_ldap_filter):
        """Sets the user_ldap_filter of this CreateLdapServerXo.

        LDAP search filter to limit user search  # noqa: E501

        :param user_ldap_filter: The user_ldap_filter of this CreateLdapServerXo.  # noqa: E501
        :type: str
        """

        self._user_ldap_filter = user_ldap_filter

    @property
    def user_id_attribute(self):
        """Gets the user_id_attribute of this CreateLdapServerXo.  # noqa: E501

        This is used to find a user given its user ID  # noqa: E501

        :return: The user_id_attribute of this CreateLdapServerXo.  # noqa: E501
        :rtype: str
        """
        return self._user_id_attribute

    @user_id_attribute.setter
    def user_id_attribute(self, user_id_attribute):
        """Sets the user_id_attribute of this CreateLdapServerXo.

        This is used to find a user given its user ID  # noqa: E501

        :param user_id_attribute: The user_id_attribute of this CreateLdapServerXo.  # noqa: E501
        :type: str
        """

        self._user_id_attribute = user_id_attribute

    @property
    def user_real_name_attribute(self):
        """Gets the user_real_name_attribute of this CreateLdapServerXo.  # noqa: E501

        This is used to find a real name given the user ID  # noqa: E501

        :return: The user_real_name_attribute of this CreateLdapServerXo.  # noqa: E501
        :rtype: str
        """
        return self._user_real_name_attribute

    @user_real_name_attribute.setter
    def user_real_name_attribute(self, user_real_name_attribute):
        """Sets the user_real_name_attribute of this CreateLdapServerXo.

        This is used to find a real name given the user ID  # noqa: E501

        :param user_real_name_attribute: The user_real_name_attribute of this CreateLdapServerXo.  # noqa: E501
        :type: str
        """

        self._user_real_name_attribute = user_real_name_attribute

    @property
    def user_email_address_attribute(self):
        """Gets the user_email_address_attribute of this CreateLdapServerXo.  # noqa: E501

        This is used to find an email address given the user ID  # noqa: E501

        :return: The user_email_address_attribute of this CreateLdapServerXo.  # noqa: E501
        :rtype: str
        """
        return self._user_email_address_attribute

    @user_email_address_attribute.setter
    def user_email_address_attribute(self, user_email_address_attribute):
        """Sets the user_email_address_attribute of this CreateLdapServerXo.

        This is used to find an email address given the user ID  # noqa: E501

        :param user_email_address_attribute: The user_email_address_attribute of this CreateLdapServerXo.  # noqa: E501
        :type: str
        """

        self._user_email_address_attribute = user_email_address_attribute

    @property
    def user_password_attribute(self):
        """Gets the user_password_attribute of this CreateLdapServerXo.  # noqa: E501

        If this field is blank the user will be authenticated against a bind with the LDAP server  # noqa: E501

        :return: The user_password_attribute of this CreateLdapServerXo.  # noqa: E501
        :rtype: str
        """
        return self._user_password_attribute

    @user_password_attribute.setter
    def user_password_attribute(self, user_password_attribute):
        """Sets the user_password_attribute of this CreateLdapServerXo.

        If this field is blank the user will be authenticated against a bind with the LDAP server  # noqa: E501

        :param user_password_attribute: The user_password_attribute of this CreateLdapServerXo.  # noqa: E501
        :type: str
        """

        self._user_password_attribute = user_password_attribute

    @property
    def ldap_groups_as_roles(self):
        """Gets the ldap_groups_as_roles of this CreateLdapServerXo.  # noqa: E501

        Denotes whether LDAP assigned roles are used as Nexus Repository Manager roles  # noqa: E501

        :return: The ldap_groups_as_roles of this CreateLdapServerXo.  # noqa: E501
        :rtype: bool
        """
        return self._ldap_groups_as_roles

    @ldap_groups_as_roles.setter
    def ldap_groups_as_roles(self, ldap_groups_as_roles):
        """Sets the ldap_groups_as_roles of this CreateLdapServerXo.

        Denotes whether LDAP assigned roles are used as Nexus Repository Manager roles  # noqa: E501

        :param ldap_groups_as_roles: The ldap_groups_as_roles of this CreateLdapServerXo.  # noqa: E501
        :type: bool
        """

        self._ldap_groups_as_roles = ldap_groups_as_roles

    @property
    def group_type(self):
        """Gets the group_type of this CreateLdapServerXo.  # noqa: E501

        Defines a type of groups used: static (a group contains a list of users) or dynamic (a user contains a list of groups). Required if ldapGroupsAsRoles is true.  # noqa: E501

        :return: The group_type of this CreateLdapServerXo.  # noqa: E501
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        """Sets the group_type of this CreateLdapServerXo.

        Defines a type of groups used: static (a group contains a list of users) or dynamic (a user contains a list of groups). Required if ldapGroupsAsRoles is true.  # noqa: E501

        :param group_type: The group_type of this CreateLdapServerXo.  # noqa: E501
        :type: str
        """
        if group_type is None:
            raise ValueError(
                "Invalid value for `group_type`, must not be `None`"
            )  # noqa: E501
        allowed_values = ["static", "dynamic"]  # noqa: E501
        if group_type not in allowed_values:
            raise ValueError(
                "Invalid value for `group_type` ({0}), must be one of {1}".format(  # noqa: E501
                    group_type, allowed_values
                )
            )

        self._group_type = group_type

    @property
    def group_base_dn(self):
        """Gets the group_base_dn of this CreateLdapServerXo.  # noqa: E501

        The relative DN where group objects are found (e.g. ou=Group). This value will have the Search base DN value appended to form the full Group search base DN.  # noqa: E501

        :return: The group_base_dn of this CreateLdapServerXo.  # noqa: E501
        :rtype: str
        """
        return self._group_base_dn

    @group_base_dn.setter
    def group_base_dn(self, group_base_dn):
        """Sets the group_base_dn of this CreateLdapServerXo.

        The relative DN where group objects are found (e.g. ou=Group). This value will have the Search base DN value appended to form the full Group search base DN.  # noqa: E501

        :param group_base_dn: The group_base_dn of this CreateLdapServerXo.  # noqa: E501
        :type: str
        """

        self._group_base_dn = group_base_dn

    @property
    def group_subtree(self):
        """Gets the group_subtree of this CreateLdapServerXo.  # noqa: E501

        Are groups located in structures below the group base DN  # noqa: E501

        :return: The group_subtree of this CreateLdapServerXo.  # noqa: E501
        :rtype: bool
        """
        return self._group_subtree

    @group_subtree.setter
    def group_subtree(self, group_subtree):
        """Sets the group_subtree of this CreateLdapServerXo.

        Are groups located in structures below the group base DN  # noqa: E501

        :param group_subtree: The group_subtree of this CreateLdapServerXo.  # noqa: E501
        :type: bool
        """

        self._group_subtree = group_subtree

    @property
    def group_object_class(self):
        """Gets the group_object_class of this CreateLdapServerXo.  # noqa: E501

        LDAP class for group objects. Required if groupType is static  # noqa: E501

        :return: The group_object_class of this CreateLdapServerXo.  # noqa: E501
        :rtype: str
        """
        return self._group_object_class

    @group_object_class.setter
    def group_object_class(self, group_object_class):
        """Sets the group_object_class of this CreateLdapServerXo.

        LDAP class for group objects. Required if groupType is static  # noqa: E501

        :param group_object_class: The group_object_class of this CreateLdapServerXo.  # noqa: E501
        :type: str
        """

        self._group_object_class = group_object_class

    @property
    def group_id_attribute(self):
        """Gets the group_id_attribute of this CreateLdapServerXo.  # noqa: E501

        This field specifies the attribute of the Object class that defines the Group ID. Required if groupType is static  # noqa: E501

        :return: The group_id_attribute of this CreateLdapServerXo.  # noqa: E501
        :rtype: str
        """
        return self._group_id_attribute

    @group_id_attribute.setter
    def group_id_attribute(self, group_id_attribute):
        """Sets the group_id_attribute of this CreateLdapServerXo.

        This field specifies the attribute of the Object class that defines the Group ID. Required if groupType is static  # noqa: E501

        :param group_id_attribute: The group_id_attribute of this CreateLdapServerXo.  # noqa: E501
        :type: str
        """

        self._group_id_attribute = group_id_attribute

    @property
    def group_member_attribute(self):
        """Gets the group_member_attribute of this CreateLdapServerXo.  # noqa: E501

        LDAP attribute containing the usernames for the group. Required if groupType is static  # noqa: E501

        :return: The group_member_attribute of this CreateLdapServerXo.  # noqa: E501
        :rtype: str
        """
        return self._group_member_attribute

    @group_member_attribute.setter
    def group_member_attribute(self, group_member_attribute):
        """Sets the group_member_attribute of this CreateLdapServerXo.

        LDAP attribute containing the usernames for the group. Required if groupType is static  # noqa: E501

        :param group_member_attribute: The group_member_attribute of this CreateLdapServerXo.  # noqa: E501
        :type: str
        """

        self._group_member_attribute = group_member_attribute

    @property
    def group_member_format(self):
        """Gets the group_member_format of this CreateLdapServerXo.  # noqa: E501

        The format of user ID stored in the group member attribute. Required if groupType is static  # noqa: E501

        :return: The group_member_format of this CreateLdapServerXo.  # noqa: E501
        :rtype: str
        """
        return self._group_member_format

    @group_member_format.setter
    def group_member_format(self, group_member_format):
        """Sets the group_member_format of this CreateLdapServerXo.

        The format of user ID stored in the group member attribute. Required if groupType is static  # noqa: E501

        :param group_member_format: The group_member_format of this CreateLdapServerXo.  # noqa: E501
        :type: str
        """

        self._group_member_format = group_member_format

    @property
    def user_member_of_attribute(self):
        """Gets the user_member_of_attribute of this CreateLdapServerXo.  # noqa: E501

        Set this to the attribute used to store the attribute which holds groups DN in the user object. Required if groupType is dynamic  # noqa: E501

        :return: The user_member_of_attribute of this CreateLdapServerXo.  # noqa: E501
        :rtype: str
        """
        return self._user_member_of_attribute

    @user_member_of_attribute.setter
    def user_member_of_attribute(self, user_member_of_attribute):
        """Sets the user_member_of_attribute of this CreateLdapServerXo.

        Set this to the attribute used to store the attribute which holds groups DN in the user object. Required if groupType is dynamic  # noqa: E501

        :param user_member_of_attribute: The user_member_of_attribute of this CreateLdapServerXo.  # noqa: E501
        :type: str
        """

        self._user_member_of_attribute = user_member_of_attribute

    @property
    def auth_password(self):
        """Gets the auth_password of this CreateLdapServerXo.  # noqa: E501

        The password to bind with. Required if authScheme other than none.  # noqa: E501

        :return: The auth_password of this CreateLdapServerXo.  # noqa: E501
        :rtype: str
        """
        return self._auth_password

    @auth_password.setter
    def auth_password(self, auth_password):
        """Sets the auth_password of this CreateLdapServerXo.

        The password to bind with. Required if authScheme other than none.  # noqa: E501

        :param auth_password: The auth_password of this CreateLdapServerXo.  # noqa: E501
        :type: str
        """
        if auth_password is None:
            raise ValueError(
                "Invalid value for `auth_password`, must not be `None`"
            )  # noqa: E501

        self._auth_password = auth_password

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(CreateLdapServerXo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateLdapServerXo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other