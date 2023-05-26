<a id="__pageTop"></a>

# nexus_sdk.apis.tags.components_api.ComponentsApi

All URIs are relative to _http://localhost/service/rest_

| Method                                          | HTTP request                   | Description               |
| ----------------------------------------------- | ------------------------------ | ------------------------- |
| [**delete_component**](#delete_component)       | **delete** /v1/components/{id} | Delete a single component |
| [**get_component_by_id**](#get_component_by_id) | **get** /v1/components/{id}    | Get a single component    |
| [**get_components**](#get_components)           | **get** /v1/components         | List components           |
| [**upload_component**](#upload_component)       | **post** /v1/components        | Upload a single component |

# **delete_component**

<a id="delete_component"></a>

> delete_component(id)

Delete a single component

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import components_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = components_api.ComponentsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Delete a single component
        api_response = api_instance.delete_component(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling ComponentsApi->delete_component: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description      | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                  |
| stream               | bool                                             | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None  | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name | Type     | Description | Notes |
| ---- | -------- | ----------- | ----- |
| id   | IdSchema |             |

# IdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#delete_component.ApiResponseFor204) | Component was successfully deleted                          |
| 403  | [ApiResponseFor403](#delete_component.ApiResponseFor403) | Insufficient permissions to delete component                |
| 404  | [ApiResponseFor404](#delete_component.ApiResponseFor404) | Component not found                                         |
| 422  | [ApiResponseFor422](#delete_component.ApiResponseFor422) | Malformed ID                                                |

#### delete_component.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_component.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_component.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_component.ApiResponseFor422

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_component_by_id**

<a id="get_component_by_id"></a>

> ComponentXO get_component_by_id(id)

Get a single component

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import components_api
from nexus_sdk.model.component_xo import ComponentXO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = components_api.ComponentsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Get a single component
        api_response = api_instance.get_component_by_id(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling ComponentsApi->get_component_by_id: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name | Type     | Description | Notes |
| ---- | -------- | ----------- | ----- |
| id   | IdSchema |             |

# IdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_component_by_id.ApiResponseFor200) | successful operation                                        |
| 403  | [ApiResponseFor403](#get_component_by_id.ApiResponseFor403) | Insufficient permissions to get component                   |
| 404  | [ApiResponseFor404](#get_component_by_id.ApiResponseFor404) | Component not found                                         |
| 422  | [ApiResponseFor422](#get_component_by_id.ApiResponseFor422) | Malformed ID                                                |

#### get_component_by_id.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                           | Description | Notes |
| ---------------------------------------------- | ----------- | ----- |
| [**ComponentXO**](../../models/ComponentXO.md) |             |

#### get_component_by_id.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_component_by_id.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_component_by_id.ApiResponseFor422

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_components**

<a id="get_components"></a>

> PageComponentXO get_components(repository)

List components

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import components_api
from nexus_sdk.model.page_component_xo import PageComponentXO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = components_api.ComponentsApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'repository': "repository_example",
    }
    try:
        # List components
        api_response = api_instance.get_components(
            query_params=query_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling ComponentsApi->get_components: %s\n" % e)

    # example passing only optional values
    query_params = {
        'continuationToken': "continuationToken_example",
        'repository': "repository_example",
    }
    try:
        # List components
        api_response = api_instance.get_components(
            query_params=query_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling ComponentsApi->get_components: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| query_params         | RequestQueryParams                               |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### query_params

#### RequestQueryParams

| Name              | Type                    | Description | Notes    |
| ----------------- | ----------------------- | ----------- | -------- |
| continuationToken | ContinuationTokenSchema |             | optional |
| repository        | RepositorySchema        |             |

# ContinuationTokenSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# RepositorySchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                  | Description                                                 |
| ---- | ------------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization           | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_components.ApiResponseFor200) | successful operation                                        |
| 403  | [ApiResponseFor403](#get_components.ApiResponseFor403) | Insufficient permissions to list components                 |
| 422  | [ApiResponseFor422](#get_components.ApiResponseFor422) | Parameter &#x27;repository&#x27; is required                |

#### get_components.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                   | Description | Notes |
| ------------------------------------------------------ | ----------- | ----- |
| [**PageComponentXO**](../../models/PageComponentXO.md) |             |

#### get_components.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_components.ApiResponseFor422

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **upload_component**

<a id="upload_component"></a>

> upload_component(repository)

Upload a single component

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import components_api
from nexus_sdk.model.v1_components_body import V1ComponentsBody
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = components_api.ComponentsApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'repository': "repository_example",
    }
    try:
        # Upload a single component
        api_response = api_instance.upload_component(
            query_params=query_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling ComponentsApi->upload_component: %s\n" % e)

    # example passing only optional values
    query_params = {
        'repository': "repository_example",
    }
    body = None
    try:
        # Upload a single component
        api_response = api_instance.upload_component(
            query_params=query_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling ComponentsApi->upload_component: %s\n" % e)
```

### Parameters

| Name                 | Type                                                       | Description                                | Notes                                                                                                                                                                                              |
| -------------------- | ---------------------------------------------------------- | ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyMultipartFormData, Unset] | optional, default is unset                 |
| query_params         | RequestQueryParams                                         |                                            |
| content_type         | str                                                        | optional, default is 'multipart/form-data' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                       | default is False                           | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]           | default is None                            | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                       | default is False                           | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyMultipartFormData

| Type                                                     | Description | Notes |
| -------------------------------------------------------- | ----------- | ----- |
| [**V1ComponentsBody**](../../models/V1ComponentsBody.md) |             |

### query_params

#### RequestQueryParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| repository | RepositorySchema |             |

# RepositorySchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 403  | [ApiResponseFor403](#upload_component.ApiResponseFor403) | Insufficient permissions to upload a component              |
| 422  | [ApiResponseFor422](#upload_component.ApiResponseFor422) | Parameter &#x27;repository&#x27; is required                |

#### upload_component.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_component.ApiResponseFor422

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
