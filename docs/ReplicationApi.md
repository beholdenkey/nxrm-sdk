# swagger_client.ReplicationApi

All URIs are relative to */service/rest/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create2**](ReplicationApi.md#create2) | **POST** /beta/replication/connection | Create a replication connection.
[**delete3**](ReplicationApi.md#delete3) | **DELETE** /beta/replication/connection/{name} | Delete a replication connection.
[**disable**](ReplicationApi.md#disable) | **DELETE** /beta/replicationtarget/repository/{repositoryName}/enable | Disable replication on a target repository..
[**enable**](ReplicationApi.md#enable) | **PUT** /beta/replicationtarget/repository/enable | Enable replication on a target repository.
[**get4**](ReplicationApi.md#get4) | **GET** /beta/replication/connection/{name} | Fetch a replication connection.
[**list**](ReplicationApi.md#list) | **GET** /beta/replication/connection | List the replication connections.
[**update2**](ReplicationApi.md#update2) | **PUT** /beta/replication/connection/{name} | Update a replication connection.

# **create2**
> create2(body=body)

Create a replication connection.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReplicationApi()
body = swagger_client.ReplicationConnectionXO() # ReplicationConnectionXO |  (optional)

try:
    # Create a replication connection.
    api_instance.create2(body=body)
except ApiException as e:
    print("Exception when calling ReplicationApi->create2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReplicationConnectionXO**](ReplicationConnectionXO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete3**
> delete3(name)

Delete a replication connection.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReplicationApi()
name = 'name_example' # str | Replication connection name

try:
    # Delete a replication connection.
    api_instance.delete3(name)
except ApiException as e:
    print("Exception when calling ReplicationApi->delete3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Replication connection name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable**
> disable(repository_name)

Disable replication on a target repository..

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReplicationApi()
repository_name = 'repository_name_example' # str | Repository name

try:
    # Disable replication on a target repository..
    api_instance.disable(repository_name)
except ApiException as e:
    print("Exception when calling ReplicationApi->disable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Repository name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable**
> enable(body=body)

Enable replication on a target repository.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReplicationApi()
body = swagger_client.ReplicationEnableXO() # ReplicationEnableXO |  (optional)

try:
    # Enable replication on a target repository.
    api_instance.enable(body=body)
except ApiException as e:
    print("Exception when calling ReplicationApi->enable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReplicationEnableXO**](ReplicationEnableXO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get4**
> get4(name)

Fetch a replication connection.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReplicationApi()
name = 'name_example' # str | Replication connection name

try:
    # Fetch a replication connection.
    api_instance.get4(name)
except ApiException as e:
    print("Exception when calling ReplicationApi->get4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Replication connection name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> list()

List the replication connections.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReplicationApi()

try:
    # List the replication connections.
    api_instance.list()
except ApiException as e:
    print("Exception when calling ReplicationApi->list: %s\n" % e)
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

# **update2**
> update2(name, body=body)

Update a replication connection.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReplicationApi()
name = 'name_example' # str | Replication connection name
body = swagger_client.ReplicationConnectionXO() # ReplicationConnectionXO |  (optional)

try:
    # Update a replication connection.
    api_instance.update2(name, body=body)
except ApiException as e:
    print("Exception when calling ReplicationApi->update2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Replication connection name | 
 **body** | [**ReplicationConnectionXO**](ReplicationConnectionXO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

