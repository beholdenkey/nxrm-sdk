<a id="__pageTop"></a>
# nexus_sdk.apis.tags.replication_api.ReplicationApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**call_list**](#call_list) | **get** /beta/replication/connection | List the replication connections.
[**create2**](#create2) | **post** /beta/replication/connection | Create a replication connection.
[**delete3**](#delete3) | **delete** /beta/replication/connection/{name} | Delete a replication connection.
[**disable**](#disable) | **delete** /beta/replicationtarget/repository/{repositoryName}/enable | Disable replication on a target repository..
[**enable**](#enable) | **put** /beta/replicationtarget/repository/enable | Enable replication on a target repository.
[**get4**](#get4) | **get** /beta/replication/connection/{name} | Fetch a replication connection.
[**update2**](#update2) | **put** /beta/replication/connection/{name} | Update a replication connection.

# **call_list**
<a id="call_list"></a>
> call_list()

List the replication connections.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import replication_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = replication_api.ReplicationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List the replication connections.
        api_response = api_instance.call_list()
    except nexus_sdk.ApiException as e:
        print("Exception when calling ReplicationApi->call_list: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#call_list.ApiResponseFor200) | Replication connection list returned
401 | [ApiResponseFor401](#call_list.ApiResponseFor401) | Authentication required
403 | [ApiResponseFor403](#call_list.ApiResponseFor403) | Insufficient permissions

#### call_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### call_list.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### call_list.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create2**
<a id="create2"></a>
> create2()

Create a replication connection.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import replication_api
from nexus_sdk.model.replication_connection_xo import ReplicationConnectionXO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = replication_api.ReplicationApi(api_client)

    # example passing only optional values
    body = ReplicationConnectionXO(
        id="id_example",
        name="name_example",
        source_repository_name="maven-releases",
        destination_instance_url="https://example.com/",
        destination_instance_username="admin",
        destination_instance_password="admin123",
        destination_repository_name="maven-releases",
        content_regexes=[
            "content_regexes_example"
        ],
        include_existing_content=True,
        use_trust_store=True,
    )
    try:
        # Create a replication connection.
        api_response = api_instance.create2(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling ReplicationApi->create2: %s\n" % e)
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
[**ReplicationConnectionXO**](../../models/ReplicationConnectionXO.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create2.ApiResponseFor200) | Replication connection created
400 | [ApiResponseFor400](#create2.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#create2.ApiResponseFor401) | Authentication required
403 | [ApiResponseFor403](#create2.ApiResponseFor403) | Insufficient permissions

#### create2.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create2.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create2.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create2.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete3**
<a id="delete3"></a>
> delete3(name)

Delete a replication connection.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import replication_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = replication_api.ReplicationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    try:
        # Delete a replication connection.
        api_response = api_instance.delete3(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling ReplicationApi->delete3: %s\n" % e)
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
204 | [ApiResponseFor204](#delete3.ApiResponseFor204) | Replication connection deleted
400 | [ApiResponseFor400](#delete3.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#delete3.ApiResponseFor401) | Authentication required
403 | [ApiResponseFor403](#delete3.ApiResponseFor403) | Insufficient permissions
404 | [ApiResponseFor404](#delete3.ApiResponseFor404) | Replication connection not found

#### delete3.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete3.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete3.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete3.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete3.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **disable**
<a id="disable"></a>
> disable(repository_name)

Disable replication on a target repository..

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import replication_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = replication_api.ReplicationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Disable replication on a target repository..
        api_response = api_instance.disable(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling ReplicationApi->disable: %s\n" % e)
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
repositoryName | RepositoryNameSchema | | 

# RepositoryNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#disable.ApiResponseFor204) | Replication already disabled
400 | [ApiResponseFor400](#disable.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#disable.ApiResponseFor401) | Authentication required
403 | [ApiResponseFor403](#disable.ApiResponseFor403) | Insufficient permissions
404 | [ApiResponseFor404](#disable.ApiResponseFor404) | Repository not found

#### disable.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### disable.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### disable.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### disable.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### disable.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **enable**
<a id="enable"></a>
> enable()

Enable replication on a target repository.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import replication_api
from nexus_sdk.model.replication_enable_xo import ReplicationEnableXO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = replication_api.ReplicationApi(api_client)

    # example passing only optional values
    body = ReplicationEnableXO(
        target_repository_name="target_repository_name_example",
        replication_connection_name="replication_connection_name_example",
        source_repository_name="source_repository_name_example",
    )
    try:
        # Enable replication on a target repository.
        api_response = api_instance.enable(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling ReplicationApi->enable: %s\n" % e)
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
[**ReplicationEnableXO**](../../models/ReplicationEnableXO.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#enable.ApiResponseFor204) | Replication already enabled
400 | [ApiResponseFor400](#enable.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#enable.ApiResponseFor401) | Authentication required
403 | [ApiResponseFor403](#enable.ApiResponseFor403) | Insufficient permissions
404 | [ApiResponseFor404](#enable.ApiResponseFor404) | Repository not found

#### enable.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### enable.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### enable.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### enable.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### enable.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get4**
<a id="get4"></a>
> get4(name)

Fetch a replication connection.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import replication_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = replication_api.ReplicationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    try:
        # Fetch a replication connection.
        api_response = api_instance.get4(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling ReplicationApi->get4: %s\n" % e)
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
200 | [ApiResponseFor200](#get4.ApiResponseFor200) | Replication connection returned
400 | [ApiResponseFor400](#get4.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get4.ApiResponseFor401) | Authentication required
403 | [ApiResponseFor403](#get4.ApiResponseFor403) | Insufficient permissions
404 | [ApiResponseFor404](#get4.ApiResponseFor404) | Replication connection not found

#### get4.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get4.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get4.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get4.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get4.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update2**
<a id="update2"></a>
> update2(name)

Update a replication connection.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import replication_api
from nexus_sdk.model.replication_connection_xo import ReplicationConnectionXO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = replication_api.ReplicationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    try:
        # Update a replication connection.
        api_response = api_instance.update2(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling ReplicationApi->update2: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
    }
    body = ReplicationConnectionXO(
        id="id_example",
        name="name_example",
        source_repository_name="maven-releases",
        destination_instance_url="https://example.com/",
        destination_instance_username="admin",
        destination_instance_password="admin123",
        destination_repository_name="maven-releases",
        content_regexes=[
            "content_regexes_example"
        ],
        include_existing_content=True,
        use_trust_store=True,
    )
    try:
        # Update a replication connection.
        api_response = api_instance.update2(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling ReplicationApi->update2: %s\n" % e)
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
[**ReplicationConnectionXO**](../../models/ReplicationConnectionXO.md) |  | 


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
204 | [ApiResponseFor204](#update2.ApiResponseFor204) | Replication connection updated
400 | [ApiResponseFor400](#update2.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#update2.ApiResponseFor401) | Authentication required
403 | [ApiResponseFor403](#update2.ApiResponseFor403) | Insufficient permissions
404 | [ApiResponseFor404](#update2.ApiResponseFor404) | Replication connection not found

#### update2.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update2.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update2.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update2.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update2.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

