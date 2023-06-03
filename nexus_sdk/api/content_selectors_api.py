# coding: utf-8

"""
    Nexus Repository Manager REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.42.0-01
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from nexus_sdk.api_client import ApiClient


class ContentSelectorsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_content_selector(self, **kwargs):  # noqa: E501
        """Create a new content selector  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_content_selector(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ContentSelectorApiCreateRequest body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.create_content_selector_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_content_selector_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_content_selector_with_http_info(self, **kwargs):  # noqa: E501
        """Create a new content selector  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_content_selector_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ContentSelectorApiCreateRequest body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_content_selector" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params:
            body_params = params["body"]
        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/v1/security/content-selectors",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def delete_content_selector(self, name, **kwargs):  # noqa: E501
        """Delete a content selector  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_content_selector(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.delete_content_selector_with_http_info(
                name, **kwargs
            )  # noqa: E501
        else:
            (data) = self.delete_content_selector_with_http_info(
                name, **kwargs
            )  # noqa: E501
            return data

    def delete_content_selector_with_http_info(self, name, **kwargs):  # noqa: E501
        """Delete a content selector  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_content_selector_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["name"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_content_selector" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'name' is set
        if "name" not in params or params["name"] is None:
            raise ValueError(
                "Missing the required parameter `name` when calling `delete_content_selector`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "name" in params:
            path_params["name"] = params["name"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/v1/security/content-selectors/{name}",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_content_selector(self, name, **kwargs):  # noqa: E501
        """Get a content selector by name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_content_selector(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: The content selector name (required)
        :return: ContentSelectorApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_content_selector_with_http_info(
                name, **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_content_selector_with_http_info(
                name, **kwargs
            )  # noqa: E501
            return data

    def get_content_selector_with_http_info(self, name, **kwargs):  # noqa: E501
        """Get a content selector by name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_content_selector_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: The content selector name (required)
        :return: ContentSelectorApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["name"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_content_selector" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'name' is set
        if "name" not in params or params["name"] is None:
            raise ValueError(
                "Missing the required parameter `name` when calling `get_content_selector`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "name" in params:
            path_params["name"] = params["name"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/v1/security/content-selectors/{name}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ContentSelectorApiResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_content_selectors(self, **kwargs):  # noqa: E501
        """List content selectors  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_content_selectors(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[ContentSelectorApiResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_content_selectors_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_content_selectors_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_content_selectors_with_http_info(self, **kwargs):  # noqa: E501
        """List content selectors  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_content_selectors_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[ContentSelectorApiResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_content_selectors" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/v1/security/content-selectors",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[ContentSelectorApiResponse]",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def update_content_selector(self, name, **kwargs):  # noqa: E501
        """Update a content selector  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_content_selector(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: The content selector name (required)
        :param ContentSelectorApiUpdateRequest body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.update_content_selector_with_http_info(
                name, **kwargs
            )  # noqa: E501
        else:
            (data) = self.update_content_selector_with_http_info(
                name, **kwargs
            )  # noqa: E501
            return data

    def update_content_selector_with_http_info(self, name, **kwargs):  # noqa: E501
        """Update a content selector  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_content_selector_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: The content selector name (required)
        :param ContentSelectorApiUpdateRequest body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["name", "body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_content_selector" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'name' is set
        if "name" not in params or params["name"] is None:
            raise ValueError(
                "Missing the required parameter `name` when calling `update_content_selector`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "name" in params:
            path_params["name"] = params["name"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params:
            body_params = params["body"]
        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/v1/security/content-selectors/{name}",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
