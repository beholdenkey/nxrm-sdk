<a id="__pageTop"></a>
# nexus_sdk.apis.tags.azure_blob_store_api.AzureBlobStoreApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**verify_connection2**](#verify_connection2) | **post** /v1/azureblobstore/test-connection | Verify connection using supplied Azure Blob Store settings

# **verify_connection2**
<a id="verify_connection2"></a>
> verify_connection2()

Verify connection using supplied Azure Blob Store settings

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import azure_blob_store_api
from nexus_sdk.model.azure_connection_xo import AzureConnectionXO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = azure_blob_store_api.AzureBlobStoreApi(api_client)

    # example passing only optional values
    body = AzureConnectionXO(
        account_name="account_name_example",
        account_key="account_key_example",
        container_name="container_name_example",
        authentication_method="authentication_method_example",
    )
    try:
        # Verify connection using supplied Azure Blob Store settings
        api_response = api_instance.verify_connection2(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling AzureBlobStoreApi->verify_connection2: %s\n" % e)
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
[**AzureConnectionXO**](../../models/AzureConnectionXO.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#verify_connection2.ApiResponseFor204) | Azure Blob Store connection was successful
400 | [ApiResponseFor400](#verify_connection2.ApiResponseFor400) | Azure Blob Store connection failed
401 | [ApiResponseFor401](#verify_connection2.ApiResponseFor401) | Authentication required
403 | [ApiResponseFor403](#verify_connection2.ApiResponseFor403) | Insufficient permissions

#### verify_connection2.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### verify_connection2.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### verify_connection2.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### verify_connection2.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

