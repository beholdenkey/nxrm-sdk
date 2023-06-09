"""
    Nexus Repository Manager REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.42.0-01

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class HttpClientConnectionAttributes:
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
        'retries': 'int',
        'user_agent_suffix': 'str',
        'timeout': 'int',
        'enable_circular_redirects': 'bool',
        'enable_cookies': 'bool',
        'use_trust_store': 'bool',
    }

    attribute_map = {
        'retries': 'retries',
        'user_agent_suffix': 'userAgentSuffix',
        'timeout': 'timeout',
        'enable_circular_redirects': 'enableCircularRedirects',
        'enable_cookies': 'enableCookies',
        'use_trust_store': 'useTrustStore',
    }

    def __init__(
        self,
        retries=None,
        user_agent_suffix=None,
        timeout=None,
        enable_circular_redirects=None,
        enable_cookies=None,
        use_trust_store=None,
    ):  # noqa: E501
        """HttpClientConnectionAttributes - a model defined in Swagger"""  # noqa: E501
        self._retries = None
        self._user_agent_suffix = None
        self._timeout = None
        self._enable_circular_redirects = None
        self._enable_cookies = None
        self._use_trust_store = None
        self.discriminator = None
        if retries is not None:
            self.retries = retries
        if user_agent_suffix is not None:
            self.user_agent_suffix = user_agent_suffix
        if timeout is not None:
            self.timeout = timeout
        if enable_circular_redirects is not None:
            self.enable_circular_redirects = enable_circular_redirects
        if enable_cookies is not None:
            self.enable_cookies = enable_cookies
        if use_trust_store is not None:
            self.use_trust_store = use_trust_store

    @property
    def retries(self):
        """Gets the retries of this HttpClientConnectionAttributes.  # noqa: E501

        Total retries if the initial connection attempt suffers a timeout  # noqa: E501

        :return: The retries of this HttpClientConnectionAttributes.  # noqa: E501
        :rtype: int
        """
        return self._retries

    @retries.setter
    def retries(self, retries):
        """Sets the retries of this HttpClientConnectionAttributes.

        Total retries if the initial connection attempt suffers a timeout  # noqa: E501

        :param retries: The retries of this HttpClientConnectionAttributes.  # noqa: E501
        :type: int
        """

        self._retries = retries

    @property
    def user_agent_suffix(self):
        """Gets the user_agent_suffix of this HttpClientConnectionAttributes.  # noqa: E501

        Custom fragment to append to User-Agent header in HTTP requests  # noqa: E501

        :return: The user_agent_suffix of this HttpClientConnectionAttributes.  # noqa: E501
        :rtype: str
        """
        return self._user_agent_suffix

    @user_agent_suffix.setter
    def user_agent_suffix(self, user_agent_suffix):
        """Sets the user_agent_suffix of this HttpClientConnectionAttributes.

        Custom fragment to append to User-Agent header in HTTP requests  # noqa: E501

        :param user_agent_suffix: The user_agent_suffix of this HttpClientConnectionAttributes.  # noqa: E501
        :type: str
        """

        self._user_agent_suffix = user_agent_suffix

    @property
    def timeout(self):
        """Gets the timeout of this HttpClientConnectionAttributes.  # noqa: E501

        Seconds to wait for activity before stopping and retrying the connection  # noqa: E501

        :return: The timeout of this HttpClientConnectionAttributes.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this HttpClientConnectionAttributes.

        Seconds to wait for activity before stopping and retrying the connection  # noqa: E501

        :param timeout: The timeout of this HttpClientConnectionAttributes.  # noqa: E501
        :type: int
        """

        self._timeout = timeout

    @property
    def enable_circular_redirects(self):
        """Gets the enable_circular_redirects of this HttpClientConnectionAttributes.  # noqa: E501

        Whether to enable redirects to the same location (may be required by some servers)  # noqa: E501

        :return: The enable_circular_redirects of this HttpClientConnectionAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._enable_circular_redirects

    @enable_circular_redirects.setter
    def enable_circular_redirects(self, enable_circular_redirects):
        """Sets the enable_circular_redirects of this HttpClientConnectionAttributes.

        Whether to enable redirects to the same location (may be required by some servers)  # noqa: E501

        :param enable_circular_redirects: The enable_circular_redirects of this HttpClientConnectionAttributes.  # noqa: E501
        :type: bool
        """

        self._enable_circular_redirects = enable_circular_redirects

    @property
    def enable_cookies(self):
        """Gets the enable_cookies of this HttpClientConnectionAttributes.  # noqa: E501

        Whether to allow cookies to be stored and used  # noqa: E501

        :return: The enable_cookies of this HttpClientConnectionAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._enable_cookies

    @enable_cookies.setter
    def enable_cookies(self, enable_cookies):
        """Sets the enable_cookies of this HttpClientConnectionAttributes.

        Whether to allow cookies to be stored and used  # noqa: E501

        :param enable_cookies: The enable_cookies of this HttpClientConnectionAttributes.  # noqa: E501
        :type: bool
        """

        self._enable_cookies = enable_cookies

    @property
    def use_trust_store(self):
        """Gets the use_trust_store of this HttpClientConnectionAttributes.  # noqa: E501

        Use certificates stored in the Nexus Repository Manager truststore to connect to external systems  # noqa: E501

        :return: The use_trust_store of this HttpClientConnectionAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._use_trust_store

    @use_trust_store.setter
    def use_trust_store(self, use_trust_store):
        """Sets the use_trust_store of this HttpClientConnectionAttributes.

        Use certificates stored in the Nexus Repository Manager truststore to connect to external systems  # noqa: E501

        :param use_trust_store: The use_trust_store of this HttpClientConnectionAttributes.  # noqa: E501
        :type: bool
        """

        self._use_trust_store = use_trust_store

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
        if issubclass(HttpClientConnectionAttributes, dict):
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
        if not isinstance(other, HttpClientConnectionAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
