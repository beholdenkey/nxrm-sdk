<a id="__pageTop"></a>
# nexus_sdk.apis.tags.security_atlassian_crowd_api.SecurityAtlassianCrowdApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_cache**](#clear_cache) | **post** /v1/security/atlassian-crowd/clear-cache | Clear Atlassian Crowd cache
[**read_settings**](#read_settings) | **get** /v1/security/atlassian-crowd | Retrieve Atlassian Crowd settings configured in Nexus Repository Manager
[**update_settings**](#update_settings) | **put** /v1/security/atlassian-crowd | Update Atlassian Crowd settings configured in Nexus Repository Manager
[**verify_connection1**](#verify_connection1) | **post** /v1/security/atlassian-crowd/verify-connection | Verify connection using supplied Atlassian Crowd settings

# **clear_cache**
<a id="clear_cache"></a>
> clear_cache()

Clear Atlassian Crowd cache

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_atlassian_crowd_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_atlassian_crowd_api.SecurityAtlassianCrowdApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Clear Atlassian Crowd cache
        api_response = api_instance.clear_cache()
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityAtlassianCrowdApi->clear_cache: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#clear_cache.ApiResponseFor204) | Atlassian Crowd cache has been cleared
401 | [ApiResponseFor401](#clear_cache.ApiResponseFor401) | Authentication required
403 | [ApiResponseFor403](#clear_cache.ApiResponseFor403) | Insufficient permissions

#### clear_cache.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clear_cache.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clear_cache.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **read_settings**
<a id="read_settings"></a>
> read_settings()

Retrieve Atlassian Crowd settings configured in Nexus Repository Manager

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_atlassian_crowd_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_atlassian_crowd_api.SecurityAtlassianCrowdApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve Atlassian Crowd settings configured in Nexus Repository Manager
        api_response = api_instance.read_settings()
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityAtlassianCrowdApi->read_settings: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#read_settings.ApiResponseFor200) | Atlassian Crowd settings returned
401 | [ApiResponseFor401](#read_settings.ApiResponseFor401) | Authentication required
403 | [ApiResponseFor403](#read_settings.ApiResponseFor403) | Insufficient permissions

#### read_settings.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### read_settings.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### read_settings.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_settings**
<a id="update_settings"></a>
> update_settings()

Update Atlassian Crowd settings configured in Nexus Repository Manager

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_atlassian_crowd_api
from nexus_sdk.model.crowd_api_xo import CrowdApiXO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_atlassian_crowd_api.SecurityAtlassianCrowdApi(api_client)

    # example passing only optional values
    body = CrowdApiXO(
        enabled=True,
        realm_active=True,
        application_name="application_name_example",
        application_password="application_password_example",
        url="url_example",
        use_trust_store_for_url=True,
        timeout=1,
    )
    try:
        # Update Atlassian Crowd settings configured in Nexus Repository Manager
        api_response = api_instance.update_settings(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityAtlassianCrowdApi->update_settings: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody, Unset] | optional, default is unset |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody
Type | Description  | Notes
------------- | ------------- | -------------
[**CrowdApiXO**](../../models/CrowdApiXO.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_settings.ApiResponseFor200) | Atlassian Crowd settings updated
401 | [ApiResponseFor401](#update_settings.ApiResponseFor401) | Authentication required
403 | [ApiResponseFor403](#update_settings.ApiResponseFor403) | Insufficient permissions

#### update_settings.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_settings.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_settings.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **verify_connection1**
<a id="verify_connection1"></a>
> verify_connection1()

Verify connection using supplied Atlassian Crowd settings

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_atlassian_crowd_api
from nexus_sdk.model.crowd_api_xo import CrowdApiXO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_atlassian_crowd_api.SecurityAtlassianCrowdApi(api_client)

    # example passing only optional values
    body = CrowdApiXO(
        enabled=True,
        realm_active=True,
        application_name="application_name_example",
        application_password="application_password_example",
        url="url_example",
        use_trust_store_for_url=True,
        timeout=1,
    )
    try:
        # Verify connection using supplied Atlassian Crowd settings
        api_response = api_instance.verify_connection1(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityAtlassianCrowdApi->verify_connection1: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody, Unset] | optional, default is unset |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody
Type | Description  | Notes
------------- | ------------- | -------------
[**CrowdApiXO**](../../models/CrowdApiXO.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#verify_connection1.ApiResponseFor204) | Atlassian Crowd connection was successful
400 | [ApiResponseFor400](#verify_connection1.ApiResponseFor400) | Atlassian Crowd connection failed
401 | [ApiResponseFor401](#verify_connection1.ApiResponseFor401) | Authentication required
403 | [ApiResponseFor403](#verify_connection1.ApiResponseFor403) | Insufficient permissions

#### verify_connection1.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### verify_connection1.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### verify_connection1.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### verify_connection1.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

