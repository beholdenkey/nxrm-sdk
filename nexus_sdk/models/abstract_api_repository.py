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

class AbstractApiRepository(object):
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
        'name': 'str',
        'format': 'str',
        'type': 'str',
        'url': 'str',
        'online': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'format': 'format',
        'type': 'type',
        'url': 'url',
        'online': 'online'
    }

    def __init__(self, name=None, format=None, type=None, url=None, online=None):  # noqa: E501
        """AbstractApiRepository - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._format = None
        self._type = None
        self._url = None
        self._online = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if format is not None:
            self.format = format
        if type is not None:
            self.type = type
        if url is not None:
            self.url = url
        self.online = online

    @property
    def name(self):
        """Gets the name of this AbstractApiRepository.  # noqa: E501

        A unique identifier for this repository  # noqa: E501

        :return: The name of this AbstractApiRepository.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AbstractApiRepository.

        A unique identifier for this repository  # noqa: E501

        :param name: The name of this AbstractApiRepository.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def format(self):
        """Gets the format of this AbstractApiRepository.  # noqa: E501

        Component format held in this repository  # noqa: E501

        :return: The format of this AbstractApiRepository.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this AbstractApiRepository.

        Component format held in this repository  # noqa: E501

        :param format: The format of this AbstractApiRepository.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def type(self):
        """Gets the type of this AbstractApiRepository.  # noqa: E501

        Controls if deployments of and updates to artifacts are allowed  # noqa: E501

        :return: The type of this AbstractApiRepository.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AbstractApiRepository.

        Controls if deployments of and updates to artifacts are allowed  # noqa: E501

        :param type: The type of this AbstractApiRepository.  # noqa: E501
        :type: str
        """
        allowed_values = ["hosted", "proxy", "group"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def url(self):
        """Gets the url of this AbstractApiRepository.  # noqa: E501

        URL to the repository  # noqa: E501

        :return: The url of this AbstractApiRepository.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this AbstractApiRepository.

        URL to the repository  # noqa: E501

        :param url: The url of this AbstractApiRepository.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def online(self):
        """Gets the online of this AbstractApiRepository.  # noqa: E501

        Whether this repository accepts incoming requests  # noqa: E501

        :return: The online of this AbstractApiRepository.  # noqa: E501
        :rtype: bool
        """
        return self._online

    @online.setter
    def online(self, online):
        """Sets the online of this AbstractApiRepository.

        Whether this repository accepts incoming requests  # noqa: E501

        :param online: The online of this AbstractApiRepository.  # noqa: E501
        :type: bool
        """
        if online is None:
            raise ValueError("Invalid value for `online`, must not be `None`")  # noqa: E501

        self._online = online

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
        if issubclass(AbstractApiRepository, dict):
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
        if not isinstance(other, AbstractApiRepository):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
