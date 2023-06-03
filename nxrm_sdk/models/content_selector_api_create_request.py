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


class ContentSelectorApiCreateRequest(object):
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
    swagger_types = {"name": "str", "description": "str", "expression": "str"}

    attribute_map = {
        "name": "name",
        "description": "description",
        "expression": "expression",
    }

    def __init__(self, name=None, description=None, expression=None):  # noqa: E501
        """ContentSelectorApiCreateRequest - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._expression = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if expression is not None:
            self.expression = expression

    @property
    def name(self):
        """Gets the name of this ContentSelectorApiCreateRequest.  # noqa: E501

        The content selector name cannot be changed after creation  # noqa: E501

        :return: The name of this ContentSelectorApiCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ContentSelectorApiCreateRequest.

        The content selector name cannot be changed after creation  # noqa: E501

        :param name: The name of this ContentSelectorApiCreateRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ContentSelectorApiCreateRequest.  # noqa: E501

        A human-readable description  # noqa: E501

        :return: The description of this ContentSelectorApiCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ContentSelectorApiCreateRequest.

        A human-readable description  # noqa: E501

        :param description: The description of this ContentSelectorApiCreateRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def expression(self):
        """Gets the expression of this ContentSelectorApiCreateRequest.  # noqa: E501

        The expression used to identify content  # noqa: E501

        :return: The expression of this ContentSelectorApiCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this ContentSelectorApiCreateRequest.

        The expression used to identify content  # noqa: E501

        :param expression: The expression of this ContentSelectorApiCreateRequest.  # noqa: E501
        :type: str
        """

        self._expression = expression

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
        if issubclass(ContentSelectorApiCreateRequest, dict):
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
        if not isinstance(other, ContentSelectorApiCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
