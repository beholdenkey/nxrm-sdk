# swagger_client.SecurityManagementApi

All URIs are relative to */service/rest/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_sources**](SecurityManagementApi.md#get_user_sources) | **GET** /v1/security/user-sources | Retrieve a list of the available user sources.

# **get_user_sources**
> list[ApiUserSource] get_user_sources()

Retrieve a list of the available user sources.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementApi()

try:
    # Retrieve a list of the available user sources.
    api_response = api_instance.get_user_sources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityManagementApi->get_user_sources: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ApiUserSource]**](ApiUserSource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

