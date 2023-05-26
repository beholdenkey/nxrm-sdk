# coding: utf-8

"""
    Nexus Repository Manager REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 3.42.0-01
    Generated by: https://openapi-generator.tech
"""

from nexus_sdk.paths.v1_security_atlassian_crowd_clear_cache.post import ClearCache
from nexus_sdk.paths.v1_security_atlassian_crowd.get import ReadSettings
from nexus_sdk.paths.v1_security_atlassian_crowd.put import UpdateSettings
from nexus_sdk.paths.v1_security_atlassian_crowd_verify_connection.post import VerifyConnection1


class SecurityAtlassianCrowdApi(
    ClearCache,
    ReadSettings,
    UpdateSettings,
    VerifyConnection1,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass