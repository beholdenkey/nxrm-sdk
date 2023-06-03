# swagger_client.RepositoryManagementApi

All URIs are relative to */service/rest/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_repository**](RepositoryManagementApi.md#create_repository) | **POST** /v1/repositories/maven/group | Create Maven group repository
[**create_repository1**](RepositoryManagementApi.md#create_repository1) | **POST** /v1/repositories/maven/hosted | Create Maven hosted repository
[**create_repository10**](RepositoryManagementApi.md#create_repository10) | **POST** /v1/repositories/npm/proxy | Create npm proxy repository
[**create_repository11**](RepositoryManagementApi.md#create_repository11) | **POST** /v1/repositories/nuget/group | Create NuGet group repository
[**create_repository12**](RepositoryManagementApi.md#create_repository12) | **POST** /v1/repositories/nuget/hosted | Create NuGet hosted repository
[**create_repository13**](RepositoryManagementApi.md#create_repository13) | **POST** /v1/repositories/nuget/proxy | Create NuGet proxy repository
[**create_repository14**](RepositoryManagementApi.md#create_repository14) | **POST** /v1/repositories/rubygems/group | Create RubyGems group repository
[**create_repository15**](RepositoryManagementApi.md#create_repository15) | **POST** /v1/repositories/rubygems/hosted | Create RubyGems hosted repository
[**create_repository16**](RepositoryManagementApi.md#create_repository16) | **POST** /v1/repositories/rubygems/proxy | Create RubyGems proxy repository
[**create_repository17**](RepositoryManagementApi.md#create_repository17) | **POST** /v1/repositories/yum/group | Create Yum group repository
[**create_repository18**](RepositoryManagementApi.md#create_repository18) | **POST** /v1/repositories/yum/hosted | Create Yum hosted repository
[**create_repository19**](RepositoryManagementApi.md#create_repository19) | **POST** /v1/repositories/yum/proxy | Create Yum proxy repository
[**create_repository2**](RepositoryManagementApi.md#create_repository2) | **POST** /v1/repositories/maven/proxy | Create Maven proxy repository
[**create_repository20**](RepositoryManagementApi.md#create_repository20) | **POST** /v1/repositories/docker/group | Create Docker group repository
[**create_repository21**](RepositoryManagementApi.md#create_repository21) | **POST** /v1/repositories/docker/hosted | Create Docker hosted repository
[**create_repository22**](RepositoryManagementApi.md#create_repository22) | **POST** /v1/repositories/docker/proxy | Create Docker proxy repository
[**create_repository23**](RepositoryManagementApi.md#create_repository23) | **POST** /v1/repositories/pypi/group | Create PyPI group repository
[**create_repository24**](RepositoryManagementApi.md#create_repository24) | **POST** /v1/repositories/pypi/hosted | Create PyPI hosted repository
[**create_repository25**](RepositoryManagementApi.md#create_repository25) | **POST** /v1/repositories/pypi/proxy | Create PyPI proxy repository
[**create_repository26**](RepositoryManagementApi.md#create_repository26) | **POST** /v1/repositories/conda/proxy | Create conda proxy repository
[**create_repository27**](RepositoryManagementApi.md#create_repository27) | **POST** /v1/repositories/conan/proxy | Create Conan proxy repository
[**create_repository28**](RepositoryManagementApi.md#create_repository28) | **POST** /v1/repositories/gitlfs/hosted | Create Git LFS hosted repository
[**create_repository29**](RepositoryManagementApi.md#create_repository29) | **POST** /v1/repositories/r/group | Create R group repository
[**create_repository3**](RepositoryManagementApi.md#create_repository3) | **POST** /v1/repositories/apt/hosted | Create APT hosted repository
[**create_repository30**](RepositoryManagementApi.md#create_repository30) | **POST** /v1/repositories/r/hosted | Create R hosted repository
[**create_repository31**](RepositoryManagementApi.md#create_repository31) | **POST** /v1/repositories/r/proxy | Create R proxy repository
[**create_repository32**](RepositoryManagementApi.md#create_repository32) | **POST** /v1/repositories/cocoapods/proxy | Create Cocoapods proxy repository
[**create_repository33**](RepositoryManagementApi.md#create_repository33) | **POST** /v1/repositories/go/group | Create a Go group repository
[**create_repository34**](RepositoryManagementApi.md#create_repository34) | **POST** /v1/repositories/go/proxy | Create a Go proxy repository
[**create_repository35**](RepositoryManagementApi.md#create_repository35) | **POST** /v1/repositories/p2/proxy | Create p2 proxy repository
[**create_repository36**](RepositoryManagementApi.md#create_repository36) | **POST** /v1/repositories/helm/hosted | Create Helm hosted repository
[**create_repository37**](RepositoryManagementApi.md#create_repository37) | **POST** /v1/repositories/helm/proxy | Create Helm proxy repository
[**create_repository38**](RepositoryManagementApi.md#create_repository38) | **POST** /v1/repositories/bower/group | Create Bower group repository
[**create_repository39**](RepositoryManagementApi.md#create_repository39) | **POST** /v1/repositories/bower/hosted | Create Bower hosted repository
[**create_repository4**](RepositoryManagementApi.md#create_repository4) | **POST** /v1/repositories/apt/proxy | Create APT proxy repository
[**create_repository40**](RepositoryManagementApi.md#create_repository40) | **POST** /v1/repositories/bower/proxy | Create Bower proxy repository
[**create_repository5**](RepositoryManagementApi.md#create_repository5) | **POST** /v1/repositories/raw/group | Create raw group repository
[**create_repository6**](RepositoryManagementApi.md#create_repository6) | **POST** /v1/repositories/raw/hosted | Create raw hosted repository
[**create_repository7**](RepositoryManagementApi.md#create_repository7) | **POST** /v1/repositories/raw/proxy | Create raw proxy repository
[**create_repository8**](RepositoryManagementApi.md#create_repository8) | **POST** /v1/repositories/npm/group | Create npm group repository
[**create_repository9**](RepositoryManagementApi.md#create_repository9) | **POST** /v1/repositories/npm/hosted | Create npm hosted repository
[**delete_repository**](RepositoryManagementApi.md#delete_repository) | **DELETE** /v1/repositories/{repositoryName} | Delete repository of any format
[**disable_repository_health_check**](RepositoryManagementApi.md#disable_repository_health_check) | **DELETE** /v1/repositories/{repositoryName}/health-check | Disable repository health check. Proxy repositories only.
[**enable_repository_health_check**](RepositoryManagementApi.md#enable_repository_health_check) | **POST** /v1/repositories/{repositoryName}/health-check | Enable repository health check. Proxy repositories only.
[**get_repositories**](RepositoryManagementApi.md#get_repositories) | **GET** /v1/repositorySettings | List repositories
[**get_repositories1**](RepositoryManagementApi.md#get_repositories1) | **GET** /v1/repositories | List repositories
[**get_repository**](RepositoryManagementApi.md#get_repository) | **GET** /v1/repositories/{repositoryName} | Get repository details
[**get_repository1**](RepositoryManagementApi.md#get_repository1) | **GET** /v1/repositories/maven/group/{repositoryName} | Get repository
[**get_repository10**](RepositoryManagementApi.md#get_repository10) | **GET** /v1/repositories/npm/hosted/{repositoryName} | Get repository
[**get_repository11**](RepositoryManagementApi.md#get_repository11) | **GET** /v1/repositories/npm/proxy/{repositoryName} | Get repository
[**get_repository12**](RepositoryManagementApi.md#get_repository12) | **GET** /v1/repositories/nuget/group/{repositoryName} | Get repository
[**get_repository13**](RepositoryManagementApi.md#get_repository13) | **GET** /v1/repositories/nuget/hosted/{repositoryName} | Get repository
[**get_repository14**](RepositoryManagementApi.md#get_repository14) | **GET** /v1/repositories/nuget/proxy/{repositoryName} | Get repository
[**get_repository15**](RepositoryManagementApi.md#get_repository15) | **GET** /v1/repositories/rubygems/group/{repositoryName} | Get repository
[**get_repository16**](RepositoryManagementApi.md#get_repository16) | **GET** /v1/repositories/rubygems/hosted/{repositoryName} | Get repository
[**get_repository17**](RepositoryManagementApi.md#get_repository17) | **GET** /v1/repositories/rubygems/proxy/{repositoryName} | Get repository
[**get_repository18**](RepositoryManagementApi.md#get_repository18) | **GET** /v1/repositories/yum/group/{repositoryName} | Get repository
[**get_repository19**](RepositoryManagementApi.md#get_repository19) | **GET** /v1/repositories/yum/hosted/{repositoryName} | Get repository
[**get_repository2**](RepositoryManagementApi.md#get_repository2) | **GET** /v1/repositories/maven/hosted/{repositoryName} | Get repository
[**get_repository20**](RepositoryManagementApi.md#get_repository20) | **GET** /v1/repositories/yum/proxy/{repositoryName} | Get repository
[**get_repository21**](RepositoryManagementApi.md#get_repository21) | **GET** /v1/repositories/docker/group/{repositoryName} | Get repository
[**get_repository22**](RepositoryManagementApi.md#get_repository22) | **GET** /v1/repositories/docker/hosted/{repositoryName} | Get repository
[**get_repository23**](RepositoryManagementApi.md#get_repository23) | **GET** /v1/repositories/docker/proxy/{repositoryName} | Get repository
[**get_repository24**](RepositoryManagementApi.md#get_repository24) | **GET** /v1/repositories/pypi/group/{repositoryName} | Get repository
[**get_repository25**](RepositoryManagementApi.md#get_repository25) | **GET** /v1/repositories/pypi/hosted/{repositoryName} | Get repository
[**get_repository26**](RepositoryManagementApi.md#get_repository26) | **GET** /v1/repositories/pypi/proxy/{repositoryName} | Get repository
[**get_repository27**](RepositoryManagementApi.md#get_repository27) | **GET** /v1/repositories/conda/proxy/{repositoryName} | Get repository
[**get_repository28**](RepositoryManagementApi.md#get_repository28) | **GET** /v1/repositories/conan/proxy/{repositoryName} | Get repository
[**get_repository29**](RepositoryManagementApi.md#get_repository29) | **GET** /v1/repositories/gitlfs/hosted/{repositoryName} | Get repository
[**get_repository3**](RepositoryManagementApi.md#get_repository3) | **GET** /v1/repositories/maven/proxy/{repositoryName} | Get repository
[**get_repository30**](RepositoryManagementApi.md#get_repository30) | **GET** /v1/repositories/r/group/{repositoryName} | Get repository
[**get_repository31**](RepositoryManagementApi.md#get_repository31) | **GET** /v1/repositories/r/hosted/{repositoryName} | Get repository
[**get_repository32**](RepositoryManagementApi.md#get_repository32) | **GET** /v1/repositories/r/proxy/{repositoryName} | Get repository
[**get_repository33**](RepositoryManagementApi.md#get_repository33) | **GET** /v1/repositories/cocoapods/proxy/{repositoryName} | Get repository
[**get_repository34**](RepositoryManagementApi.md#get_repository34) | **GET** /v1/repositories/go/group/{repositoryName} | Get repository
[**get_repository35**](RepositoryManagementApi.md#get_repository35) | **GET** /v1/repositories/go/proxy/{repositoryName} | Get repository
[**get_repository36**](RepositoryManagementApi.md#get_repository36) | **GET** /v1/repositories/p2/proxy/{repositoryName} | Get repository
[**get_repository37**](RepositoryManagementApi.md#get_repository37) | **GET** /v1/repositories/helm/hosted/{repositoryName} | Get repository
[**get_repository38**](RepositoryManagementApi.md#get_repository38) | **GET** /v1/repositories/helm/proxy/{repositoryName} | Get repository
[**get_repository39**](RepositoryManagementApi.md#get_repository39) | **GET** /v1/repositories/bower/group/{repositoryName} | Get repository
[**get_repository4**](RepositoryManagementApi.md#get_repository4) | **GET** /v1/repositories/apt/hosted/{repositoryName} | Get repository
[**get_repository40**](RepositoryManagementApi.md#get_repository40) | **GET** /v1/repositories/bower/hosted/{repositoryName} | Get repository
[**get_repository41**](RepositoryManagementApi.md#get_repository41) | **GET** /v1/repositories/bower/proxy/{repositoryName} | Get repository
[**get_repository5**](RepositoryManagementApi.md#get_repository5) | **GET** /v1/repositories/apt/proxy/{repositoryName} | Get repository
[**get_repository6**](RepositoryManagementApi.md#get_repository6) | **GET** /v1/repositories/raw/group/{repositoryName} | Get repository
[**get_repository7**](RepositoryManagementApi.md#get_repository7) | **GET** /v1/repositories/raw/hosted/{repositoryName} | Get repository
[**get_repository8**](RepositoryManagementApi.md#get_repository8) | **GET** /v1/repositories/raw/proxy/{repositoryName} | Get repository
[**get_repository9**](RepositoryManagementApi.md#get_repository9) | **GET** /v1/repositories/npm/group/{repositoryName} | Get repository
[**invalidate_cache**](RepositoryManagementApi.md#invalidate_cache) | **POST** /v1/repositories/{repositoryName}/invalidate-cache | Invalidate repository cache. Proxy or group repositories only.
[**rebuild_index**](RepositoryManagementApi.md#rebuild_index) | **POST** /v1/repositories/{repositoryName}/rebuild-index | Schedule a &#x27;Repair - Rebuild repository search&#x27; Task. Hosted or proxy repositories only.
[**update_repository**](RepositoryManagementApi.md#update_repository) | **PUT** /v1/repositories/maven/group/{repositoryName} | Update Maven group repository
[**update_repository1**](RepositoryManagementApi.md#update_repository1) | **PUT** /v1/repositories/maven/hosted/{repositoryName} | Update Maven hosted repository
[**update_repository10**](RepositoryManagementApi.md#update_repository10) | **PUT** /v1/repositories/npm/proxy/{repositoryName} | Update npm proxy repository
[**update_repository11**](RepositoryManagementApi.md#update_repository11) | **PUT** /v1/repositories/nuget/group/{repositoryName} | Update NuGet group repository
[**update_repository12**](RepositoryManagementApi.md#update_repository12) | **PUT** /v1/repositories/nuget/hosted/{repositoryName} | Update NuGet hosted repository
[**update_repository13**](RepositoryManagementApi.md#update_repository13) | **PUT** /v1/repositories/nuget/proxy/{repositoryName} | Update NuGet proxy repository
[**update_repository14**](RepositoryManagementApi.md#update_repository14) | **PUT** /v1/repositories/rubygems/group/{repositoryName} | Update RubyGems group repository
[**update_repository15**](RepositoryManagementApi.md#update_repository15) | **PUT** /v1/repositories/rubygems/hosted/{repositoryName} | Update RubyGems hosted repository
[**update_repository16**](RepositoryManagementApi.md#update_repository16) | **PUT** /v1/repositories/rubygems/proxy/{repositoryName} | Update RubyGems proxy repository
[**update_repository17**](RepositoryManagementApi.md#update_repository17) | **PUT** /v1/repositories/yum/group/{repositoryName} | Update Yum group repository
[**update_repository18**](RepositoryManagementApi.md#update_repository18) | **PUT** /v1/repositories/yum/hosted/{repositoryName} | Update Yum hosted repository
[**update_repository19**](RepositoryManagementApi.md#update_repository19) | **PUT** /v1/repositories/yum/proxy/{repositoryName} | Update Yum proxy repository
[**update_repository2**](RepositoryManagementApi.md#update_repository2) | **PUT** /v1/repositories/maven/proxy/{repositoryName} | Update Maven proxy repository
[**update_repository20**](RepositoryManagementApi.md#update_repository20) | **PUT** /v1/repositories/docker/group/{repositoryName} | Update Docker group repository
[**update_repository21**](RepositoryManagementApi.md#update_repository21) | **PUT** /v1/repositories/docker/hosted/{repositoryName} | Update Docker hosted repository
[**update_repository22**](RepositoryManagementApi.md#update_repository22) | **PUT** /v1/repositories/docker/proxy/{repositoryName} | Update Docker group repository
[**update_repository23**](RepositoryManagementApi.md#update_repository23) | **PUT** /v1/repositories/pypi/group/{repositoryName} | Update PyPI group repository
[**update_repository24**](RepositoryManagementApi.md#update_repository24) | **PUT** /v1/repositories/pypi/hosted/{repositoryName} | Update PyPI hosted repository
[**update_repository25**](RepositoryManagementApi.md#update_repository25) | **PUT** /v1/repositories/pypi/proxy/{repositoryName} | Update PyPI proxy repository
[**update_repository26**](RepositoryManagementApi.md#update_repository26) | **PUT** /v1/repositories/conda/proxy/{repositoryName} | Update conda proxy repository
[**update_repository27**](RepositoryManagementApi.md#update_repository27) | **PUT** /v1/repositories/conan/proxy/{repositoryName} | Update Conan proxy repository
[**update_repository28**](RepositoryManagementApi.md#update_repository28) | **PUT** /v1/repositories/gitlfs/hosted/{repositoryName} | Update Git LFS hosted repository
[**update_repository29**](RepositoryManagementApi.md#update_repository29) | **PUT** /v1/repositories/r/group/{repositoryName} | Update R group repository
[**update_repository3**](RepositoryManagementApi.md#update_repository3) | **PUT** /v1/repositories/apt/hosted/{repositoryName} | Update APT hosted repository
[**update_repository30**](RepositoryManagementApi.md#update_repository30) | **PUT** /v1/repositories/r/hosted/{repositoryName} | Update R hosted repository
[**update_repository31**](RepositoryManagementApi.md#update_repository31) | **PUT** /v1/repositories/r/proxy/{repositoryName} | Update R proxy repository
[**update_repository32**](RepositoryManagementApi.md#update_repository32) | **PUT** /v1/repositories/cocoapods/proxy/{repositoryName} | Update Cocoapods proxy repository
[**update_repository33**](RepositoryManagementApi.md#update_repository33) | **PUT** /v1/repositories/go/group/{repositoryName} | Update a Go group repository
[**update_repository34**](RepositoryManagementApi.md#update_repository34) | **PUT** /v1/repositories/go/proxy/{repositoryName} | Update a Go proxy repository
[**update_repository35**](RepositoryManagementApi.md#update_repository35) | **PUT** /v1/repositories/p2/proxy/{repositoryName} | Update p2 proxy repository
[**update_repository36**](RepositoryManagementApi.md#update_repository36) | **PUT** /v1/repositories/helm/hosted/{repositoryName} | Update Helm hosted repository
[**update_repository37**](RepositoryManagementApi.md#update_repository37) | **PUT** /v1/repositories/helm/proxy/{repositoryName} | Update Helm proxy repository
[**update_repository38**](RepositoryManagementApi.md#update_repository38) | **PUT** /v1/repositories/bower/group/{repositoryName} | Update Bower group repository
[**update_repository39**](RepositoryManagementApi.md#update_repository39) | **PUT** /v1/repositories/bower/hosted/{repositoryName} | Update Bower hosted repository
[**update_repository4**](RepositoryManagementApi.md#update_repository4) | **PUT** /v1/repositories/apt/proxy/{repositoryName} | Update APT proxy repository
[**update_repository40**](RepositoryManagementApi.md#update_repository40) | **PUT** /v1/repositories/bower/proxy/{repositoryName} | Update Bower proxy repository
[**update_repository5**](RepositoryManagementApi.md#update_repository5) | **PUT** /v1/repositories/raw/group/{repositoryName} | Update raw group repository
[**update_repository6**](RepositoryManagementApi.md#update_repository6) | **PUT** /v1/repositories/raw/hosted/{repositoryName} | Update raw hosted repository
[**update_repository7**](RepositoryManagementApi.md#update_repository7) | **PUT** /v1/repositories/raw/proxy/{repositoryName} | Update raw proxy repository
[**update_repository8**](RepositoryManagementApi.md#update_repository8) | **PUT** /v1/repositories/npm/group/{repositoryName} | Update npm group repository
[**update_repository9**](RepositoryManagementApi.md#update_repository9) | **PUT** /v1/repositories/npm/hosted/{repositoryName} | Update npm hosted repository

# **create_repository**
> create_repository(body=body)

Create Maven group repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.MavenGroupRepositoryApiRequest() # MavenGroupRepositoryApiRequest |  (optional)

try:
    # Create Maven group repository
    api_instance.create_repository(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MavenGroupRepositoryApiRequest**](MavenGroupRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository1**
> create_repository1(body=body)

Create Maven hosted repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.MavenHostedRepositoryApiRequest() # MavenHostedRepositoryApiRequest |  (optional)

try:
    # Create Maven hosted repository
    api_instance.create_repository1(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MavenHostedRepositoryApiRequest**](MavenHostedRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository10**
> create_repository10(body=body)

Create npm proxy repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.NpmProxyRepositoryApiRequest() # NpmProxyRepositoryApiRequest |  (optional)

try:
    # Create npm proxy repository
    api_instance.create_repository10(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository10: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NpmProxyRepositoryApiRequest**](NpmProxyRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository11**
> create_repository11(body=body)

Create NuGet group repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.NugetGroupRepositoryApiRequest() # NugetGroupRepositoryApiRequest |  (optional)

try:
    # Create NuGet group repository
    api_instance.create_repository11(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository11: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NugetGroupRepositoryApiRequest**](NugetGroupRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository12**
> create_repository12(body=body)

Create NuGet hosted repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.NugetHostedRepositoryApiRequest() # NugetHostedRepositoryApiRequest |  (optional)

try:
    # Create NuGet hosted repository
    api_instance.create_repository12(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository12: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NugetHostedRepositoryApiRequest**](NugetHostedRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository13**
> create_repository13(body=body)

Create NuGet proxy repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.NugetProxyRepositoryApiRequest() # NugetProxyRepositoryApiRequest |  (optional)

try:
    # Create NuGet proxy repository
    api_instance.create_repository13(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository13: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NugetProxyRepositoryApiRequest**](NugetProxyRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository14**
> create_repository14(body=body)

Create RubyGems group repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.RubyGemsGroupRepositoryApiRequest() # RubyGemsGroupRepositoryApiRequest |  (optional)

try:
    # Create RubyGems group repository
    api_instance.create_repository14(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository14: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RubyGemsGroupRepositoryApiRequest**](RubyGemsGroupRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository15**
> create_repository15(body=body)

Create RubyGems hosted repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.RubyGemsHostedRepositoryApiRequest() # RubyGemsHostedRepositoryApiRequest |  (optional)

try:
    # Create RubyGems hosted repository
    api_instance.create_repository15(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository15: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RubyGemsHostedRepositoryApiRequest**](RubyGemsHostedRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository16**
> create_repository16(body=body)

Create RubyGems proxy repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.RubyGemsProxyRepositoryApiRequest() # RubyGemsProxyRepositoryApiRequest |  (optional)

try:
    # Create RubyGems proxy repository
    api_instance.create_repository16(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository16: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RubyGemsProxyRepositoryApiRequest**](RubyGemsProxyRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository17**
> create_repository17(body=body)

Create Yum group repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.YumGroupRepositoryApiRequest() # YumGroupRepositoryApiRequest |  (optional)

try:
    # Create Yum group repository
    api_instance.create_repository17(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository17: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**YumGroupRepositoryApiRequest**](YumGroupRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository18**
> create_repository18(body=body)

Create Yum hosted repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.YumHostedRepositoryApiRequest() # YumHostedRepositoryApiRequest |  (optional)

try:
    # Create Yum hosted repository
    api_instance.create_repository18(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository18: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**YumHostedRepositoryApiRequest**](YumHostedRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository19**
> create_repository19(body=body)

Create Yum proxy repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.YumProxyRepositoryApiRequest() # YumProxyRepositoryApiRequest |  (optional)

try:
    # Create Yum proxy repository
    api_instance.create_repository19(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository19: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**YumProxyRepositoryApiRequest**](YumProxyRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository2**
> create_repository2(body=body)

Create Maven proxy repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.MavenProxyRepositoryApiRequest() # MavenProxyRepositoryApiRequest |  (optional)

try:
    # Create Maven proxy repository
    api_instance.create_repository2(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MavenProxyRepositoryApiRequest**](MavenProxyRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository20**
> create_repository20(body=body)

Create Docker group repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.DockerGroupRepositoryApiRequest() # DockerGroupRepositoryApiRequest |  (optional)

try:
    # Create Docker group repository
    api_instance.create_repository20(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository20: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DockerGroupRepositoryApiRequest**](DockerGroupRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository21**
> create_repository21(body=body)

Create Docker hosted repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.DockerHostedRepositoryApiRequest() # DockerHostedRepositoryApiRequest |  (optional)

try:
    # Create Docker hosted repository
    api_instance.create_repository21(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository21: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DockerHostedRepositoryApiRequest**](DockerHostedRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository22**
> create_repository22(body=body)

Create Docker proxy repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.DockerProxyRepositoryApiRequest() # DockerProxyRepositoryApiRequest |  (optional)

try:
    # Create Docker proxy repository
    api_instance.create_repository22(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository22: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DockerProxyRepositoryApiRequest**](DockerProxyRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository23**
> create_repository23(body=body)

Create PyPI group repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.PypiGroupRepositoryApiRequest() # PypiGroupRepositoryApiRequest |  (optional)

try:
    # Create PyPI group repository
    api_instance.create_repository23(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository23: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PypiGroupRepositoryApiRequest**](PypiGroupRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository24**
> create_repository24(body=body)

Create PyPI hosted repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.PypiHostedRepositoryApiRequest() # PypiHostedRepositoryApiRequest |  (optional)

try:
    # Create PyPI hosted repository
    api_instance.create_repository24(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository24: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PypiHostedRepositoryApiRequest**](PypiHostedRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository25**
> create_repository25(body=body)

Create PyPI proxy repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.PypiProxyRepositoryApiRequest() # PypiProxyRepositoryApiRequest |  (optional)

try:
    # Create PyPI proxy repository
    api_instance.create_repository25(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository25: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PypiProxyRepositoryApiRequest**](PypiProxyRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository26**
> create_repository26(body=body)

Create conda proxy repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.CondaProxyRepositoryApiRequest() # CondaProxyRepositoryApiRequest |  (optional)

try:
    # Create conda proxy repository
    api_instance.create_repository26(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository26: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CondaProxyRepositoryApiRequest**](CondaProxyRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository27**
> create_repository27(body=body)

Create Conan proxy repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.ConanProxyRepositoryApiRequest() # ConanProxyRepositoryApiRequest |  (optional)

try:
    # Create Conan proxy repository
    api_instance.create_repository27(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository27: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConanProxyRepositoryApiRequest**](ConanProxyRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository28**
> create_repository28(body=body)

Create Git LFS hosted repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.GitLfsHostedRepositoryApiRequest() # GitLfsHostedRepositoryApiRequest |  (optional)

try:
    # Create Git LFS hosted repository
    api_instance.create_repository28(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository28: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GitLfsHostedRepositoryApiRequest**](GitLfsHostedRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository29**
> create_repository29(body=body)

Create R group repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.RGroupRepositoryApiRequest() # RGroupRepositoryApiRequest |  (optional)

try:
    # Create R group repository
    api_instance.create_repository29(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository29: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RGroupRepositoryApiRequest**](RGroupRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository3**
> create_repository3(body=body)

Create APT hosted repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.AptHostedRepositoryApiRequest() # AptHostedRepositoryApiRequest |  (optional)

try:
    # Create APT hosted repository
    api_instance.create_repository3(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AptHostedRepositoryApiRequest**](AptHostedRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository30**
> create_repository30(body=body)

Create R hosted repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.RHostedRepositoryApiRequest() # RHostedRepositoryApiRequest |  (optional)

try:
    # Create R hosted repository
    api_instance.create_repository30(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository30: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RHostedRepositoryApiRequest**](RHostedRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository31**
> create_repository31(body=body)

Create R proxy repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.RProxyRepositoryApiRequest() # RProxyRepositoryApiRequest |  (optional)

try:
    # Create R proxy repository
    api_instance.create_repository31(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository31: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RProxyRepositoryApiRequest**](RProxyRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository32**
> create_repository32(body=body)

Create Cocoapods proxy repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.CocoapodsProxyRepositoryApiRequest() # CocoapodsProxyRepositoryApiRequest |  (optional)

try:
    # Create Cocoapods proxy repository
    api_instance.create_repository32(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository32: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CocoapodsProxyRepositoryApiRequest**](CocoapodsProxyRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository33**
> create_repository33(body=body)

Create a Go group repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.GolangGroupRepositoryApiRequest() # GolangGroupRepositoryApiRequest |  (optional)

try:
    # Create a Go group repository
    api_instance.create_repository33(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository33: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GolangGroupRepositoryApiRequest**](GolangGroupRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository34**
> create_repository34(body=body)

Create a Go proxy repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.GolangProxyRepositoryApiRequest() # GolangProxyRepositoryApiRequest |  (optional)

try:
    # Create a Go proxy repository
    api_instance.create_repository34(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository34: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GolangProxyRepositoryApiRequest**](GolangProxyRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository35**
> create_repository35(body=body)

Create p2 proxy repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.P2ProxyRepositoryApiRequest() # P2ProxyRepositoryApiRequest |  (optional)

try:
    # Create p2 proxy repository
    api_instance.create_repository35(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository35: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**P2ProxyRepositoryApiRequest**](P2ProxyRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository36**
> create_repository36(body=body)

Create Helm hosted repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.HelmHostedRepositoryApiRequest() # HelmHostedRepositoryApiRequest |  (optional)

try:
    # Create Helm hosted repository
    api_instance.create_repository36(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository36: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HelmHostedRepositoryApiRequest**](HelmHostedRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository37**
> create_repository37(body=body)

Create Helm proxy repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.HelmProxyRepositoryApiRequest() # HelmProxyRepositoryApiRequest |  (optional)

try:
    # Create Helm proxy repository
    api_instance.create_repository37(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository37: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HelmProxyRepositoryApiRequest**](HelmProxyRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository38**
> create_repository38(body=body)

Create Bower group repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.BowerGroupRepositoryApiRequest() # BowerGroupRepositoryApiRequest |  (optional)

try:
    # Create Bower group repository
    api_instance.create_repository38(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository38: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BowerGroupRepositoryApiRequest**](BowerGroupRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository39**
> create_repository39(body=body)

Create Bower hosted repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.BowerHostedRepositoryApiRequest() # BowerHostedRepositoryApiRequest |  (optional)

try:
    # Create Bower hosted repository
    api_instance.create_repository39(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository39: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BowerHostedRepositoryApiRequest**](BowerHostedRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository4**
> create_repository4(body=body)

Create APT proxy repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.AptProxyRepositoryApiRequest() # AptProxyRepositoryApiRequest |  (optional)

try:
    # Create APT proxy repository
    api_instance.create_repository4(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AptProxyRepositoryApiRequest**](AptProxyRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository40**
> create_repository40(body=body)

Create Bower proxy repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.BowerProxyRepositoryApiRequest() # BowerProxyRepositoryApiRequest |  (optional)

try:
    # Create Bower proxy repository
    api_instance.create_repository40(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository40: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BowerProxyRepositoryApiRequest**](BowerProxyRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository5**
> create_repository5(body=body)

Create raw group repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.RawGroupRepositoryApiRequest() # RawGroupRepositoryApiRequest |  (optional)

try:
    # Create raw group repository
    api_instance.create_repository5(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository5: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RawGroupRepositoryApiRequest**](RawGroupRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository6**
> create_repository6(body=body)

Create raw hosted repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.RawHostedRepositoryApiRequest() # RawHostedRepositoryApiRequest |  (optional)

try:
    # Create raw hosted repository
    api_instance.create_repository6(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository6: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RawHostedRepositoryApiRequest**](RawHostedRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository7**
> create_repository7(body=body)

Create raw proxy repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.RawProxyRepositoryApiRequest() # RawProxyRepositoryApiRequest |  (optional)

try:
    # Create raw proxy repository
    api_instance.create_repository7(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository7: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RawProxyRepositoryApiRequest**](RawProxyRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository8**
> create_repository8(body=body)

Create npm group repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.NpmGroupRepositoryApiRequest() # NpmGroupRepositoryApiRequest |  (optional)

try:
    # Create npm group repository
    api_instance.create_repository8(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository8: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NpmGroupRepositoryApiRequest**](NpmGroupRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository9**
> create_repository9(body=body)

Create npm hosted repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
body = swagger_client.NpmHostedRepositoryApiRequest() # NpmHostedRepositoryApiRequest |  (optional)

try:
    # Create npm hosted repository
    api_instance.create_repository9(body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->create_repository9: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NpmHostedRepositoryApiRequest**](NpmHostedRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_repository**
> delete_repository(repository_name)

Delete repository of any format

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to delete

try:
    # Delete repository of any format
    api_instance.delete_repository(repository_name)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->delete_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_repository_health_check**
> disable_repository_health_check(repository_name)

Disable repository health check. Proxy repositories only.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to disable Repository Health Check for

try:
    # Disable repository health check. Proxy repositories only.
    api_instance.disable_repository_health_check(repository_name)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->disable_repository_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to disable Repository Health Check for | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_repository_health_check**
> enable_repository_health_check(repository_name)

Enable repository health check. Proxy repositories only.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to enable Repository Health Check for

try:
    # Enable repository health check. Proxy repositories only.
    api_instance.enable_repository_health_check(repository_name)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->enable_repository_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to enable Repository Health Check for | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories**
> list[AbstractApiRepository] get_repositories()

List repositories

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()

try:
    # List repositories
    api_response = api_instance.get_repositories()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repositories: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AbstractApiRepository]**](AbstractApiRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories1**
> list[RepositoryXO] get_repositories1()

List repositories

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()

try:
    # List repositories
    api_response = api_instance.get_repositories1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repositories1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[RepositoryXO]**](RepositoryXO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository**
> RepositoryXO get_repository(repository_name)

Get repository details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to get

try:
    # Get repository details
    api_response = api_instance.get_repository(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to get | 

### Return type

[**RepositoryXO**](RepositoryXO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository1**
> SimpleApiGroupRepository get_repository1(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository1(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**SimpleApiGroupRepository**](SimpleApiGroupRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository10**
> SimpleApiHostedRepository get_repository10(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository10(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository10: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**SimpleApiHostedRepository**](SimpleApiHostedRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository11**
> NpmProxyApiRepository get_repository11(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository11(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository11: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**NpmProxyApiRepository**](NpmProxyApiRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository12**
> SimpleApiGroupRepository get_repository12(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository12(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository12: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**SimpleApiGroupRepository**](SimpleApiGroupRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository13**
> SimpleApiHostedRepository get_repository13(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository13(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository13: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**SimpleApiHostedRepository**](SimpleApiHostedRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository14**
> NugetProxyApiRepository get_repository14(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository14(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository14: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**NugetProxyApiRepository**](NugetProxyApiRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository15**
> SimpleApiGroupRepository get_repository15(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository15(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository15: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**SimpleApiGroupRepository**](SimpleApiGroupRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository16**
> SimpleApiHostedRepository get_repository16(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository16(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository16: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**SimpleApiHostedRepository**](SimpleApiHostedRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository17**
> SimpleApiProxyRepository get_repository17(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository17(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository17: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**SimpleApiProxyRepository**](SimpleApiProxyRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository18**
> SimpleApiGroupRepository get_repository18(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository18(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository18: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**SimpleApiGroupRepository**](SimpleApiGroupRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository19**
> YumHostedApiRepository get_repository19(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository19(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository19: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**YumHostedApiRepository**](YumHostedApiRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository2**
> MavenHostedApiRepository get_repository2(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository2(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**MavenHostedApiRepository**](MavenHostedApiRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository20**
> SimpleApiProxyRepository get_repository20(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository20(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository20: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**SimpleApiProxyRepository**](SimpleApiProxyRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository21**
> DockerGroupApiRepository get_repository21(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository21(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository21: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**DockerGroupApiRepository**](DockerGroupApiRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository22**
> DockerHostedApiRepository get_repository22(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository22(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository22: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**DockerHostedApiRepository**](DockerHostedApiRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository23**
> DockerProxyApiRepository get_repository23(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository23(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository23: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**DockerProxyApiRepository**](DockerProxyApiRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository24**
> SimpleApiGroupRepository get_repository24(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository24(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository24: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**SimpleApiGroupRepository**](SimpleApiGroupRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository25**
> SimpleApiHostedRepository get_repository25(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository25(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository25: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**SimpleApiHostedRepository**](SimpleApiHostedRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository26**
> SimpleApiProxyRepository get_repository26(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository26(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository26: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**SimpleApiProxyRepository**](SimpleApiProxyRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository27**
> SimpleApiProxyRepository get_repository27(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository27(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository27: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**SimpleApiProxyRepository**](SimpleApiProxyRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository28**
> SimpleApiProxyRepository get_repository28(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository28(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository28: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**SimpleApiProxyRepository**](SimpleApiProxyRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository29**
> SimpleApiHostedRepository get_repository29(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository29(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository29: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**SimpleApiHostedRepository**](SimpleApiHostedRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository3**
> MavenProxyApiRepository get_repository3(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository3(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**MavenProxyApiRepository**](MavenProxyApiRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository30**
> SimpleApiGroupRepository get_repository30(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository30(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository30: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**SimpleApiGroupRepository**](SimpleApiGroupRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository31**
> SimpleApiHostedRepository get_repository31(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository31(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository31: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**SimpleApiHostedRepository**](SimpleApiHostedRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository32**
> SimpleApiProxyRepository get_repository32(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository32(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository32: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**SimpleApiProxyRepository**](SimpleApiProxyRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository33**
> SimpleApiProxyRepository get_repository33(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository33(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository33: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**SimpleApiProxyRepository**](SimpleApiProxyRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository34**
> SimpleApiGroupRepository get_repository34(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository34(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository34: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**SimpleApiGroupRepository**](SimpleApiGroupRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository35**
> SimpleApiProxyRepository get_repository35(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository35(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository35: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**SimpleApiProxyRepository**](SimpleApiProxyRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository36**
> SimpleApiProxyRepository get_repository36(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository36(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository36: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**SimpleApiProxyRepository**](SimpleApiProxyRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository37**
> SimpleApiHostedRepository get_repository37(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository37(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository37: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**SimpleApiHostedRepository**](SimpleApiHostedRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository38**
> SimpleApiProxyRepository get_repository38(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository38(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository38: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**SimpleApiProxyRepository**](SimpleApiProxyRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository39**
> SimpleApiGroupRepository get_repository39(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository39(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository39: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**SimpleApiGroupRepository**](SimpleApiGroupRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository4**
> AptHostedApiRepository get_repository4(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository4(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**AptHostedApiRepository**](AptHostedApiRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository40**
> SimpleApiHostedRepository get_repository40(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository40(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository40: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**SimpleApiHostedRepository**](SimpleApiHostedRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository41**
> BowerProxyApiRepository get_repository41(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository41(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository41: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**BowerProxyApiRepository**](BowerProxyApiRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository5**
> AptProxyApiRepository get_repository5(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository5(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository5: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**AptProxyApiRepository**](AptProxyApiRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository6**
> SimpleApiGroupRepository get_repository6(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository6(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository6: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**SimpleApiGroupRepository**](SimpleApiGroupRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository7**
> SimpleApiHostedRepository get_repository7(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository7(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository7: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**SimpleApiHostedRepository**](SimpleApiHostedRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository8**
> SimpleApiProxyRepository get_repository8(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository8(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository8: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**SimpleApiProxyRepository**](SimpleApiProxyRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository9**
> SimpleApiGroupDeployRepository get_repository9(repository_name)

Get repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | 

try:
    # Get repository
    api_response = api_instance.get_repository9(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->get_repository9: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 

### Return type

[**SimpleApiGroupDeployRepository**](SimpleApiGroupDeployRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invalidate_cache**
> invalidate_cache(repository_name)

Invalidate repository cache. Proxy or group repositories only.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to invalidate cache

try:
    # Invalidate repository cache. Proxy or group repositories only.
    api_instance.invalidate_cache(repository_name)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->invalidate_cache: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to invalidate cache | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rebuild_index**
> rebuild_index(repository_name)

Schedule a 'Repair - Rebuild repository search' Task. Hosted or proxy repositories only.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to rebuild index

try:
    # Schedule a 'Repair - Rebuild repository search' Task. Hosted or proxy repositories only.
    api_instance.rebuild_index(repository_name)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->rebuild_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to rebuild index | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository**
> update_repository(repository_name, body=body)

Update Maven group repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.MavenGroupRepositoryApiRequest() # MavenGroupRepositoryApiRequest |  (optional)

try:
    # Update Maven group repository
    api_instance.update_repository(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**MavenGroupRepositoryApiRequest**](MavenGroupRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository1**
> update_repository1(repository_name, body=body)

Update Maven hosted repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.MavenHostedRepositoryApiRequest() # MavenHostedRepositoryApiRequest |  (optional)

try:
    # Update Maven hosted repository
    api_instance.update_repository1(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**MavenHostedRepositoryApiRequest**](MavenHostedRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository10**
> update_repository10(repository_name, body=body)

Update npm proxy repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.NpmProxyRepositoryApiRequest() # NpmProxyRepositoryApiRequest |  (optional)

try:
    # Update npm proxy repository
    api_instance.update_repository10(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository10: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**NpmProxyRepositoryApiRequest**](NpmProxyRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository11**
> update_repository11(repository_name, body=body)

Update NuGet group repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.NugetGroupRepositoryApiRequest() # NugetGroupRepositoryApiRequest |  (optional)

try:
    # Update NuGet group repository
    api_instance.update_repository11(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository11: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**NugetGroupRepositoryApiRequest**](NugetGroupRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository12**
> update_repository12(repository_name, body=body)

Update NuGet hosted repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.NugetHostedRepositoryApiRequest() # NugetHostedRepositoryApiRequest |  (optional)

try:
    # Update NuGet hosted repository
    api_instance.update_repository12(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository12: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**NugetHostedRepositoryApiRequest**](NugetHostedRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository13**
> update_repository13(repository_name, body=body)

Update NuGet proxy repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.NugetProxyRepositoryApiRequest() # NugetProxyRepositoryApiRequest |  (optional)

try:
    # Update NuGet proxy repository
    api_instance.update_repository13(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository13: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**NugetProxyRepositoryApiRequest**](NugetProxyRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository14**
> update_repository14(repository_name, body=body)

Update RubyGems group repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.RubyGemsGroupRepositoryApiRequest() # RubyGemsGroupRepositoryApiRequest |  (optional)

try:
    # Update RubyGems group repository
    api_instance.update_repository14(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository14: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**RubyGemsGroupRepositoryApiRequest**](RubyGemsGroupRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository15**
> update_repository15(repository_name, body=body)

Update RubyGems hosted repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.RubyGemsHostedRepositoryApiRequest() # RubyGemsHostedRepositoryApiRequest |  (optional)

try:
    # Update RubyGems hosted repository
    api_instance.update_repository15(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository15: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**RubyGemsHostedRepositoryApiRequest**](RubyGemsHostedRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository16**
> update_repository16(repository_name, body=body)

Update RubyGems proxy repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.RubyGemsProxyRepositoryApiRequest() # RubyGemsProxyRepositoryApiRequest |  (optional)

try:
    # Update RubyGems proxy repository
    api_instance.update_repository16(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository16: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**RubyGemsProxyRepositoryApiRequest**](RubyGemsProxyRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository17**
> update_repository17(repository_name, body=body)

Update Yum group repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.YumGroupRepositoryApiRequest() # YumGroupRepositoryApiRequest |  (optional)

try:
    # Update Yum group repository
    api_instance.update_repository17(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository17: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**YumGroupRepositoryApiRequest**](YumGroupRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository18**
> update_repository18(repository_name, body=body)

Update Yum hosted repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.YumHostedRepositoryApiRequest() # YumHostedRepositoryApiRequest |  (optional)

try:
    # Update Yum hosted repository
    api_instance.update_repository18(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository18: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**YumHostedRepositoryApiRequest**](YumHostedRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository19**
> update_repository19(repository_name, body=body)

Update Yum proxy repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.YumProxyRepositoryApiRequest() # YumProxyRepositoryApiRequest |  (optional)

try:
    # Update Yum proxy repository
    api_instance.update_repository19(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository19: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**YumProxyRepositoryApiRequest**](YumProxyRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository2**
> update_repository2(repository_name, body=body)

Update Maven proxy repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.MavenProxyRepositoryApiRequest() # MavenProxyRepositoryApiRequest |  (optional)

try:
    # Update Maven proxy repository
    api_instance.update_repository2(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**MavenProxyRepositoryApiRequest**](MavenProxyRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository20**
> update_repository20(repository_name, body=body)

Update Docker group repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.DockerGroupRepositoryApiRequest() # DockerGroupRepositoryApiRequest |  (optional)

try:
    # Update Docker group repository
    api_instance.update_repository20(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository20: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**DockerGroupRepositoryApiRequest**](DockerGroupRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository21**
> update_repository21(repository_name, body=body)

Update Docker hosted repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.DockerHostedRepositoryApiRequest() # DockerHostedRepositoryApiRequest |  (optional)

try:
    # Update Docker hosted repository
    api_instance.update_repository21(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository21: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**DockerHostedRepositoryApiRequest**](DockerHostedRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository22**
> update_repository22(repository_name, body=body)

Update Docker group repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.DockerProxyRepositoryApiRequest() # DockerProxyRepositoryApiRequest |  (optional)

try:
    # Update Docker group repository
    api_instance.update_repository22(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository22: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**DockerProxyRepositoryApiRequest**](DockerProxyRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository23**
> update_repository23(repository_name, body=body)

Update PyPI group repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.PypiGroupRepositoryApiRequest() # PypiGroupRepositoryApiRequest |  (optional)

try:
    # Update PyPI group repository
    api_instance.update_repository23(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository23: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**PypiGroupRepositoryApiRequest**](PypiGroupRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository24**
> update_repository24(repository_name, body=body)

Update PyPI hosted repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.PypiHostedRepositoryApiRequest() # PypiHostedRepositoryApiRequest |  (optional)

try:
    # Update PyPI hosted repository
    api_instance.update_repository24(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository24: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**PypiHostedRepositoryApiRequest**](PypiHostedRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository25**
> update_repository25(repository_name, body=body)

Update PyPI proxy repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.PypiProxyRepositoryApiRequest() # PypiProxyRepositoryApiRequest |  (optional)

try:
    # Update PyPI proxy repository
    api_instance.update_repository25(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository25: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**PypiProxyRepositoryApiRequest**](PypiProxyRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository26**
> update_repository26(repository_name, body=body)

Update conda proxy repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.CondaProxyRepositoryApiRequest() # CondaProxyRepositoryApiRequest |  (optional)

try:
    # Update conda proxy repository
    api_instance.update_repository26(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository26: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**CondaProxyRepositoryApiRequest**](CondaProxyRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository27**
> update_repository27(repository_name, body=body)

Update Conan proxy repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.ConanProxyRepositoryApiRequest() # ConanProxyRepositoryApiRequest |  (optional)

try:
    # Update Conan proxy repository
    api_instance.update_repository27(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository27: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**ConanProxyRepositoryApiRequest**](ConanProxyRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository28**
> update_repository28(repository_name, body=body)

Update Git LFS hosted repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.GitLfsHostedRepositoryApiRequest() # GitLfsHostedRepositoryApiRequest |  (optional)

try:
    # Update Git LFS hosted repository
    api_instance.update_repository28(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository28: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**GitLfsHostedRepositoryApiRequest**](GitLfsHostedRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository29**
> update_repository29(repository_name, body=body)

Update R group repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.RGroupRepositoryApiRequest() # RGroupRepositoryApiRequest |  (optional)

try:
    # Update R group repository
    api_instance.update_repository29(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository29: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**RGroupRepositoryApiRequest**](RGroupRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository3**
> update_repository3(repository_name, body=body)

Update APT hosted repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.AptHostedRepositoryApiRequest() # AptHostedRepositoryApiRequest |  (optional)

try:
    # Update APT hosted repository
    api_instance.update_repository3(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**AptHostedRepositoryApiRequest**](AptHostedRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository30**
> update_repository30(repository_name, body=body)

Update R hosted repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.RHostedRepositoryApiRequest() # RHostedRepositoryApiRequest |  (optional)

try:
    # Update R hosted repository
    api_instance.update_repository30(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository30: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**RHostedRepositoryApiRequest**](RHostedRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository31**
> update_repository31(repository_name, body=body)

Update R proxy repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.RProxyRepositoryApiRequest() # RProxyRepositoryApiRequest |  (optional)

try:
    # Update R proxy repository
    api_instance.update_repository31(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository31: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**RProxyRepositoryApiRequest**](RProxyRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository32**
> update_repository32(repository_name, body=body)

Update Cocoapods proxy repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.CocoapodsProxyRepositoryApiRequest() # CocoapodsProxyRepositoryApiRequest |  (optional)

try:
    # Update Cocoapods proxy repository
    api_instance.update_repository32(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository32: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**CocoapodsProxyRepositoryApiRequest**](CocoapodsProxyRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository33**
> update_repository33(repository_name, body=body)

Update a Go group repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.GolangGroupRepositoryApiRequest() # GolangGroupRepositoryApiRequest |  (optional)

try:
    # Update a Go group repository
    api_instance.update_repository33(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository33: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**GolangGroupRepositoryApiRequest**](GolangGroupRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository34**
> update_repository34(repository_name, body=body)

Update a Go proxy repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.GolangProxyRepositoryApiRequest() # GolangProxyRepositoryApiRequest |  (optional)

try:
    # Update a Go proxy repository
    api_instance.update_repository34(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository34: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**GolangProxyRepositoryApiRequest**](GolangProxyRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository35**
> update_repository35(repository_name, body=body)

Update p2 proxy repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.P2ProxyRepositoryApiRequest() # P2ProxyRepositoryApiRequest |  (optional)

try:
    # Update p2 proxy repository
    api_instance.update_repository35(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository35: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**P2ProxyRepositoryApiRequest**](P2ProxyRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository36**
> update_repository36(repository_name, body=body)

Update Helm hosted repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.HelmHostedRepositoryApiRequest() # HelmHostedRepositoryApiRequest |  (optional)

try:
    # Update Helm hosted repository
    api_instance.update_repository36(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository36: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**HelmHostedRepositoryApiRequest**](HelmHostedRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository37**
> update_repository37(repository_name, body=body)

Update Helm proxy repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.HelmProxyRepositoryApiRequest() # HelmProxyRepositoryApiRequest |  (optional)

try:
    # Update Helm proxy repository
    api_instance.update_repository37(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository37: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**HelmProxyRepositoryApiRequest**](HelmProxyRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository38**
> update_repository38(repository_name, body=body)

Update Bower group repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.BowerGroupRepositoryApiRequest() # BowerGroupRepositoryApiRequest |  (optional)

try:
    # Update Bower group repository
    api_instance.update_repository38(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository38: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**BowerGroupRepositoryApiRequest**](BowerGroupRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository39**
> update_repository39(repository_name, body=body)

Update Bower hosted repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.BowerHostedRepositoryApiRequest() # BowerHostedRepositoryApiRequest |  (optional)

try:
    # Update Bower hosted repository
    api_instance.update_repository39(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository39: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**BowerHostedRepositoryApiRequest**](BowerHostedRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository4**
> update_repository4(repository_name, body=body)

Update APT proxy repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.AptProxyRepositoryApiRequest() # AptProxyRepositoryApiRequest |  (optional)

try:
    # Update APT proxy repository
    api_instance.update_repository4(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**AptProxyRepositoryApiRequest**](AptProxyRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository40**
> update_repository40(repository_name, body=body)

Update Bower proxy repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.BowerProxyRepositoryApiRequest() # BowerProxyRepositoryApiRequest |  (optional)

try:
    # Update Bower proxy repository
    api_instance.update_repository40(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository40: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**BowerProxyRepositoryApiRequest**](BowerProxyRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository5**
> update_repository5(repository_name, body=body)

Update raw group repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.RawGroupRepositoryApiRequest() # RawGroupRepositoryApiRequest |  (optional)

try:
    # Update raw group repository
    api_instance.update_repository5(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository5: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**RawGroupRepositoryApiRequest**](RawGroupRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository6**
> update_repository6(repository_name, body=body)

Update raw hosted repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.RawHostedRepositoryApiRequest() # RawHostedRepositoryApiRequest |  (optional)

try:
    # Update raw hosted repository
    api_instance.update_repository6(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository6: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**RawHostedRepositoryApiRequest**](RawHostedRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository7**
> update_repository7(repository_name, body=body)

Update raw proxy repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.RawProxyRepositoryApiRequest() # RawProxyRepositoryApiRequest |  (optional)

try:
    # Update raw proxy repository
    api_instance.update_repository7(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository7: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**RawProxyRepositoryApiRequest**](RawProxyRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository8**
> update_repository8(repository_name, body=body)

Update npm group repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.NpmGroupRepositoryApiRequest() # NpmGroupRepositoryApiRequest |  (optional)

try:
    # Update npm group repository
    api_instance.update_repository8(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository8: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**NpmGroupRepositoryApiRequest**](NpmGroupRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository9**
> update_repository9(repository_name, body=body)

Update npm hosted repository

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RepositoryManagementApi()
repository_name = 'repository_name_example' # str | Name of the repository to update
body = swagger_client.NpmHostedRepositoryApiRequest() # NpmHostedRepositoryApiRequest |  (optional)

try:
    # Update npm hosted repository
    api_instance.update_repository9(repository_name, body=body)
except ApiException as e:
    print("Exception when calling RepositoryManagementApi->update_repository9: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to update | 
 **body** | [**NpmHostedRepositoryApiRequest**](NpmHostedRepositoryApiRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

