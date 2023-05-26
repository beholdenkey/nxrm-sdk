<a id="__pageTop"></a>

# nexus_sdk.apis.tags.status_api.StatusApi

All URIs are relative to _http://localhost/service/rest_

| Method                                                    | HTTP request                | Description                                                                        |
| --------------------------------------------------------- | --------------------------- | ---------------------------------------------------------------------------------- |
| [**get_system_status_checks**](#get_system_status_checks) | **get** /v1/status/check    | Health check endpoint that returns the results of the system status checks         |
| [**is_available**](#is_available)                         | **get** /v1/status          | Health check endpoint that validates server can respond to read requests           |
| [**is_writable**](#is_writable)                           | **get** /v1/status/writable | Health check endpoint that validates server can respond to read and write requests |

# **get_system_status_checks**

<a id="get_system_status_checks"></a>

> {str: (Result,)} get_system_status_checks()

Health check endpoint that returns the results of the system status checks

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import status_api
from nexus_sdk.model.result import Result
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = status_api.StatusApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Health check endpoint that returns the results of the system status checks
        api_response = api_instance.get_system_status_checks()
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling StatusApi->get_system_status_checks: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return Types, Responses

| Code | Class                                                            | Description                                                 |
| ---- | ---------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                     | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_system_status_checks.ApiResponseFor200) | The system status check results                             |

#### get_system_status_checks.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                 | Input Type                                   | Accessed Type                                | Description                                                        | Notes      |
| ------------------- | -------------------------------------------- | -------------------------------------------- | ------------------------------------------------------------------ | ---------- |
| **any_string_name** | [**Result**]({{complexTypePrefix}}Result.md) | [**Result**]({{complexTypePrefix}}Result.md) | any string name can be used but the value must be the correct type | [optional] |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **is_available**

<a id="is_available"></a>

> is_available()

Health check endpoint that validates server can respond to read requests

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import status_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = status_api.StatusApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Health check endpoint that validates server can respond to read requests
        api_response = api_instance.is_available()
    except nexus_sdk.ApiException as e:
        print("Exception when calling StatusApi->is_available: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return Types, Responses

| Code | Class                                                | Description                                                 |
| ---- | ---------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization         | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#is_available.ApiResponseFor200) | Available to service requests                               |
| 503  | [ApiResponseFor503](#is_available.ApiResponseFor503) | Unavailable to service requests                             |

#### is_available.ApiResponseFor200

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### is_available.ApiResponseFor503

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **is_writable**

<a id="is_writable"></a>

> is_writable()

Health check endpoint that validates server can respond to read and write requests

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import status_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = status_api.StatusApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Health check endpoint that validates server can respond to read and write requests
        api_response = api_instance.is_writable()
    except nexus_sdk.ApiException as e:
        print("Exception when calling StatusApi->is_writable: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return Types, Responses

| Code | Class                                               | Description                                                 |
| ---- | --------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization        | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#is_writable.ApiResponseFor200) | Available to service requests                               |
| 503  | [ApiResponseFor503](#is_writable.ApiResponseFor503) | Unavailable to service requests                             |

#### is_writable.ApiResponseFor200

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### is_writable.ApiResponseFor503

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
