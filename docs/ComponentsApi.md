# swagger_client.ComponentsApi

All URIs are relative to */service/rest/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_component**](ComponentsApi.md#delete_component) | **DELETE** /v1/components/{id} | Delete a single component
[**get_component_by_id**](ComponentsApi.md#get_component_by_id) | **GET** /v1/components/{id} | Get a single component
[**get_components**](ComponentsApi.md#get_components) | **GET** /v1/components | List components
[**upload_component**](ComponentsApi.md#upload_component) | **POST** /v1/components | Upload a single component

# **delete_component**
> delete_component(id)

Delete a single component

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComponentsApi()
id = 'id_example' # str | ID of the component to delete

try:
    # Delete a single component
    api_instance.delete_component(id)
except ApiException as e:
    print("Exception when calling ComponentsApi->delete_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the component to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_component_by_id**
> ComponentXO get_component_by_id(id)

Get a single component

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComponentsApi()
id = 'id_example' # str | ID of the component to retrieve

try:
    # Get a single component
    api_response = api_instance.get_component_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->get_component_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the component to retrieve | 

### Return type

[**ComponentXO**](ComponentXO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_components**
> PageComponentXO get_components(repository, continuation_token=continuation_token)

List components

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComponentsApi()
repository = 'repository_example' # str | Repository from which you would like to retrieve components
continuation_token = 'continuation_token_example' # str | A token returned by a prior request. If present, the next page of results are returned (optional)

try:
    # List components
    api_response = api_instance.get_components(repository, continuation_token=continuation_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->get_components: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **str**| Repository from which you would like to retrieve components | 
 **continuation_token** | **str**| A token returned by a prior request. If present, the next page of results are returned | [optional] 

### Return type

[**PageComponentXO**](PageComponentXO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_component**
> upload_component(repository, helm_tag=helm_tag, helm_asset=helm_asset, r_tag=r_tag, r_asset=r_asset, r_asset_path_id=r_asset_path_id, pypi_tag=pypi_tag, pypi_asset=pypi_asset, docker_tag=docker_tag, docker_asset=docker_asset, yum_directory=yum_directory, yum_tag=yum_tag, yum_asset=yum_asset, yum_asset_filename=yum_asset_filename, rubygems_tag=rubygems_tag, rubygems_asset=rubygems_asset, nuget_tag=nuget_tag, nuget_asset=nuget_asset, npm_tag=npm_tag, npm_asset=npm_asset, raw_directory=raw_directory, raw_tag=raw_tag, raw_asset1=raw_asset1, raw_asset1_filename=raw_asset1_filename, raw_asset2=raw_asset2, raw_asset2_filename=raw_asset2_filename, raw_asset3=raw_asset3, raw_asset3_filename=raw_asset3_filename, apt_tag=apt_tag, apt_asset=apt_asset, maven2_group_id=maven2_group_id, maven2_artifact_id=maven2_artifact_id, maven2_version=maven2_version, maven2_generate_pom=maven2_generate_pom, maven2_packaging=maven2_packaging, maven2_tag=maven2_tag, maven2_asset1=maven2_asset1, maven2_asset1_classifier=maven2_asset1_classifier, maven2_asset1_extension=maven2_asset1_extension, maven2_asset2=maven2_asset2, maven2_asset2_classifier=maven2_asset2_classifier, maven2_asset2_extension=maven2_asset2_extension, maven2_asset3=maven2_asset3, maven2_asset3_classifier=maven2_asset3_classifier, maven2_asset3_extension=maven2_asset3_extension)

Upload a single component

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComponentsApi()
repository = 'repository_example' # str | Name of the repository to which you would like to upload the component
helm_tag = 'helm_tag_example' # str |  (optional)
helm_asset = 'helm_asset_example' # str |  (optional)
r_tag = 'r_tag_example' # str |  (optional)
r_asset = 'r_asset_example' # str |  (optional)
r_asset_path_id = 'r_asset_path_id_example' # str |  (optional)
pypi_tag = 'pypi_tag_example' # str |  (optional)
pypi_asset = 'pypi_asset_example' # str |  (optional)
docker_tag = 'docker_tag_example' # str |  (optional)
docker_asset = 'docker_asset_example' # str |  (optional)
yum_directory = 'yum_directory_example' # str |  (optional)
yum_tag = 'yum_tag_example' # str |  (optional)
yum_asset = 'yum_asset_example' # str |  (optional)
yum_asset_filename = 'yum_asset_filename_example' # str |  (optional)
rubygems_tag = 'rubygems_tag_example' # str |  (optional)
rubygems_asset = 'rubygems_asset_example' # str |  (optional)
nuget_tag = 'nuget_tag_example' # str |  (optional)
nuget_asset = 'nuget_asset_example' # str |  (optional)
npm_tag = 'npm_tag_example' # str |  (optional)
npm_asset = 'npm_asset_example' # str |  (optional)
raw_directory = 'raw_directory_example' # str |  (optional)
raw_tag = 'raw_tag_example' # str |  (optional)
raw_asset1 = 'raw_asset1_example' # str |  (optional)
raw_asset1_filename = 'raw_asset1_filename_example' # str |  (optional)
raw_asset2 = 'raw_asset2_example' # str |  (optional)
raw_asset2_filename = 'raw_asset2_filename_example' # str |  (optional)
raw_asset3 = 'raw_asset3_example' # str |  (optional)
raw_asset3_filename = 'raw_asset3_filename_example' # str |  (optional)
apt_tag = 'apt_tag_example' # str |  (optional)
apt_asset = 'apt_asset_example' # str |  (optional)
maven2_group_id = 'maven2_group_id_example' # str |  (optional)
maven2_artifact_id = 'maven2_artifact_id_example' # str |  (optional)
maven2_version = 'maven2_version_example' # str |  (optional)
maven2_generate_pom = true # bool |  (optional)
maven2_packaging = 'maven2_packaging_example' # str |  (optional)
maven2_tag = 'maven2_tag_example' # str |  (optional)
maven2_asset1 = 'maven2_asset1_example' # str |  (optional)
maven2_asset1_classifier = 'maven2_asset1_classifier_example' # str |  (optional)
maven2_asset1_extension = 'maven2_asset1_extension_example' # str |  (optional)
maven2_asset2 = 'maven2_asset2_example' # str |  (optional)
maven2_asset2_classifier = 'maven2_asset2_classifier_example' # str |  (optional)
maven2_asset2_extension = 'maven2_asset2_extension_example' # str |  (optional)
maven2_asset3 = 'maven2_asset3_example' # str |  (optional)
maven2_asset3_classifier = 'maven2_asset3_classifier_example' # str |  (optional)
maven2_asset3_extension = 'maven2_asset3_extension_example' # str |  (optional)

try:
    # Upload a single component
    api_instance.upload_component(repository, helm_tag=helm_tag, helm_asset=helm_asset, r_tag=r_tag, r_asset=r_asset, r_asset_path_id=r_asset_path_id, pypi_tag=pypi_tag, pypi_asset=pypi_asset, docker_tag=docker_tag, docker_asset=docker_asset, yum_directory=yum_directory, yum_tag=yum_tag, yum_asset=yum_asset, yum_asset_filename=yum_asset_filename, rubygems_tag=rubygems_tag, rubygems_asset=rubygems_asset, nuget_tag=nuget_tag, nuget_asset=nuget_asset, npm_tag=npm_tag, npm_asset=npm_asset, raw_directory=raw_directory, raw_tag=raw_tag, raw_asset1=raw_asset1, raw_asset1_filename=raw_asset1_filename, raw_asset2=raw_asset2, raw_asset2_filename=raw_asset2_filename, raw_asset3=raw_asset3, raw_asset3_filename=raw_asset3_filename, apt_tag=apt_tag, apt_asset=apt_asset, maven2_group_id=maven2_group_id, maven2_artifact_id=maven2_artifact_id, maven2_version=maven2_version, maven2_generate_pom=maven2_generate_pom, maven2_packaging=maven2_packaging, maven2_tag=maven2_tag, maven2_asset1=maven2_asset1, maven2_asset1_classifier=maven2_asset1_classifier, maven2_asset1_extension=maven2_asset1_extension, maven2_asset2=maven2_asset2, maven2_asset2_classifier=maven2_asset2_classifier, maven2_asset2_extension=maven2_asset2_extension, maven2_asset3=maven2_asset3, maven2_asset3_classifier=maven2_asset3_classifier, maven2_asset3_extension=maven2_asset3_extension)
except ApiException as e:
    print("Exception when calling ComponentsApi->upload_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **str**| Name of the repository to which you would like to upload the component | 
 **helm_tag** | **str**|  | [optional] 
 **helm_asset** | **str**|  | [optional] 
 **r_tag** | **str**|  | [optional] 
 **r_asset** | **str**|  | [optional] 
 **r_asset_path_id** | **str**|  | [optional] 
 **pypi_tag** | **str**|  | [optional] 
 **pypi_asset** | **str**|  | [optional] 
 **docker_tag** | **str**|  | [optional] 
 **docker_asset** | **str**|  | [optional] 
 **yum_directory** | **str**|  | [optional] 
 **yum_tag** | **str**|  | [optional] 
 **yum_asset** | **str**|  | [optional] 
 **yum_asset_filename** | **str**|  | [optional] 
 **rubygems_tag** | **str**|  | [optional] 
 **rubygems_asset** | **str**|  | [optional] 
 **nuget_tag** | **str**|  | [optional] 
 **nuget_asset** | **str**|  | [optional] 
 **npm_tag** | **str**|  | [optional] 
 **npm_asset** | **str**|  | [optional] 
 **raw_directory** | **str**|  | [optional] 
 **raw_tag** | **str**|  | [optional] 
 **raw_asset1** | **str**|  | [optional] 
 **raw_asset1_filename** | **str**|  | [optional] 
 **raw_asset2** | **str**|  | [optional] 
 **raw_asset2_filename** | **str**|  | [optional] 
 **raw_asset3** | **str**|  | [optional] 
 **raw_asset3_filename** | **str**|  | [optional] 
 **apt_tag** | **str**|  | [optional] 
 **apt_asset** | **str**|  | [optional] 
 **maven2_group_id** | **str**|  | [optional] 
 **maven2_artifact_id** | **str**|  | [optional] 
 **maven2_version** | **str**|  | [optional] 
 **maven2_generate_pom** | **bool**|  | [optional] 
 **maven2_packaging** | **str**|  | [optional] 
 **maven2_tag** | **str**|  | [optional] 
 **maven2_asset1** | **str**|  | [optional] 
 **maven2_asset1_classifier** | **str**|  | [optional] 
 **maven2_asset1_extension** | **str**|  | [optional] 
 **maven2_asset2** | **str**|  | [optional] 
 **maven2_asset2_classifier** | **str**|  | [optional] 
 **maven2_asset2_extension** | **str**|  | [optional] 
 **maven2_asset3** | **str**|  | [optional] 
 **maven2_asset3_classifier** | **str**|  | [optional] 
 **maven2_asset3_extension** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

