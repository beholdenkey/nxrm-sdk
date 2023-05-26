<a id="__pageTop"></a>

# nexus_sdk.apis.tags.security_management_api.SecurityManagementApi

All URIs are relative to _http://localhost/service/rest_

| Method                                    | HTTP request                      | Description                                    |
| ----------------------------------------- | --------------------------------- | ---------------------------------------------- |
| [**get_user_sources**](#get_user_sources) | **get** /v1/security/user-sources | Retrieve a list of the available user sources. |

# **get_user_sources**

<a id="get_user_sources"></a>

> [ApiUserSource] get_user_sources()

Retrieve a list of the available user sources.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_api
from nexus_sdk.model.api_user_source import ApiUserSource
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_api.SecurityManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve a list of the available user sources.
        api_response = api_instance.get_user_sources()
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementApi->get_user_sources: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_user_sources.ApiResponseFor200) | successful operation                                        |
| 403  | [ApiResponseFor403](#get_user_sources.ApiResponseFor403) | The user does not have permission to perform the operation. |

#### get_user_sources.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                                                 | Input Type                                                 | Accessed Type                                              | Description | Notes |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ----------- | ----- |
| [**ApiUserSource**]({{complexTypePrefix}}ApiUserSource.md) | [**ApiUserSource**]({{complexTypePrefix}}ApiUserSource.md) | [**ApiUserSource**]({{complexTypePrefix}}ApiUserSource.md) |             |

#### get_user_sources.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
