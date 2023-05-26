<a id="__pageTop"></a>
# nexus_sdk.apis.tags.email_api.EmailApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_email_configuration**](#delete_email_configuration) | **delete** /v1/email | Disable and clear the email configuration
[**get_email_configuration**](#get_email_configuration) | **get** /v1/email | Retrieve the current email configuration
[**set_email_configuration**](#set_email_configuration) | **put** /v1/email | Set the current email configuration
[**test_email_configuration**](#test_email_configuration) | **post** /v1/email/verify | Send a test email to the email address provided in the request body

# **delete_email_configuration**
<a id="delete_email_configuration"></a>
> delete_email_configuration()

Disable and clear the email configuration

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import email_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = email_api.EmailApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Disable and clear the email configuration
        api_response = api_instance.delete_email_configuration()
    except nexus_sdk.ApiException as e:
        print("Exception when calling EmailApi->delete_email_configuration: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_email_configuration.ApiResponseFor204) | Email configuration was successfully cleared

#### delete_email_configuration.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_email_configuration**
<a id="get_email_configuration"></a>
> ApiEmailConfiguration get_email_configuration()

Retrieve the current email configuration

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import email_api
from nexus_sdk.model.api_email_configuration import ApiEmailConfiguration
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = email_api.EmailApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve the current email configuration
        api_response = api_instance.get_email_configuration()
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling EmailApi->get_email_configuration: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_email_configuration.ApiResponseFor200) | successful operation
403 | [ApiResponseFor403](#get_email_configuration.ApiResponseFor403) | Insufficient permissions to retrieve the email configuration

#### get_email_configuration.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiEmailConfiguration**](../../models/ApiEmailConfiguration.md) |  | 


#### get_email_configuration.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **set_email_configuration**
<a id="set_email_configuration"></a>
> set_email_configuration(body)

Set the current email configuration

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import email_api
from nexus_sdk.model.api_email_configuration import ApiEmailConfiguration
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = email_api.EmailApi(api_client)

    # example passing only required values which don't have defaults set
    body = ApiEmailConfiguration(
        enabled=True,
        host="host_example",
        port=1,
        username="username_example",
        password="password_example",
        from_address="nexus@example.org",
        subject_prefix="subject_prefix_example",
        start_tls_enabled=True,
        start_tls_required=True,
        ssl_on_connect_enabled=True,
        ssl_server_identity_check_enabled=True,
        nexus_trust_store_enabled=True,
    )
    try:
        # Set the current email configuration
        api_response = api_instance.set_email_configuration(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling EmailApi->set_email_configuration: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody] | required |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiEmailConfiguration**](../../models/ApiEmailConfiguration.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#set_email_configuration.ApiResponseFor204) | Email configuration was successfully updated
400 | [ApiResponseFor400](#set_email_configuration.ApiResponseFor400) | Invalid request
403 | [ApiResponseFor403](#set_email_configuration.ApiResponseFor403) | Insufficient permissions to update the email configuration

#### set_email_configuration.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_email_configuration.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_email_configuration.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **test_email_configuration**
<a id="test_email_configuration"></a>
> ApiEmailValidation test_email_configuration(body)

Send a test email to the email address provided in the request body

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import email_api
from nexus_sdk.model.api_email_validation import ApiEmailValidation
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = email_api.EmailApi(api_client)

    # example passing only required values which don't have defaults set
    body = "body_example"
    try:
        # Send a test email to the email address provided in the request body
        api_response = api_instance.test_email_configuration(
            body=body,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling EmailApi->test_email_configuration: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody] | required |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#test_email_configuration.ApiResponseFor200) | Validation was complete, look at the body to determine success
403 | [ApiResponseFor403](#test_email_configuration.ApiResponseFor403) | Insufficient permissions to verify the email configuration

#### test_email_configuration.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiEmailValidation**](../../models/ApiEmailValidation.md) |  | 


#### test_email_configuration.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

