"""
    Nexus Repository Manager REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.42.0-01

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class FileBlobStoreApiCreateRequest:
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
        'path': 'str',
        'name': 'str',
    }

    attribute_map = {'soft_quota': 'softQuota', 'path': 'path', 'name': 'name'}

    def __init__(self, soft_quota=None, path=None, name=None):  # noqa: E501
        """FileBlobStoreApiCreateRequest - a model defined in Swagger"""  # noqa: E501
        self._soft_quota = None
        self._path = None
        self._name = None
        self.discriminator = None
        if soft_quota is not None:
            self.soft_quota = soft_quota
        if path is not None:
            self.path = path
        if name is not None:
            self.name = name

    @property
    def soft_quota(self):
        """Gets the soft_quota of this FileBlobStoreApiCreateRequest.  # noqa: E501


        :return: The soft_quota of this FileBlobStoreApiCreateRequest.  # noqa: E501
        :rtype: BlobStoreApiSoftQuota
        """
        return self._soft_quota

    @soft_quota.setter
    def soft_quota(self, soft_quota):
        """Sets the soft_quota of this FileBlobStoreApiCreateRequest.


        :param soft_quota: The soft_quota of this FileBlobStoreApiCreateRequest.  # noqa: E501
        :type: BlobStoreApiSoftQuota
        """

        self._soft_quota = soft_quota

    @property
    def path(self):
        """Gets the path of this FileBlobStoreApiCreateRequest.  # noqa: E501

        The path to the blobstore contents. This can be an absolute path to anywhere on the system Nexus Repository Manager has access to or it can be a path relative to the sonatype-work directory.  # noqa: E501

        :return: The path of this FileBlobStoreApiCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this FileBlobStoreApiCreateRequest.

        The path to the blobstore contents. This can be an absolute path to anywhere on the system Nexus Repository Manager has access to or it can be a path relative to the sonatype-work directory.  # noqa: E501

        :param path: The path of this FileBlobStoreApiCreateRequest.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def name(self):
        """Gets the name of this FileBlobStoreApiCreateRequest.  # noqa: E501


        :return: The name of this FileBlobStoreApiCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FileBlobStoreApiCreateRequest.


        :param name: The name of this FileBlobStoreApiCreateRequest.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(FileBlobStoreApiCreateRequest, dict):
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
        if not isinstance(other, FileBlobStoreApiCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
