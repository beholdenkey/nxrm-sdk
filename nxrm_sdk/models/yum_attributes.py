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


class YumAttributes(object):
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
    swagger_types = {"repodata_depth": "int", "deploy_policy": "str"}

    attribute_map = {"repodata_depth": "repodataDepth", "deploy_policy": "deployPolicy"}

    def __init__(self, repodata_depth=None, deploy_policy=None):  # noqa: E501
        """YumAttributes - a model defined in Swagger"""  # noqa: E501
        self._repodata_depth = None
        self._deploy_policy = None
        self.discriminator = None
        self.repodata_depth = repodata_depth
        if deploy_policy is not None:
            self.deploy_policy = deploy_policy

    @property
    def repodata_depth(self):
        """Gets the repodata_depth of this YumAttributes.  # noqa: E501

        Specifies the repository depth where repodata folder(s) are created  # noqa: E501

        :return: The repodata_depth of this YumAttributes.  # noqa: E501
        :rtype: int
        """
        return self._repodata_depth

    @repodata_depth.setter
    def repodata_depth(self, repodata_depth):
        """Sets the repodata_depth of this YumAttributes.

        Specifies the repository depth where repodata folder(s) are created  # noqa: E501

        :param repodata_depth: The repodata_depth of this YumAttributes.  # noqa: E501
        :type: int
        """
        if repodata_depth is None:
            raise ValueError(
                "Invalid value for `repodata_depth`, must not be `None`"
            )  # noqa: E501

        self._repodata_depth = repodata_depth

    @property
    def deploy_policy(self):
        """Gets the deploy_policy of this YumAttributes.  # noqa: E501

        Validate that all paths are RPMs or yum metadata  # noqa: E501

        :return: The deploy_policy of this YumAttributes.  # noqa: E501
        :rtype: str
        """
        return self._deploy_policy

    @deploy_policy.setter
    def deploy_policy(self, deploy_policy):
        """Sets the deploy_policy of this YumAttributes.

        Validate that all paths are RPMs or yum metadata  # noqa: E501

        :param deploy_policy: The deploy_policy of this YumAttributes.  # noqa: E501
        :type: str
        """
        allowed_values = ["PERMISSIVE", "STRICT"]  # noqa: E501
        if deploy_policy not in allowed_values:
            raise ValueError(
                "Invalid value for `deploy_policy` ({0}), must be one of {1}".format(  # noqa: E501
                    deploy_policy, allowed_values
                )
            )

        self._deploy_policy = deploy_policy

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
        if issubclass(YumAttributes, dict):
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
        if not isinstance(other, YumAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
