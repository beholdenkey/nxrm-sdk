# swagger_client.StatusApi

All URIs are relative to _/service/rest/_

| Method                                                                | HTTP request                | Description                                                                        |
| --------------------------------------------------------------------- | --------------------------- | ---------------------------------------------------------------------------------- |
| [**get_system_status_checks**](StatusApi.md#get_system_status_checks) | **GET** /v1/status/check    | Health check endpoint that returns the results of the system status checks         |
| [**is_available**](StatusApi.md#is_available)                         | **GET** /v1/status          | Health check endpoint that validates server can respond to read requests           |
| [**is_writable**](StatusApi.md#is_writable)                           | **GET** /v1/status/writable | Health check endpoint that validates server can respond to read and write requests |

# **get_system_status_checks**

> dict(str, Result) get_system_status_checks()

Health check endpoint that returns the results of the system status checks

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusApi()

try:
    # Health check endpoint that returns the results of the system status checks
    api_response = api_instance.get_system_status_checks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusApi->get_system_status_checks: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**dict(str, Result)**](Result.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_available**

> is_available()

Health check endpoint that validates server can respond to read requests

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusApi()

try:
    # Health check endpoint that validates server can respond to read requests
    api_instance.is_available()
except ApiException as e:
    print("Exception when calling StatusApi->is_available: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_writable**

> is_writable()

Health check endpoint that validates server can respond to read and write requests

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusApi()

try:
    # Health check endpoint that validates server can respond to read and write requests
    api_instance.is_writable()
except ApiException as e:
    print("Exception when calling StatusApi->is_writable: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
