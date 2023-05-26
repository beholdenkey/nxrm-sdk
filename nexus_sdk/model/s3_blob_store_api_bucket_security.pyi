# coding: utf-8

"""
    Nexus Repository Manager REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 3.42.0-01
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from nexus_sdk import schemas  # noqa: F401


class S3BlobStoreApiBucketSecurity(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            accessKeyId = schemas.StrSchema
            secretAccessKey = schemas.StrSchema
            role = schemas.StrSchema
            sessionToken = schemas.StrSchema
            __annotations__ = {
                "accessKeyId": accessKeyId,
                "secretAccessKey": secretAccessKey,
                "role": role,
                "sessionToken": sessionToken,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accessKeyId"]) -> MetaOapg.properties.accessKeyId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secretAccessKey"]) -> MetaOapg.properties.secretAccessKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["role"]) -> MetaOapg.properties.role: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sessionToken"]) -> MetaOapg.properties.sessionToken: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["accessKeyId", "secretAccessKey", "role", "sessionToken", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accessKeyId"]) -> typing.Union[MetaOapg.properties.accessKeyId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secretAccessKey"]) -> typing.Union[MetaOapg.properties.secretAccessKey, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["role"]) -> typing.Union[MetaOapg.properties.role, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sessionToken"]) -> typing.Union[MetaOapg.properties.sessionToken, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["accessKeyId", "secretAccessKey", "role", "sessionToken", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        accessKeyId: typing.Union[MetaOapg.properties.accessKeyId, str, schemas.Unset] = schemas.unset,
        secretAccessKey: typing.Union[MetaOapg.properties.secretAccessKey, str, schemas.Unset] = schemas.unset,
        role: typing.Union[MetaOapg.properties.role, str, schemas.Unset] = schemas.unset,
        sessionToken: typing.Union[MetaOapg.properties.sessionToken, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'S3BlobStoreApiBucketSecurity':
        return super().__new__(
            cls,
            *_args,
            accessKeyId=accessKeyId,
            secretAccessKey=secretAccessKey,
            role=role,
            sessionToken=sessionToken,
            _configuration=_configuration,
            **kwargs,
        )