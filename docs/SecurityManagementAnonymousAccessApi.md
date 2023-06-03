# swagger_client.SecurityManagementAnonymousAccessApi

All URIs are relative to */service/rest/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read**](SecurityManagementAnonymousAccessApi.md#read) | **GET** /v1/security/anonymous | Get Anonymous Access settings
[**update**](SecurityManagementAnonymousAccessApi.md#update) | **PUT** /v1/security/anonymous | Update Anonymous Access settings

# **read**
> AnonymousAccessSettingsXO read()

Get Anonymous Access settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementAnonymousAccessApi()

try:
    # Get Anonymous Access settings
    api_response = api_instance.read()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityManagementAnonymousAccessApi->read: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AnonymousAccessSettingsXO**](AnonymousAccessSettingsXO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> AnonymousAccessSettingsXO update(body=body)

Update Anonymous Access settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementAnonymousAccessApi()
body = swagger_client.AnonymousAccessSettingsXO() # AnonymousAccessSettingsXO |  (optional)

try:
    # Update Anonymous Access settings
    api_response = api_instance.update(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityManagementAnonymousAccessApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnonymousAccessSettingsXO**](AnonymousAccessSettingsXO.md)|  | [optional] 

### Return type

[**AnonymousAccessSettingsXO**](AnonymousAccessSettingsXO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

