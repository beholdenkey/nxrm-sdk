# swagger_client.SupportApi

All URIs are relative to */service/rest/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**supportzip**](SupportApi.md#supportzip) | **POST** /v1/support/supportzip | Creates and downloads a support zip
[**supportzippath**](SupportApi.md#supportzippath) | **POST** /v1/support/supportzippath | Creates a support zip and returns the path

# **supportzip**
> supportzip(body=body)

Creates and downloads a support zip

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SupportApi()
body = swagger_client.SupportZipGeneratorRequest() # SupportZipGeneratorRequest |  (optional)

try:
    # Creates and downloads a support zip
    api_instance.supportzip(body=body)
except ApiException as e:
    print("Exception when calling SupportApi->supportzip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SupportZipGeneratorRequest**](SupportZipGeneratorRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **supportzippath**
> SupportZipXO supportzippath(body=body)

Creates a support zip and returns the path

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SupportApi()
body = swagger_client.SupportZipGeneratorRequest() # SupportZipGeneratorRequest |  (optional)

try:
    # Creates a support zip and returns the path
    api_response = api_instance.supportzippath(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupportApi->supportzippath: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SupportZipGeneratorRequest**](SupportZipGeneratorRequest.md)|  | [optional] 

### Return type

[**SupportZipXO**](SupportZipXO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

