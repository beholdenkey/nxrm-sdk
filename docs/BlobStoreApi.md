# swagger_client.BlobStoreApi

All URIs are relative to */service/rest/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert_blob_store_to_group**](BlobStoreApi.md#convert_blob_store_to_group) | **POST** /v1/blobstores/group/convert/{name}/{newNameForOriginal} | Convert a blob store to a group blob store
[**create_blob_store**](BlobStoreApi.md#create_blob_store) | **POST** /v1/blobstores/s3 | Create an S3 blob store
[**create_blob_store1**](BlobStoreApi.md#create_blob_store1) | **POST** /v1/blobstores/azure | Create an Azure blob store
[**create_file_blob_store**](BlobStoreApi.md#create_file_blob_store) | **POST** /v1/blobstores/file | Create a file blob store
[**create_group_blob_store**](BlobStoreApi.md#create_group_blob_store) | **POST** /v1/blobstores/group | Create a group blob store
[**delete_blob_store**](BlobStoreApi.md#delete_blob_store) | **DELETE** /v1/blobstores/{name} | Delete a blob store by name
[**get_blob_store**](BlobStoreApi.md#get_blob_store) | **GET** /v1/blobstores/s3/{name} | Get a S3 blob store configuration by name
[**get_blob_store1**](BlobStoreApi.md#get_blob_store1) | **GET** /v1/blobstores/azure/{name} | Get an Azure blob store configuration by name
[**get_file_blob_store_configuration**](BlobStoreApi.md#get_file_blob_store_configuration) | **GET** /v1/blobstores/file/{name} | Get a file blob store configuration by name
[**get_group_blob_store_configuration**](BlobStoreApi.md#get_group_blob_store_configuration) | **GET** /v1/blobstores/group/{name} | Get a group blob store configuration by name
[**list_blob_stores**](BlobStoreApi.md#list_blob_stores) | **GET** /v1/blobstores | List the blob stores
[**quota_status**](BlobStoreApi.md#quota_status) | **GET** /v1/blobstores/{name}/quota-status | Get quota status for a given blob store
[**update_blob_store**](BlobStoreApi.md#update_blob_store) | **PUT** /v1/blobstores/s3/{name} | Update an S3 blob store configuration by name
[**update_blob_store1**](BlobStoreApi.md#update_blob_store1) | **PUT** /v1/blobstores/azure/{name} | Update an Azure blob store configuration by name
[**update_file_blob_store**](BlobStoreApi.md#update_file_blob_store) | **PUT** /v1/blobstores/file/{name} | Update a file blob store configuration by name
[**update_group_blob_store**](BlobStoreApi.md#update_group_blob_store) | **PUT** /v1/blobstores/group/{name} | Update a group blob store configuration by name

# **convert_blob_store_to_group**
> GroupBlobStoreApiModel convert_blob_store_to_group(name, new_name_for_original)

Convert a blob store to a group blob store

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlobStoreApi()
name = 'name_example' # str | The name of the group blob store
new_name_for_original = 'new_name_for_original_example' # str | A new name to the original blob store

try:
    # Convert a blob store to a group blob store
    api_response = api_instance.convert_blob_store_to_group(name, new_name_for_original)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlobStoreApi->convert_blob_store_to_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the group blob store | 
 **new_name_for_original** | **str**| A new name to the original blob store | 

### Return type

[**GroupBlobStoreApiModel**](GroupBlobStoreApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_blob_store**
> create_blob_store(body=body)

Create an S3 blob store

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlobStoreApi()
body = swagger_client.S3BlobStoreApiModel() # S3BlobStoreApiModel |  (optional)

try:
    # Create an S3 blob store
    api_instance.create_blob_store(body=body)
except ApiException as e:
    print("Exception when calling BlobStoreApi->create_blob_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**S3BlobStoreApiModel**](S3BlobStoreApiModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_blob_store1**
> create_blob_store1(body=body)

Create an Azure blob store

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlobStoreApi()
body = swagger_client.AzureBlobStoreApiModel() # AzureBlobStoreApiModel |  (optional)

try:
    # Create an Azure blob store
    api_instance.create_blob_store1(body=body)
except ApiException as e:
    print("Exception when calling BlobStoreApi->create_blob_store1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AzureBlobStoreApiModel**](AzureBlobStoreApiModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_file_blob_store**
> create_file_blob_store(body=body)

Create a file blob store

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlobStoreApi()
body = swagger_client.FileBlobStoreApiCreateRequest() # FileBlobStoreApiCreateRequest |  (optional)

try:
    # Create a file blob store
    api_instance.create_file_blob_store(body=body)
except ApiException as e:
    print("Exception when calling BlobStoreApi->create_file_blob_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileBlobStoreApiCreateRequest**](FileBlobStoreApiCreateRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group_blob_store**
> create_group_blob_store(body=body)

Create a group blob store

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlobStoreApi()
body = swagger_client.GroupBlobStoreApiCreateRequest() # GroupBlobStoreApiCreateRequest |  (optional)

try:
    # Create a group blob store
    api_instance.create_group_blob_store(body=body)
except ApiException as e:
    print("Exception when calling BlobStoreApi->create_group_blob_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupBlobStoreApiCreateRequest**](GroupBlobStoreApiCreateRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_blob_store**
> delete_blob_store(name)

Delete a blob store by name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlobStoreApi()
name = 'name_example' # str | The name of the blob store to delete

try:
    # Delete a blob store by name
    api_instance.delete_blob_store(name)
except ApiException as e:
    print("Exception when calling BlobStoreApi->delete_blob_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the blob store to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blob_store**
> S3BlobStoreApiModel get_blob_store(name)

Get a S3 blob store configuration by name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlobStoreApi()
name = 'name_example' # str | Name of the blob store configuration to fetch

try:
    # Get a S3 blob store configuration by name
    api_response = api_instance.get_blob_store(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlobStoreApi->get_blob_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the blob store configuration to fetch | 

### Return type

[**S3BlobStoreApiModel**](S3BlobStoreApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blob_store1**
> AzureBlobStoreApiModel get_blob_store1(name)

Get an Azure blob store configuration by name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlobStoreApi()
name = 'name_example' # str | Name of the blob store configuration to fetch

try:
    # Get an Azure blob store configuration by name
    api_response = api_instance.get_blob_store1(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlobStoreApi->get_blob_store1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the blob store configuration to fetch | 

### Return type

[**AzureBlobStoreApiModel**](AzureBlobStoreApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_blob_store_configuration**
> FileBlobStoreApiModel get_file_blob_store_configuration(name)

Get a file blob store configuration by name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlobStoreApi()
name = 'name_example' # str | The name of the file blob store to read

try:
    # Get a file blob store configuration by name
    api_response = api_instance.get_file_blob_store_configuration(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlobStoreApi->get_file_blob_store_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file blob store to read | 

### Return type

[**FileBlobStoreApiModel**](FileBlobStoreApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_blob_store_configuration**
> GroupBlobStoreApiModel get_group_blob_store_configuration(name)

Get a group blob store configuration by name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlobStoreApi()
name = 'name_example' # str | The name of the group blob store

try:
    # Get a group blob store configuration by name
    api_response = api_instance.get_group_blob_store_configuration(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlobStoreApi->get_group_blob_store_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the group blob store | 

### Return type

[**GroupBlobStoreApiModel**](GroupBlobStoreApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_blob_stores**
> list[GenericBlobStoreApiResponse] list_blob_stores()

List the blob stores

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlobStoreApi()

try:
    # List the blob stores
    api_response = api_instance.list_blob_stores()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlobStoreApi->list_blob_stores: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GenericBlobStoreApiResponse]**](GenericBlobStoreApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quota_status**
> BlobStoreQuotaResultXO quota_status(name)

Get quota status for a given blob store

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlobStoreApi()
name = 'name_example' # str | 

try:
    # Get quota status for a given blob store
    api_response = api_instance.quota_status(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlobStoreApi->quota_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**BlobStoreQuotaResultXO**](BlobStoreQuotaResultXO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_blob_store**
> update_blob_store(name, body=body)

Update an S3 blob store configuration by name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlobStoreApi()
name = 'name_example' # str | Name of the blob store to update
body = swagger_client.S3BlobStoreApiModel() # S3BlobStoreApiModel |  (optional)

try:
    # Update an S3 blob store configuration by name
    api_instance.update_blob_store(name, body=body)
except ApiException as e:
    print("Exception when calling BlobStoreApi->update_blob_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the blob store to update | 
 **body** | [**S3BlobStoreApiModel**](S3BlobStoreApiModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_blob_store1**
> update_blob_store1(name, body=body)

Update an Azure blob store configuration by name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlobStoreApi()
name = 'name_example' # str | Name of the blob store to update
body = swagger_client.AzureBlobStoreApiModel() # AzureBlobStoreApiModel |  (optional)

try:
    # Update an Azure blob store configuration by name
    api_instance.update_blob_store1(name, body=body)
except ApiException as e:
    print("Exception when calling BlobStoreApi->update_blob_store1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the blob store to update | 
 **body** | [**AzureBlobStoreApiModel**](AzureBlobStoreApiModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_file_blob_store**
> update_file_blob_store(name, body=body)

Update a file blob store configuration by name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlobStoreApi()
name = 'name_example' # str | The name of the file blob store to update
body = swagger_client.FileBlobStoreApiUpdateRequest() # FileBlobStoreApiUpdateRequest |  (optional)

try:
    # Update a file blob store configuration by name
    api_instance.update_file_blob_store(name, body=body)
except ApiException as e:
    print("Exception when calling BlobStoreApi->update_file_blob_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file blob store to update | 
 **body** | [**FileBlobStoreApiUpdateRequest**](FileBlobStoreApiUpdateRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_blob_store**
> update_group_blob_store(name, body=body)

Update a group blob store configuration by name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlobStoreApi()
name = 'name_example' # str | The name of the blob store to update
body = swagger_client.GroupBlobStoreApiUpdateRequest() # GroupBlobStoreApiUpdateRequest |  (optional)

try:
    # Update a group blob store configuration by name
    api_instance.update_group_blob_store(name, body=body)
except ApiException as e:
    print("Exception when calling BlobStoreApi->update_group_blob_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the blob store to update | 
 **body** | [**GroupBlobStoreApiUpdateRequest**](GroupBlobStoreApiUpdateRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

