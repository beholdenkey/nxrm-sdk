# swagger_client.EmailApi

All URIs are relative to _/service/rest/_

| Method                                                                   | HTTP request              | Description                                                         |
| ------------------------------------------------------------------------ | ------------------------- | ------------------------------------------------------------------- |
| [**delete_email_configuration**](EmailApi.md#delete_email_configuration) | **DELETE** /v1/email      | Disable and clear the email configuration                           |
| [**get_email_configuration**](EmailApi.md#get_email_configuration)       | **GET** /v1/email         | Retrieve the current email configuration                            |
| [**set_email_configuration**](EmailApi.md#set_email_configuration)       | **PUT** /v1/email         | Set the current email configuration                                 |
| [**test_email_configuration**](EmailApi.md#test_email_configuration)     | **POST** /v1/email/verify | Send a test email to the email address provided in the request body |

# **delete_email_configuration**

> delete_email_configuration()

Disable and clear the email configuration

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EmailApi()

try:
    # Disable and clear the email configuration
    api_instance.delete_email_configuration()
except ApiException as e:
    print("Exception when calling EmailApi->delete_email_configuration: %s\n" % e)
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

# **get_email_configuration**

> ApiEmailConfiguration get_email_configuration()

Retrieve the current email configuration

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EmailApi()

try:
    # Retrieve the current email configuration
    api_response = api_instance.get_email_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailApi->get_email_configuration: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiEmailConfiguration**](ApiEmailConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_email_configuration**

> set_email_configuration(body)

Set the current email configuration

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EmailApi()
body = swagger_client.ApiEmailConfiguration() # ApiEmailConfiguration |

try:
    # Set the current email configuration
    api_instance.set_email_configuration(body)
except ApiException as e:
    print("Exception when calling EmailApi->set_email_configuration: %s\n" % e)
```

### Parameters

| Name     | Type                                                  | Description | Notes |
| -------- | ----------------------------------------------------- | ----------- | ----- |
| **body** | [**ApiEmailConfiguration**](ApiEmailConfiguration.md) |             |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: _/_
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_email_configuration**

> ApiEmailValidation test_email_configuration(body)

Send a test email to the email address provided in the request body

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EmailApi()
body = 'body_example' # str | An email address to send a test email to

try:
    # Send a test email to the email address provided in the request body
    api_response = api_instance.test_email_configuration(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailApi->test_email_configuration: %s\n" % e)
```

### Parameters

| Name     | Type              | Description                              | Notes |
| -------- | ----------------- | ---------------------------------------- | ----- |
| **body** | [**str**](str.md) | An email address to send a test email to |

### Return type

[**ApiEmailValidation**](ApiEmailValidation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: _/_
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
