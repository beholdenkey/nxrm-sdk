<a id="__pageTop"></a>

# nexus_sdk.apis.tags.read_only_api.ReadOnlyApi

All URIs are relative to _http://localhost/service/rest_

| Method                              | HTTP request                         | Description                |
| ----------------------------------- | ------------------------------------ | -------------------------- |
| [**force_release**](#force_release) | **post** /v1/read-only/force-release | Forcibly release read-only |
| [**freeze**](#freeze)               | **post** /v1/read-only/freeze        | Enable read-only           |
| [**get**](#get)                     | **get** /v1/read-only                | Get read-only state        |
| [**release**](#release)             | **post** /v1/read-only/release       | Release read-only          |

# **force_release**

<a id="force_release"></a>

> force_release()

Forcibly release read-only

Forcibly release read-only status, including System initiated tasks. Warning: may result in data loss.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import read_only_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = read_only_api.ReadOnlyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Forcibly release read-only
        api_response = api_instance.force_release()
    except nexus_sdk.ApiException as e:
        print("Exception when calling ReadOnlyApi->force_release: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return Types, Responses

| Code | Class                                                 | Description                                                 |
| ---- | ----------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization          | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#force_release.ApiResponseFor204) | System is no longer read-only                               |
| 403  | [ApiResponseFor403](#force_release.ApiResponseFor403) | Authentication required                                     |
| 404  | [ApiResponseFor404](#force_release.ApiResponseFor404) | No change to read-only state                                |

#### force_release.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### force_release.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### force_release.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **freeze**

<a id="freeze"></a>

> freeze()

Enable read-only

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import read_only_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = read_only_api.ReadOnlyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Enable read-only
        api_response = api_instance.freeze()
    except nexus_sdk.ApiException as e:
        print("Exception when calling ReadOnlyApi->freeze: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return Types, Responses

| Code | Class                                          | Description                                                 |
| ---- | ---------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization   | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#freeze.ApiResponseFor204) | System is now read-only                                     |
| 403  | [ApiResponseFor403](#freeze.ApiResponseFor403) | Authentication required                                     |
| 404  | [ApiResponseFor404](#freeze.ApiResponseFor404) | No change to read-only state                                |

#### freeze.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### freeze.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### freeze.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get**

<a id="get"></a>

> ReadOnlyState get()

Get read-only state

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import read_only_api
from nexus_sdk.model.read_only_state import ReadOnlyState
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = read_only_api.ReadOnlyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get read-only state
        api_response = api_instance.get()
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling ReadOnlyApi->get: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return Types, Responses

| Code | Class                                        | Description                                                 |
| ---- | -------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get.ApiResponseFor200)  | successful operation                                        |

#### get.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                               | Description | Notes |
| -------------------------------------------------- | ----------- | ----- |
| [**ReadOnlyState**](../../models/ReadOnlyState.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **release**

<a id="release"></a>

> release()

Release read-only

Release administrator initiated read-only status. Will not release read-only caused by system tasks.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import read_only_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = read_only_api.ReadOnlyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Release read-only
        api_response = api_instance.release()
    except nexus_sdk.ApiException as e:
        print("Exception when calling ReadOnlyApi->release: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return Types, Responses

| Code | Class                                           | Description                                                 |
| ---- | ----------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization    | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#release.ApiResponseFor204) | System is no longer read-only                               |
| 403  | [ApiResponseFor403](#release.ApiResponseFor403) | Authentication required                                     |
| 404  | [ApiResponseFor404](#release.ApiResponseFor404) | No change to read-only state                                |

#### release.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### release.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### release.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
