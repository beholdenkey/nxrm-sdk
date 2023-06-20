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


class TagXO(object):
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
        "attributes": "dict(str, object)",
        "first_created": "datetime",
        "last_updated": "datetime",
    }

    attribute_map = {
        "name": "name",
        "attributes": "attributes",
        "first_created": "firstCreated",
        "last_updated": "lastUpdated",
    }

    def __init__(
        self, name=None, attributes=None, first_created=None, last_updated=None
    ):  # noqa: E501
        """TagXO - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._attributes = None
        self._first_created = None
        self._last_updated = None
        self.discriminator = None
        self.name = name
        if attributes is not None:
            self.attributes = attributes
        if first_created is not None:
            self.first_created = first_created
        if last_updated is not None:
            self.last_updated = last_updated

    @property
    def name(self):
        """Gets the name of this TagXO.  # noqa: E501


        :return: The name of this TagXO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TagXO.


        :param name: The name of this TagXO.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError(
                "Invalid value for `name`, must not be `None`"
            )  # noqa: E501

        self._name = name

    @property
    def attributes(self):
        """Gets the attributes of this TagXO.  # noqa: E501


        :return: The attributes of this TagXO.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this TagXO.


        :param attributes: The attributes of this TagXO.  # noqa: E501
        :type: dict(str, object)
        """

        self._attributes = attributes

    @property
    def first_created(self):
        """Gets the first_created of this TagXO.  # noqa: E501


        :return: The first_created of this TagXO.  # noqa: E501
        :rtype: datetime
        """
        return self._first_created

    @first_created.setter
    def first_created(self, first_created):
        """Sets the first_created of this TagXO.


        :param first_created: The first_created of this TagXO.  # noqa: E501
        :type: datetime
        """

        self._first_created = first_created

    @property
    def last_updated(self):
        """Gets the last_updated of this TagXO.  # noqa: E501


        :return: The last_updated of this TagXO.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this TagXO.


        :param last_updated: The last_updated of this TagXO.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

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
        if issubclass(TagXO, dict):
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
        if not isinstance(other, TagXO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other