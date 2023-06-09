"""
    Nexus Repository Manager REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.42.0-01

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Result:
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
        'healthy': 'bool',
        'message': 'str',
        'error': 'Throwable',
        'details': 'dict(str, object)',
        'time': 'int',
        'duration': 'int',
        'timestamp': 'str',
    }

    attribute_map = {
        'healthy': 'healthy',
        'message': 'message',
        'error': 'error',
        'details': 'details',
        'time': 'time',
        'duration': 'duration',
        'timestamp': 'timestamp',
    }

    def __init__(
        self,
        healthy=None,
        message=None,
        error=None,
        details=None,
        time=None,
        duration=None,
        timestamp=None,
    ):  # noqa: E501
        """Result - a model defined in Swagger"""  # noqa: E501
        self._healthy = None
        self._message = None
        self._error = None
        self._details = None
        self._time = None
        self._duration = None
        self._timestamp = None
        self.discriminator = None
        if healthy is not None:
            self.healthy = healthy
        if message is not None:
            self.message = message
        if error is not None:
            self.error = error
        if details is not None:
            self.details = details
        if time is not None:
            self.time = time
        if duration is not None:
            self.duration = duration
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def healthy(self):
        """Gets the healthy of this Result.  # noqa: E501


        :return: The healthy of this Result.  # noqa: E501
        :rtype: bool
        """
        return self._healthy

    @healthy.setter
    def healthy(self, healthy):
        """Sets the healthy of this Result.


        :param healthy: The healthy of this Result.  # noqa: E501
        :type: bool
        """

        self._healthy = healthy

    @property
    def message(self):
        """Gets the message of this Result.  # noqa: E501


        :return: The message of this Result.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Result.


        :param message: The message of this Result.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def error(self):
        """Gets the error of this Result.  # noqa: E501


        :return: The error of this Result.  # noqa: E501
        :rtype: Throwable
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this Result.


        :param error: The error of this Result.  # noqa: E501
        :type: Throwable
        """

        self._error = error

    @property
    def details(self):
        """Gets the details of this Result.  # noqa: E501


        :return: The details of this Result.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this Result.


        :param details: The details of this Result.  # noqa: E501
        :type: dict(str, object)
        """

        self._details = details

    @property
    def time(self):
        """Gets the time of this Result.  # noqa: E501


        :return: The time of this Result.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this Result.


        :param time: The time of this Result.  # noqa: E501
        :type: int
        """

        self._time = time

    @property
    def duration(self):
        """Gets the duration of this Result.  # noqa: E501


        :return: The duration of this Result.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Result.


        :param duration: The duration of this Result.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def timestamp(self):
        """Gets the timestamp of this Result.  # noqa: E501


        :return: The timestamp of this Result.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Result.


        :param timestamp: The timestamp of this Result.  # noqa: E501
        :type: str
        """

        self._timestamp = timestamp

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
        if issubclass(Result, dict):
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
        if not isinstance(other, Result):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
