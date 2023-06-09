# swagger_client.LifecycleApi

All URIs are relative to _/service/rest/_

| Method                                     | HTTP request                 | Description                 |
| ------------------------------------------ | ---------------------------- | --------------------------- |
| [**bounce**](LifecycleApi.md#bounce)       | **PUT** /v1/lifecycle/bounce | Bounce lifecycle phase      |
| [**get_phase**](LifecycleApi.md#get_phase) | **GET** /v1/lifecycle/phase  | Get current lifecycle phase |
| [**set_phase**](LifecycleApi.md#set_phase) | **PUT** /v1/lifecycle/phase  | Move to new lifecycle phase |

# **bounce**

> bounce(body=body)

Bounce lifecycle phase

Re-runs all phases from the given phase to the current phase

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LifecycleApi()
body = 'body_example' # str | The phase to bounce (optional)

try:
    # Bounce lifecycle phase
    api_instance.bounce(body=body)
except ApiException as e:
    print("Exception when calling LifecycleApi->bounce: %s\n" % e)
```

### Parameters

| Name     | Type              | Description         | Notes      |
| -------- | ----------------- | ------------------- | ---------- |
| **body** | [**str**](str.md) | The phase to bounce | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_phase**

> str get_phase()

Get current lifecycle phase

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LifecycleApi()

try:
    # Get current lifecycle phase
    api_response = api_instance.get_phase()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LifecycleApi->get_phase: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_phase**

> set_phase(body=body)

Move to new lifecycle phase

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LifecycleApi()
body = 'body_example' # str | The phase to move to (optional)

try:
    # Move to new lifecycle phase
    api_instance.set_phase(body=body)
except ApiException as e:
    print("Exception when calling LifecycleApi->set_phase: %s\n" % e)
```

### Parameters

| Name     | Type              | Description          | Notes      |
| -------- | ----------------- | -------------------- | ---------- |
| **body** | [**str**](str.md) | The phase to move to | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
