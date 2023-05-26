<a id="__pageTop"></a>
# nexus_sdk.apis.tags.security_management_privileges_api.SecurityManagementPrivilegesApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_privilege**](#create_privilege) | **post** /v1/security/privileges/wildcard | Create a wildcard type privilege.
[**create_privilege1**](#create_privilege1) | **post** /v1/security/privileges/application | Create an application type privilege.
[**create_privilege2**](#create_privilege2) | **post** /v1/security/privileges/repository-content-selector | Create a repository content selector type privilege.
[**create_privilege3**](#create_privilege3) | **post** /v1/security/privileges/repository-admin | Create a repository admin type privilege.
[**create_privilege4**](#create_privilege4) | **post** /v1/security/privileges/repository-view | Create a repository view type privilege.
[**create_privilege5**](#create_privilege5) | **post** /v1/security/privileges/script | Create a script type privilege.
[**delete_privilege**](#delete_privilege) | **delete** /v1/security/privileges/{privilegeName} | Delete a privilege by name.
[**get_privilege**](#get_privilege) | **get** /v1/security/privileges/{privilegeName} | Retrieve a privilege by name.
[**get_privileges**](#get_privileges) | **get** /v1/security/privileges | Retrieve a list of privileges.
[**update_privilege**](#update_privilege) | **put** /v1/security/privileges/wildcard/{privilegeName} | Update a wildcard type privilege.
[**update_privilege1**](#update_privilege1) | **put** /v1/security/privileges/application/{privilegeName} | Update an application type privilege.
[**update_privilege2**](#update_privilege2) | **put** /v1/security/privileges/repository-view/{privilegeName} | Update a repository view type privilege.
[**update_privilege3**](#update_privilege3) | **put** /v1/security/privileges/repository-content-selector/{privilegeName} | Update a repository content selector type privilege.
[**update_privilege4**](#update_privilege4) | **put** /v1/security/privileges/repository-admin/{privilegeName} | Update a repository admin type privilege.
[**update_privilege5**](#update_privilege5) | **put** /v1/security/privileges/script/{privilegeName} | Update a script type privilege.

# **create_privilege**
<a id="create_privilege"></a>
> create_privilege()

Create a wildcard type privilege.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_privileges_api
from nexus_sdk.model.api_privilege_wildcard_request import ApiPrivilegeWildcardRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_privileges_api.SecurityManagementPrivilegesApi(api_client)

    # example passing only optional values
    body = ApiPrivilegeWildcardRequest(
        name="e6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        description="description_example",
        pattern="pattern_example",
    )
    try:
        # Create a wildcard type privilege.
        api_response = api_instance.create_privilege(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementPrivilegesApi->create_privilege: %s\n" % e)
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
[**ApiPrivilegeWildcardRequest**](../../models/ApiPrivilegeWildcardRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
400 | [ApiResponseFor400](#create_privilege.ApiResponseFor400) | Privilege object not configured properly.
403 | [ApiResponseFor403](#create_privilege.ApiResponseFor403) | The user does not have permission to perform the operation.

#### create_privilege.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_privilege.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_privilege1**
<a id="create_privilege1"></a>
> create_privilege1()

Create an application type privilege.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_privileges_api
from nexus_sdk.model.api_privilege_application_request import ApiPrivilegeApplicationRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_privileges_api.SecurityManagementPrivilegesApi(api_client)

    # example passing only optional values
    body = ApiPrivilegeApplicationRequest(
        name="e6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        description="description_example",
        actions=[
            "READ"
        ],
        domain="domain_example",
    )
    try:
        # Create an application type privilege.
        api_response = api_instance.create_privilege1(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementPrivilegesApi->create_privilege1: %s\n" % e)
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
[**ApiPrivilegeApplicationRequest**](../../models/ApiPrivilegeApplicationRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
400 | [ApiResponseFor400](#create_privilege1.ApiResponseFor400) | Privilege object not configured properly.
403 | [ApiResponseFor403](#create_privilege1.ApiResponseFor403) | The user does not have permission to perform the operation.

#### create_privilege1.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_privilege1.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_privilege2**
<a id="create_privilege2"></a>
> create_privilege2()

Create a repository content selector type privilege.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_privileges_api
from nexus_sdk.model.api_privilege_repository_content_selector_request import ApiPrivilegeRepositoryContentSelectorRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_privileges_api.SecurityManagementPrivilegesApi(api_client)

    # example passing only optional values
    body = ApiPrivilegeRepositoryContentSelectorRequest(
        name="e6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        description="description_example",
        actions=[
            "READ"
        ],
        format="format_example",
        repository="repository_example",
        content_selector="content_selector_example",
    )
    try:
        # Create a repository content selector type privilege.
        api_response = api_instance.create_privilege2(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementPrivilegesApi->create_privilege2: %s\n" % e)
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
[**ApiPrivilegeRepositoryContentSelectorRequest**](../../models/ApiPrivilegeRepositoryContentSelectorRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
400 | [ApiResponseFor400](#create_privilege2.ApiResponseFor400) | Privilege object not configured properly.
403 | [ApiResponseFor403](#create_privilege2.ApiResponseFor403) | The user does not have permission to perform the operation.

#### create_privilege2.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_privilege2.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_privilege3**
<a id="create_privilege3"></a>
> create_privilege3()

Create a repository admin type privilege.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_privileges_api
from nexus_sdk.model.api_privilege_repository_admin_request import ApiPrivilegeRepositoryAdminRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_privileges_api.SecurityManagementPrivilegesApi(api_client)

    # example passing only optional values
    body = ApiPrivilegeRepositoryAdminRequest(
        name="e6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        description="description_example",
        actions=[
            "READ"
        ],
        format="format_example",
        repository="repository_example",
    )
    try:
        # Create a repository admin type privilege.
        api_response = api_instance.create_privilege3(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementPrivilegesApi->create_privilege3: %s\n" % e)
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
[**ApiPrivilegeRepositoryAdminRequest**](../../models/ApiPrivilegeRepositoryAdminRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
400 | [ApiResponseFor400](#create_privilege3.ApiResponseFor400) | Privilege object not configured properly.
403 | [ApiResponseFor403](#create_privilege3.ApiResponseFor403) | The user does not have permission to perform the operation.

#### create_privilege3.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_privilege3.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_privilege4**
<a id="create_privilege4"></a>
> create_privilege4()

Create a repository view type privilege.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_privileges_api
from nexus_sdk.model.api_privilege_repository_view_request import ApiPrivilegeRepositoryViewRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_privileges_api.SecurityManagementPrivilegesApi(api_client)

    # example passing only optional values
    body = ApiPrivilegeRepositoryViewRequest(
        name="e6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        description="description_example",
        actions=[
            "READ"
        ],
        format="format_example",
        repository="repository_example",
    )
    try:
        # Create a repository view type privilege.
        api_response = api_instance.create_privilege4(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementPrivilegesApi->create_privilege4: %s\n" % e)
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
[**ApiPrivilegeRepositoryViewRequest**](../../models/ApiPrivilegeRepositoryViewRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
400 | [ApiResponseFor400](#create_privilege4.ApiResponseFor400) | Privilege object not configured properly.
403 | [ApiResponseFor403](#create_privilege4.ApiResponseFor403) | The user does not have permission to perform the operation.

#### create_privilege4.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_privilege4.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_privilege5**
<a id="create_privilege5"></a>
> create_privilege5()

Create a script type privilege.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_privileges_api
from nexus_sdk.model.api_privilege_script_request import ApiPrivilegeScriptRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_privileges_api.SecurityManagementPrivilegesApi(api_client)

    # example passing only optional values
    body = ApiPrivilegeScriptRequest(
        name="e6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        description="description_example",
        actions=[
            "READ"
        ],
        script_name="script_name_example",
    )
    try:
        # Create a script type privilege.
        api_response = api_instance.create_privilege5(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementPrivilegesApi->create_privilege5: %s\n" % e)
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
[**ApiPrivilegeScriptRequest**](../../models/ApiPrivilegeScriptRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
400 | [ApiResponseFor400](#create_privilege5.ApiResponseFor400) | Privilege object not configured properly.
403 | [ApiResponseFor403](#create_privilege5.ApiResponseFor403) | The user does not have permission to perform the operation.

#### create_privilege5.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_privilege5.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_privilege**
<a id="delete_privilege"></a>
> delete_privilege(privilege_name)

Delete a privilege by name.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_privileges_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_privileges_api.SecurityManagementPrivilegesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'privilegeName': "privilegeName_example",
    }
    try:
        # Delete a privilege by name.
        api_response = api_instance.delete_privilege(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementPrivilegesApi->delete_privilege: %s\n" % e)
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
privilegeName | PrivilegeNameSchema | | 

# PrivilegeNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
400 | [ApiResponseFor400](#delete_privilege.ApiResponseFor400) | The privilege is internal and may not be altered.
403 | [ApiResponseFor403](#delete_privilege.ApiResponseFor403) | The user does not have permission to perform the operation.
404 | [ApiResponseFor404](#delete_privilege.ApiResponseFor404) | Privilege not found in the system.

#### delete_privilege.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_privilege.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_privilege.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_privilege**
<a id="get_privilege"></a>
> ApiPrivilege get_privilege(privilege_name)

Retrieve a privilege by name.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_privileges_api
from nexus_sdk.model.api_privilege import ApiPrivilege
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_privileges_api.SecurityManagementPrivilegesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'privilegeName': "privilegeName_example",
    }
    try:
        # Retrieve a privilege by name.
        api_response = api_instance.get_privilege(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementPrivilegesApi->get_privilege: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
privilegeName | PrivilegeNameSchema | | 

# PrivilegeNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_privilege.ApiResponseFor200) | successful operation
403 | [ApiResponseFor403](#get_privilege.ApiResponseFor403) | The user does not have permission to perform the operation.
404 | [ApiResponseFor404](#get_privilege.ApiResponseFor404) | Privilege not found in the system.

#### get_privilege.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiPrivilege**](../../models/ApiPrivilege.md) |  | 


#### get_privilege.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_privilege.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_privileges**
<a id="get_privileges"></a>
> [ApiPrivilege] get_privileges()

Retrieve a list of privileges.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_privileges_api
from nexus_sdk.model.api_privilege import ApiPrivilege
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_privileges_api.SecurityManagementPrivilegesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve a list of privileges.
        api_response = api_instance.get_privileges()
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementPrivilegesApi->get_privileges: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_privileges.ApiResponseFor200) | successful operation
403 | [ApiResponseFor403](#get_privileges.ApiResponseFor403) | The user does not have permission to perform the operation.

#### get_privileges.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ApiPrivilege**]({{complexTypePrefix}}ApiPrivilege.md) | [**ApiPrivilege**]({{complexTypePrefix}}ApiPrivilege.md) | [**ApiPrivilege**]({{complexTypePrefix}}ApiPrivilege.md) |  | 

#### get_privileges.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_privilege**
<a id="update_privilege"></a>
> update_privilege(privilege_name)

Update a wildcard type privilege.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_privileges_api
from nexus_sdk.model.api_privilege_wildcard_request import ApiPrivilegeWildcardRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_privileges_api.SecurityManagementPrivilegesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'privilegeName': "privilegeName_example",
    }
    try:
        # Update a wildcard type privilege.
        api_response = api_instance.update_privilege(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementPrivilegesApi->update_privilege: %s\n" % e)

    # example passing only optional values
    path_params = {
        'privilegeName': "privilegeName_example",
    }
    body = ApiPrivilegeWildcardRequest(
        name="e6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        description="description_example",
        pattern="pattern_example",
    )
    try:
        # Update a wildcard type privilege.
        api_response = api_instance.update_privilege(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementPrivilegesApi->update_privilege: %s\n" % e)
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
[**ApiPrivilegeWildcardRequest**](../../models/ApiPrivilegeWildcardRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
privilegeName | PrivilegeNameSchema | | 

# PrivilegeNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
400 | [ApiResponseFor400](#update_privilege.ApiResponseFor400) | Privilege object not configured properly.
403 | [ApiResponseFor403](#update_privilege.ApiResponseFor403) | The user does not have permission to perform the operation.
404 | [ApiResponseFor404](#update_privilege.ApiResponseFor404) | Privilege not found in the system.

#### update_privilege.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_privilege.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_privilege.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_privilege1**
<a id="update_privilege1"></a>
> update_privilege1(privilege_name)

Update an application type privilege.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_privileges_api
from nexus_sdk.model.api_privilege_application_request import ApiPrivilegeApplicationRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_privileges_api.SecurityManagementPrivilegesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'privilegeName': "privilegeName_example",
    }
    try:
        # Update an application type privilege.
        api_response = api_instance.update_privilege1(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementPrivilegesApi->update_privilege1: %s\n" % e)

    # example passing only optional values
    path_params = {
        'privilegeName': "privilegeName_example",
    }
    body = ApiPrivilegeApplicationRequest(
        name="e6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        description="description_example",
        actions=[
            "READ"
        ],
        domain="domain_example",
    )
    try:
        # Update an application type privilege.
        api_response = api_instance.update_privilege1(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementPrivilegesApi->update_privilege1: %s\n" % e)
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
[**ApiPrivilegeApplicationRequest**](../../models/ApiPrivilegeApplicationRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
privilegeName | PrivilegeNameSchema | | 

# PrivilegeNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
400 | [ApiResponseFor400](#update_privilege1.ApiResponseFor400) | Privilege object not configured properly.
403 | [ApiResponseFor403](#update_privilege1.ApiResponseFor403) | The user does not have permission to perform the operation.
404 | [ApiResponseFor404](#update_privilege1.ApiResponseFor404) | Privilege not found in the system.

#### update_privilege1.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_privilege1.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_privilege1.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_privilege2**
<a id="update_privilege2"></a>
> update_privilege2(privilege_name)

Update a repository view type privilege.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_privileges_api
from nexus_sdk.model.api_privilege_repository_view_request import ApiPrivilegeRepositoryViewRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_privileges_api.SecurityManagementPrivilegesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'privilegeName': "privilegeName_example",
    }
    try:
        # Update a repository view type privilege.
        api_response = api_instance.update_privilege2(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementPrivilegesApi->update_privilege2: %s\n" % e)

    # example passing only optional values
    path_params = {
        'privilegeName': "privilegeName_example",
    }
    body = ApiPrivilegeRepositoryViewRequest(
        name="e6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        description="description_example",
        actions=[
            "READ"
        ],
        format="format_example",
        repository="repository_example",
    )
    try:
        # Update a repository view type privilege.
        api_response = api_instance.update_privilege2(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementPrivilegesApi->update_privilege2: %s\n" % e)
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
[**ApiPrivilegeRepositoryViewRequest**](../../models/ApiPrivilegeRepositoryViewRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
privilegeName | PrivilegeNameSchema | | 

# PrivilegeNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
400 | [ApiResponseFor400](#update_privilege2.ApiResponseFor400) | Privilege object not configured properly.
403 | [ApiResponseFor403](#update_privilege2.ApiResponseFor403) | The user does not have permission to perform the operation.
404 | [ApiResponseFor404](#update_privilege2.ApiResponseFor404) | Privilege not found in the system.

#### update_privilege2.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_privilege2.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_privilege2.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_privilege3**
<a id="update_privilege3"></a>
> update_privilege3(privilege_name)

Update a repository content selector type privilege.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_privileges_api
from nexus_sdk.model.api_privilege_repository_content_selector_request import ApiPrivilegeRepositoryContentSelectorRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_privileges_api.SecurityManagementPrivilegesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'privilegeName': "privilegeName_example",
    }
    try:
        # Update a repository content selector type privilege.
        api_response = api_instance.update_privilege3(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementPrivilegesApi->update_privilege3: %s\n" % e)

    # example passing only optional values
    path_params = {
        'privilegeName': "privilegeName_example",
    }
    body = ApiPrivilegeRepositoryContentSelectorRequest(
        name="e6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        description="description_example",
        actions=[
            "READ"
        ],
        format="format_example",
        repository="repository_example",
        content_selector="content_selector_example",
    )
    try:
        # Update a repository content selector type privilege.
        api_response = api_instance.update_privilege3(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementPrivilegesApi->update_privilege3: %s\n" % e)
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
[**ApiPrivilegeRepositoryContentSelectorRequest**](../../models/ApiPrivilegeRepositoryContentSelectorRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
privilegeName | PrivilegeNameSchema | | 

# PrivilegeNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
400 | [ApiResponseFor400](#update_privilege3.ApiResponseFor400) | Privilege object not configured properly.
403 | [ApiResponseFor403](#update_privilege3.ApiResponseFor403) | The user does not have permission to perform the operation.
404 | [ApiResponseFor404](#update_privilege3.ApiResponseFor404) | Privilege not found in the system.

#### update_privilege3.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_privilege3.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_privilege3.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_privilege4**
<a id="update_privilege4"></a>
> update_privilege4(privilege_name)

Update a repository admin type privilege.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_privileges_api
from nexus_sdk.model.api_privilege_repository_admin_request import ApiPrivilegeRepositoryAdminRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_privileges_api.SecurityManagementPrivilegesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'privilegeName': "privilegeName_example",
    }
    try:
        # Update a repository admin type privilege.
        api_response = api_instance.update_privilege4(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementPrivilegesApi->update_privilege4: %s\n" % e)

    # example passing only optional values
    path_params = {
        'privilegeName': "privilegeName_example",
    }
    body = ApiPrivilegeRepositoryAdminRequest(
        name="e6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        description="description_example",
        actions=[
            "READ"
        ],
        format="format_example",
        repository="repository_example",
    )
    try:
        # Update a repository admin type privilege.
        api_response = api_instance.update_privilege4(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementPrivilegesApi->update_privilege4: %s\n" % e)
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
[**ApiPrivilegeRepositoryAdminRequest**](../../models/ApiPrivilegeRepositoryAdminRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
privilegeName | PrivilegeNameSchema | | 

# PrivilegeNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
400 | [ApiResponseFor400](#update_privilege4.ApiResponseFor400) | Privilege object not configured properly.
403 | [ApiResponseFor403](#update_privilege4.ApiResponseFor403) | The user does not have permission to perform the operation.
404 | [ApiResponseFor404](#update_privilege4.ApiResponseFor404) | Privilege not found in the system.

#### update_privilege4.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_privilege4.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_privilege4.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_privilege5**
<a id="update_privilege5"></a>
> update_privilege5(privilege_name)

Update a script type privilege.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_privileges_api
from nexus_sdk.model.api_privilege_script_request import ApiPrivilegeScriptRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_privileges_api.SecurityManagementPrivilegesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'privilegeName': "privilegeName_example",
    }
    try:
        # Update a script type privilege.
        api_response = api_instance.update_privilege5(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementPrivilegesApi->update_privilege5: %s\n" % e)

    # example passing only optional values
    path_params = {
        'privilegeName': "privilegeName_example",
    }
    body = ApiPrivilegeScriptRequest(
        name="e6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        description="description_example",
        actions=[
            "READ"
        ],
        script_name="script_name_example",
    )
    try:
        # Update a script type privilege.
        api_response = api_instance.update_privilege5(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementPrivilegesApi->update_privilege5: %s\n" % e)
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
[**ApiPrivilegeScriptRequest**](../../models/ApiPrivilegeScriptRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
privilegeName | PrivilegeNameSchema | | 

# PrivilegeNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
400 | [ApiResponseFor400](#update_privilege5.ApiResponseFor400) | Privilege object not configured properly.
403 | [ApiResponseFor403](#update_privilege5.ApiResponseFor403) | The user does not have permission to perform the operation.
404 | [ApiResponseFor404](#update_privilege5.ApiResponseFor404) | Privilege not found in the system.

#### update_privilege5.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_privilege5.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_privilege5.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

