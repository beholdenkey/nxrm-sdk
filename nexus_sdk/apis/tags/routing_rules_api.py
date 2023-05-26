# coding: utf-8

"""
    Nexus Repository Manager REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 3.42.0-01
    Generated by: https://openapi-generator.tech
"""

from nexus_sdk.paths.v1_routing_rules.post import CreateRoutingRule
from nexus_sdk.paths.v1_routing_rules_name.delete import DeleteRoutingRule
from nexus_sdk.paths.v1_routing_rules_name.get import GetRoutingRule
from nexus_sdk.paths.v1_routing_rules.get import GetRoutingRules
from nexus_sdk.paths.v1_routing_rules_name.put import UpdateRoutingRule


class RoutingRulesApi(
    CreateRoutingRule,
    DeleteRoutingRule,
    GetRoutingRule,
    GetRoutingRules,
    UpdateRoutingRule,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass