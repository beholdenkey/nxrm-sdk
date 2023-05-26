<a id="__pageTop"></a>
# nexus_sdk.apis.tags.security_management_anonymous_access_api.SecurityManagementAnonymousAccessApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read**](#read) | **get** /v1/security/anonymous | Get Anonymous Access settings
[**update**](#update) | **put** /v1/security/anonymous | Update Anonymous Access settings

# **read**
<a id="read"></a>
> AnonymousAccessSettingsXO read()

Get Anonymous Access settings

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_anonymous_access_api
from nexus_sdk.model.anonymous_access_settings_xo import AnonymousAccessSettingsXO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_anonymous_access_api.SecurityManagementAnonymousAccessApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Anonymous Access settings
        api_response = api_instance.read()
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementAnonymousAccessApi->read: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#read.ApiResponseFor200) | successful operation
403 | [ApiResponseFor403](#read.ApiResponseFor403) | Insufficient permissions to update settings

#### read.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AnonymousAccessSettingsXO**](../../models/AnonymousAccessSettingsXO.md) |  | 


#### read.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update**
<a id="update"></a>
> AnonymousAccessSettingsXO update()

Update Anonymous Access settings

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_anonymous_access_api
from nexus_sdk.model.anonymous_access_settings_xo import AnonymousAccessSettingsXO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_anonymous_access_api.SecurityManagementAnonymousAccessApi(api_client)

    # example passing only optional values
    body = AnonymousAccessSettingsXO(
        enabled=True,
        user_id="user_id_example",
        realm_name="realm_name_example",
    )
    try:
        # Update Anonymous Access settings
        api_response = api_instance.update(
            body=body,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementAnonymousAccessApi->update: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AnonymousAccessSettingsXO**](../../models/AnonymousAccessSettingsXO.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update.ApiResponseFor200) | successful operation
403 | [ApiResponseFor403](#update.ApiResponseFor403) | Insufficient permissions to update settings

#### update.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AnonymousAccessSettingsXO**](../../models/AnonymousAccessSettingsXO.md) |  | 


#### update.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

