<a id="__pageTop"></a>
# nexus_sdk.apis.tags.security_management_realms_api.SecurityManagementRealmsApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_active_realms**](#get_active_realms) | **get** /v1/security/realms/active | List the active realm IDs in order
[**get_realms**](#get_realms) | **get** /v1/security/realms/available | List the available realms
[**set_active_realms**](#set_active_realms) | **put** /v1/security/realms/active | Set the active security realms in the order they should be used

# **get_active_realms**
<a id="get_active_realms"></a>
> [str] get_active_realms()

List the active realm IDs in order

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_realms_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_realms_api.SecurityManagementRealmsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List the active realm IDs in order
        api_response = api_instance.get_active_realms()
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementRealmsApi->get_active_realms: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_active_realms.ApiResponseFor200) | successful operation

#### get_active_realms.ApiResponseFor200
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
items | str,  | str,  |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_realms**
<a id="get_realms"></a>
> [RealmApiXO] get_realms()

List the available realms

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_realms_api
from nexus_sdk.model.realm_api_xo import RealmApiXO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_realms_api.SecurityManagementRealmsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List the available realms
        api_response = api_instance.get_realms()
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementRealmsApi->get_realms: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_realms.ApiResponseFor200) | successful operation

#### get_realms.ApiResponseFor200
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
[**RealmApiXO**]({{complexTypePrefix}}RealmApiXO.md) | [**RealmApiXO**]({{complexTypePrefix}}RealmApiXO.md) | [**RealmApiXO**]({{complexTypePrefix}}RealmApiXO.md) |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **set_active_realms**
<a id="set_active_realms"></a>
> set_active_realms()

Set the active security realms in the order they should be used

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_realms_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_realms_api.SecurityManagementRealmsApi(api_client)

    # example passing only optional values
    body = [
        "body_example"
    ]
    try:
        # Set the active security realms in the order they should be used
        api_response = api_instance.set_active_realms(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementRealmsApi->set_active_realms: %s\n" % e)
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
default | [ApiResponseForDefault](#set_active_realms.ApiResponseForDefault) | successful operation

#### set_active_realms.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

