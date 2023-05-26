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


class ApiPrivilegeRepositoryContentSelectorRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            description = schemas.StrSchema
            
            
            class actions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def READ(cls):
                            return cls("READ")
                        
                        @schemas.classproperty
                        def BROWSE(cls):
                            return cls("BROWSE")
                        
                        @schemas.classproperty
                        def EDIT(cls):
                            return cls("EDIT")
                        
                        @schemas.classproperty
                        def ADD(cls):
                            return cls("ADD")
                        
                        @schemas.classproperty
                        def DELETE(cls):
                            return cls("DELETE")
                        
                        @schemas.classproperty
                        def RUN(cls):
                            return cls("RUN")
                        
                        @schemas.classproperty
                        def ASSOCIATE(cls):
                            return cls("ASSOCIATE")
                        
                        @schemas.classproperty
                        def DISASSOCIATE(cls):
                            return cls("DISASSOCIATE")
                        
                        @schemas.classproperty
                        def ALL(cls):
                            return cls("ALL")
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'actions':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            format = schemas.StrSchema
            repository = schemas.StrSchema
            contentSelector = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "description": description,
                "actions": actions,
                "format": format,
                "repository": repository,
                "contentSelector": contentSelector,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["actions"]) -> MetaOapg.properties.actions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["format"]) -> MetaOapg.properties.format: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["repository"]) -> MetaOapg.properties.repository: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contentSelector"]) -> MetaOapg.properties.contentSelector: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "description", "actions", "format", "repository", "contentSelector", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["actions"]) -> typing.Union[MetaOapg.properties.actions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["format"]) -> typing.Union[MetaOapg.properties.format, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["repository"]) -> typing.Union[MetaOapg.properties.repository, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contentSelector"]) -> typing.Union[MetaOapg.properties.contentSelector, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "description", "actions", "format", "repository", "contentSelector", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        actions: typing.Union[MetaOapg.properties.actions, list, tuple, schemas.Unset] = schemas.unset,
        format: typing.Union[MetaOapg.properties.format, str, schemas.Unset] = schemas.unset,
        repository: typing.Union[MetaOapg.properties.repository, str, schemas.Unset] = schemas.unset,
        contentSelector: typing.Union[MetaOapg.properties.contentSelector, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApiPrivilegeRepositoryContentSelectorRequest':
        return super().__new__(
            cls,
            *_args,
            name=name,
            description=description,
            actions=actions,
            format=format,
            repository=repository,
            contentSelector=contentSelector,
            _configuration=_configuration,
            **kwargs,
        )