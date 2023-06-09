"""
    Nexus Repository Manager REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.42.0-01

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class AzureConnectionXO:
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
        'account_name': 'str',
        'account_key': 'str',
        'container_name': 'str',
        'authentication_method': 'str',
    }

    attribute_map = {
        'account_name': 'accountName',
        'account_key': 'accountKey',
        'container_name': 'containerName',
        'authentication_method': 'authenticationMethod',
    }

    def __init__(
        self,
        account_name=None,
        account_key=None,
        container_name=None,
        authentication_method=None,
    ):  # noqa: E501
        """AzureConnectionXO - a model defined in Swagger"""  # noqa: E501
        self._account_name = None
        self._account_key = None
        self._container_name = None
        self._authentication_method = None
        self.discriminator = None
        if account_name is not None:
            self.account_name = account_name
        if account_key is not None:
            self.account_key = account_key
        if container_name is not None:
            self.container_name = container_name
        if authentication_method is not None:
            self.authentication_method = authentication_method

    @property
    def account_name(self):
        """Gets the account_name of this AzureConnectionXO.  # noqa: E501


        :return: The account_name of this AzureConnectionXO.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this AzureConnectionXO.


        :param account_name: The account_name of this AzureConnectionXO.  # noqa: E501
        :type: str
        """

        self._account_name = account_name

    @property
    def account_key(self):
        """Gets the account_key of this AzureConnectionXO.  # noqa: E501


        :return: The account_key of this AzureConnectionXO.  # noqa: E501
        :rtype: str
        """
        return self._account_key

    @account_key.setter
    def account_key(self, account_key):
        """Sets the account_key of this AzureConnectionXO.


        :param account_key: The account_key of this AzureConnectionXO.  # noqa: E501
        :type: str
        """

        self._account_key = account_key

    @property
    def container_name(self):
        """Gets the container_name of this AzureConnectionXO.  # noqa: E501


        :return: The container_name of this AzureConnectionXO.  # noqa: E501
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        """Sets the container_name of this AzureConnectionXO.


        :param container_name: The container_name of this AzureConnectionXO.  # noqa: E501
        :type: str
        """

        self._container_name = container_name

    @property
    def authentication_method(self):
        """Gets the authentication_method of this AzureConnectionXO.  # noqa: E501


        :return: The authentication_method of this AzureConnectionXO.  # noqa: E501
        :rtype: str
        """
        return self._authentication_method

    @authentication_method.setter
    def authentication_method(self, authentication_method):
        """Sets the authentication_method of this AzureConnectionXO.


        :param authentication_method: The authentication_method of this AzureConnectionXO.  # noqa: E501
        :type: str
        """

        self._authentication_method = authentication_method

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in self.swagger_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, 'to_dict') else x, value)
                )
            elif hasattr(value, 'to_dict'):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], 'to_dict')
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(AzureConnectionXO, dict):
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
        if not isinstance(other, AzureConnectionXO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
