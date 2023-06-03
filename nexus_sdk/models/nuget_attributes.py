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

class NugetAttributes(object):
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
        'query_cache_item_max_age': 'int',
        'nuget_version': 'str'
    }

    attribute_map = {
        'query_cache_item_max_age': 'queryCacheItemMaxAge',
        'nuget_version': 'nugetVersion'
    }

    def __init__(self, query_cache_item_max_age=None, nuget_version=None):  # noqa: E501
        """NugetAttributes - a model defined in Swagger"""  # noqa: E501
        self._query_cache_item_max_age = None
        self._nuget_version = None
        self.discriminator = None
        if query_cache_item_max_age is not None:
            self.query_cache_item_max_age = query_cache_item_max_age
        if nuget_version is not None:
            self.nuget_version = nuget_version

    @property
    def query_cache_item_max_age(self):
        """Gets the query_cache_item_max_age of this NugetAttributes.  # noqa: E501

        How long to cache query results from the proxied repository (in seconds)  # noqa: E501

        :return: The query_cache_item_max_age of this NugetAttributes.  # noqa: E501
        :rtype: int
        """
        return self._query_cache_item_max_age

    @query_cache_item_max_age.setter
    def query_cache_item_max_age(self, query_cache_item_max_age):
        """Sets the query_cache_item_max_age of this NugetAttributes.

        How long to cache query results from the proxied repository (in seconds)  # noqa: E501

        :param query_cache_item_max_age: The query_cache_item_max_age of this NugetAttributes.  # noqa: E501
        :type: int
        """

        self._query_cache_item_max_age = query_cache_item_max_age

    @property
    def nuget_version(self):
        """Gets the nuget_version of this NugetAttributes.  # noqa: E501

        Nuget protocol version  # noqa: E501

        :return: The nuget_version of this NugetAttributes.  # noqa: E501
        :rtype: str
        """
        return self._nuget_version

    @nuget_version.setter
    def nuget_version(self, nuget_version):
        """Sets the nuget_version of this NugetAttributes.

        Nuget protocol version  # noqa: E501

        :param nuget_version: The nuget_version of this NugetAttributes.  # noqa: E501
        :type: str
        """
        allowed_values = ["V2", "V3"]  # noqa: E501
        if nuget_version not in allowed_values:
            raise ValueError(
                "Invalid value for `nuget_version` ({0}), must be one of {1}"  # noqa: E501
                .format(nuget_version, allowed_values)
            )

        self._nuget_version = nuget_version

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
        if issubclass(NugetAttributes, dict):
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
        if not isinstance(other, NugetAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
