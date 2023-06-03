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

class GenericBlobStoreApiResponse(object):
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
        'soft_quota': 'BlobStoreApiSoftQuota',
        'name': 'str',
        'type': 'str',
        'unavailable': 'bool',
        'blob_count': 'int',
        'total_size_in_bytes': 'int',
        'available_space_in_bytes': 'int'
    }

    attribute_map = {
        'soft_quota': 'softQuota',
        'name': 'name',
        'type': 'type',
        'unavailable': 'unavailable',
        'blob_count': 'blobCount',
        'total_size_in_bytes': 'totalSizeInBytes',
        'available_space_in_bytes': 'availableSpaceInBytes'
    }

    def __init__(self, soft_quota=None, name=None, type=None, unavailable=None, blob_count=None, total_size_in_bytes=None, available_space_in_bytes=None):  # noqa: E501
        """GenericBlobStoreApiResponse - a model defined in Swagger"""  # noqa: E501
        self._soft_quota = None
        self._name = None
        self._type = None
        self._unavailable = None
        self._blob_count = None
        self._total_size_in_bytes = None
        self._available_space_in_bytes = None
        self.discriminator = None
        if soft_quota is not None:
            self.soft_quota = soft_quota
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if unavailable is not None:
            self.unavailable = unavailable
        if blob_count is not None:
            self.blob_count = blob_count
        if total_size_in_bytes is not None:
            self.total_size_in_bytes = total_size_in_bytes
        if available_space_in_bytes is not None:
            self.available_space_in_bytes = available_space_in_bytes

    @property
    def soft_quota(self):
        """Gets the soft_quota of this GenericBlobStoreApiResponse.  # noqa: E501


        :return: The soft_quota of this GenericBlobStoreApiResponse.  # noqa: E501
        :rtype: BlobStoreApiSoftQuota
        """
        return self._soft_quota

    @soft_quota.setter
    def soft_quota(self, soft_quota):
        """Sets the soft_quota of this GenericBlobStoreApiResponse.


        :param soft_quota: The soft_quota of this GenericBlobStoreApiResponse.  # noqa: E501
        :type: BlobStoreApiSoftQuota
        """

        self._soft_quota = soft_quota

    @property
    def name(self):
        """Gets the name of this GenericBlobStoreApiResponse.  # noqa: E501


        :return: The name of this GenericBlobStoreApiResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GenericBlobStoreApiResponse.


        :param name: The name of this GenericBlobStoreApiResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this GenericBlobStoreApiResponse.  # noqa: E501


        :return: The type of this GenericBlobStoreApiResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GenericBlobStoreApiResponse.


        :param type: The type of this GenericBlobStoreApiResponse.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def unavailable(self):
        """Gets the unavailable of this GenericBlobStoreApiResponse.  # noqa: E501


        :return: The unavailable of this GenericBlobStoreApiResponse.  # noqa: E501
        :rtype: bool
        """
        return self._unavailable

    @unavailable.setter
    def unavailable(self, unavailable):
        """Sets the unavailable of this GenericBlobStoreApiResponse.


        :param unavailable: The unavailable of this GenericBlobStoreApiResponse.  # noqa: E501
        :type: bool
        """

        self._unavailable = unavailable

    @property
    def blob_count(self):
        """Gets the blob_count of this GenericBlobStoreApiResponse.  # noqa: E501


        :return: The blob_count of this GenericBlobStoreApiResponse.  # noqa: E501
        :rtype: int
        """
        return self._blob_count

    @blob_count.setter
    def blob_count(self, blob_count):
        """Sets the blob_count of this GenericBlobStoreApiResponse.


        :param blob_count: The blob_count of this GenericBlobStoreApiResponse.  # noqa: E501
        :type: int
        """

        self._blob_count = blob_count

    @property
    def total_size_in_bytes(self):
        """Gets the total_size_in_bytes of this GenericBlobStoreApiResponse.  # noqa: E501


        :return: The total_size_in_bytes of this GenericBlobStoreApiResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_size_in_bytes

    @total_size_in_bytes.setter
    def total_size_in_bytes(self, total_size_in_bytes):
        """Sets the total_size_in_bytes of this GenericBlobStoreApiResponse.


        :param total_size_in_bytes: The total_size_in_bytes of this GenericBlobStoreApiResponse.  # noqa: E501
        :type: int
        """

        self._total_size_in_bytes = total_size_in_bytes

    @property
    def available_space_in_bytes(self):
        """Gets the available_space_in_bytes of this GenericBlobStoreApiResponse.  # noqa: E501


        :return: The available_space_in_bytes of this GenericBlobStoreApiResponse.  # noqa: E501
        :rtype: int
        """
        return self._available_space_in_bytes

    @available_space_in_bytes.setter
    def available_space_in_bytes(self, available_space_in_bytes):
        """Sets the available_space_in_bytes of this GenericBlobStoreApiResponse.


        :param available_space_in_bytes: The available_space_in_bytes of this GenericBlobStoreApiResponse.  # noqa: E501
        :type: int
        """

        self._available_space_in_bytes = available_space_in_bytes

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
        if issubclass(GenericBlobStoreApiResponse, dict):
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
        if not isinstance(other, GenericBlobStoreApiResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
