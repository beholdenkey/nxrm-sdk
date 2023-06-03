# swagger_client.SecurityAtlassianCrowdApi

All URIs are relative to _/service/rest/_

| Method                                                                    | HTTP request                                            | Description                                                              |
| ------------------------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------ |
| [**clear_cache**](SecurityAtlassianCrowdApi.md#clear_cache)               | **POST** /v1/security/atlassian-crowd/clear-cache       | Clear Atlassian Crowd cache                                              |
| [**read_settings**](SecurityAtlassianCrowdApi.md#read_settings)           | **GET** /v1/security/atlassian-crowd                    | Retrieve Atlassian Crowd settings configured in Nexus Repository Manager |
| [**update_settings**](SecurityAtlassianCrowdApi.md#update_settings)       | **PUT** /v1/security/atlassian-crowd                    | Update Atlassian Crowd settings configured in Nexus Repository Manager   |
| [**verify_connection1**](SecurityAtlassianCrowdApi.md#verify_connection1) | **POST** /v1/security/atlassian-crowd/verify-connection | Verify connection using supplied Atlassian Crowd settings                |

# **clear_cache**

> clear_cache()

Clear Atlassian Crowd cache

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityAtlassianCrowdApi()

try:
    # Clear Atlassian Crowd cache
    api_instance.clear_cache()
except ApiException as e:
    print("Exception when calling SecurityAtlassianCrowdApi->clear_cache: %s\n" % e)
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

# **read_settings**

> read_settings()

Retrieve Atlassian Crowd settings configured in Nexus Repository Manager

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityAtlassianCrowdApi()

try:
    # Retrieve Atlassian Crowd settings configured in Nexus Repository Manager
    api_instance.read_settings()
except ApiException as e:
    print("Exception when calling SecurityAtlassianCrowdApi->read_settings: %s\n" % e)
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

# **update_settings**

> update_settings(body=body)

Update Atlassian Crowd settings configured in Nexus Repository Manager

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityAtlassianCrowdApi()
body = swagger_client.CrowdApiXO() # CrowdApiXO |  (optional)

try:
    # Update Atlassian Crowd settings configured in Nexus Repository Manager
    api_instance.update_settings(body=body)
except ApiException as e:
    print("Exception when calling SecurityAtlassianCrowdApi->update_settings: %s\n" % e)
```

### Parameters

| Name     | Type                            | Description | Notes      |
| -------- | ------------------------------- | ----------- | ---------- |
| **body** | [**CrowdApiXO**](CrowdApiXO.md) |             | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: _/_
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_connection1**

> verify_connection1(body=body)

Verify connection using supplied Atlassian Crowd settings

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityAtlassianCrowdApi()
body = swagger_client.CrowdApiXO() # CrowdApiXO |  (optional)

try:
    # Verify connection using supplied Atlassian Crowd settings
    api_instance.verify_connection1(body=body)
except ApiException as e:
    print("Exception when calling SecurityAtlassianCrowdApi->verify_connection1: %s\n" % e)
```

### Parameters

| Name     | Type                            | Description | Notes      |
| -------- | ------------------------------- | ----------- | ---------- |
| **body** | [**CrowdApiXO**](CrowdApiXO.md) |             | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: _/_
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
