# swagger_client.ManageIQServerConfigurationApi

All URIs are relative to _/service/rest/_

| Method                                                                             | HTTP request                      | Description                    |
| ---------------------------------------------------------------------------------- | --------------------------------- | ------------------------------ |
| [**disable_iq**](ManageIQServerConfigurationApi.md#disable_iq)                     | **POST** /v1/iq/disable           | Disable IQ server              |
| [**enable_iq**](ManageIQServerConfigurationApi.md#enable_iq)                       | **POST** /v1/iq/enable            | Enable IQ server               |
| [**get_configuration**](ManageIQServerConfigurationApi.md#get_configuration)       | **GET** /v1/iq                    | Get IQ server configuration    |
| [**update_configuration**](ManageIQServerConfigurationApi.md#update_configuration) | **PUT** /v1/iq                    | Update IQ server configuration |
| [**verify_connection**](ManageIQServerConfigurationApi.md#verify_connection)       | **POST** /v1/iq/verify-connection | Verify IQ server connection    |

# **disable_iq**

> disable_iq()

Disable IQ server

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ManageIQServerConfigurationApi()

try:
    # Disable IQ server
    api_instance.disable_iq()
except ApiException as e:
    print("Exception when calling ManageIQServerConfigurationApi->disable_iq: %s\n" % e)
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

# **enable_iq**

> enable_iq()

Enable IQ server

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ManageIQServerConfigurationApi()

try:
    # Enable IQ server
    api_instance.enable_iq()
except ApiException as e:
    print("Exception when calling ManageIQServerConfigurationApi->enable_iq: %s\n" % e)
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

# **get_configuration**

> get_configuration()

Get IQ server configuration

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ManageIQServerConfigurationApi()

try:
    # Get IQ server configuration
    api_instance.get_configuration()
except ApiException as e:
    print("Exception when calling ManageIQServerConfigurationApi->get_configuration: %s\n" % e)
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

# **update_configuration**

> update_configuration(body=body)

Update IQ server configuration

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ManageIQServerConfigurationApi()
body = swagger_client.IqConnectionXo() # IqConnectionXo |  (optional)

try:
    # Update IQ server configuration
    api_instance.update_configuration(body=body)
except ApiException as e:
    print("Exception when calling ManageIQServerConfigurationApi->update_configuration: %s\n" % e)
```

### Parameters

| Name     | Type                                    | Description | Notes      |
| -------- | --------------------------------------- | ----------- | ---------- |
| **body** | [**IqConnectionXo**](IqConnectionXo.md) |             | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_connection**

> verify_connection()

Verify IQ server connection

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ManageIQServerConfigurationApi()

try:
    # Verify IQ server connection
    api_instance.verify_connection()
except ApiException as e:
    print("Exception when calling ManageIQServerConfigurationApi->verify_connection: %s\n" % e)
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
