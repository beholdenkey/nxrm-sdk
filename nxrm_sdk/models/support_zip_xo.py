"""
    Nexus Repository Manager REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.42.0-01

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class SupportZipXO:
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
    swagger_types = {'file': 'str', 'name': 'str', 'size': 'str', 'truncated': 'bool'}

    attribute_map = {
        'file': 'file',
        'name': 'name',
        'size': 'size',
        'truncated': 'truncated',
    }

    def __init__(self, file=None, name=None, size=None, truncated=None):  # noqa: E501
        """SupportZipXO - a model defined in Swagger"""  # noqa: E501
        self._file = None
        self._name = None
        self._size = None
        self._truncated = None
        self.discriminator = None
        if file is not None:
            self.file = file
        if name is not None:
            self.name = name
        if size is not None:
            self.size = size
        if truncated is not None:
            self.truncated = truncated

    @property
    def file(self):
        """Gets the file of this SupportZipXO.  # noqa: E501


        :return: The file of this SupportZipXO.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this SupportZipXO.


        :param file: The file of this SupportZipXO.  # noqa: E501
        :type: str
        """

        self._file = file

    @property
    def name(self):
        """Gets the name of this SupportZipXO.  # noqa: E501


        :return: The name of this SupportZipXO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SupportZipXO.


        :param name: The name of this SupportZipXO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def size(self):
        """Gets the size of this SupportZipXO.  # noqa: E501


        :return: The size of this SupportZipXO.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this SupportZipXO.


        :param size: The size of this SupportZipXO.  # noqa: E501
        :type: str
        """

        self._size = size

    @property
    def truncated(self):
        """Gets the truncated of this SupportZipXO.  # noqa: E501


        :return: The truncated of this SupportZipXO.  # noqa: E501
        :rtype: bool
        """
        return self._truncated

    @truncated.setter
    def truncated(self, truncated):
        """Sets the truncated of this SupportZipXO.


        :param truncated: The truncated of this SupportZipXO.  # noqa: E501
        :type: bool
        """

        self._truncated = truncated

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
        if issubclass(SupportZipXO, dict):
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
        if not isinstance(other, SupportZipXO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
