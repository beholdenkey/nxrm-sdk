"""
    Nexus Repository Manager REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.42.0-01

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class NpmAttributes:
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
    swagger_types = {'remove_non_cataloged': 'bool', 'remove_quarantined': 'bool'}

    attribute_map = {
        'remove_non_cataloged': 'removeNonCataloged',
        'remove_quarantined': 'removeQuarantined',
    }

    def __init__(
        self, remove_non_cataloged=None, remove_quarantined=None
    ):  # noqa: E501
        """NpmAttributes - a model defined in Swagger"""  # noqa: E501
        self._remove_non_cataloged = None
        self._remove_quarantined = None
        self.discriminator = None
        self.remove_non_cataloged = remove_non_cataloged
        self.remove_quarantined = remove_quarantined

    @property
    def remove_non_cataloged(self):
        """Gets the remove_non_cataloged of this NpmAttributes.  # noqa: E501

        Remove Non-Cataloged Versions  # noqa: E501

        :return: The remove_non_cataloged of this NpmAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._remove_non_cataloged

    @remove_non_cataloged.setter
    def remove_non_cataloged(self, remove_non_cataloged):
        """Sets the remove_non_cataloged of this NpmAttributes.

        Remove Non-Cataloged Versions  # noqa: E501

        :param remove_non_cataloged: The remove_non_cataloged of this NpmAttributes.  # noqa: E501
        :type: bool
        """
        if remove_non_cataloged is None:
            raise ValueError(
                'Invalid value for `remove_non_cataloged`, must not be `None`'
            )  # noqa: E501

        self._remove_non_cataloged = remove_non_cataloged

    @property
    def remove_quarantined(self):
        """Gets the remove_quarantined of this NpmAttributes.  # noqa: E501

        Remove Quarantined Versions  # noqa: E501

        :return: The remove_quarantined of this NpmAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._remove_quarantined

    @remove_quarantined.setter
    def remove_quarantined(self, remove_quarantined):
        """Sets the remove_quarantined of this NpmAttributes.

        Remove Quarantined Versions  # noqa: E501

        :param remove_quarantined: The remove_quarantined of this NpmAttributes.  # noqa: E501
        :type: bool
        """
        if remove_quarantined is None:
            raise ValueError(
                'Invalid value for `remove_quarantined`, must not be `None`'
            )  # noqa: E501

        self._remove_quarantined = remove_quarantined

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
        if issubclass(NpmAttributes, dict):
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
        if not isinstance(other, NpmAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
