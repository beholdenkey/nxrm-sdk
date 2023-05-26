<a id="__pageTop"></a>
# nexus_sdk.apis.tags.manage_iq_server_configuration_api.ManageIQServerConfigurationApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disable_iq**](#disable_iq) | **post** /v1/iq/disable | Disable IQ server
[**enable_iq**](#enable_iq) | **post** /v1/iq/enable | Enable IQ server
[**get_configuration**](#get_configuration) | **get** /v1/iq | Get IQ server configuration
[**update_configuration**](#update_configuration) | **put** /v1/iq | Update IQ server configuration
[**verify_connection**](#verify_connection) | **post** /v1/iq/verify-connection | Verify IQ server connection

# **disable_iq**
<a id="disable_iq"></a>
> disable_iq()

Disable IQ server

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import manage_iq_server_configuration_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = manage_iq_server_configuration_api.ManageIQServerConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Disable IQ server
        api_response = api_instance.disable_iq()
    except nexus_sdk.ApiException as e:
        print("Exception when calling ManageIQServerConfigurationApi->disable_iq: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#disable_iq.ApiResponseFor204) | IQ server has been disabled
400 | [ApiResponseFor400](#disable_iq.ApiResponseFor400) | IQ server connection not configured

#### disable_iq.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### disable_iq.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **enable_iq**
<a id="enable_iq"></a>
> enable_iq()

Enable IQ server

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import manage_iq_server_configuration_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = manage_iq_server_configuration_api.ManageIQServerConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Enable IQ server
        api_response = api_instance.enable_iq()
    except nexus_sdk.ApiException as e:
        print("Exception when calling ManageIQServerConfigurationApi->enable_iq: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#enable_iq.ApiResponseFor204) | IQ server has been enabled
400 | [ApiResponseFor400](#enable_iq.ApiResponseFor400) | IQ server connection not configured

#### enable_iq.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### enable_iq.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_configuration**
<a id="get_configuration"></a>
> get_configuration()

Get IQ server configuration

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import manage_iq_server_configuration_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = manage_iq_server_configuration_api.ManageIQServerConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get IQ server configuration
        api_response = api_instance.get_configuration()
    except nexus_sdk.ApiException as e:
        print("Exception when calling ManageIQServerConfigurationApi->get_configuration: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_configuration.ApiResponseFor200) | IQ server configuration returned

#### get_configuration.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_configuration**
<a id="update_configuration"></a>
> update_configuration()

Update IQ server configuration

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import manage_iq_server_configuration_api
from nexus_sdk.model.iq_connection_xo import IqConnectionXo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = manage_iq_server_configuration_api.ManageIQServerConfigurationApi(api_client)

    # example passing only optional values
    body = IqConnectionXo(
        enabled=True,
        show_link=True,
        url="url_example",
        authentication_type="USER",
        username="username_example",
        password="password_example",
        use_trust_store_for_url=True,
        timeout_seconds=1,
        properties="properties_example",
    )
    try:
        # Update IQ server configuration
        api_response = api_instance.update_configuration(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling ManageIQServerConfigurationApi->update_configuration: %s\n" % e)
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
[**IqConnectionXo**](../../models/IqConnectionXo.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#update_configuration.ApiResponseFor204) | IQ server configuration has been updated

#### update_configuration.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **verify_connection**
<a id="verify_connection"></a>
> verify_connection()

Verify IQ server connection

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import manage_iq_server_configuration_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = manage_iq_server_configuration_api.ManageIQServerConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Verify IQ server connection
        api_response = api_instance.verify_connection()
    except nexus_sdk.ApiException as e:
        print("Exception when calling ManageIQServerConfigurationApi->verify_connection: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#verify_connection.ApiResponseFor200) | Connection verification complete, check response body for result

#### verify_connection.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

