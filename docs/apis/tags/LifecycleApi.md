<a id="__pageTop"></a>
# nexus_sdk.apis.tags.lifecycle_api.LifecycleApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bounce**](#bounce) | **put** /v1/lifecycle/bounce | Bounce lifecycle phase
[**get_phase**](#get_phase) | **get** /v1/lifecycle/phase | Get current lifecycle phase
[**set_phase**](#set_phase) | **put** /v1/lifecycle/phase | Move to new lifecycle phase

# **bounce**
<a id="bounce"></a>
> bounce()

Bounce lifecycle phase

Re-runs all phases from the given phase to the current phase

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import lifecycle_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lifecycle_api.LifecycleApi(api_client)

    # example passing only optional values
    body = "body_example"
    try:
        # Bounce lifecycle phase
        api_response = api_instance.bounce(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling LifecycleApi->bounce: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyTextPlain, Unset] | optional, default is unset |
content_type | str | optional, default is 'text/plain' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#bounce.ApiResponseForDefault) | successful operation

#### bounce.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_phase**
<a id="get_phase"></a>
> str get_phase()

Get current lifecycle phase

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import lifecycle_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lifecycle_api.LifecycleApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get current lifecycle phase
        api_response = api_instance.get_phase()
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling LifecycleApi->get_phase: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_phase.ApiResponseFor200) | successful operation

#### get_phase.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **set_phase**
<a id="set_phase"></a>
> set_phase()

Move to new lifecycle phase

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import lifecycle_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lifecycle_api.LifecycleApi(api_client)

    # example passing only optional values
    body = "body_example"
    try:
        # Move to new lifecycle phase
        api_response = api_instance.set_phase(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling LifecycleApi->set_phase: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyTextPlain, Unset] | optional, default is unset |
content_type | str | optional, default is 'text/plain' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#set_phase.ApiResponseForDefault) | successful operation

#### set_phase.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

