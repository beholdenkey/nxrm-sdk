"""
    Nexus Repository Manager REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.42.0-01

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class YumProxyRepositoryApiRequest:
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
        'online': 'bool',
        'storage': 'StorageAttributes',
        'cleanup': 'CleanupPolicyAttributes',
        'proxy': 'ProxyAttributes',
        'negative_cache': 'NegativeCacheAttributes',
        'http_client': 'HttpClientAttributes',
        'routing_rule': 'str',
        'replication': 'ReplicationAttributes',
        'yum_signing': 'YumSigningRepositoriesAttributes',
    }

    attribute_map = {
        'name': 'name',
        'online': 'online',
        'storage': 'storage',
        'cleanup': 'cleanup',
        'proxy': 'proxy',
        'negative_cache': 'negativeCache',
        'http_client': 'httpClient',
        'routing_rule': 'routingRule',
        'replication': 'replication',
        'yum_signing': 'yumSigning',
    }

    def __init__(
        self,
        name=None,
        online=None,
        storage=None,
        cleanup=None,
        proxy=None,
        negative_cache=None,
        http_client=None,
        routing_rule=None,
        replication=None,
        yum_signing=None,
    ):  # noqa: E501
        """YumProxyRepositoryApiRequest - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._online = None
        self._storage = None
        self._cleanup = None
        self._proxy = None
        self._negative_cache = None
        self._http_client = None
        self._routing_rule = None
        self._replication = None
        self._yum_signing = None
        self.discriminator = None
        self.name = name
        self.online = online
        self.storage = storage
        if cleanup is not None:
            self.cleanup = cleanup
        self.proxy = proxy
        self.negative_cache = negative_cache
        self.http_client = http_client
        if routing_rule is not None:
            self.routing_rule = routing_rule
        if replication is not None:
            self.replication = replication
        if yum_signing is not None:
            self.yum_signing = yum_signing

    @property
    def name(self):
        """Gets the name of this YumProxyRepositoryApiRequest.  # noqa: E501

        A unique identifier for this repository  # noqa: E501

        :return: The name of this YumProxyRepositoryApiRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this YumProxyRepositoryApiRequest.

        A unique identifier for this repository  # noqa: E501

        :param name: The name of this YumProxyRepositoryApiRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError(
                'Invalid value for `name`, must not be `None`'
            )  # noqa: E501

        self._name = name

    @property
    def online(self):
        """Gets the online of this YumProxyRepositoryApiRequest.  # noqa: E501

        Whether this repository accepts incoming requests  # noqa: E501

        :return: The online of this YumProxyRepositoryApiRequest.  # noqa: E501
        :rtype: bool
        """
        return self._online

    @online.setter
    def online(self, online):
        """Sets the online of this YumProxyRepositoryApiRequest.

        Whether this repository accepts incoming requests  # noqa: E501

        :param online: The online of this YumProxyRepositoryApiRequest.  # noqa: E501
        :type: bool
        """
        if online is None:
            raise ValueError(
                'Invalid value for `online`, must not be `None`'
            )  # noqa: E501

        self._online = online

    @property
    def storage(self):
        """Gets the storage of this YumProxyRepositoryApiRequest.  # noqa: E501


        :return: The storage of this YumProxyRepositoryApiRequest.  # noqa: E501
        :rtype: StorageAttributes
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this YumProxyRepositoryApiRequest.


        :param storage: The storage of this YumProxyRepositoryApiRequest.  # noqa: E501
        :type: StorageAttributes
        """
        if storage is None:
            raise ValueError(
                'Invalid value for `storage`, must not be `None`'
            )  # noqa: E501

        self._storage = storage

    @property
    def cleanup(self):
        """Gets the cleanup of this YumProxyRepositoryApiRequest.  # noqa: E501


        :return: The cleanup of this YumProxyRepositoryApiRequest.  # noqa: E501
        :rtype: CleanupPolicyAttributes
        """
        return self._cleanup

    @cleanup.setter
    def cleanup(self, cleanup):
        """Sets the cleanup of this YumProxyRepositoryApiRequest.


        :param cleanup: The cleanup of this YumProxyRepositoryApiRequest.  # noqa: E501
        :type: CleanupPolicyAttributes
        """

        self._cleanup = cleanup

    @property
    def proxy(self):
        """Gets the proxy of this YumProxyRepositoryApiRequest.  # noqa: E501


        :return: The proxy of this YumProxyRepositoryApiRequest.  # noqa: E501
        :rtype: ProxyAttributes
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this YumProxyRepositoryApiRequest.


        :param proxy: The proxy of this YumProxyRepositoryApiRequest.  # noqa: E501
        :type: ProxyAttributes
        """
        if proxy is None:
            raise ValueError(
                'Invalid value for `proxy`, must not be `None`'
            )  # noqa: E501

        self._proxy = proxy

    @property
    def negative_cache(self):
        """Gets the negative_cache of this YumProxyRepositoryApiRequest.  # noqa: E501


        :return: The negative_cache of this YumProxyRepositoryApiRequest.  # noqa: E501
        :rtype: NegativeCacheAttributes
        """
        return self._negative_cache

    @negative_cache.setter
    def negative_cache(self, negative_cache):
        """Sets the negative_cache of this YumProxyRepositoryApiRequest.


        :param negative_cache: The negative_cache of this YumProxyRepositoryApiRequest.  # noqa: E501
        :type: NegativeCacheAttributes
        """
        if negative_cache is None:
            raise ValueError(
                'Invalid value for `negative_cache`, must not be `None`'
            )  # noqa: E501

        self._negative_cache = negative_cache

    @property
    def http_client(self):
        """Gets the http_client of this YumProxyRepositoryApiRequest.  # noqa: E501


        :return: The http_client of this YumProxyRepositoryApiRequest.  # noqa: E501
        :rtype: HttpClientAttributes
        """
        return self._http_client

    @http_client.setter
    def http_client(self, http_client):
        """Sets the http_client of this YumProxyRepositoryApiRequest.


        :param http_client: The http_client of this YumProxyRepositoryApiRequest.  # noqa: E501
        :type: HttpClientAttributes
        """
        if http_client is None:
            raise ValueError(
                'Invalid value for `http_client`, must not be `None`'
            )  # noqa: E501

        self._http_client = http_client

    @property
    def routing_rule(self):
        """Gets the routing_rule of this YumProxyRepositoryApiRequest.  # noqa: E501


        :return: The routing_rule of this YumProxyRepositoryApiRequest.  # noqa: E501
        :rtype: str
        """
        return self._routing_rule

    @routing_rule.setter
    def routing_rule(self, routing_rule):
        """Sets the routing_rule of this YumProxyRepositoryApiRequest.


        :param routing_rule: The routing_rule of this YumProxyRepositoryApiRequest.  # noqa: E501
        :type: str
        """

        self._routing_rule = routing_rule

    @property
    def replication(self):
        """Gets the replication of this YumProxyRepositoryApiRequest.  # noqa: E501


        :return: The replication of this YumProxyRepositoryApiRequest.  # noqa: E501
        :rtype: ReplicationAttributes
        """
        return self._replication

    @replication.setter
    def replication(self, replication):
        """Sets the replication of this YumProxyRepositoryApiRequest.


        :param replication: The replication of this YumProxyRepositoryApiRequest.  # noqa: E501
        :type: ReplicationAttributes
        """

        self._replication = replication

    @property
    def yum_signing(self):
        """Gets the yum_signing of this YumProxyRepositoryApiRequest.  # noqa: E501


        :return: The yum_signing of this YumProxyRepositoryApiRequest.  # noqa: E501
        :rtype: YumSigningRepositoriesAttributes
        """
        return self._yum_signing

    @yum_signing.setter
    def yum_signing(self, yum_signing):
        """Sets the yum_signing of this YumProxyRepositoryApiRequest.


        :param yum_signing: The yum_signing of this YumProxyRepositoryApiRequest.  # noqa: E501
        :type: YumSigningRepositoriesAttributes
        """

        self._yum_signing = yum_signing

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
        if issubclass(YumProxyRepositoryApiRequest, dict):
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
        if not isinstance(other, YumProxyRepositoryApiRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
