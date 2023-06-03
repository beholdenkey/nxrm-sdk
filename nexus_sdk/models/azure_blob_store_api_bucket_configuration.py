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

class AzureBlobStoreApiBucketConfiguration(object):
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
        'container_name': 'str',
        'authentication': 'AzureBlobStoreApiAuthentication'
    }

    attribute_map = {
        'account_name': 'accountName',
        'container_name': 'containerName',
        'authentication': 'authentication'
    }

    def __init__(self, account_name=None, container_name=None, authentication=None):  # noqa: E501
        """AzureBlobStoreApiBucketConfiguration - a model defined in Swagger"""  # noqa: E501
        self._account_name = None
        self._container_name = None
        self._authentication = None
        self.discriminator = None
        self.account_name = account_name
        self.container_name = container_name
        self.authentication = authentication

    @property
    def account_name(self):
        """Gets the account_name of this AzureBlobStoreApiBucketConfiguration.  # noqa: E501

        Account name found under Access keys for the storage account.  # noqa: E501

        :return: The account_name of this AzureBlobStoreApiBucketConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this AzureBlobStoreApiBucketConfiguration.

        Account name found under Access keys for the storage account.  # noqa: E501

        :param account_name: The account_name of this AzureBlobStoreApiBucketConfiguration.  # noqa: E501
        :type: str
        """
        if account_name is None:
            raise ValueError("Invalid value for `account_name`, must not be `None`")  # noqa: E501

        self._account_name = account_name

    @property
    def container_name(self):
        """Gets the container_name of this AzureBlobStoreApiBucketConfiguration.  # noqa: E501

        The name of an existing container to be used for storage.  # noqa: E501

        :return: The container_name of this AzureBlobStoreApiBucketConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        """Sets the container_name of this AzureBlobStoreApiBucketConfiguration.

        The name of an existing container to be used for storage.  # noqa: E501

        :param container_name: The container_name of this AzureBlobStoreApiBucketConfiguration.  # noqa: E501
        :type: str
        """
        if container_name is None:
            raise ValueError("Invalid value for `container_name`, must not be `None`")  # noqa: E501

        self._container_name = container_name

    @property
    def authentication(self):
        """Gets the authentication of this AzureBlobStoreApiBucketConfiguration.  # noqa: E501


        :return: The authentication of this AzureBlobStoreApiBucketConfiguration.  # noqa: E501
        :rtype: AzureBlobStoreApiAuthentication
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """Sets the authentication of this AzureBlobStoreApiBucketConfiguration.


        :param authentication: The authentication of this AzureBlobStoreApiBucketConfiguration.  # noqa: E501
        :type: AzureBlobStoreApiAuthentication
        """
        if authentication is None:
            raise ValueError("Invalid value for `authentication`, must not be `None`")  # noqa: E501

        self._authentication = authentication

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AzureBlobStoreApiBucketConfiguration, dict):
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
        if not isinstance(other, AzureBlobStoreApiBucketConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
