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

class DockerProxyAttributes(object):
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
        'index_type': 'str',
        'index_url': 'str',
        'cache_foreign_layers': 'bool',
        'foreign_layer_url_whitelist': 'list[str]'
    }

    attribute_map = {
        'index_type': 'indexType',
        'index_url': 'indexUrl',
        'cache_foreign_layers': 'cacheForeignLayers',
        'foreign_layer_url_whitelist': 'foreignLayerUrlWhitelist'
    }

    def __init__(self, index_type=None, index_url=None, cache_foreign_layers=None, foreign_layer_url_whitelist=None):  # noqa: E501
        """DockerProxyAttributes - a model defined in Swagger"""  # noqa: E501
        self._index_type = None
        self._index_url = None
        self._cache_foreign_layers = None
        self._foreign_layer_url_whitelist = None
        self.discriminator = None
        if index_type is not None:
            self.index_type = index_type
        if index_url is not None:
            self.index_url = index_url
        if cache_foreign_layers is not None:
            self.cache_foreign_layers = cache_foreign_layers
        if foreign_layer_url_whitelist is not None:
            self.foreign_layer_url_whitelist = foreign_layer_url_whitelist

    @property
    def index_type(self):
        """Gets the index_type of this DockerProxyAttributes.  # noqa: E501

        Type of Docker Index  # noqa: E501

        :return: The index_type of this DockerProxyAttributes.  # noqa: E501
        :rtype: str
        """
        return self._index_type

    @index_type.setter
    def index_type(self, index_type):
        """Sets the index_type of this DockerProxyAttributes.

        Type of Docker Index  # noqa: E501

        :param index_type: The index_type of this DockerProxyAttributes.  # noqa: E501
        :type: str
        """
        allowed_values = ["HUB", "REGISTRY", "CUSTOM"]  # noqa: E501
        if index_type not in allowed_values:
            raise ValueError(
                "Invalid value for `index_type` ({0}), must be one of {1}"  # noqa: E501
                .format(index_type, allowed_values)
            )

        self._index_type = index_type

    @property
    def index_url(self):
        """Gets the index_url of this DockerProxyAttributes.  # noqa: E501

        Url of Docker Index to use  # noqa: E501

        :return: The index_url of this DockerProxyAttributes.  # noqa: E501
        :rtype: str
        """
        return self._index_url

    @index_url.setter
    def index_url(self, index_url):
        """Sets the index_url of this DockerProxyAttributes.

        Url of Docker Index to use  # noqa: E501

        :param index_url: The index_url of this DockerProxyAttributes.  # noqa: E501
        :type: str
        """

        self._index_url = index_url

    @property
    def cache_foreign_layers(self):
        """Gets the cache_foreign_layers of this DockerProxyAttributes.  # noqa: E501

        Allow Nexus Repository Manager to download and cache foreign layers  # noqa: E501

        :return: The cache_foreign_layers of this DockerProxyAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._cache_foreign_layers

    @cache_foreign_layers.setter
    def cache_foreign_layers(self, cache_foreign_layers):
        """Sets the cache_foreign_layers of this DockerProxyAttributes.

        Allow Nexus Repository Manager to download and cache foreign layers  # noqa: E501

        :param cache_foreign_layers: The cache_foreign_layers of this DockerProxyAttributes.  # noqa: E501
        :type: bool
        """

        self._cache_foreign_layers = cache_foreign_layers

    @property
    def foreign_layer_url_whitelist(self):
        """Gets the foreign_layer_url_whitelist of this DockerProxyAttributes.  # noqa: E501

        Regular expressions used to identify URLs that are allowed for foreign layer requests  # noqa: E501

        :return: The foreign_layer_url_whitelist of this DockerProxyAttributes.  # noqa: E501
        :rtype: list[str]
        """
        return self._foreign_layer_url_whitelist

    @foreign_layer_url_whitelist.setter
    def foreign_layer_url_whitelist(self, foreign_layer_url_whitelist):
        """Sets the foreign_layer_url_whitelist of this DockerProxyAttributes.

        Regular expressions used to identify URLs that are allowed for foreign layer requests  # noqa: E501

        :param foreign_layer_url_whitelist: The foreign_layer_url_whitelist of this DockerProxyAttributes.  # noqa: E501
        :type: list[str]
        """

        self._foreign_layer_url_whitelist = foreign_layer_url_whitelist

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
        if issubclass(DockerProxyAttributes, dict):
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
        if not isinstance(other, DockerProxyAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
