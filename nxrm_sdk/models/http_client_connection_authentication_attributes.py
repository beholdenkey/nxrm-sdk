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


class HttpClientConnectionAuthenticationAttributes(object):
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
        "type": "str",
        "username": "str",
        "password": "str",
        "ntlm_host": "str",
        "ntlm_domain": "str",
    }

    attribute_map = {
        "type": "type",
        "username": "username",
        "password": "password",
        "ntlm_host": "ntlmHost",
        "ntlm_domain": "ntlmDomain",
    }

    def __init__(
        self, type=None, username=None, password=None, ntlm_host=None, ntlm_domain=None
    ):  # noqa: E501
        """HttpClientConnectionAuthenticationAttributes - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._username = None
        self._password = None
        self._ntlm_host = None
        self._ntlm_domain = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if ntlm_host is not None:
            self.ntlm_host = ntlm_host
        if ntlm_domain is not None:
            self.ntlm_domain = ntlm_domain

    @property
    def type(self):
        """Gets the type of this HttpClientConnectionAuthenticationAttributes.  # noqa: E501

        Authentication type  # noqa: E501

        :return: The type of this HttpClientConnectionAuthenticationAttributes.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HttpClientConnectionAuthenticationAttributes.

        Authentication type  # noqa: E501

        :param type: The type of this HttpClientConnectionAuthenticationAttributes.  # noqa: E501
        :type: str
        """
        allowed_values = ["username", "ntlm"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}".format(  # noqa: E501
                    type, allowed_values
                )
            )

        self._type = type

    @property
    def username(self):
        """Gets the username of this HttpClientConnectionAuthenticationAttributes.  # noqa: E501


        :return: The username of this HttpClientConnectionAuthenticationAttributes.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this HttpClientConnectionAuthenticationAttributes.


        :param username: The username of this HttpClientConnectionAuthenticationAttributes.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this HttpClientConnectionAuthenticationAttributes.  # noqa: E501


        :return: The password of this HttpClientConnectionAuthenticationAttributes.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this HttpClientConnectionAuthenticationAttributes.


        :param password: The password of this HttpClientConnectionAuthenticationAttributes.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def ntlm_host(self):
        """Gets the ntlm_host of this HttpClientConnectionAuthenticationAttributes.  # noqa: E501


        :return: The ntlm_host of this HttpClientConnectionAuthenticationAttributes.  # noqa: E501
        :rtype: str
        """
        return self._ntlm_host

    @ntlm_host.setter
    def ntlm_host(self, ntlm_host):
        """Sets the ntlm_host of this HttpClientConnectionAuthenticationAttributes.


        :param ntlm_host: The ntlm_host of this HttpClientConnectionAuthenticationAttributes.  # noqa: E501
        :type: str
        """

        self._ntlm_host = ntlm_host

    @property
    def ntlm_domain(self):
        """Gets the ntlm_domain of this HttpClientConnectionAuthenticationAttributes.  # noqa: E501


        :return: The ntlm_domain of this HttpClientConnectionAuthenticationAttributes.  # noqa: E501
        :rtype: str
        """
        return self._ntlm_domain

    @ntlm_domain.setter
    def ntlm_domain(self, ntlm_domain):
        """Sets the ntlm_domain of this HttpClientConnectionAuthenticationAttributes.


        :param ntlm_domain: The ntlm_domain of this HttpClientConnectionAuthenticationAttributes.  # noqa: E501
        :type: str
        """

        self._ntlm_domain = ntlm_domain

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
        if issubclass(HttpClientConnectionAuthenticationAttributes, dict):
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
        if not isinstance(other, HttpClientConnectionAuthenticationAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other