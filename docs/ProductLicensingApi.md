# swagger_client.ProductLicensingApi

All URIs are relative to _/service/rest/_

| Method                                                              | HTTP request                  | Description                     |
| ------------------------------------------------------------------- | ----------------------------- | ------------------------------- |
| [**get_license_status**](ProductLicensingApi.md#get_license_status) | **GET** /v1/system/license    | Get the current license status. |
| [**remove_license**](ProductLicensingApi.md#remove_license)         | **DELETE** /v1/system/license | Uninstall license if present.   |
| [**set_license**](ProductLicensingApi.md#set_license)               | **POST** /v1/system/license   | Upload a new license file.      |

# **get_license_status**

> ApiLicenseDetailsXO get_license_status()

Get the current license status.

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductLicensingApi()

try:
    # Get the current license status.
    api_response = api_instance.get_license_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductLicensingApi->get_license_status: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiLicenseDetailsXO**](ApiLicenseDetailsXO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_license**

> remove_license()

Uninstall license if present.

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductLicensingApi()

try:
    # Uninstall license if present.
    api_instance.remove_license()
except ApiException as e:
    print("Exception when calling ProductLicensingApi->remove_license: %s\n" % e)
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

# **set_license**

> ApiLicenseDetailsXO set_license(body=body)

Upload a new license file.

Server must be restarted to take effect

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductLicensingApi()
body = swagger_client.InputStream() # InputStream |  (optional)

try:
    # Upload a new license file.
    api_response = api_instance.set_license(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductLicensingApi->set_license: %s\n" % e)
```

### Parameters

| Name     | Type                              | Description | Notes      |
| -------- | --------------------------------- | ----------- | ---------- |
| **body** | [**InputStream**](InputStream.md) |             | [optional] |

### Return type

[**ApiLicenseDetailsXO**](ApiLicenseDetailsXO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
