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

class S3BlobStoreApiBucketSecurity(object):
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
        'access_key_id': 'str',
        'secret_access_key': 'str',
        'role': 'str',
        'session_token': 'str'
    }

    attribute_map = {
        'access_key_id': 'accessKeyId',
        'secret_access_key': 'secretAccessKey',
        'role': 'role',
        'session_token': 'sessionToken'
    }

    def __init__(self, access_key_id=None, secret_access_key=None, role=None, session_token=None):  # noqa: E501
        """S3BlobStoreApiBucketSecurity - a model defined in Swagger"""  # noqa: E501
        self._access_key_id = None
        self._secret_access_key = None
        self._role = None
        self._session_token = None
        self.discriminator = None
        if access_key_id is not None:
            self.access_key_id = access_key_id
        if secret_access_key is not None:
            self.secret_access_key = secret_access_key
        if role is not None:
            self.role = role
        if session_token is not None:
            self.session_token = session_token

    @property
    def access_key_id(self):
        """Gets the access_key_id of this S3BlobStoreApiBucketSecurity.  # noqa: E501

        An IAM access key ID for granting access to the S3 bucket  # noqa: E501

        :return: The access_key_id of this S3BlobStoreApiBucketSecurity.  # noqa: E501
        :rtype: str
        """
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, access_key_id):
        """Sets the access_key_id of this S3BlobStoreApiBucketSecurity.

        An IAM access key ID for granting access to the S3 bucket  # noqa: E501

        :param access_key_id: The access_key_id of this S3BlobStoreApiBucketSecurity.  # noqa: E501
        :type: str
        """

        self._access_key_id = access_key_id

    @property
    def secret_access_key(self):
        """Gets the secret_access_key of this S3BlobStoreApiBucketSecurity.  # noqa: E501

        The secret access key associated with the specified IAM access key ID  # noqa: E501

        :return: The secret_access_key of this S3BlobStoreApiBucketSecurity.  # noqa: E501
        :rtype: str
        """
        return self._secret_access_key

    @secret_access_key.setter
    def secret_access_key(self, secret_access_key):
        """Sets the secret_access_key of this S3BlobStoreApiBucketSecurity.

        The secret access key associated with the specified IAM access key ID  # noqa: E501

        :param secret_access_key: The secret_access_key of this S3BlobStoreApiBucketSecurity.  # noqa: E501
        :type: str
        """

        self._secret_access_key = secret_access_key

    @property
    def role(self):
        """Gets the role of this S3BlobStoreApiBucketSecurity.  # noqa: E501

        An IAM role to assume in order to access the S3 bucket  # noqa: E501

        :return: The role of this S3BlobStoreApiBucketSecurity.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this S3BlobStoreApiBucketSecurity.

        An IAM role to assume in order to access the S3 bucket  # noqa: E501

        :param role: The role of this S3BlobStoreApiBucketSecurity.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def session_token(self):
        """Gets the session_token of this S3BlobStoreApiBucketSecurity.  # noqa: E501

        An AWS STS session token associated with temporary security credentials which grant access to the S3 bucket  # noqa: E501

        :return: The session_token of this S3BlobStoreApiBucketSecurity.  # noqa: E501
        :rtype: str
        """
        return self._session_token

    @session_token.setter
    def session_token(self, session_token):
        """Sets the session_token of this S3BlobStoreApiBucketSecurity.

        An AWS STS session token associated with temporary security credentials which grant access to the S3 bucket  # noqa: E501

        :param session_token: The session_token of this S3BlobStoreApiBucketSecurity.  # noqa: E501
        :type: str
        """

        self._session_token = session_token

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
        if issubclass(S3BlobStoreApiBucketSecurity, dict):
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
        if not isinstance(other, S3BlobStoreApiBucketSecurity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
