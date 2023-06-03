# swagger_client.ContentSelectorsApi

All URIs are relative to */service/rest/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_content_selector**](ContentSelectorsApi.md#create_content_selector) | **POST** /v1/security/content-selectors | Create a new content selector
[**delete_content_selector**](ContentSelectorsApi.md#delete_content_selector) | **DELETE** /v1/security/content-selectors/{name} | Delete a content selector
[**get_content_selector**](ContentSelectorsApi.md#get_content_selector) | **GET** /v1/security/content-selectors/{name} | Get a content selector by name
[**get_content_selectors**](ContentSelectorsApi.md#get_content_selectors) | **GET** /v1/security/content-selectors | List content selectors
[**update_content_selector**](ContentSelectorsApi.md#update_content_selector) | **PUT** /v1/security/content-selectors/{name} | Update a content selector

# **create_content_selector**
> create_content_selector(body=body)

Create a new content selector

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContentSelectorsApi()
body = swagger_client.ContentSelectorApiCreateRequest() # ContentSelectorApiCreateRequest |  (optional)

try:
    # Create a new content selector
    api_instance.create_content_selector(body=body)
except ApiException as e:
    print("Exception when calling ContentSelectorsApi->create_content_selector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ContentSelectorApiCreateRequest**](ContentSelectorApiCreateRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_content_selector**
> delete_content_selector(name)

Delete a content selector

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContentSelectorsApi()
name = 'name_example' # str | 

try:
    # Delete a content selector
    api_instance.delete_content_selector(name)
except ApiException as e:
    print("Exception when calling ContentSelectorsApi->delete_content_selector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_content_selector**
> ContentSelectorApiResponse get_content_selector(name)

Get a content selector by name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContentSelectorsApi()
name = 'name_example' # str | The content selector name

try:
    # Get a content selector by name
    api_response = api_instance.get_content_selector(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentSelectorsApi->get_content_selector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The content selector name | 

### Return type

[**ContentSelectorApiResponse**](ContentSelectorApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_content_selectors**
> list[ContentSelectorApiResponse] get_content_selectors()

List content selectors

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContentSelectorsApi()

try:
    # List content selectors
    api_response = api_instance.get_content_selectors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentSelectorsApi->get_content_selectors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ContentSelectorApiResponse]**](ContentSelectorApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_content_selector**
> update_content_selector(name, body=body)

Update a content selector

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContentSelectorsApi()
name = 'name_example' # str | The content selector name
body = swagger_client.ContentSelectorApiUpdateRequest() # ContentSelectorApiUpdateRequest |  (optional)

try:
    # Update a content selector
    api_instance.update_content_selector(name, body=body)
except ApiException as e:
    print("Exception when calling ContentSelectorsApi->update_content_selector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The content selector name | 
 **body** | [**ContentSelectorApiUpdateRequest**](ContentSelectorApiUpdateRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

