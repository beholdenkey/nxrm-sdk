# swagger_client.AzureBlobStoreApi

All URIs are relative to _/service/rest/_

| Method                                                            | HTTP request                                | Description                                                |
| ----------------------------------------------------------------- | ------------------------------------------- | ---------------------------------------------------------- |
| [**verify_connection2**](AzureBlobStoreApi.md#verify_connection2) | **POST** /v1/azureblobstore/test-connection | Verify connection using supplied Azure Blob Store settings |

# **verify_connection2**

> verify_connection2(body=body)

Verify connection using supplied Azure Blob Store settings

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AzureBlobStoreApi()
body = swagger_client.AzureConnectionXO() # AzureConnectionXO |  (optional)

try:
    # Verify connection using supplied Azure Blob Store settings
    api_instance.verify_connection2(body=body)
except ApiException as e:
    print("Exception when calling AzureBlobStoreApi->verify_connection2: %s\n" % e)
```

### Parameters

| Name     | Type                                          | Description | Notes      |
| -------- | --------------------------------------------- | ----------- | ---------- |
| **body** | [**AzureConnectionXO**](AzureConnectionXO.md) |             | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
