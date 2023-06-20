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


class PageAssetXO(object):
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
    swagger_types = {"items": "list[AssetXO]", "continuation_token": "str"}

    attribute_map = {"items": "items", "continuation_token": "continuationToken"}

    def __init__(self, items=None, continuation_token=None):  # noqa: E501
        """PageAssetXO - a model defined in Swagger"""  # noqa: E501
        self._items = None
        self._continuation_token = None
        self.discriminator = None
        if items is not None:
            self.items = items
        if continuation_token is not None:
            self.continuation_token = continuation_token

    @property
    def items(self):
        """Gets the items of this PageAssetXO.  # noqa: E501


        :return: The items of this PageAssetXO.  # noqa: E501
        :rtype: list[AssetXO]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this PageAssetXO.


        :param items: The items of this PageAssetXO.  # noqa: E501
        :type: list[AssetXO]
        """

        self._items = items

    @property
    def continuation_token(self):
        """Gets the continuation_token of this PageAssetXO.  # noqa: E501


        :return: The continuation_token of this PageAssetXO.  # noqa: E501
        :rtype: str
        """
        return self._continuation_token

    @continuation_token.setter
    def continuation_token(self, continuation_token):
        """Sets the continuation_token of this PageAssetXO.


        :param continuation_token: The continuation_token of this PageAssetXO.  # noqa: E501
        :type: str
        """

        self._continuation_token = continuation_token

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
        if issubclass(PageAssetXO, dict):
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
        if not isinstance(other, PageAssetXO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other