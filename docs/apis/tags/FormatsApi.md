<a id="__pageTop"></a>

# nexus_sdk.apis.tags.formats_api.FormatsApi

All URIs are relative to _http://localhost/service/rest_

| Method            | HTTP request                              | Description                                             |
| ----------------- | ----------------------------------------- | ------------------------------------------------------- |
| [**get1**](#get1) | **get** /v1/formats/{format}/upload-specs | Get upload field requirements for the desired format    |
| [**get2**](#get2) | **get** /v1/formats/upload-specs          | Get upload field requirements for each supported format |

# **get1**

<a id="get1"></a>

> UploadDefinitionXO get1(format)

Get upload field requirements for the desired format

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import formats_api
from nexus_sdk.model.upload_definition_xo import UploadDefinitionXO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formats_api.FormatsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'format': "format_example",
    }
    try:
        # Get upload field requirements for the desired format
        api_response = api_instance.get1(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling FormatsApi->get1: %s\n" % e)
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

| Name   | Type         | Description | Notes |
| ------ | ------------ | ----------- | ----- |
| format | FormatSchema |             |

# FormatSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                        | Description                                                 |
| ---- | -------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get1.ApiResponseFor200) | successful operation                                        |

#### get1.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                         | Description | Notes |
| ------------------------------------------------------------ | ----------- | ----- |
| [**UploadDefinitionXO**](../../models/UploadDefinitionXO.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get2**

<a id="get2"></a>

> [UploadDefinitionXO] get2()

Get upload field requirements for each supported format

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import formats_api
from nexus_sdk.model.upload_definition_xo import UploadDefinitionXO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formats_api.FormatsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get upload field requirements for each supported format
        api_response = api_instance.get2()
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling FormatsApi->get2: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return Types, Responses

| Code | Class                                        | Description                                                 |
| ---- | -------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get2.ApiResponseFor200) | successful operation                                        |

#### get2.ApiResponseFor200

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

| Class Name                                                           | Input Type                                                           | Accessed Type                                                        | Description | Notes |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | ----------- | ----- |
| [**UploadDefinitionXO**]({{complexTypePrefix}}UploadDefinitionXO.md) | [**UploadDefinitionXO**]({{complexTypePrefix}}UploadDefinitionXO.md) | [**UploadDefinitionXO**]({{complexTypePrefix}}UploadDefinitionXO.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
