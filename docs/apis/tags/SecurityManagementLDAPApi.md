<a id="__pageTop"></a>
# nexus_sdk.apis.tags.security_management_ldap_api.SecurityManagementLDAPApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_order**](#change_order) | **post** /v1/security/ldap/change-order | Change LDAP server order
[**create_ldap_server**](#create_ldap_server) | **post** /v1/security/ldap | Create LDAP server
[**delete_ldap_server**](#delete_ldap_server) | **delete** /v1/security/ldap/{name} | Delete LDAP server
[**get_ldap_server**](#get_ldap_server) | **get** /v1/security/ldap/{name} | Get LDAP server
[**get_ldap_servers**](#get_ldap_servers) | **get** /v1/security/ldap | List LDAP servers
[**update_ldap_server**](#update_ldap_server) | **put** /v1/security/ldap/{name} | Update LDAP server

# **change_order**
<a id="change_order"></a>
> change_order()

Change LDAP server order

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_ldap_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_ldap_api.SecurityManagementLDAPApi(api_client)

    # example passing only optional values
    body = [
        "body_example"
    ]
    try:
        # Change LDAP server order
        api_response = api_instance.change_order(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementLDAPApi->change_order: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#change_order.ApiResponseFor204) | LDAP server order changed
401 | [ApiResponseFor401](#change_order.ApiResponseFor401) | Authentication required
403 | [ApiResponseFor403](#change_order.ApiResponseFor403) | Insufficient permissions

#### change_order.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### change_order.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### change_order.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_ldap_server**
<a id="create_ldap_server"></a>
> create_ldap_server()

Create LDAP server

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_ldap_api
from nexus_sdk.model.create_ldap_server_xo import CreateLdapServerXo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_ldap_api.SecurityManagementLDAPApi(api_client)

    # example passing only optional values
    body = CreateLdapServerXo(
        name="name_example",
        protocol="ldap",
        use_trust_store=True,
        host="host_example",
        port=636,
        search_base="dc=example,dc=com",
        auth_scheme="NONE",
        auth_realm="example.com",
        auth_username="auth_username_example",
        connection_timeout_seconds=1,
        connection_retry_delay_seconds=0,
        max_incidents_count=0,
        user_base_dn="ou=people",
        user_subtree=True,
        user_object_class="inetOrgPerson",
        user_ldap_filter="(|(mail=*@example.com)(uid=dom*))",
        user_id_attribute="uid",
        user_real_name_attribute="cn",
        user_email_address_attribute="mail",
        user_password_attribute="user_password_attribute_example",
        ldap_groups_as_roles=True,
        group_type="static",
        group_base_dn="ou=Group",
        group_subtree=True,
        group_object_class="posixGroup",
        group_id_attribute="cn",
        group_member_attribute="memberUid",
        group_member_format="uid=${username},ou=people,dc=example,dc=com",
        user_member_of_attribute="memberOf",
        auth_password="auth_password_example",
    )
    try:
        # Create LDAP server
        api_response = api_instance.create_ldap_server(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementLDAPApi->create_ldap_server: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateLdapServerXo**](../../models/CreateLdapServerXo.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_ldap_server.ApiResponseFor201) | LDAP server created
401 | [ApiResponseFor401](#create_ldap_server.ApiResponseFor401) | Authentication required
403 | [ApiResponseFor403](#create_ldap_server.ApiResponseFor403) | Insufficient permissions

#### create_ldap_server.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_ldap_server.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_ldap_server.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_ldap_server**
<a id="delete_ldap_server"></a>
> delete_ldap_server(name)

Delete LDAP server

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_ldap_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_ldap_api.SecurityManagementLDAPApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    try:
        # Delete LDAP server
        api_response = api_instance.delete_ldap_server(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementLDAPApi->delete_ldap_server: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_ldap_server.ApiResponseFor204) | LDAP server deleted
401 | [ApiResponseFor401](#delete_ldap_server.ApiResponseFor401) | Authentication required
403 | [ApiResponseFor403](#delete_ldap_server.ApiResponseFor403) | Insufficient permissions
404 | [ApiResponseFor404](#delete_ldap_server.ApiResponseFor404) | LDAP server not found

#### delete_ldap_server.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_ldap_server.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_ldap_server.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_ldap_server.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_ldap_server**
<a id="get_ldap_server"></a>
> get_ldap_server(name)

Get LDAP server

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_ldap_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_ldap_api.SecurityManagementLDAPApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    try:
        # Get LDAP server
        api_response = api_instance.get_ldap_server(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementLDAPApi->get_ldap_server: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_ldap_server.ApiResponseFor200) | LDAP server returned
401 | [ApiResponseFor401](#get_ldap_server.ApiResponseFor401) | Authentication required
403 | [ApiResponseFor403](#get_ldap_server.ApiResponseFor403) | Insufficient permissions
404 | [ApiResponseFor404](#get_ldap_server.ApiResponseFor404) | LDAP server not found

#### get_ldap_server.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_ldap_server.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_ldap_server.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_ldap_server.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_ldap_servers**
<a id="get_ldap_servers"></a>
> get_ldap_servers()

List LDAP servers

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_ldap_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_ldap_api.SecurityManagementLDAPApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List LDAP servers
        api_response = api_instance.get_ldap_servers()
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementLDAPApi->get_ldap_servers: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_ldap_servers.ApiResponseFor200) | LDAP server list returned
401 | [ApiResponseFor401](#get_ldap_servers.ApiResponseFor401) | Authentication required
403 | [ApiResponseFor403](#get_ldap_servers.ApiResponseFor403) | Insufficient permissions

#### get_ldap_servers.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_ldap_servers.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_ldap_servers.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_ldap_server**
<a id="update_ldap_server"></a>
> update_ldap_server(name)

Update LDAP server

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_ldap_api
from nexus_sdk.model.update_ldap_server_xo import UpdateLdapServerXo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_ldap_api.SecurityManagementLDAPApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    try:
        # Update LDAP server
        api_response = api_instance.update_ldap_server(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementLDAPApi->update_ldap_server: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
    }
    body = UpdateLdapServerXo(
        name="name_example",
        protocol="ldap",
        use_trust_store=True,
        host="host_example",
        port=636,
        search_base="dc=example,dc=com",
        auth_scheme="NONE",
        auth_realm="example.com",
        auth_username="auth_username_example",
        connection_timeout_seconds=1,
        connection_retry_delay_seconds=0,
        max_incidents_count=0,
        user_base_dn="ou=people",
        user_subtree=True,
        user_object_class="inetOrgPerson",
        user_ldap_filter="(|(mail=*@example.com)(uid=dom*))",
        user_id_attribute="uid",
        user_real_name_attribute="cn",
        user_email_address_attribute="mail",
        user_password_attribute="user_password_attribute_example",
        ldap_groups_as_roles=True,
        group_type="static",
        group_base_dn="ou=Group",
        group_subtree=True,
        group_object_class="posixGroup",
        group_id_attribute="cn",
        group_member_attribute="memberUid",
        group_member_format="uid=${username},ou=people,dc=example,dc=com",
        user_member_of_attribute="memberOf",
        auth_password="auth_password_example",
        id="id_example",
    )
    try:
        # Update LDAP server
        api_response = api_instance.update_ldap_server(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementLDAPApi->update_ldap_server: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateLdapServerXo**](../../models/UpdateLdapServerXo.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#update_ldap_server.ApiResponseFor204) | LDAP server updated
401 | [ApiResponseFor401](#update_ldap_server.ApiResponseFor401) | Authentication required
403 | [ApiResponseFor403](#update_ldap_server.ApiResponseFor403) | Insufficient permissions
404 | [ApiResponseFor404](#update_ldap_server.ApiResponseFor404) | LDAP server not found

#### update_ldap_server.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_ldap_server.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_ldap_server.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_ldap_server.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

