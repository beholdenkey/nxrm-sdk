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


class S3BlobStoreApiModel(object):
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
        "soft_quota": "BlobStoreApiSoftQuota",
        "bucket_configuration": "S3BlobStoreApiBucketConfiguration",
        "type": "str",
    }

    attribute_map = {
        "name": "name",
        "soft_quota": "softQuota",
        "bucket_configuration": "bucketConfiguration",
        "type": "type",
    }

    def __init__(
        self, name=None, soft_quota=None, bucket_configuration=None, type=None
    ):  # noqa: E501
        """S3BlobStoreApiModel - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._soft_quota = None
        self._bucket_configuration = None
        self._type = None
        self.discriminator = None
        self.name = name
        if soft_quota is not None:
            self.soft_quota = soft_quota
        self.bucket_configuration = bucket_configuration
        if type is not None:
            self.type = type

    @property
    def name(self):
        """Gets the name of this S3BlobStoreApiModel.  # noqa: E501

        The name of the S3 blob store.  # noqa: E501

        :return: The name of this S3BlobStoreApiModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this S3BlobStoreApiModel.

        The name of the S3 blob store.  # noqa: E501

        :param name: The name of this S3BlobStoreApiModel.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError(
                "Invalid value for `name`, must not be `None`"
            )  # noqa: E501

        self._name = name

    @property
    def soft_quota(self):
        """Gets the soft_quota of this S3BlobStoreApiModel.  # noqa: E501


        :return: The soft_quota of this S3BlobStoreApiModel.  # noqa: E501
        :rtype: BlobStoreApiSoftQuota
        """
        return self._soft_quota

    @soft_quota.setter
    def soft_quota(self, soft_quota):
        """Sets the soft_quota of this S3BlobStoreApiModel.


        :param soft_quota: The soft_quota of this S3BlobStoreApiModel.  # noqa: E501
        :type: BlobStoreApiSoftQuota
        """

        self._soft_quota = soft_quota

    @property
    def bucket_configuration(self):
        """Gets the bucket_configuration of this S3BlobStoreApiModel.  # noqa: E501


        :return: The bucket_configuration of this S3BlobStoreApiModel.  # noqa: E501
        :rtype: S3BlobStoreApiBucketConfiguration
        """
        return self._bucket_configuration

    @bucket_configuration.setter
    def bucket_configuration(self, bucket_configuration):
        """Sets the bucket_configuration of this S3BlobStoreApiModel.


        :param bucket_configuration: The bucket_configuration of this S3BlobStoreApiModel.  # noqa: E501
        :type: S3BlobStoreApiBucketConfiguration
        """
        if bucket_configuration is None:
            raise ValueError(
                "Invalid value for `bucket_configuration`, must not be `None`"
            )  # noqa: E501

        self._bucket_configuration = bucket_configuration

    @property
    def type(self):
        """Gets the type of this S3BlobStoreApiModel.  # noqa: E501

        The blob store type.  # noqa: E501

        :return: The type of this S3BlobStoreApiModel.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this S3BlobStoreApiModel.

        The blob store type.  # noqa: E501

        :param type: The type of this S3BlobStoreApiModel.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(S3BlobStoreApiModel, dict):
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
        if not isinstance(other, S3BlobStoreApiModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other