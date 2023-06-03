# swagger_client.SecurityManagementJWTApi

All URIs are relative to _/service/rest/_

| Method                                                       | HTTP request             | Description                                                                      |
| ------------------------------------------------------------ | ------------------------ | -------------------------------------------------------------------------------- |
| [**reset_secret**](SecurityManagementJWTApi.md#reset_secret) | **PUT** /v1/security/jwt | Reset JWT secret (note that session will be expired for the all logged-in users) |

# **reset_secret**

> reset_secret()

Reset JWT secret (note that session will be expired for the all logged-in users)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementJWTApi()

try:
    # Reset JWT secret (note that session will be expired for the all logged-in users)
    api_instance.reset_secret()
except ApiException as e:
    print("Exception when calling SecurityManagementJWTApi->reset_secret: %s\n" % e)
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
