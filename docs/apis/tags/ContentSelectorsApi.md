<a id="__pageTop"></a>
# nexus_sdk.apis.tags.content_selectors_api.ContentSelectorsApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_content_selector**](#create_content_selector) | **post** /v1/security/content-selectors | Create a new content selector
[**delete_content_selector**](#delete_content_selector) | **delete** /v1/security/content-selectors/{name} | Delete a content selector
[**get_content_selector**](#get_content_selector) | **get** /v1/security/content-selectors/{name} | Get a content selector by name
[**get_content_selectors**](#get_content_selectors) | **get** /v1/security/content-selectors | List content selectors
[**update_content_selector**](#update_content_selector) | **put** /v1/security/content-selectors/{name} | Update a content selector

# **create_content_selector**
<a id="create_content_selector"></a>
> create_content_selector()

Create a new content selector

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import content_selectors_api
from nexus_sdk.model.content_selector_api_create_request import ContentSelectorApiCreateRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = content_selectors_api.ContentSelectorsApi(api_client)

    # example passing only optional values
    body = ContentSelectorApiCreateRequest(
        name="e6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        description="description_example",
        expression="format == \"maven2\" and path =^ \"/org/sonatype/nexus\"",
    )
    try:
        # Create a new content selector
        api_response = api_instance.create_content_selector(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling ContentSelectorsApi->create_content_selector: %s\n" % e)
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
[**ContentSelectorApiCreateRequest**](../../models/ContentSelectorApiCreateRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#create_content_selector.ApiResponseFor204) | Content selector successfully created
400 | [ApiResponseFor400](#create_content_selector.ApiResponseFor400) | Invalid request
403 | [ApiResponseFor403](#create_content_selector.ApiResponseFor403) | Insufficient permissions to create content selectors

#### create_content_selector.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_content_selector.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_content_selector.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_content_selector**
<a id="delete_content_selector"></a>
> delete_content_selector(name)

Delete a content selector

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import content_selectors_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = content_selectors_api.ContentSelectorsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    try:
        # Delete a content selector
        api_response = api_instance.delete_content_selector(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling ContentSelectorsApi->delete_content_selector: %s\n" % e)
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
204 | [ApiResponseFor204](#delete_content_selector.ApiResponseFor204) | Content selector deleted successfully
400 | [ApiResponseFor400](#delete_content_selector.ApiResponseFor400) | Invalid request
403 | [ApiResponseFor403](#delete_content_selector.ApiResponseFor403) | Insufficient permissions to delete the content selector

#### delete_content_selector.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_content_selector.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_content_selector.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_content_selector**
<a id="get_content_selector"></a>
> ContentSelectorApiResponse get_content_selector(name)

Get a content selector by name

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import content_selectors_api
from nexus_sdk.model.content_selector_api_response import ContentSelectorApiResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = content_selectors_api.ContentSelectorsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    try:
        # Get a content selector by name
        api_response = api_instance.get_content_selector(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling ContentSelectorsApi->get_content_selector: %s\n" % e)
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
200 | [ApiResponseFor200](#get_content_selector.ApiResponseFor200) | successful operation
403 | [ApiResponseFor403](#get_content_selector.ApiResponseFor403) | Insufficient permissions to read the content selector

#### get_content_selector.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ContentSelectorApiResponse**](../../models/ContentSelectorApiResponse.md) |  | 


#### get_content_selector.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_content_selectors**
<a id="get_content_selectors"></a>
> [ContentSelectorApiResponse] get_content_selectors()

List content selectors

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import content_selectors_api
from nexus_sdk.model.content_selector_api_response import ContentSelectorApiResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = content_selectors_api.ContentSelectorsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List content selectors
        api_response = api_instance.get_content_selectors()
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling ContentSelectorsApi->get_content_selectors: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_content_selectors.ApiResponseFor200) | successful operation
403 | [ApiResponseFor403](#get_content_selectors.ApiResponseFor403) | Insufficient permissions to read content selectors

#### get_content_selectors.ApiResponseFor200
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
[**ContentSelectorApiResponse**]({{complexTypePrefix}}ContentSelectorApiResponse.md) | [**ContentSelectorApiResponse**]({{complexTypePrefix}}ContentSelectorApiResponse.md) | [**ContentSelectorApiResponse**]({{complexTypePrefix}}ContentSelectorApiResponse.md) |  | 

#### get_content_selectors.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_content_selector**
<a id="update_content_selector"></a>
> update_content_selector(name)

Update a content selector

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import content_selectors_api
from nexus_sdk.model.content_selector_api_update_request import ContentSelectorApiUpdateRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = content_selectors_api.ContentSelectorsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    try:
        # Update a content selector
        api_response = api_instance.update_content_selector(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling ContentSelectorsApi->update_content_selector: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
    }
    body = ContentSelectorApiUpdateRequest(
        description="description_example",
        expression="format == \"maven2\" and path =^ \"/org/sonatype/nexus\"",
    )
    try:
        # Update a content selector
        api_response = api_instance.update_content_selector(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling ContentSelectorsApi->update_content_selector: %s\n" % e)
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
[**ContentSelectorApiUpdateRequest**](../../models/ContentSelectorApiUpdateRequest.md) |  | 


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
204 | [ApiResponseFor204](#update_content_selector.ApiResponseFor204) | Content selector updated successfully
400 | [ApiResponseFor400](#update_content_selector.ApiResponseFor400) | Invalid request
403 | [ApiResponseFor403](#update_content_selector.ApiResponseFor403) | Insufficient permissions to update the content selector

#### update_content_selector.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_content_selector.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_content_selector.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

