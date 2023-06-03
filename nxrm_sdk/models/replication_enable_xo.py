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


class ReplicationEnableXO(object):
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
        "target_repository_name": "str",
        "replication_connection_name": "str",
        "source_repository_name": "str",
    }

    attribute_map = {
        "target_repository_name": "targetRepositoryName",
        "replication_connection_name": "replicationConnectionName",
        "source_repository_name": "sourceRepositoryName",
    }

    def __init__(
        self,
        target_repository_name=None,
        replication_connection_name=None,
        source_repository_name=None,
    ):  # noqa: E501
        """ReplicationEnableXO - a model defined in Swagger"""  # noqa: E501
        self._target_repository_name = None
        self._replication_connection_name = None
        self._source_repository_name = None
        self.discriminator = None
        self.target_repository_name = target_repository_name
        self.replication_connection_name = replication_connection_name
        self.source_repository_name = source_repository_name

    @property
    def target_repository_name(self):
        """Gets the target_repository_name of this ReplicationEnableXO.  # noqa: E501

        Target Repository Name  # noqa: E501

        :return: The target_repository_name of this ReplicationEnableXO.  # noqa: E501
        :rtype: str
        """
        return self._target_repository_name

    @target_repository_name.setter
    def target_repository_name(self, target_repository_name):
        """Sets the target_repository_name of this ReplicationEnableXO.

        Target Repository Name  # noqa: E501

        :param target_repository_name: The target_repository_name of this ReplicationEnableXO.  # noqa: E501
        :type: str
        """
        if target_repository_name is None:
            raise ValueError(
                "Invalid value for `target_repository_name`, must not be `None`"
            )  # noqa: E501

        self._target_repository_name = target_repository_name

    @property
    def replication_connection_name(self):
        """Gets the replication_connection_name of this ReplicationEnableXO.  # noqa: E501

        Replication Connection Name  # noqa: E501

        :return: The replication_connection_name of this ReplicationEnableXO.  # noqa: E501
        :rtype: str
        """
        return self._replication_connection_name

    @replication_connection_name.setter
    def replication_connection_name(self, replication_connection_name):
        """Sets the replication_connection_name of this ReplicationEnableXO.

        Replication Connection Name  # noqa: E501

        :param replication_connection_name: The replication_connection_name of this ReplicationEnableXO.  # noqa: E501
        :type: str
        """
        if replication_connection_name is None:
            raise ValueError(
                "Invalid value for `replication_connection_name`, must not be `None`"
            )  # noqa: E501

        self._replication_connection_name = replication_connection_name

    @property
    def source_repository_name(self):
        """Gets the source_repository_name of this ReplicationEnableXO.  # noqa: E501

        Source Repository Name  # noqa: E501

        :return: The source_repository_name of this ReplicationEnableXO.  # noqa: E501
        :rtype: str
        """
        return self._source_repository_name

    @source_repository_name.setter
    def source_repository_name(self, source_repository_name):
        """Sets the source_repository_name of this ReplicationEnableXO.

        Source Repository Name  # noqa: E501

        :param source_repository_name: The source_repository_name of this ReplicationEnableXO.  # noqa: E501
        :type: str
        """
        if source_repository_name is None:
            raise ValueError(
                "Invalid value for `source_repository_name`, must not be `None`"
            )  # noqa: E501

        self._source_repository_name = source_repository_name

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
        if issubclass(ReplicationEnableXO, dict):
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
        if not isinstance(other, ReplicationEnableXO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
