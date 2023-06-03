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


class RubyGemsHostedRepositoryApiRequest(object):
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
        "online": "bool",
        "storage": "HostedStorageAttributes",
        "cleanup": "CleanupPolicyAttributes",
        "component": "ComponentAttributes",
    }

    attribute_map = {
        "name": "name",
        "online": "online",
        "storage": "storage",
        "cleanup": "cleanup",
        "component": "component",
    }

    def __init__(
        self, name=None, online=None, storage=None, cleanup=None, component=None
    ):  # noqa: E501
        """RubyGemsHostedRepositoryApiRequest - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._online = None
        self._storage = None
        self._cleanup = None
        self._component = None
        self.discriminator = None
        self.name = name
        self.online = online
        self.storage = storage
        if cleanup is not None:
            self.cleanup = cleanup
        if component is not None:
            self.component = component

    @property
    def name(self):
        """Gets the name of this RubyGemsHostedRepositoryApiRequest.  # noqa: E501

        A unique identifier for this repository  # noqa: E501

        :return: The name of this RubyGemsHostedRepositoryApiRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RubyGemsHostedRepositoryApiRequest.

        A unique identifier for this repository  # noqa: E501

        :param name: The name of this RubyGemsHostedRepositoryApiRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError(
                "Invalid value for `name`, must not be `None`"
            )  # noqa: E501

        self._name = name

    @property
    def online(self):
        """Gets the online of this RubyGemsHostedRepositoryApiRequest.  # noqa: E501

        Whether this repository accepts incoming requests  # noqa: E501

        :return: The online of this RubyGemsHostedRepositoryApiRequest.  # noqa: E501
        :rtype: bool
        """
        return self._online

    @online.setter
    def online(self, online):
        """Sets the online of this RubyGemsHostedRepositoryApiRequest.

        Whether this repository accepts incoming requests  # noqa: E501

        :param online: The online of this RubyGemsHostedRepositoryApiRequest.  # noqa: E501
        :type: bool
        """
        if online is None:
            raise ValueError(
                "Invalid value for `online`, must not be `None`"
            )  # noqa: E501

        self._online = online

    @property
    def storage(self):
        """Gets the storage of this RubyGemsHostedRepositoryApiRequest.  # noqa: E501


        :return: The storage of this RubyGemsHostedRepositoryApiRequest.  # noqa: E501
        :rtype: HostedStorageAttributes
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this RubyGemsHostedRepositoryApiRequest.


        :param storage: The storage of this RubyGemsHostedRepositoryApiRequest.  # noqa: E501
        :type: HostedStorageAttributes
        """
        if storage is None:
            raise ValueError(
                "Invalid value for `storage`, must not be `None`"
            )  # noqa: E501

        self._storage = storage

    @property
    def cleanup(self):
        """Gets the cleanup of this RubyGemsHostedRepositoryApiRequest.  # noqa: E501


        :return: The cleanup of this RubyGemsHostedRepositoryApiRequest.  # noqa: E501
        :rtype: CleanupPolicyAttributes
        """
        return self._cleanup

    @cleanup.setter
    def cleanup(self, cleanup):
        """Sets the cleanup of this RubyGemsHostedRepositoryApiRequest.


        :param cleanup: The cleanup of this RubyGemsHostedRepositoryApiRequest.  # noqa: E501
        :type: CleanupPolicyAttributes
        """

        self._cleanup = cleanup

    @property
    def component(self):
        """Gets the component of this RubyGemsHostedRepositoryApiRequest.  # noqa: E501


        :return: The component of this RubyGemsHostedRepositoryApiRequest.  # noqa: E501
        :rtype: ComponentAttributes
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this RubyGemsHostedRepositoryApiRequest.


        :param component: The component of this RubyGemsHostedRepositoryApiRequest.  # noqa: E501
        :type: ComponentAttributes
        """

        self._component = component

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
        if issubclass(RubyGemsHostedRepositoryApiRequest, dict):
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
        if not isinstance(other, RubyGemsHostedRepositoryApiRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
