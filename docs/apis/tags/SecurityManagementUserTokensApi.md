<a id="__pageTop"></a>

# nexus_sdk.apis.tags.security_management_user_tokens_api.SecurityManagementUserTokensApi

All URIs are relative to _http://localhost/service/rest_

| Method                                              | HTTP request                        | Description                                         |
| --------------------------------------------------- | ----------------------------------- | --------------------------------------------------- |
| [**reset_all_user_tokens**](#reset_all_user_tokens) | **delete** /v1/security/user-tokens | Invalidate all existing user tokens.                |
| [**service_status**](#service_status)               | **get** /v1/security/user-tokens    | Show if the user token capability is enabled or not |
| [**set_service_status**](#set_service_status)       | **put** /v1/security/user-tokens    | Enable/Disable the user token capability            |

# **reset_all_user_tokens**

<a id="reset_all_user_tokens"></a>

> reset_all_user_tokens()

Invalidate all existing user tokens.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_user_tokens_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_user_tokens_api.SecurityManagementUserTokensApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Invalidate all existing user tokens.
        api_response = api_instance.reset_all_user_tokens()
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementUserTokensApi->reset_all_user_tokens: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return Types, Responses

| Code    | Class                                                                 | Description                                                 |
| ------- | --------------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a     | api_client.ApiResponseWithoutDeserialization                          | When skip_deserialization is True this response is returned |
| default | [ApiResponseForDefault](#reset_all_user_tokens.ApiResponseForDefault) | successful operation                                        |

#### reset_all_user_tokens.ApiResponseForDefault

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **service_status**

<a id="service_status"></a>

> UserTokensApiModel service_status()

Show if the user token capability is enabled or not

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_user_tokens_api
from nexus_sdk.model.user_tokens_api_model import UserTokensApiModel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_user_tokens_api.SecurityManagementUserTokensApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Show if the user token capability is enabled or not
        api_response = api_instance.service_status()
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementUserTokensApi->service_status: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return Types, Responses

| Code | Class                                                  | Description                                                 |
| ---- | ------------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization           | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#service_status.ApiResponseFor200) | successful operation                                        |

#### service_status.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                         | Description | Notes |
| ------------------------------------------------------------ | ----------- | ----- |
| [**UserTokensApiModel**](../../models/UserTokensApiModel.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **set_service_status**

<a id="set_service_status"></a>

> UserTokensApiModel set_service_status()

Enable/Disable the user token capability

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_user_tokens_api
from nexus_sdk.model.user_tokens_api_model import UserTokensApiModel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_user_tokens_api.SecurityManagementUserTokensApi(api_client)

    # example passing only optional values
    body = UserTokensApiModel(
        enabled=True,
        protect_content=True,
    )
    try:
        # Enable/Disable the user token capability
        api_response = api_instance.set_service_status(
            body=body,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementUserTokensApi->set_service_status: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                        | default is ('application/json', )       | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                         | Description | Notes |
| ------------------------------------------------------------ | ----------- | ----- |
| [**UserTokensApiModel**](../../models/UserTokensApiModel.md) |             |

### Return Types, Responses

| Code | Class                                                      | Description                                                 |
| ---- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization               | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#set_service_status.ApiResponseFor200) | successful operation                                        |

#### set_service_status.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                         | Description | Notes |
| ------------------------------------------------------------ | ----------- | ----- |
| [**UserTokensApiModel**](../../models/UserTokensApiModel.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
