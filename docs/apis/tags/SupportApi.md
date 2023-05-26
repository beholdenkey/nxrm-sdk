<a id="__pageTop"></a>

# nexus_sdk.apis.tags.support_api.SupportApi

All URIs are relative to _http://localhost/service/rest_

| Method                                | HTTP request                        | Description                                |
| ------------------------------------- | ----------------------------------- | ------------------------------------------ |
| [**supportzip**](#supportzip)         | **post** /v1/support/supportzip     | Creates and downloads a support zip        |
| [**supportzippath**](#supportzippath) | **post** /v1/support/supportzippath | Creates a support zip and returns the path |

# **supportzip**

<a id="supportzip"></a>

> supportzip()

Creates and downloads a support zip

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import support_api
from nexus_sdk.model.support_zip_generator_request import SupportZipGeneratorRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = support_api.SupportApi(api_client)

    # example passing only optional values
    body = SupportZipGeneratorRequest(
        system_information=True,
        thread_dump=True,
        metrics=True,
        configuration=True,
        security=True,
        log=True,
        task_log=True,
        audit_log=True,
        jmx=True,
        replication=True,
        limit_file_sizes=True,
        limit_zip_size=True,
    )
    try:
        # Creates and downloads a support zip
        api_response = api_instance.supportzip(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SupportApi->supportzip: %s\n" % e)
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

| Type                                                                         | Description | Notes |
| ---------------------------------------------------------------------------- | ----------- | ----- |
| [**SupportZipGeneratorRequest**](../../models/SupportZipGeneratorRequest.md) |             |

### Return Types, Responses

| Code    | Class                                                      | Description                                                 |
| ------- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| n/a     | api_client.ApiResponseWithoutDeserialization               | When skip_deserialization is True this response is returned |
| default | [ApiResponseForDefault](#supportzip.ApiResponseForDefault) | successful operation                                        |

#### supportzip.ApiResponseForDefault

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **supportzippath**

<a id="supportzippath"></a>

> SupportZipXO supportzippath()

Creates a support zip and returns the path

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import support_api
from nexus_sdk.model.support_zip_xo import SupportZipXO
from nexus_sdk.model.support_zip_generator_request import SupportZipGeneratorRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = support_api.SupportApi(api_client)

    # example passing only optional values
    body = SupportZipGeneratorRequest(
        system_information=True,
        thread_dump=True,
        metrics=True,
        configuration=True,
        security=True,
        log=True,
        task_log=True,
        audit_log=True,
        jmx=True,
        replication=True,
        limit_file_sizes=True,
        limit_zip_size=True,
    )
    try:
        # Creates a support zip and returns the path
        api_response = api_instance.supportzippath(
            body=body,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling SupportApi->supportzippath: %s\n" % e)
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

| Type                                                                         | Description | Notes |
| ---------------------------------------------------------------------------- | ----------- | ----- |
| [**SupportZipGeneratorRequest**](../../models/SupportZipGeneratorRequest.md) |             |

### Return Types, Responses

| Code | Class                                                  | Description                                                 |
| ---- | ------------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization           | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#supportzippath.ApiResponseFor200) | successful operation                                        |

#### supportzippath.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                             | Description | Notes |
| ------------------------------------------------ | ----------- | ----- |
| [**SupportZipXO**](../../models/SupportZipXO.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
