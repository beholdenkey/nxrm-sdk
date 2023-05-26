<a id="__pageTop"></a>
# nexus_sdk.apis.tags.product_licensing_api.ProductLicensingApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_license_status**](#get_license_status) | **get** /v1/system/license | Get the current license status.
[**remove_license**](#remove_license) | **delete** /v1/system/license | Uninstall license if present.
[**set_license**](#set_license) | **post** /v1/system/license | Upload a new license file.

# **get_license_status**
<a id="get_license_status"></a>
> ApiLicenseDetailsXO get_license_status()

Get the current license status.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import product_licensing_api
from nexus_sdk.model.api_license_details_xo import ApiLicenseDetailsXO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product_licensing_api.ProductLicensingApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the current license status.
        api_response = api_instance.get_license_status()
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling ProductLicensingApi->get_license_status: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_license_status.ApiResponseFor200) | successful operation

#### get_license_status.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiLicenseDetailsXO**](../../models/ApiLicenseDetailsXO.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **remove_license**
<a id="remove_license"></a>
> remove_license()

Uninstall license if present.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import product_licensing_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product_licensing_api.ProductLicensingApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Uninstall license if present.
        api_response = api_instance.remove_license()
    except nexus_sdk.ApiException as e:
        print("Exception when calling ProductLicensingApi->remove_license: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#remove_license.ApiResponseForDefault) | successful operation

#### remove_license.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **set_license**
<a id="set_license"></a>
> ApiLicenseDetailsXO set_license()

Upload a new license file.

Server must be restarted to take effect

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import product_licensing_api
from nexus_sdk.model.api_license_details_xo import ApiLicenseDetailsXO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product_licensing_api.ProductLicensingApi(api_client)

    # example passing only optional values
    body = dict()
    try:
        # Upload a new license file.
        api_response = api_instance.set_license(
            body=body,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling ProductLicensingApi->set_license: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationOctetStream, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/octet-stream' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationOctetStream

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#set_license.ApiResponseFor200) | successful operation

#### set_license.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiLicenseDetailsXO**](../../models/ApiLicenseDetailsXO.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

