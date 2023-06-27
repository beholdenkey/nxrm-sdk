"""
    Nexus Repository Manager REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.42.0-01

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ApiCertificate:
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
        'expires_on': 'int',
        'fingerprint': 'str',
        'id': 'str',
        'issued_on': 'int',
        'issuer_common_name': 'str',
        'issuer_organization': 'str',
        'issuer_organizational_unit': 'str',
        'pem': 'str',
        'serial_number': 'str',
        'subject_common_name': 'str',
        'subject_organization': 'str',
        'subject_organizational_unit': 'str',
    }

    attribute_map = {
        'expires_on': 'expiresOn',
        'fingerprint': 'fingerprint',
        'id': 'id',
        'issued_on': 'issuedOn',
        'issuer_common_name': 'issuerCommonName',
        'issuer_organization': 'issuerOrganization',
        'issuer_organizational_unit': 'issuerOrganizationalUnit',
        'pem': 'pem',
        'serial_number': 'serialNumber',
        'subject_common_name': 'subjectCommonName',
        'subject_organization': 'subjectOrganization',
        'subject_organizational_unit': 'subjectOrganizationalUnit',
    }

    def __init__(
        self,
        expires_on=None,
        fingerprint=None,
        id=None,
        issued_on=None,
        issuer_common_name=None,
        issuer_organization=None,
        issuer_organizational_unit=None,
        pem=None,
        serial_number=None,
        subject_common_name=None,
        subject_organization=None,
        subject_organizational_unit=None,
    ):  # noqa: E501
        """ApiCertificate - a model defined in Swagger"""  # noqa: E501
        self._expires_on = None
        self._fingerprint = None
        self._id = None
        self._issued_on = None
        self._issuer_common_name = None
        self._issuer_organization = None
        self._issuer_organizational_unit = None
        self._pem = None
        self._serial_number = None
        self._subject_common_name = None
        self._subject_organization = None
        self._subject_organizational_unit = None
        self.discriminator = None
        if expires_on is not None:
            self.expires_on = expires_on
        if fingerprint is not None:
            self.fingerprint = fingerprint
        if id is not None:
            self.id = id
        if issued_on is not None:
            self.issued_on = issued_on
        if issuer_common_name is not None:
            self.issuer_common_name = issuer_common_name
        if issuer_organization is not None:
            self.issuer_organization = issuer_organization
        if issuer_organizational_unit is not None:
            self.issuer_organizational_unit = issuer_organizational_unit
        if pem is not None:
            self.pem = pem
        if serial_number is not None:
            self.serial_number = serial_number
        if subject_common_name is not None:
            self.subject_common_name = subject_common_name
        if subject_organization is not None:
            self.subject_organization = subject_organization
        if subject_organizational_unit is not None:
            self.subject_organizational_unit = subject_organizational_unit

    @property
    def expires_on(self):
        """Gets the expires_on of this ApiCertificate.  # noqa: E501


        :return: The expires_on of this ApiCertificate.  # noqa: E501
        :rtype: int
        """
        return self._expires_on

    @expires_on.setter
    def expires_on(self, expires_on):
        """Sets the expires_on of this ApiCertificate.


        :param expires_on: The expires_on of this ApiCertificate.  # noqa: E501
        :type: int
        """

        self._expires_on = expires_on

    @property
    def fingerprint(self):
        """Gets the fingerprint of this ApiCertificate.  # noqa: E501


        :return: The fingerprint of this ApiCertificate.  # noqa: E501
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """Sets the fingerprint of this ApiCertificate.


        :param fingerprint: The fingerprint of this ApiCertificate.  # noqa: E501
        :type: str
        """

        self._fingerprint = fingerprint

    @property
    def id(self):
        """Gets the id of this ApiCertificate.  # noqa: E501


        :return: The id of this ApiCertificate.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiCertificate.


        :param id: The id of this ApiCertificate.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def issued_on(self):
        """Gets the issued_on of this ApiCertificate.  # noqa: E501


        :return: The issued_on of this ApiCertificate.  # noqa: E501
        :rtype: int
        """
        return self._issued_on

    @issued_on.setter
    def issued_on(self, issued_on):
        """Sets the issued_on of this ApiCertificate.


        :param issued_on: The issued_on of this ApiCertificate.  # noqa: E501
        :type: int
        """

        self._issued_on = issued_on

    @property
    def issuer_common_name(self):
        """Gets the issuer_common_name of this ApiCertificate.  # noqa: E501


        :return: The issuer_common_name of this ApiCertificate.  # noqa: E501
        :rtype: str
        """
        return self._issuer_common_name

    @issuer_common_name.setter
    def issuer_common_name(self, issuer_common_name):
        """Sets the issuer_common_name of this ApiCertificate.


        :param issuer_common_name: The issuer_common_name of this ApiCertificate.  # noqa: E501
        :type: str
        """

        self._issuer_common_name = issuer_common_name

    @property
    def issuer_organization(self):
        """Gets the issuer_organization of this ApiCertificate.  # noqa: E501


        :return: The issuer_organization of this ApiCertificate.  # noqa: E501
        :rtype: str
        """
        return self._issuer_organization

    @issuer_organization.setter
    def issuer_organization(self, issuer_organization):
        """Sets the issuer_organization of this ApiCertificate.


        :param issuer_organization: The issuer_organization of this ApiCertificate.  # noqa: E501
        :type: str
        """

        self._issuer_organization = issuer_organization

    @property
    def issuer_organizational_unit(self):
        """Gets the issuer_organizational_unit of this ApiCertificate.  # noqa: E501


        :return: The issuer_organizational_unit of this ApiCertificate.  # noqa: E501
        :rtype: str
        """
        return self._issuer_organizational_unit

    @issuer_organizational_unit.setter
    def issuer_organizational_unit(self, issuer_organizational_unit):
        """Sets the issuer_organizational_unit of this ApiCertificate.


        :param issuer_organizational_unit: The issuer_organizational_unit of this ApiCertificate.  # noqa: E501
        :type: str
        """

        self._issuer_organizational_unit = issuer_organizational_unit

    @property
    def pem(self):
        """Gets the pem of this ApiCertificate.  # noqa: E501


        :return: The pem of this ApiCertificate.  # noqa: E501
        :rtype: str
        """
        return self._pem

    @pem.setter
    def pem(self, pem):
        """Sets the pem of this ApiCertificate.


        :param pem: The pem of this ApiCertificate.  # noqa: E501
        :type: str
        """

        self._pem = pem

    @property
    def serial_number(self):
        """Gets the serial_number of this ApiCertificate.  # noqa: E501


        :return: The serial_number of this ApiCertificate.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this ApiCertificate.


        :param serial_number: The serial_number of this ApiCertificate.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def subject_common_name(self):
        """Gets the subject_common_name of this ApiCertificate.  # noqa: E501


        :return: The subject_common_name of this ApiCertificate.  # noqa: E501
        :rtype: str
        """
        return self._subject_common_name

    @subject_common_name.setter
    def subject_common_name(self, subject_common_name):
        """Sets the subject_common_name of this ApiCertificate.


        :param subject_common_name: The subject_common_name of this ApiCertificate.  # noqa: E501
        :type: str
        """

        self._subject_common_name = subject_common_name

    @property
    def subject_organization(self):
        """Gets the subject_organization of this ApiCertificate.  # noqa: E501


        :return: The subject_organization of this ApiCertificate.  # noqa: E501
        :rtype: str
        """
        return self._subject_organization

    @subject_organization.setter
    def subject_organization(self, subject_organization):
        """Sets the subject_organization of this ApiCertificate.


        :param subject_organization: The subject_organization of this ApiCertificate.  # noqa: E501
        :type: str
        """

        self._subject_organization = subject_organization

    @property
    def subject_organizational_unit(self):
        """Gets the subject_organizational_unit of this ApiCertificate.  # noqa: E501


        :return: The subject_organizational_unit of this ApiCertificate.  # noqa: E501
        :rtype: str
        """
        return self._subject_organizational_unit

    @subject_organizational_unit.setter
    def subject_organizational_unit(self, subject_organizational_unit):
        """Sets the subject_organizational_unit of this ApiCertificate.


        :param subject_organizational_unit: The subject_organizational_unit of this ApiCertificate.  # noqa: E501
        :type: str
        """

        self._subject_organizational_unit = subject_organizational_unit

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
        if issubclass(ApiCertificate, dict):
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
        if not isinstance(other, ApiCertificate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
