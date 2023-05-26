<a id="__pageTop"></a>

# nexus_sdk.apis.tags.script_api.ScriptApi

All URIs are relative to _http://localhost/service/rest_

| Method                  | HTTP request                   | Description                  |
| ----------------------- | ------------------------------ | ---------------------------- |
| [**add**](#add)         | **post** /v1/script            | Add a new script             |
| [**browse**](#browse)   | **get** /v1/script             | List all stored scripts      |
| [**delete1**](#delete1) | **delete** /v1/script/{name}   | Delete stored script by name |
| [**edit**](#edit)       | **put** /v1/script/{name}      | Update stored script by name |
| [**read1**](#read1)     | **get** /v1/script/{name}      | Read stored script by name   |
| [**run1**](#run1)       | **post** /v1/script/{name}/run | Run stored script by name    |

# **add**

<a id="add"></a>

> add()

Add a new script

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import script_api
from nexus_sdk.model.script_xo import ScriptXO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = script_api.ScriptApi(api_client)

    # example passing only optional values
    body = ScriptXO(
        name="e6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        content="content_example",
        type="type_example",
    )
    try:
        # Add a new script
        api_response = api_instance.add(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling ScriptApi->add: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                     | Description | Notes |
| ---------------------------------------- | ----------- | ----- |
| [**ScriptXO**](../../models/ScriptXO.md) |             |

### Return Types, Responses

| Code | Class                                        | Description                                                 |
| ---- | -------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#add.ApiResponseFor204)  | Script was added                                            |
| 410  | [ApiResponseFor410](#add.ApiResponseFor410)  | Script creation is disabled                                 |

#### add.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### add.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **browse**

<a id="browse"></a>

> [ScriptXO] browse()

List all stored scripts

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import script_api
from nexus_sdk.model.script_xo import ScriptXO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = script_api.ScriptApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List all stored scripts
        api_response = api_instance.browse()
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling ScriptApi->browse: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return Types, Responses

| Code | Class                                          | Description                                                 |
| ---- | ---------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization   | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#browse.ApiResponseFor200) | successful operation                                        |

#### browse.ApiResponseFor200

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

| Class Name                                       | Input Type                                       | Accessed Type                                    | Description | Notes |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ----------- | ----- |
| [**ScriptXO**]({{complexTypePrefix}}ScriptXO.md) | [**ScriptXO**]({{complexTypePrefix}}ScriptXO.md) | [**ScriptXO**]({{complexTypePrefix}}ScriptXO.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete1**

<a id="delete1"></a>

> delete1(name)

Delete stored script by name

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import script_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = script_api.ScriptApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    try:
        # Delete stored script by name
        api_response = api_instance.delete1(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling ScriptApi->delete1: %s\n" % e)
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

| Name | Type       | Description | Notes |
| ---- | ---------- | ----------- | ----- |
| name | NameSchema |             |

# NameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                           | Description                                                 |
| ---- | ----------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization    | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#delete1.ApiResponseFor204) | Script was deleted                                          |
| 404  | [ApiResponseFor404](#delete1.ApiResponseFor404) | No script with the specified name                           |

#### delete1.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete1.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edit**

<a id="edit"></a>

> edit(name)

Update stored script by name

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import script_api
from nexus_sdk.model.script_xo import ScriptXO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = script_api.ScriptApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    try:
        # Update stored script by name
        api_response = api_instance.edit(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling ScriptApi->edit: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
    }
    body = ScriptXO(
        name="e6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        content="content_example",
        type="type_example",
    )
    try:
        # Update stored script by name
        api_response = api_instance.edit(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling ScriptApi->edit: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                     | Description | Notes |
| ---------------------------------------- | ----------- | ----- |
| [**ScriptXO**](../../models/ScriptXO.md) |             |

### path_params

#### RequestPathParams

| Name | Type       | Description | Notes |
| ---- | ---------- | ----------- | ----- |
| name | NameSchema |             |

# NameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                        | Description                                                 |
| ---- | -------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#edit.ApiResponseFor204) | Script was updated                                          |
| 404  | [ApiResponseFor404](#edit.ApiResponseFor404) | No script with the specified name                           |
| 410  | [ApiResponseFor410](#edit.ApiResponseFor410) | Script updating is disabled                                 |

#### edit.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **read1**

<a id="read1"></a>

> ScriptXO read1(name)

Read stored script by name

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import script_api
from nexus_sdk.model.script_xo import ScriptXO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = script_api.ScriptApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    try:
        # Read stored script by name
        api_response = api_instance.read1(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling ScriptApi->read1: %s\n" % e)
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

| Name | Type       | Description | Notes |
| ---- | ---------- | ----------- | ----- |
| name | NameSchema |             |

# NameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                         | Description                                                 |
| ---- | --------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization  | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#read1.ApiResponseFor200) | successful operation                                        |
| 404  | [ApiResponseFor404](#read1.ApiResponseFor404) | No script with the specified name                           |

#### read1.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                     | Description | Notes |
| ---------------------------------------- | ----------- | ----- |
| [**ScriptXO**](../../models/ScriptXO.md) |             |

#### read1.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **run1**

<a id="run1"></a>

> ScriptResultXO run1(name)

Run stored script by name

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import script_api
from nexus_sdk.model.script_result_xo import ScriptResultXO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = script_api.ScriptApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    try:
        # Run stored script by name
        api_response = api_instance.run1(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling ScriptApi->run1: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
    }
    body = "body_example"
    try:
        # Run stored script by name
        api_response = api_instance.run1(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling ScriptApi->run1: %s\n" % e)
```

### Parameters

| Name                 | Type                                                                                    | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | --------------------------------------------------------------------------------------- | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyTextPlain, SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset        |
| path_params          | RequestPathParams                                                                       |                                   |
| content_type         | str                                                                                     | optional, default is 'text/plain' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                                                       | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                                                    | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]                                        | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                                                    | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyTextPlain

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# SchemaForRequestBodyApplicationJson

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### path_params

#### RequestPathParams

| Name | Type       | Description | Notes |
| ---- | ---------- | ----------- | ----- |
| name | NameSchema |             |

# NameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                        | Description                                                 |
| ---- | -------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#run1.ApiResponseFor200) | successful operation                                        |
| 404  | [ApiResponseFor404](#run1.ApiResponseFor404) | No script with the specified name                           |
| 500  | [ApiResponseFor500](#run1.ApiResponseFor500) | Script execution failed with exception                      |

#### run1.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                 | Description | Notes |
| ---------------------------------------------------- | ----------- | ----- |
| [**ScriptResultXO**](../../models/ScriptResultXO.md) |             |

#### run1.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### run1.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
