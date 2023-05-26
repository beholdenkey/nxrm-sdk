<a id="__pageTop"></a>

# nexus_sdk.apis.tags.repository_management_api.RepositoryManagementApi

All URIs are relative to _http://localhost/service/rest_

| Method                                                                  | HTTP request                                                | Description                                                                                        |
| ----------------------------------------------------------------------- | ----------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| [**create_repository**](#create_repository)                             | **post** /v1/repositories/maven/group                       | Create Maven group repository                                                                      |
| [**create_repository1**](#create_repository1)                           | **post** /v1/repositories/maven/hosted                      | Create Maven hosted repository                                                                     |
| [**create_repository10**](#create_repository10)                         | **post** /v1/repositories/npm/proxy                         | Create npm proxy repository                                                                        |
| [**create_repository11**](#create_repository11)                         | **post** /v1/repositories/nuget/group                       | Create NuGet group repository                                                                      |
| [**create_repository12**](#create_repository12)                         | **post** /v1/repositories/nuget/hosted                      | Create NuGet hosted repository                                                                     |
| [**create_repository13**](#create_repository13)                         | **post** /v1/repositories/nuget/proxy                       | Create NuGet proxy repository                                                                      |
| [**create_repository14**](#create_repository14)                         | **post** /v1/repositories/rubygems/group                    | Create RubyGems group repository                                                                   |
| [**create_repository15**](#create_repository15)                         | **post** /v1/repositories/rubygems/hosted                   | Create RubyGems hosted repository                                                                  |
| [**create_repository16**](#create_repository16)                         | **post** /v1/repositories/rubygems/proxy                    | Create RubyGems proxy repository                                                                   |
| [**create_repository17**](#create_repository17)                         | **post** /v1/repositories/yum/group                         | Create Yum group repository                                                                        |
| [**create_repository18**](#create_repository18)                         | **post** /v1/repositories/yum/hosted                        | Create Yum hosted repository                                                                       |
| [**create_repository19**](#create_repository19)                         | **post** /v1/repositories/yum/proxy                         | Create Yum proxy repository                                                                        |
| [**create_repository2**](#create_repository2)                           | **post** /v1/repositories/maven/proxy                       | Create Maven proxy repository                                                                      |
| [**create_repository20**](#create_repository20)                         | **post** /v1/repositories/docker/group                      | Create Docker group repository                                                                     |
| [**create_repository21**](#create_repository21)                         | **post** /v1/repositories/docker/hosted                     | Create Docker hosted repository                                                                    |
| [**create_repository22**](#create_repository22)                         | **post** /v1/repositories/docker/proxy                      | Create Docker proxy repository                                                                     |
| [**create_repository23**](#create_repository23)                         | **post** /v1/repositories/pypi/group                        | Create PyPI group repository                                                                       |
| [**create_repository24**](#create_repository24)                         | **post** /v1/repositories/pypi/hosted                       | Create PyPI hosted repository                                                                      |
| [**create_repository25**](#create_repository25)                         | **post** /v1/repositories/pypi/proxy                        | Create PyPI proxy repository                                                                       |
| [**create_repository26**](#create_repository26)                         | **post** /v1/repositories/conda/proxy                       | Create conda proxy repository                                                                      |
| [**create_repository27**](#create_repository27)                         | **post** /v1/repositories/conan/proxy                       | Create Conan proxy repository                                                                      |
| [**create_repository28**](#create_repository28)                         | **post** /v1/repositories/gitlfs/hosted                     | Create Git LFS hosted repository                                                                   |
| [**create_repository29**](#create_repository29)                         | **post** /v1/repositories/r/group                           | Create R group repository                                                                          |
| [**create_repository3**](#create_repository3)                           | **post** /v1/repositories/apt/hosted                        | Create APT hosted repository                                                                       |
| [**create_repository30**](#create_repository30)                         | **post** /v1/repositories/r/hosted                          | Create R hosted repository                                                                         |
| [**create_repository31**](#create_repository31)                         | **post** /v1/repositories/r/proxy                           | Create R proxy repository                                                                          |
| [**create_repository32**](#create_repository32)                         | **post** /v1/repositories/cocoapods/proxy                   | Create Cocoapods proxy repository                                                                  |
| [**create_repository33**](#create_repository33)                         | **post** /v1/repositories/go/group                          | Create a Go group repository                                                                       |
| [**create_repository34**](#create_repository34)                         | **post** /v1/repositories/go/proxy                          | Create a Go proxy repository                                                                       |
| [**create_repository35**](#create_repository35)                         | **post** /v1/repositories/p2/proxy                          | Create p2 proxy repository                                                                         |
| [**create_repository36**](#create_repository36)                         | **post** /v1/repositories/helm/hosted                       | Create Helm hosted repository                                                                      |
| [**create_repository37**](#create_repository37)                         | **post** /v1/repositories/helm/proxy                        | Create Helm proxy repository                                                                       |
| [**create_repository38**](#create_repository38)                         | **post** /v1/repositories/bower/group                       | Create Bower group repository                                                                      |
| [**create_repository39**](#create_repository39)                         | **post** /v1/repositories/bower/hosted                      | Create Bower hosted repository                                                                     |
| [**create_repository4**](#create_repository4)                           | **post** /v1/repositories/apt/proxy                         | Create APT proxy repository                                                                        |
| [**create_repository40**](#create_repository40)                         | **post** /v1/repositories/bower/proxy                       | Create Bower proxy repository                                                                      |
| [**create_repository5**](#create_repository5)                           | **post** /v1/repositories/raw/group                         | Create raw group repository                                                                        |
| [**create_repository6**](#create_repository6)                           | **post** /v1/repositories/raw/hosted                        | Create raw hosted repository                                                                       |
| [**create_repository7**](#create_repository7)                           | **post** /v1/repositories/raw/proxy                         | Create raw proxy repository                                                                        |
| [**create_repository8**](#create_repository8)                           | **post** /v1/repositories/npm/group                         | Create npm group repository                                                                        |
| [**create_repository9**](#create_repository9)                           | **post** /v1/repositories/npm/hosted                        | Create npm hosted repository                                                                       |
| [**delete_repository**](#delete_repository)                             | **delete** /v1/repositories/{repositoryName}                | Delete repository of any format                                                                    |
| [**disable_repository_health_check**](#disable_repository_health_check) | **delete** /v1/repositories/{repositoryName}/health-check   | Disable repository health check. Proxy repositories only.                                          |
| [**enable_repository_health_check**](#enable_repository_health_check)   | **post** /v1/repositories/{repositoryName}/health-check     | Enable repository health check. Proxy repositories only.                                           |
| [**get_repositories**](#get_repositories)                               | **get** /v1/repositorySettings                              | List repositories                                                                                  |
| [**get_repositories1**](#get_repositories1)                             | **get** /v1/repositories                                    | List repositories                                                                                  |
| [**get_repository**](#get_repository)                                   | **get** /v1/repositories/{repositoryName}                   | Get repository details                                                                             |
| [**get_repository1**](#get_repository1)                                 | **get** /v1/repositories/maven/group/{repositoryName}       | Get repository                                                                                     |
| [**get_repository10**](#get_repository10)                               | **get** /v1/repositories/npm/hosted/{repositoryName}        | Get repository                                                                                     |
| [**get_repository11**](#get_repository11)                               | **get** /v1/repositories/npm/proxy/{repositoryName}         | Get repository                                                                                     |
| [**get_repository12**](#get_repository12)                               | **get** /v1/repositories/nuget/group/{repositoryName}       | Get repository                                                                                     |
| [**get_repository13**](#get_repository13)                               | **get** /v1/repositories/nuget/hosted/{repositoryName}      | Get repository                                                                                     |
| [**get_repository14**](#get_repository14)                               | **get** /v1/repositories/nuget/proxy/{repositoryName}       | Get repository                                                                                     |
| [**get_repository15**](#get_repository15)                               | **get** /v1/repositories/rubygems/group/{repositoryName}    | Get repository                                                                                     |
| [**get_repository16**](#get_repository16)                               | **get** /v1/repositories/rubygems/hosted/{repositoryName}   | Get repository                                                                                     |
| [**get_repository17**](#get_repository17)                               | **get** /v1/repositories/rubygems/proxy/{repositoryName}    | Get repository                                                                                     |
| [**get_repository18**](#get_repository18)                               | **get** /v1/repositories/yum/group/{repositoryName}         | Get repository                                                                                     |
| [**get_repository19**](#get_repository19)                               | **get** /v1/repositories/yum/hosted/{repositoryName}        | Get repository                                                                                     |
| [**get_repository2**](#get_repository2)                                 | **get** /v1/repositories/maven/hosted/{repositoryName}      | Get repository                                                                                     |
| [**get_repository20**](#get_repository20)                               | **get** /v1/repositories/yum/proxy/{repositoryName}         | Get repository                                                                                     |
| [**get_repository21**](#get_repository21)                               | **get** /v1/repositories/docker/group/{repositoryName}      | Get repository                                                                                     |
| [**get_repository22**](#get_repository22)                               | **get** /v1/repositories/docker/hosted/{repositoryName}     | Get repository                                                                                     |
| [**get_repository23**](#get_repository23)                               | **get** /v1/repositories/docker/proxy/{repositoryName}      | Get repository                                                                                     |
| [**get_repository24**](#get_repository24)                               | **get** /v1/repositories/pypi/group/{repositoryName}        | Get repository                                                                                     |
| [**get_repository25**](#get_repository25)                               | **get** /v1/repositories/pypi/hosted/{repositoryName}       | Get repository                                                                                     |
| [**get_repository26**](#get_repository26)                               | **get** /v1/repositories/pypi/proxy/{repositoryName}        | Get repository                                                                                     |
| [**get_repository27**](#get_repository27)                               | **get** /v1/repositories/conda/proxy/{repositoryName}       | Get repository                                                                                     |
| [**get_repository28**](#get_repository28)                               | **get** /v1/repositories/conan/proxy/{repositoryName}       | Get repository                                                                                     |
| [**get_repository29**](#get_repository29)                               | **get** /v1/repositories/gitlfs/hosted/{repositoryName}     | Get repository                                                                                     |
| [**get_repository3**](#get_repository3)                                 | **get** /v1/repositories/maven/proxy/{repositoryName}       | Get repository                                                                                     |
| [**get_repository30**](#get_repository30)                               | **get** /v1/repositories/r/group/{repositoryName}           | Get repository                                                                                     |
| [**get_repository31**](#get_repository31)                               | **get** /v1/repositories/r/hosted/{repositoryName}          | Get repository                                                                                     |
| [**get_repository32**](#get_repository32)                               | **get** /v1/repositories/r/proxy/{repositoryName}           | Get repository                                                                                     |
| [**get_repository33**](#get_repository33)                               | **get** /v1/repositories/cocoapods/proxy/{repositoryName}   | Get repository                                                                                     |
| [**get_repository34**](#get_repository34)                               | **get** /v1/repositories/go/group/{repositoryName}          | Get repository                                                                                     |
| [**get_repository35**](#get_repository35)                               | **get** /v1/repositories/go/proxy/{repositoryName}          | Get repository                                                                                     |
| [**get_repository36**](#get_repository36)                               | **get** /v1/repositories/p2/proxy/{repositoryName}          | Get repository                                                                                     |
| [**get_repository37**](#get_repository37)                               | **get** /v1/repositories/helm/hosted/{repositoryName}       | Get repository                                                                                     |
| [**get_repository38**](#get_repository38)                               | **get** /v1/repositories/helm/proxy/{repositoryName}        | Get repository                                                                                     |
| [**get_repository39**](#get_repository39)                               | **get** /v1/repositories/bower/group/{repositoryName}       | Get repository                                                                                     |
| [**get_repository4**](#get_repository4)                                 | **get** /v1/repositories/apt/hosted/{repositoryName}        | Get repository                                                                                     |
| [**get_repository40**](#get_repository40)                               | **get** /v1/repositories/bower/hosted/{repositoryName}      | Get repository                                                                                     |
| [**get_repository41**](#get_repository41)                               | **get** /v1/repositories/bower/proxy/{repositoryName}       | Get repository                                                                                     |
| [**get_repository5**](#get_repository5)                                 | **get** /v1/repositories/apt/proxy/{repositoryName}         | Get repository                                                                                     |
| [**get_repository6**](#get_repository6)                                 | **get** /v1/repositories/raw/group/{repositoryName}         | Get repository                                                                                     |
| [**get_repository7**](#get_repository7)                                 | **get** /v1/repositories/raw/hosted/{repositoryName}        | Get repository                                                                                     |
| [**get_repository8**](#get_repository8)                                 | **get** /v1/repositories/raw/proxy/{repositoryName}         | Get repository                                                                                     |
| [**get_repository9**](#get_repository9)                                 | **get** /v1/repositories/npm/group/{repositoryName}         | Get repository                                                                                     |
| [**invalidate_cache**](#invalidate_cache)                               | **post** /v1/repositories/{repositoryName}/invalidate-cache | Invalidate repository cache. Proxy or group repositories only.                                     |
| [**rebuild_index**](#rebuild_index)                                     | **post** /v1/repositories/{repositoryName}/rebuild-index    | Schedule a &#x27;Repair - Rebuild repository search&#x27; Task. Hosted or proxy repositories only. |
| [**update_repository**](#update_repository)                             | **put** /v1/repositories/maven/group/{repositoryName}       | Update Maven group repository                                                                      |
| [**update_repository1**](#update_repository1)                           | **put** /v1/repositories/maven/hosted/{repositoryName}      | Update Maven hosted repository                                                                     |
| [**update_repository10**](#update_repository10)                         | **put** /v1/repositories/npm/proxy/{repositoryName}         | Update npm proxy repository                                                                        |
| [**update_repository11**](#update_repository11)                         | **put** /v1/repositories/nuget/group/{repositoryName}       | Update NuGet group repository                                                                      |
| [**update_repository12**](#update_repository12)                         | **put** /v1/repositories/nuget/hosted/{repositoryName}      | Update NuGet hosted repository                                                                     |
| [**update_repository13**](#update_repository13)                         | **put** /v1/repositories/nuget/proxy/{repositoryName}       | Update NuGet proxy repository                                                                      |
| [**update_repository14**](#update_repository14)                         | **put** /v1/repositories/rubygems/group/{repositoryName}    | Update RubyGems group repository                                                                   |
| [**update_repository15**](#update_repository15)                         | **put** /v1/repositories/rubygems/hosted/{repositoryName}   | Update RubyGems hosted repository                                                                  |
| [**update_repository16**](#update_repository16)                         | **put** /v1/repositories/rubygems/proxy/{repositoryName}    | Update RubyGems proxy repository                                                                   |
| [**update_repository17**](#update_repository17)                         | **put** /v1/repositories/yum/group/{repositoryName}         | Update Yum group repository                                                                        |
| [**update_repository18**](#update_repository18)                         | **put** /v1/repositories/yum/hosted/{repositoryName}        | Update Yum hosted repository                                                                       |
| [**update_repository19**](#update_repository19)                         | **put** /v1/repositories/yum/proxy/{repositoryName}         | Update Yum proxy repository                                                                        |
| [**update_repository2**](#update_repository2)                           | **put** /v1/repositories/maven/proxy/{repositoryName}       | Update Maven proxy repository                                                                      |
| [**update_repository20**](#update_repository20)                         | **put** /v1/repositories/docker/group/{repositoryName}      | Update Docker group repository                                                                     |
| [**update_repository21**](#update_repository21)                         | **put** /v1/repositories/docker/hosted/{repositoryName}     | Update Docker hosted repository                                                                    |
| [**update_repository22**](#update_repository22)                         | **put** /v1/repositories/docker/proxy/{repositoryName}      | Update Docker group repository                                                                     |
| [**update_repository23**](#update_repository23)                         | **put** /v1/repositories/pypi/group/{repositoryName}        | Update PyPI group repository                                                                       |
| [**update_repository24**](#update_repository24)                         | **put** /v1/repositories/pypi/hosted/{repositoryName}       | Update PyPI hosted repository                                                                      |
| [**update_repository25**](#update_repository25)                         | **put** /v1/repositories/pypi/proxy/{repositoryName}        | Update PyPI proxy repository                                                                       |
| [**update_repository26**](#update_repository26)                         | **put** /v1/repositories/conda/proxy/{repositoryName}       | Update conda proxy repository                                                                      |
| [**update_repository27**](#update_repository27)                         | **put** /v1/repositories/conan/proxy/{repositoryName}       | Update Conan proxy repository                                                                      |
| [**update_repository28**](#update_repository28)                         | **put** /v1/repositories/gitlfs/hosted/{repositoryName}     | Update Git LFS hosted repository                                                                   |
| [**update_repository29**](#update_repository29)                         | **put** /v1/repositories/r/group/{repositoryName}           | Update R group repository                                                                          |
| [**update_repository3**](#update_repository3)                           | **put** /v1/repositories/apt/hosted/{repositoryName}        | Update APT hosted repository                                                                       |
| [**update_repository30**](#update_repository30)                         | **put** /v1/repositories/r/hosted/{repositoryName}          | Update R hosted repository                                                                         |
| [**update_repository31**](#update_repository31)                         | **put** /v1/repositories/r/proxy/{repositoryName}           | Update R proxy repository                                                                          |
| [**update_repository32**](#update_repository32)                         | **put** /v1/repositories/cocoapods/proxy/{repositoryName}   | Update Cocoapods proxy repository                                                                  |
| [**update_repository33**](#update_repository33)                         | **put** /v1/repositories/go/group/{repositoryName}          | Update a Go group repository                                                                       |
| [**update_repository34**](#update_repository34)                         | **put** /v1/repositories/go/proxy/{repositoryName}          | Update a Go proxy repository                                                                       |
| [**update_repository35**](#update_repository35)                         | **put** /v1/repositories/p2/proxy/{repositoryName}          | Update p2 proxy repository                                                                         |
| [**update_repository36**](#update_repository36)                         | **put** /v1/repositories/helm/hosted/{repositoryName}       | Update Helm hosted repository                                                                      |
| [**update_repository37**](#update_repository37)                         | **put** /v1/repositories/helm/proxy/{repositoryName}        | Update Helm proxy repository                                                                       |
| [**update_repository38**](#update_repository38)                         | **put** /v1/repositories/bower/group/{repositoryName}       | Update Bower group repository                                                                      |
| [**update_repository39**](#update_repository39)                         | **put** /v1/repositories/bower/hosted/{repositoryName}      | Update Bower hosted repository                                                                     |
| [**update_repository4**](#update_repository4)                           | **put** /v1/repositories/apt/proxy/{repositoryName}         | Update APT proxy repository                                                                        |
| [**update_repository40**](#update_repository40)                         | **put** /v1/repositories/bower/proxy/{repositoryName}       | Update Bower proxy repository                                                                      |
| [**update_repository5**](#update_repository5)                           | **put** /v1/repositories/raw/group/{repositoryName}         | Update raw group repository                                                                        |
| [**update_repository6**](#update_repository6)                           | **put** /v1/repositories/raw/hosted/{repositoryName}        | Update raw hosted repository                                                                       |
| [**update_repository7**](#update_repository7)                           | **put** /v1/repositories/raw/proxy/{repositoryName}         | Update raw proxy repository                                                                        |
| [**update_repository8**](#update_repository8)                           | **put** /v1/repositories/npm/group/{repositoryName}         | Update npm group repository                                                                        |
| [**update_repository9**](#update_repository9)                           | **put** /v1/repositories/npm/hosted/{repositoryName}        | Update npm hosted repository                                                                       |

# **create_repository**

<a id="create_repository"></a>

> create_repository()

Create Maven group repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.maven_group_repository_api_request import MavenGroupRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = MavenGroupRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        group=GroupAttributes(
            member_names=[
                "member_names_example"
            ],
        ),
    )
    try:
        # Create Maven group repository
        api_response = api_instance.create_repository(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                 | Description | Notes |
| ------------------------------------------------------------------------------------ | ----------- | ----- |
| [**MavenGroupRepositoryApiRequest**](../../models/MavenGroupRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                     | Description                                                 |
| ---- | --------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization              | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository.ApiResponseFor403) | Insufficient permissions                                    |

#### create_repository.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository1**

<a id="create_repository1"></a>

> create_repository1()

Create Maven hosted repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.maven_hosted_repository_api_request import MavenHostedRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = MavenHostedRepositoryApiRequest(
        name="internal",
        online=True,
        storage=HostedStorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
            write_policy="allow_once",
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        component=ComponentAttributes(
            proprietary_components=True,
        ),
        maven=MavenAttributes(
            version_policy="MIXED",
            layout_policy="STRICT",
            content_disposition="ATTACHMENT",
        ),
    )
    try:
        # Create Maven hosted repository
        api_response = api_instance.create_repository1(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository1: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                   | Description | Notes |
| -------------------------------------------------------------------------------------- | ----------- | ----- |
| [**MavenHostedRepositoryApiRequest**](../../models/MavenHostedRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                      | Description                                                 |
| ---- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization               | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository1.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository1.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository1.ApiResponseFor403) | Insufficient permissions                                    |

#### create_repository1.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository1.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository1.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository10**

<a id="create_repository10"></a>

> create_repository10()

Create npm proxy repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.npm_proxy_repository_api_request import NpmProxyRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = NpmProxyRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        proxy=ProxyAttributes(
            remote_url="https://remote.repository.com",
            content_max_age=1440,
            metadata_max_age=1440,
        ),
        negative_cache=NegativeCacheAttributes(
            enabled=True,
            time_to_live=1440,
        ),
        http_client=HttpClientAttributes(
            blocked=False,
            auto_block=True,
            connection=HttpClientConnectionAttributes(
                retries=0,
                user_agent_suffix="user_agent_suffix_example",
                timeout=60,
                enable_circular_redirects=False,
                enable_cookies=False,
                use_trust_store=False,
            ),
            authentication=HttpClientConnectionAuthenticationAttributes(
                type="username",
                username="username_example",
                password="password_example",
                ntlm_host="ntlm_host_example",
                ntlm_domain="ntlm_domain_example",
            ),
        ),
        routing_rule="routing_rule_example",
        replication=ReplicationAttributes(
            preemptive_pull_enabled=True,
            asset_path_regex="asset_path_regex_example",
        ),
        npm=NpmAttributes(
            remove_non_cataloged=True,
            remove_quarantined=True,
        ),
    )
    try:
        # Create npm proxy repository
        api_response = api_instance.create_repository10(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository10: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                             | Description | Notes |
| -------------------------------------------------------------------------------- | ----------- | ----- |
| [**NpmProxyRepositoryApiRequest**](../../models/NpmProxyRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository10.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository10.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository10.ApiResponseFor403) | Insufficient permissions                                    |

#### create_repository10.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository10.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository10.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository11**

<a id="create_repository11"></a>

> create_repository11()

Create NuGet group repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.nuget_group_repository_api_request import NugetGroupRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = NugetGroupRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        group=GroupAttributes(
            member_names=[
                "member_names_example"
            ],
        ),
    )
    try:
        # Create NuGet group repository
        api_response = api_instance.create_repository11(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository11: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                 | Description | Notes |
| ------------------------------------------------------------------------------------ | ----------- | ----- |
| [**NugetGroupRepositoryApiRequest**](../../models/NugetGroupRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository11.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository11.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository11.ApiResponseFor403) | Insufficient permissions                                    |

#### create_repository11.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository11.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository11.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository12**

<a id="create_repository12"></a>

> create_repository12()

Create NuGet hosted repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.nuget_hosted_repository_api_request import NugetHostedRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = NugetHostedRepositoryApiRequest(
        name="internal",
        online=True,
        storage=HostedStorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
            write_policy="allow_once",
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        component=ComponentAttributes(
            proprietary_components=True,
        ),
    )
    try:
        # Create NuGet hosted repository
        api_response = api_instance.create_repository12(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository12: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                   | Description | Notes |
| -------------------------------------------------------------------------------------- | ----------- | ----- |
| [**NugetHostedRepositoryApiRequest**](../../models/NugetHostedRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository12.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository12.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository12.ApiResponseFor403) | Insufficient permissions                                    |

#### create_repository12.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository12.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository12.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository13**

<a id="create_repository13"></a>

> create_repository13()

Create NuGet proxy repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.nuget_proxy_repository_api_request import NugetProxyRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = NugetProxyRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        proxy=ProxyAttributes(
            remote_url="https://remote.repository.com",
            content_max_age=1440,
            metadata_max_age=1440,
        ),
        negative_cache=NegativeCacheAttributes(
            enabled=True,
            time_to_live=1440,
        ),
        http_client=HttpClientAttributes(
            blocked=False,
            auto_block=True,
            connection=HttpClientConnectionAttributes(
                retries=0,
                user_agent_suffix="user_agent_suffix_example",
                timeout=60,
                enable_circular_redirects=False,
                enable_cookies=False,
                use_trust_store=False,
            ),
            authentication=HttpClientConnectionAuthenticationAttributes(
                type="username",
                username="username_example",
                password="password_example",
                ntlm_host="ntlm_host_example",
                ntlm_domain="ntlm_domain_example",
            ),
        ),
        routing_rule="routing_rule_example",
        replication=ReplicationAttributes(
            preemptive_pull_enabled=True,
            asset_path_regex="asset_path_regex_example",
        ),
        nuget_proxy=NugetAttributes(
            query_cache_item_max_age=3600,
            nuget_version="V3",
        ),
    )
    try:
        # Create NuGet proxy repository
        api_response = api_instance.create_repository13(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository13: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                 | Description | Notes |
| ------------------------------------------------------------------------------------ | ----------- | ----- |
| [**NugetProxyRepositoryApiRequest**](../../models/NugetProxyRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository13.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository13.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository13.ApiResponseFor403) | Insufficient permissions                                    |

#### create_repository13.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository13.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository13.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository14**

<a id="create_repository14"></a>

> create_repository14()

Create RubyGems group repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.ruby_gems_group_repository_api_request import RubyGemsGroupRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = RubyGemsGroupRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        group=GroupAttributes(
            member_names=[
                "member_names_example"
            ],
        ),
    )
    try:
        # Create RubyGems group repository
        api_response = api_instance.create_repository14(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository14: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                       | Description | Notes |
| ------------------------------------------------------------------------------------------ | ----------- | ----- |
| [**RubyGemsGroupRepositoryApiRequest**](../../models/RubyGemsGroupRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository14.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository14.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository14.ApiResponseFor403) | Insufficient permissions                                    |

#### create_repository14.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository14.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository14.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository15**

<a id="create_repository15"></a>

> create_repository15()

Create RubyGems hosted repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.ruby_gems_hosted_repository_api_request import RubyGemsHostedRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = RubyGemsHostedRepositoryApiRequest(
        name="internal",
        online=True,
        storage=HostedStorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
            write_policy="allow_once",
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        component=ComponentAttributes(
            proprietary_components=True,
        ),
    )
    try:
        # Create RubyGems hosted repository
        api_response = api_instance.create_repository15(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository15: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                         | Description | Notes |
| -------------------------------------------------------------------------------------------- | ----------- | ----- |
| [**RubyGemsHostedRepositoryApiRequest**](../../models/RubyGemsHostedRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository15.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository15.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository15.ApiResponseFor403) | Insufficient permissions                                    |

#### create_repository15.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository15.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository15.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository16**

<a id="create_repository16"></a>

> create_repository16()

Create RubyGems proxy repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.ruby_gems_proxy_repository_api_request import RubyGemsProxyRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = RubyGemsProxyRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        proxy=ProxyAttributes(
            remote_url="https://remote.repository.com",
            content_max_age=1440,
            metadata_max_age=1440,
        ),
        negative_cache=NegativeCacheAttributes(
            enabled=True,
            time_to_live=1440,
        ),
        http_client=HttpClientAttributes(
            blocked=False,
            auto_block=True,
            connection=HttpClientConnectionAttributes(
                retries=0,
                user_agent_suffix="user_agent_suffix_example",
                timeout=60,
                enable_circular_redirects=False,
                enable_cookies=False,
                use_trust_store=False,
            ),
            authentication=HttpClientConnectionAuthenticationAttributes(
                type="username",
                username="username_example",
                password="password_example",
                ntlm_host="ntlm_host_example",
                ntlm_domain="ntlm_domain_example",
            ),
        ),
        routing_rule="routing_rule_example",
        replication=ReplicationAttributes(
            preemptive_pull_enabled=True,
            asset_path_regex="asset_path_regex_example",
        ),
    )
    try:
        # Create RubyGems proxy repository
        api_response = api_instance.create_repository16(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository16: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                       | Description | Notes |
| ------------------------------------------------------------------------------------------ | ----------- | ----- |
| [**RubyGemsProxyRepositoryApiRequest**](../../models/RubyGemsProxyRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository16.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository16.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository16.ApiResponseFor403) | Insufficient permissions                                    |

#### create_repository16.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository16.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository16.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository17**

<a id="create_repository17"></a>

> create_repository17()

Create Yum group repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.yum_group_repository_api_request import YumGroupRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = YumGroupRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        group=GroupAttributes(
            member_names=[
                "member_names_example"
            ],
        ),
        yum_signing=YumSigningRepositoriesAttributes(
            keypair="keypair_example",
            passphrase="passphrase_example",
        ),
    )
    try:
        # Create Yum group repository
        api_response = api_instance.create_repository17(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository17: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                             | Description | Notes |
| -------------------------------------------------------------------------------- | ----------- | ----- |
| [**YumGroupRepositoryApiRequest**](../../models/YumGroupRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository17.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository17.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository17.ApiResponseFor403) | Insufficient permissions                                    |

#### create_repository17.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository17.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository17.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository18**

<a id="create_repository18"></a>

> create_repository18()

Create Yum hosted repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.yum_hosted_repository_api_request import YumHostedRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = YumHostedRepositoryApiRequest(
        name="internal",
        online=True,
        storage=HostedStorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
            write_policy="allow_once",
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        component=ComponentAttributes(
            proprietary_components=True,
        ),
        yum=YumAttributes(
            repodata_depth=5,
            deploy_policy="STRICT",
        ),
    )
    try:
        # Create Yum hosted repository
        api_response = api_instance.create_repository18(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository18: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                               | Description | Notes |
| ---------------------------------------------------------------------------------- | ----------- | ----- |
| [**YumHostedRepositoryApiRequest**](../../models/YumHostedRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository18.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository18.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository18.ApiResponseFor403) | Insufficient permissions                                    |

#### create_repository18.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository18.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository18.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository19**

<a id="create_repository19"></a>

> create_repository19()

Create Yum proxy repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.yum_proxy_repository_api_request import YumProxyRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = YumProxyRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        proxy=ProxyAttributes(
            remote_url="https://remote.repository.com",
            content_max_age=1440,
            metadata_max_age=1440,
        ),
        negative_cache=NegativeCacheAttributes(
            enabled=True,
            time_to_live=1440,
        ),
        http_client=HttpClientAttributes(
            blocked=False,
            auto_block=True,
            connection=HttpClientConnectionAttributes(
                retries=0,
                user_agent_suffix="user_agent_suffix_example",
                timeout=60,
                enable_circular_redirects=False,
                enable_cookies=False,
                use_trust_store=False,
            ),
            authentication=HttpClientConnectionAuthenticationAttributes(
                type="username",
                username="username_example",
                password="password_example",
                ntlm_host="ntlm_host_example",
                ntlm_domain="ntlm_domain_example",
            ),
        ),
        routing_rule="routing_rule_example",
        replication=ReplicationAttributes(
            preemptive_pull_enabled=True,
            asset_path_regex="asset_path_regex_example",
        ),
        yum_signing=YumSigningRepositoriesAttributes(
            keypair="keypair_example",
            passphrase="passphrase_example",
        ),
    )
    try:
        # Create Yum proxy repository
        api_response = api_instance.create_repository19(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository19: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                             | Description | Notes |
| -------------------------------------------------------------------------------- | ----------- | ----- |
| [**YumProxyRepositoryApiRequest**](../../models/YumProxyRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository19.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository19.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository19.ApiResponseFor403) | Insufficient permissions                                    |

#### create_repository19.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository19.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository19.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository2**

<a id="create_repository2"></a>

> create_repository2()

Create Maven proxy repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.maven_proxy_repository_api_request import MavenProxyRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = MavenProxyRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        proxy=ProxyAttributes(
            remote_url="https://remote.repository.com",
            content_max_age=1440,
            metadata_max_age=1440,
        ),
        negative_cache=NegativeCacheAttributes(
            enabled=True,
            time_to_live=1440,
        ),
        http_client=HttpClientAttributesWithPreemptiveAuth(
            blocked=False,
            auto_block=True,
            connection=HttpClientConnectionAttributes(
                retries=0,
                user_agent_suffix="user_agent_suffix_example",
                timeout=60,
                enable_circular_redirects=False,
                enable_cookies=False,
                use_trust_store=False,
            ),
            authentication=HttpClientConnectionAuthenticationAttributesWithPreemptive(
                type="username",
                username="username_example",
                password="password_example",
                ntlm_host="ntlm_host_example",
                ntlm_domain="ntlm_domain_example",
                preemptive=False,
            ),
        ),
        routing_rule="routing_rule_example",
        replication=ReplicationAttributes(
            preemptive_pull_enabled=True,
            asset_path_regex="asset_path_regex_example",
        ),
        maven=MavenAttributes(
            version_policy="MIXED",
            layout_policy="STRICT",
            content_disposition="ATTACHMENT",
        ),
    )
    try:
        # Create Maven proxy repository
        api_response = api_instance.create_repository2(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository2: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                 | Description | Notes |
| ------------------------------------------------------------------------------------ | ----------- | ----- |
| [**MavenProxyRepositoryApiRequest**](../../models/MavenProxyRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                      | Description                                                 |
| ---- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization               | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository2.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository2.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository2.ApiResponseFor403) | Insufficient permissions                                    |

#### create_repository2.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository2.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository2.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository20**

<a id="create_repository20"></a>

> create_repository20()

Create Docker group repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.docker_group_repository_api_request import DockerGroupRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = DockerGroupRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        group=GroupDeployAttributes(
            member_names=[
                "member_names_example"
            ],
            writable_member="writable_member_example",
        ),
        docker=DockerAttributes(
            v1_enabled=False,
            force_basic_auth=True,
            http_port=8082,
            https_port=8083,
            subdomain="docker-a",
        ),
    )
    try:
        # Create Docker group repository
        api_response = api_instance.create_repository20(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository20: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                   | Description | Notes |
| -------------------------------------------------------------------------------------- | ----------- | ----- |
| [**DockerGroupRepositoryApiRequest**](../../models/DockerGroupRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository20.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository20.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository20.ApiResponseFor403) | Insufficient permissions                                    |

#### create_repository20.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository20.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository20.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository21**

<a id="create_repository21"></a>

> create_repository21()

Create Docker hosted repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.docker_hosted_repository_api_request import DockerHostedRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = DockerHostedRepositoryApiRequest(
        name="internal",
        online=True,
        storage=DockerHostedStorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
            write_policy="allow_once",
            latest_policy=True,
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        component=ComponentAttributes(
            proprietary_components=True,
        ),
        docker=DockerAttributes(
            v1_enabled=False,
            force_basic_auth=True,
            http_port=8082,
            https_port=8083,
            subdomain="docker-a",
        ),
    )
    try:
        # Create Docker hosted repository
        api_response = api_instance.create_repository21(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository21: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                     | Description | Notes |
| ---------------------------------------------------------------------------------------- | ----------- | ----- |
| [**DockerHostedRepositoryApiRequest**](../../models/DockerHostedRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository21.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository21.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository21.ApiResponseFor403) | Repository not found                                        |

#### create_repository21.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository21.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository21.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository22**

<a id="create_repository22"></a>

> create_repository22()

Create Docker proxy repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.docker_proxy_repository_api_request import DockerProxyRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = DockerProxyRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        proxy=ProxyAttributes(
            remote_url="https://remote.repository.com",
            content_max_age=1440,
            metadata_max_age=1440,
        ),
        negative_cache=NegativeCacheAttributes(
            enabled=True,
            time_to_live=1440,
        ),
        http_client=HttpClientAttributes(
            blocked=False,
            auto_block=True,
            connection=HttpClientConnectionAttributes(
                retries=0,
                user_agent_suffix="user_agent_suffix_example",
                timeout=60,
                enable_circular_redirects=False,
                enable_cookies=False,
                use_trust_store=False,
            ),
            authentication=HttpClientConnectionAuthenticationAttributes(
                type="username",
                username="username_example",
                password="password_example",
                ntlm_host="ntlm_host_example",
                ntlm_domain="ntlm_domain_example",
            ),
        ),
        routing_rule="routing_rule_example",
        replication=ReplicationAttributes(
            preemptive_pull_enabled=True,
            asset_path_regex="asset_path_regex_example",
        ),
        docker=DockerAttributes(
            v1_enabled=False,
            force_basic_auth=True,
            http_port=8082,
            https_port=8083,
            subdomain="docker-a",
        ),
        docker_proxy=DockerProxyAttributes(
            index_type="HUB",
            index_url="index_url_example",
            cache_foreign_layers=True,
            foreign_layer_url_whitelist=[
                "foreign_layer_url_whitelist_example"
            ],
        ),
    )
    try:
        # Create Docker proxy repository
        api_response = api_instance.create_repository22(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository22: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                   | Description | Notes |
| -------------------------------------------------------------------------------------- | ----------- | ----- |
| [**DockerProxyRepositoryApiRequest**](../../models/DockerProxyRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository22.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository22.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository22.ApiResponseFor403) | Insufficient permissions                                    |

#### create_repository22.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository22.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository22.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository23**

<a id="create_repository23"></a>

> create_repository23()

Create PyPI group repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.pypi_group_repository_api_request import PypiGroupRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = PypiGroupRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        group=GroupAttributes(
            member_names=[
                "member_names_example"
            ],
        ),
    )
    try:
        # Create PyPI group repository
        api_response = api_instance.create_repository23(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository23: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                               | Description | Notes |
| ---------------------------------------------------------------------------------- | ----------- | ----- |
| [**PypiGroupRepositoryApiRequest**](../../models/PypiGroupRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository23.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository23.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository23.ApiResponseFor403) | Insufficient permissions                                    |

#### create_repository23.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository23.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository23.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository24**

<a id="create_repository24"></a>

> create_repository24()

Create PyPI hosted repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.pypi_hosted_repository_api_request import PypiHostedRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = PypiHostedRepositoryApiRequest(
        name="internal",
        online=True,
        storage=HostedStorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
            write_policy="allow_once",
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        component=ComponentAttributes(
            proprietary_components=True,
        ),
    )
    try:
        # Create PyPI hosted repository
        api_response = api_instance.create_repository24(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository24: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                 | Description | Notes |
| ------------------------------------------------------------------------------------ | ----------- | ----- |
| [**PypiHostedRepositoryApiRequest**](../../models/PypiHostedRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository24.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository24.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository24.ApiResponseFor403) | Insufficient permissions                                    |

#### create_repository24.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository24.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository24.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository25**

<a id="create_repository25"></a>

> create_repository25()

Create PyPI proxy repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.pypi_proxy_repository_api_request import PypiProxyRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = PypiProxyRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        proxy=ProxyAttributes(
            remote_url="https://remote.repository.com",
            content_max_age=1440,
            metadata_max_age=1440,
        ),
        negative_cache=NegativeCacheAttributes(
            enabled=True,
            time_to_live=1440,
        ),
        http_client=HttpClientAttributes(
            blocked=False,
            auto_block=True,
            connection=HttpClientConnectionAttributes(
                retries=0,
                user_agent_suffix="user_agent_suffix_example",
                timeout=60,
                enable_circular_redirects=False,
                enable_cookies=False,
                use_trust_store=False,
            ),
            authentication=HttpClientConnectionAuthenticationAttributes(
                type="username",
                username="username_example",
                password="password_example",
                ntlm_host="ntlm_host_example",
                ntlm_domain="ntlm_domain_example",
            ),
        ),
        routing_rule="routing_rule_example",
        replication=ReplicationAttributes(
            preemptive_pull_enabled=True,
            asset_path_regex="asset_path_regex_example",
        ),
    )
    try:
        # Create PyPI proxy repository
        api_response = api_instance.create_repository25(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository25: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                               | Description | Notes |
| ---------------------------------------------------------------------------------- | ----------- | ----- |
| [**PypiProxyRepositoryApiRequest**](../../models/PypiProxyRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository25.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository25.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository25.ApiResponseFor403) | Insufficient permissions                                    |

#### create_repository25.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository25.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository25.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository26**

<a id="create_repository26"></a>

> create_repository26()

Create conda proxy repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.conda_proxy_repository_api_request import CondaProxyRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = CondaProxyRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        proxy=ProxyAttributes(
            remote_url="https://remote.repository.com",
            content_max_age=1440,
            metadata_max_age=1440,
        ),
        negative_cache=NegativeCacheAttributes(
            enabled=True,
            time_to_live=1440,
        ),
        http_client=HttpClientAttributes(
            blocked=False,
            auto_block=True,
            connection=HttpClientConnectionAttributes(
                retries=0,
                user_agent_suffix="user_agent_suffix_example",
                timeout=60,
                enable_circular_redirects=False,
                enable_cookies=False,
                use_trust_store=False,
            ),
            authentication=HttpClientConnectionAuthenticationAttributes(
                type="username",
                username="username_example",
                password="password_example",
                ntlm_host="ntlm_host_example",
                ntlm_domain="ntlm_domain_example",
            ),
        ),
        routing_rule="routing_rule_example",
        replication=ReplicationAttributes(
            preemptive_pull_enabled=True,
            asset_path_regex="asset_path_regex_example",
        ),
    )
    try:
        # Create conda proxy repository
        api_response = api_instance.create_repository26(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository26: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                 | Description | Notes |
| ------------------------------------------------------------------------------------ | ----------- | ----- |
| [**CondaProxyRepositoryApiRequest**](../../models/CondaProxyRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository26.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository26.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository26.ApiResponseFor403) | Insufficient permissions                                    |
| 405  | [ApiResponseFor405](#create_repository26.ApiResponseFor405) | Feature is disabled in High Availability                    |

#### create_repository26.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository26.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository26.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository26.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository27**

<a id="create_repository27"></a>

> create_repository27()

Create Conan proxy repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.conan_proxy_repository_api_request import ConanProxyRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = ConanProxyRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        proxy=ProxyAttributes(
            remote_url="https://remote.repository.com",
            content_max_age=1440,
            metadata_max_age=1440,
        ),
        negative_cache=NegativeCacheAttributes(
            enabled=True,
            time_to_live=1440,
        ),
        http_client=HttpClientAttributes(
            blocked=False,
            auto_block=True,
            connection=HttpClientConnectionAttributes(
                retries=0,
                user_agent_suffix="user_agent_suffix_example",
                timeout=60,
                enable_circular_redirects=False,
                enable_cookies=False,
                use_trust_store=False,
            ),
            authentication=HttpClientConnectionAuthenticationAttributes(
                type="username",
                username="username_example",
                password="password_example",
                ntlm_host="ntlm_host_example",
                ntlm_domain="ntlm_domain_example",
            ),
        ),
        routing_rule="routing_rule_example",
        replication=ReplicationAttributes(
            preemptive_pull_enabled=True,
            asset_path_regex="asset_path_regex_example",
        ),
    )
    try:
        # Create Conan proxy repository
        api_response = api_instance.create_repository27(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository27: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                 | Description | Notes |
| ------------------------------------------------------------------------------------ | ----------- | ----- |
| [**ConanProxyRepositoryApiRequest**](../../models/ConanProxyRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository27.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository27.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository27.ApiResponseFor403) | Insufficient permissions                                    |
| 405  | [ApiResponseFor405](#create_repository27.ApiResponseFor405) | Feature is disabled in High Availability                    |

#### create_repository27.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository27.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository27.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository27.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository28**

<a id="create_repository28"></a>

> create_repository28()

Create Git LFS hosted repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.git_lfs_hosted_repository_api_request import GitLfsHostedRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = GitLfsHostedRepositoryApiRequest(
        name="internal",
        online=True,
        storage=HostedStorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
            write_policy="allow_once",
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        component=ComponentAttributes(
            proprietary_components=True,
        ),
    )
    try:
        # Create Git LFS hosted repository
        api_response = api_instance.create_repository28(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository28: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                     | Description | Notes |
| ---------------------------------------------------------------------------------------- | ----------- | ----- |
| [**GitLfsHostedRepositoryApiRequest**](../../models/GitLfsHostedRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository28.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository28.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository28.ApiResponseFor403) | Insufficient permissions                                    |

#### create_repository28.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository28.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository28.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository29**

<a id="create_repository29"></a>

> create_repository29()

Create R group repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.r_group_repository_api_request import RGroupRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = RGroupRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        group=GroupAttributes(
            member_names=[
                "member_names_example"
            ],
        ),
    )
    try:
        # Create R group repository
        api_response = api_instance.create_repository29(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository29: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                         | Description | Notes |
| ---------------------------------------------------------------------------- | ----------- | ----- |
| [**RGroupRepositoryApiRequest**](../../models/RGroupRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository29.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository29.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository29.ApiResponseFor403) | Insufficient permissions                                    |
| 405  | [ApiResponseFor405](#create_repository29.ApiResponseFor405) | Feature is disabled in High Availability                    |

#### create_repository29.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository29.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository29.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository29.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository3**

<a id="create_repository3"></a>

> create_repository3()

Create APT hosted repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.apt_hosted_repository_api_request import AptHostedRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = AptHostedRepositoryApiRequest(
        name="internal",
        online=True,
        storage=HostedStorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
            write_policy="allow_once",
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        component=ComponentAttributes(
            proprietary_components=True,
        ),
        apt=AptHostedRepositoriesAttributes(
            distribution="bionic",
        ),
        apt_signing=AptSigningRepositoriesAttributes(
            keypair="keypair_example",
            passphrase="passphrase_example",
        ),
    )
    try:
        # Create APT hosted repository
        api_response = api_instance.create_repository3(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository3: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                               | Description | Notes |
| ---------------------------------------------------------------------------------- | ----------- | ----- |
| [**AptHostedRepositoryApiRequest**](../../models/AptHostedRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                      | Description                                                 |
| ---- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization               | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository3.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository3.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository3.ApiResponseFor403) | Insufficient permissions                                    |
| 405  | [ApiResponseFor405](#create_repository3.ApiResponseFor405) | Feature is disabled in High Availability                    |

#### create_repository3.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository3.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository3.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository3.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository30**

<a id="create_repository30"></a>

> create_repository30()

Create R hosted repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.r_hosted_repository_api_request import RHostedRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = RHostedRepositoryApiRequest(
        name="internal",
        online=True,
        storage=HostedStorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
            write_policy="allow_once",
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        component=ComponentAttributes(
            proprietary_components=True,
        ),
    )
    try:
        # Create R hosted repository
        api_response = api_instance.create_repository30(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository30: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                           | Description | Notes |
| ------------------------------------------------------------------------------ | ----------- | ----- |
| [**RHostedRepositoryApiRequest**](../../models/RHostedRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository30.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository30.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository30.ApiResponseFor403) | Insufficient permissions                                    |
| 405  | [ApiResponseFor405](#create_repository30.ApiResponseFor405) | Feature is disabled in High Availability                    |

#### create_repository30.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository30.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository30.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository30.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository31**

<a id="create_repository31"></a>

> create_repository31()

Create R proxy repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.r_proxy_repository_api_request import RProxyRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = RProxyRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        proxy=ProxyAttributes(
            remote_url="https://remote.repository.com",
            content_max_age=1440,
            metadata_max_age=1440,
        ),
        negative_cache=NegativeCacheAttributes(
            enabled=True,
            time_to_live=1440,
        ),
        http_client=HttpClientAttributes(
            blocked=False,
            auto_block=True,
            connection=HttpClientConnectionAttributes(
                retries=0,
                user_agent_suffix="user_agent_suffix_example",
                timeout=60,
                enable_circular_redirects=False,
                enable_cookies=False,
                use_trust_store=False,
            ),
            authentication=HttpClientConnectionAuthenticationAttributes(
                type="username",
                username="username_example",
                password="password_example",
                ntlm_host="ntlm_host_example",
                ntlm_domain="ntlm_domain_example",
            ),
        ),
        routing_rule="routing_rule_example",
        replication=ReplicationAttributes(
            preemptive_pull_enabled=True,
            asset_path_regex="asset_path_regex_example",
        ),
    )
    try:
        # Create R proxy repository
        api_response = api_instance.create_repository31(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository31: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                         | Description | Notes |
| ---------------------------------------------------------------------------- | ----------- | ----- |
| [**RProxyRepositoryApiRequest**](../../models/RProxyRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository31.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository31.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository31.ApiResponseFor403) | Insufficient permissions                                    |
| 405  | [ApiResponseFor405](#create_repository31.ApiResponseFor405) | Feature is disabled in High Availability                    |

#### create_repository31.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository31.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository31.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository31.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository32**

<a id="create_repository32"></a>

> create_repository32()

Create Cocoapods proxy repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.cocoapods_proxy_repository_api_request import CocoapodsProxyRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = CocoapodsProxyRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        proxy=ProxyAttributes(
            remote_url="https://remote.repository.com",
            content_max_age=1440,
            metadata_max_age=1440,
        ),
        negative_cache=NegativeCacheAttributes(
            enabled=True,
            time_to_live=1440,
        ),
        http_client=HttpClientAttributes(
            blocked=False,
            auto_block=True,
            connection=HttpClientConnectionAttributes(
                retries=0,
                user_agent_suffix="user_agent_suffix_example",
                timeout=60,
                enable_circular_redirects=False,
                enable_cookies=False,
                use_trust_store=False,
            ),
            authentication=HttpClientConnectionAuthenticationAttributes(
                type="username",
                username="username_example",
                password="password_example",
                ntlm_host="ntlm_host_example",
                ntlm_domain="ntlm_domain_example",
            ),
        ),
        routing_rule="routing_rule_example",
        replication=ReplicationAttributes(
            preemptive_pull_enabled=True,
            asset_path_regex="asset_path_regex_example",
        ),
    )
    try:
        # Create Cocoapods proxy repository
        api_response = api_instance.create_repository32(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository32: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                         | Description | Notes |
| -------------------------------------------------------------------------------------------- | ----------- | ----- |
| [**CocoapodsProxyRepositoryApiRequest**](../../models/CocoapodsProxyRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository32.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository32.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository32.ApiResponseFor403) | Insufficient permissions                                    |
| 405  | [ApiResponseFor405](#create_repository32.ApiResponseFor405) | Feature is disabled in High Availability                    |

#### create_repository32.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository32.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository32.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository32.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository33**

<a id="create_repository33"></a>

> create_repository33()

Create a Go group repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.golang_group_repository_api_request import GolangGroupRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = GolangGroupRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        group=GroupAttributes(
            member_names=[
                "member_names_example"
            ],
        ),
    )
    try:
        # Create a Go group repository
        api_response = api_instance.create_repository33(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository33: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                   | Description | Notes |
| -------------------------------------------------------------------------------------- | ----------- | ----- |
| [**GolangGroupRepositoryApiRequest**](../../models/GolangGroupRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository33.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository33.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository33.ApiResponseFor403) | Insufficient permissions                                    |
| 405  | [ApiResponseFor405](#create_repository33.ApiResponseFor405) | Feature is disabled in High Availability                    |

#### create_repository33.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository33.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository33.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository33.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository34**

<a id="create_repository34"></a>

> create_repository34()

Create a Go proxy repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.golang_proxy_repository_api_request import GolangProxyRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = GolangProxyRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        proxy=ProxyAttributes(
            remote_url="https://remote.repository.com",
            content_max_age=1440,
            metadata_max_age=1440,
        ),
        negative_cache=NegativeCacheAttributes(
            enabled=True,
            time_to_live=1440,
        ),
        http_client=HttpClientAttributes(
            blocked=False,
            auto_block=True,
            connection=HttpClientConnectionAttributes(
                retries=0,
                user_agent_suffix="user_agent_suffix_example",
                timeout=60,
                enable_circular_redirects=False,
                enable_cookies=False,
                use_trust_store=False,
            ),
            authentication=HttpClientConnectionAuthenticationAttributes(
                type="username",
                username="username_example",
                password="password_example",
                ntlm_host="ntlm_host_example",
                ntlm_domain="ntlm_domain_example",
            ),
        ),
        routing_rule="routing_rule_example",
        replication=ReplicationAttributes(
            preemptive_pull_enabled=True,
            asset_path_regex="asset_path_regex_example",
        ),
    )
    try:
        # Create a Go proxy repository
        api_response = api_instance.create_repository34(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository34: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                   | Description | Notes |
| -------------------------------------------------------------------------------------- | ----------- | ----- |
| [**GolangProxyRepositoryApiRequest**](../../models/GolangProxyRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository34.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository34.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository34.ApiResponseFor403) | Insufficient permissions                                    |
| 405  | [ApiResponseFor405](#create_repository34.ApiResponseFor405) | Feature is disabled in High Availability                    |

#### create_repository34.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository34.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository34.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository34.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository35**

<a id="create_repository35"></a>

> create_repository35()

Create p2 proxy repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.p2_proxy_repository_api_request import P2ProxyRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = P2ProxyRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        proxy=ProxyAttributes(
            remote_url="https://remote.repository.com",
            content_max_age=1440,
            metadata_max_age=1440,
        ),
        negative_cache=NegativeCacheAttributes(
            enabled=True,
            time_to_live=1440,
        ),
        http_client=HttpClientAttributes(
            blocked=False,
            auto_block=True,
            connection=HttpClientConnectionAttributes(
                retries=0,
                user_agent_suffix="user_agent_suffix_example",
                timeout=60,
                enable_circular_redirects=False,
                enable_cookies=False,
                use_trust_store=False,
            ),
            authentication=HttpClientConnectionAuthenticationAttributes(
                type="username",
                username="username_example",
                password="password_example",
                ntlm_host="ntlm_host_example",
                ntlm_domain="ntlm_domain_example",
            ),
        ),
        routing_rule="routing_rule_example",
        replication=ReplicationAttributes(
            preemptive_pull_enabled=True,
            asset_path_regex="asset_path_regex_example",
        ),
    )
    try:
        # Create p2 proxy repository
        api_response = api_instance.create_repository35(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository35: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                           | Description | Notes |
| ------------------------------------------------------------------------------ | ----------- | ----- |
| [**P2ProxyRepositoryApiRequest**](../../models/P2ProxyRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository35.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository35.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository35.ApiResponseFor403) | Insufficient permissions                                    |
| 405  | [ApiResponseFor405](#create_repository35.ApiResponseFor405) | Feature is disabled in High Availability                    |

#### create_repository35.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository35.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository35.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository35.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository36**

<a id="create_repository36"></a>

> create_repository36()

Create Helm hosted repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.helm_hosted_repository_api_request import HelmHostedRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = HelmHostedRepositoryApiRequest(
        name="internal",
        online=True,
        storage=HostedStorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
            write_policy="allow_once",
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        component=ComponentAttributes(
            proprietary_components=True,
        ),
    )
    try:
        # Create Helm hosted repository
        api_response = api_instance.create_repository36(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository36: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                 | Description | Notes |
| ------------------------------------------------------------------------------------ | ----------- | ----- |
| [**HelmHostedRepositoryApiRequest**](../../models/HelmHostedRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository36.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository36.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository36.ApiResponseFor403) | Insufficient permissions                                    |
| 405  | [ApiResponseFor405](#create_repository36.ApiResponseFor405) | Feature is disabled in High Availability                    |

#### create_repository36.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository36.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository36.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository36.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository37**

<a id="create_repository37"></a>

> create_repository37()

Create Helm proxy repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.helm_proxy_repository_api_request import HelmProxyRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = HelmProxyRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        proxy=ProxyAttributes(
            remote_url="https://remote.repository.com",
            content_max_age=1440,
            metadata_max_age=1440,
        ),
        negative_cache=NegativeCacheAttributes(
            enabled=True,
            time_to_live=1440,
        ),
        http_client=HttpClientAttributes(
            blocked=False,
            auto_block=True,
            connection=HttpClientConnectionAttributes(
                retries=0,
                user_agent_suffix="user_agent_suffix_example",
                timeout=60,
                enable_circular_redirects=False,
                enable_cookies=False,
                use_trust_store=False,
            ),
            authentication=HttpClientConnectionAuthenticationAttributes(
                type="username",
                username="username_example",
                password="password_example",
                ntlm_host="ntlm_host_example",
                ntlm_domain="ntlm_domain_example",
            ),
        ),
        routing_rule="routing_rule_example",
        replication=ReplicationAttributes(
            preemptive_pull_enabled=True,
            asset_path_regex="asset_path_regex_example",
        ),
    )
    try:
        # Create Helm proxy repository
        api_response = api_instance.create_repository37(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository37: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                               | Description | Notes |
| ---------------------------------------------------------------------------------- | ----------- | ----- |
| [**HelmProxyRepositoryApiRequest**](../../models/HelmProxyRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository37.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository37.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository37.ApiResponseFor403) | Insufficient permissions                                    |
| 405  | [ApiResponseFor405](#create_repository37.ApiResponseFor405) | Feature is disabled in High Availability                    |

#### create_repository37.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository37.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository37.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository37.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository38**

<a id="create_repository38"></a>

> create_repository38()

Create Bower group repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.bower_group_repository_api_request import BowerGroupRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = BowerGroupRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        group=GroupAttributes(
            member_names=[
                "member_names_example"
            ],
        ),
    )
    try:
        # Create Bower group repository
        api_response = api_instance.create_repository38(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository38: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                 | Description | Notes |
| ------------------------------------------------------------------------------------ | ----------- | ----- |
| [**BowerGroupRepositoryApiRequest**](../../models/BowerGroupRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository38.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository38.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository38.ApiResponseFor403) | Insufficient permissions                                    |

#### create_repository38.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository38.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository38.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository39**

<a id="create_repository39"></a>

> create_repository39()

Create Bower hosted repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.bower_hosted_repository_api_request import BowerHostedRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = BowerHostedRepositoryApiRequest(
        name="internal",
        online=True,
        storage=HostedStorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
            write_policy="allow_once",
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        component=ComponentAttributes(
            proprietary_components=True,
        ),
    )
    try:
        # Create Bower hosted repository
        api_response = api_instance.create_repository39(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository39: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                   | Description | Notes |
| -------------------------------------------------------------------------------------- | ----------- | ----- |
| [**BowerHostedRepositoryApiRequest**](../../models/BowerHostedRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository39.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository39.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository39.ApiResponseFor403) | Insufficient permissions                                    |

#### create_repository39.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository39.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository39.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository4**

<a id="create_repository4"></a>

> create_repository4()

Create APT proxy repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.apt_proxy_repository_api_request import AptProxyRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = AptProxyRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        proxy=ProxyAttributes(
            remote_url="https://remote.repository.com",
            content_max_age=1440,
            metadata_max_age=1440,
        ),
        negative_cache=NegativeCacheAttributes(
            enabled=True,
            time_to_live=1440,
        ),
        http_client=HttpClientAttributes(
            blocked=False,
            auto_block=True,
            connection=HttpClientConnectionAttributes(
                retries=0,
                user_agent_suffix="user_agent_suffix_example",
                timeout=60,
                enable_circular_redirects=False,
                enable_cookies=False,
                use_trust_store=False,
            ),
            authentication=HttpClientConnectionAuthenticationAttributes(
                type="username",
                username="username_example",
                password="password_example",
                ntlm_host="ntlm_host_example",
                ntlm_domain="ntlm_domain_example",
            ),
        ),
        routing_rule="routing_rule_example",
        replication=ReplicationAttributes(
            preemptive_pull_enabled=True,
            asset_path_regex="asset_path_regex_example",
        ),
        apt=AptProxyRepositoriesAttributes(
            distribution="bionic",
            flat=False,
        ),
    )
    try:
        # Create APT proxy repository
        api_response = api_instance.create_repository4(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository4: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                             | Description | Notes |
| -------------------------------------------------------------------------------- | ----------- | ----- |
| [**AptProxyRepositoryApiRequest**](../../models/AptProxyRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                      | Description                                                 |
| ---- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization               | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository4.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository4.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository4.ApiResponseFor403) | Insufficient permissions                                    |
| 405  | [ApiResponseFor405](#create_repository4.ApiResponseFor405) | Feature is disabled in High Availability                    |

#### create_repository4.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository4.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository4.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository4.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository40**

<a id="create_repository40"></a>

> create_repository40()

Create Bower proxy repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.bower_proxy_repository_api_request import BowerProxyRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = BowerProxyRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        proxy=ProxyAttributes(
            remote_url="https://remote.repository.com",
            content_max_age=1440,
            metadata_max_age=1440,
        ),
        negative_cache=NegativeCacheAttributes(
            enabled=True,
            time_to_live=1440,
        ),
        http_client=HttpClientAttributes(
            blocked=False,
            auto_block=True,
            connection=HttpClientConnectionAttributes(
                retries=0,
                user_agent_suffix="user_agent_suffix_example",
                timeout=60,
                enable_circular_redirects=False,
                enable_cookies=False,
                use_trust_store=False,
            ),
            authentication=HttpClientConnectionAuthenticationAttributes(
                type="username",
                username="username_example",
                password="password_example",
                ntlm_host="ntlm_host_example",
                ntlm_domain="ntlm_domain_example",
            ),
        ),
        routing_rule="routing_rule_example",
        replication=ReplicationAttributes(
            preemptive_pull_enabled=True,
            asset_path_regex="asset_path_regex_example",
        ),
        bower=BowerAttributes(
            rewrite_package_urls=True,
        ),
    )
    try:
        # Create Bower proxy repository
        api_response = api_instance.create_repository40(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository40: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                 | Description | Notes |
| ------------------------------------------------------------------------------------ | ----------- | ----- |
| [**BowerProxyRepositoryApiRequest**](../../models/BowerProxyRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository40.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository40.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository40.ApiResponseFor403) | Insufficient permissions                                    |

#### create_repository40.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository40.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository40.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository5**

<a id="create_repository5"></a>

> create_repository5()

Create raw group repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.raw_group_repository_api_request import RawGroupRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = RawGroupRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        group=GroupAttributes(
            member_names=[
                "member_names_example"
            ],
        ),
        raw=RawAttributes(
            content_disposition="ATTACHMENT",
        ),
    )
    try:
        # Create raw group repository
        api_response = api_instance.create_repository5(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository5: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                             | Description | Notes |
| -------------------------------------------------------------------------------- | ----------- | ----- |
| [**RawGroupRepositoryApiRequest**](../../models/RawGroupRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                      | Description                                                 |
| ---- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization               | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository5.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository5.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository5.ApiResponseFor403) | Insufficient permissions                                    |

#### create_repository5.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository5.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository5.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository6**

<a id="create_repository6"></a>

> create_repository6()

Create raw hosted repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.raw_hosted_repository_api_request import RawHostedRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = RawHostedRepositoryApiRequest(
        name="internal",
        online=True,
        storage=HostedStorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
            write_policy="allow_once",
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        component=ComponentAttributes(
            proprietary_components=True,
        ),
        raw=RawAttributes(
            content_disposition="ATTACHMENT",
        ),
    )
    try:
        # Create raw hosted repository
        api_response = api_instance.create_repository6(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository6: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                               | Description | Notes |
| ---------------------------------------------------------------------------------- | ----------- | ----- |
| [**RawHostedRepositoryApiRequest**](../../models/RawHostedRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                      | Description                                                 |
| ---- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization               | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository6.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository6.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository6.ApiResponseFor403) | Insufficient permissions                                    |

#### create_repository6.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository6.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository6.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository7**

<a id="create_repository7"></a>

> create_repository7()

Create raw proxy repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.raw_proxy_repository_api_request import RawProxyRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = RawProxyRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        proxy=ProxyAttributes(
            remote_url="https://remote.repository.com",
            content_max_age=1440,
            metadata_max_age=1440,
        ),
        negative_cache=NegativeCacheAttributes(
            enabled=True,
            time_to_live=1440,
        ),
        http_client=HttpClientAttributes(
            blocked=False,
            auto_block=True,
            connection=HttpClientConnectionAttributes(
                retries=0,
                user_agent_suffix="user_agent_suffix_example",
                timeout=60,
                enable_circular_redirects=False,
                enable_cookies=False,
                use_trust_store=False,
            ),
            authentication=HttpClientConnectionAuthenticationAttributes(
                type="username",
                username="username_example",
                password="password_example",
                ntlm_host="ntlm_host_example",
                ntlm_domain="ntlm_domain_example",
            ),
        ),
        routing_rule="routing_rule_example",
        replication=ReplicationAttributes(
            preemptive_pull_enabled=True,
            asset_path_regex="asset_path_regex_example",
        ),
        raw=RawAttributes(
            content_disposition="ATTACHMENT",
        ),
    )
    try:
        # Create raw proxy repository
        api_response = api_instance.create_repository7(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository7: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                             | Description | Notes |
| -------------------------------------------------------------------------------- | ----------- | ----- |
| [**RawProxyRepositoryApiRequest**](../../models/RawProxyRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                      | Description                                                 |
| ---- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization               | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository7.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository7.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository7.ApiResponseFor403) | Insufficient permissions                                    |

#### create_repository7.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository7.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository7.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository8**

<a id="create_repository8"></a>

> create_repository8()

Create npm group repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.npm_group_repository_api_request import NpmGroupRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = NpmGroupRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        group=GroupDeployAttributes(
            member_names=[
                "member_names_example"
            ],
            writable_member="writable_member_example",
        ),
    )
    try:
        # Create npm group repository
        api_response = api_instance.create_repository8(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository8: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                             | Description | Notes |
| -------------------------------------------------------------------------------- | ----------- | ----- |
| [**NpmGroupRepositoryApiRequest**](../../models/NpmGroupRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                      | Description                                                 |
| ---- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization               | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository8.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository8.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository8.ApiResponseFor403) | Insufficient permissions                                    |

#### create_repository8.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository8.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository8.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_repository9**

<a id="create_repository9"></a>

> create_repository9()

Create npm hosted repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.npm_hosted_repository_api_request import NpmHostedRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only optional values
    body = NpmHostedRepositoryApiRequest(
        name="internal",
        online=True,
        storage=HostedStorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
            write_policy="allow_once",
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        component=ComponentAttributes(
            proprietary_components=True,
        ),
    )
    try:
        # Create npm hosted repository
        api_response = api_instance.create_repository9(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository9: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                               | Description | Notes |
| ---------------------------------------------------------------------------------- | ----------- | ----- |
| [**NpmHostedRepositoryApiRequest**](../../models/NpmHostedRepositoryApiRequest.md) |             |

### Return Types, Responses

| Code | Class                                                      | Description                                                 |
| ---- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization               | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_repository9.ApiResponseFor201) | Repository created                                          |
| 401  | [ApiResponseFor401](#create_repository9.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_repository9.ApiResponseFor403) | Insufficient permissions                                    |

#### create_repository9.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository9.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_repository9.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_repository**

<a id="delete_repository"></a>

> delete_repository(repository_name)

Delete repository of any format

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Delete repository of any format
        api_response = api_instance.delete_repository(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->delete_repository: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description      | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                  |
| stream               | bool                                             | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None  | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                     | Description                                                 |
| ---- | --------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization              | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#delete_repository.ApiResponseFor204) | Repository deleted                                          |
| 401  | [ApiResponseFor401](#delete_repository.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#delete_repository.ApiResponseFor403) | Insufficient permissions                                    |
| 404  | [ApiResponseFor404](#delete_repository.ApiResponseFor404) | Repository not found                                        |

#### delete_repository.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_repository.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_repository.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_repository.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **disable_repository_health_check**

<a id="disable_repository_health_check"></a>

> disable_repository_health_check(repository_name)

Disable repository health check. Proxy repositories only.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Disable repository health check. Proxy repositories only.
        api_response = api_instance.disable_repository_health_check(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->disable_repository_health_check: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description      | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                  |
| stream               | bool                                             | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None  | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                                   | Description                                                 |
| ---- | ----------------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                            | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#disable_repository_health_check.ApiResponseFor204) | Repository Health Check disabled                            |
| 401  | [ApiResponseFor401](#disable_repository_health_check.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#disable_repository_health_check.ApiResponseFor403) | Insufficient permissions                                    |
| 404  | [ApiResponseFor404](#disable_repository_health_check.ApiResponseFor404) | Repository not found                                        |

#### disable_repository_health_check.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### disable_repository_health_check.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### disable_repository_health_check.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### disable_repository_health_check.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **enable_repository_health_check**

<a id="enable_repository_health_check"></a>

> enable_repository_health_check(repository_name)

Enable repository health check. Proxy repositories only.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Enable repository health check. Proxy repositories only.
        api_response = api_instance.enable_repository_health_check(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->enable_repository_health_check: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description      | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                  |
| stream               | bool                                             | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None  | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                                  | Description                                                        |
| ---- | ---------------------------------------------------------------------- | ------------------------------------------------------------------ |
| n/a  | api_client.ApiResponseWithoutDeserialization                           | When skip_deserialization is True this response is returned        |
| 204  | [ApiResponseFor204](#enable_repository_health_check.ApiResponseFor204) | Repository Health Check enabled                                    |
| 401  | [ApiResponseFor401](#enable_repository_health_check.ApiResponseFor401) | Authentication required                                            |
| 403  | [ApiResponseFor403](#enable_repository_health_check.ApiResponseFor403) | Insufficient permissions                                           |
| 404  | [ApiResponseFor404](#enable_repository_health_check.ApiResponseFor404) | Repository not found                                               |
| 409  | [ApiResponseFor409](#enable_repository_health_check.ApiResponseFor409) | EULA not accepted or Repository Health Check capability not active |

#### enable_repository_health_check.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### enable_repository_health_check.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### enable_repository_health_check.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### enable_repository_health_check.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### enable_repository_health_check.ApiResponseFor409

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repositories**

<a id="get_repositories"></a>

> [AbstractApiRepository] get_repositories()

List repositories

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.abstract_api_repository import AbstractApiRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List repositories
        api_response = api_instance.get_repositories()
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repositories: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repositories.ApiResponseFor200) | Repositories list returned                                  |
| 401  | [ApiResponseFor401](#get_repositories.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#get_repositories.ApiResponseFor403) | Insufficient permissions                                    |

#### get_repositories.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                                                                 | Input Type                                                                 | Accessed Type                                                              | Description | Notes |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ----------- | ----- |
| [**AbstractApiRepository**]({{complexTypePrefix}}AbstractApiRepository.md) | [**AbstractApiRepository**]({{complexTypePrefix}}AbstractApiRepository.md) | [**AbstractApiRepository**]({{complexTypePrefix}}AbstractApiRepository.md) |             |

#### get_repositories.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_repositories.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repositories1**

<a id="get_repositories1"></a>

> [RepositoryXO] get_repositories1()

List repositories

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.repository_xo import RepositoryXO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List repositories
        api_response = api_instance.get_repositories1()
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repositories1: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return Types, Responses

| Code | Class                                                     | Description                                                 |
| ---- | --------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization              | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repositories1.ApiResponseFor200) | successful operation                                        |

#### get_repositories1.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                                               | Input Type                                               | Accessed Type                                            | Description | Notes |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | ----------- | ----- |
| [**RepositoryXO**]({{complexTypePrefix}}RepositoryXO.md) | [**RepositoryXO**]({{complexTypePrefix}}RepositoryXO.md) | [**RepositoryXO**]({{complexTypePrefix}}RepositoryXO.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository**

<a id="get_repository"></a>

> RepositoryXO get_repository(repository_name)

Get repository details

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.repository_xo import RepositoryXO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository details
        api_response = api_instance.get_repository(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                  | Description                                                 |
| ---- | ------------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization           | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository.ApiResponseFor200) | successful operation                                        |
| 401  | [ApiResponseFor401](#get_repository.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#get_repository.ApiResponseFor403) | Insufficient permissions                                    |
| 404  | [ApiResponseFor404](#get_repository.ApiResponseFor404) | Repository not found                                        |

#### get_repository.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                             | Description | Notes |
| ------------------------------------------------ | ----------- | ----- |
| [**RepositoryXO**](../../models/RepositoryXO.md) |             |

#### get_repository.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_repository.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_repository.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository1**

<a id="get_repository1"></a>

> SimpleApiGroupRepository get_repository1(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.simple_api_group_repository import SimpleApiGroupRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository1(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository1: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                   | Description                                                 |
| ---- | ------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization            | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository1.ApiResponseFor200) | successful operation                                        |

#### get_repository1.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                     | Description | Notes |
| ------------------------------------------------------------------------ | ----------- | ----- |
| [**SimpleApiGroupRepository**](../../models/SimpleApiGroupRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository10**

<a id="get_repository10"></a>

> SimpleApiHostedRepository get_repository10(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.simple_api_hosted_repository import SimpleApiHostedRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository10(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository10: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository10.ApiResponseFor200) | successful operation                                        |

#### get_repository10.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                       | Description | Notes |
| -------------------------------------------------------------------------- | ----------- | ----- |
| [**SimpleApiHostedRepository**](../../models/SimpleApiHostedRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository11**

<a id="get_repository11"></a>

> NpmProxyApiRepository get_repository11(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.npm_proxy_api_repository import NpmProxyApiRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository11(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository11: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository11.ApiResponseFor200) | successful operation                                        |

#### get_repository11.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                               | Description | Notes |
| ------------------------------------------------------------------ | ----------- | ----- |
| [**NpmProxyApiRepository**](../../models/NpmProxyApiRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository12**

<a id="get_repository12"></a>

> SimpleApiGroupRepository get_repository12(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.simple_api_group_repository import SimpleApiGroupRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository12(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository12: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository12.ApiResponseFor200) | successful operation                                        |

#### get_repository12.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                     | Description | Notes |
| ------------------------------------------------------------------------ | ----------- | ----- |
| [**SimpleApiGroupRepository**](../../models/SimpleApiGroupRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository13**

<a id="get_repository13"></a>

> SimpleApiHostedRepository get_repository13(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.simple_api_hosted_repository import SimpleApiHostedRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository13(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository13: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository13.ApiResponseFor200) | successful operation                                        |

#### get_repository13.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                       | Description | Notes |
| -------------------------------------------------------------------------- | ----------- | ----- |
| [**SimpleApiHostedRepository**](../../models/SimpleApiHostedRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository14**

<a id="get_repository14"></a>

> NugetProxyApiRepository get_repository14(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.nuget_proxy_api_repository import NugetProxyApiRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository14(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository14: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository14.ApiResponseFor200) | successful operation                                        |

#### get_repository14.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                   | Description | Notes |
| ---------------------------------------------------------------------- | ----------- | ----- |
| [**NugetProxyApiRepository**](../../models/NugetProxyApiRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository15**

<a id="get_repository15"></a>

> SimpleApiGroupRepository get_repository15(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.simple_api_group_repository import SimpleApiGroupRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository15(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository15: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository15.ApiResponseFor200) | successful operation                                        |

#### get_repository15.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                     | Description | Notes |
| ------------------------------------------------------------------------ | ----------- | ----- |
| [**SimpleApiGroupRepository**](../../models/SimpleApiGroupRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository16**

<a id="get_repository16"></a>

> SimpleApiHostedRepository get_repository16(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.simple_api_hosted_repository import SimpleApiHostedRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository16(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository16: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository16.ApiResponseFor200) | successful operation                                        |

#### get_repository16.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                       | Description | Notes |
| -------------------------------------------------------------------------- | ----------- | ----- |
| [**SimpleApiHostedRepository**](../../models/SimpleApiHostedRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository17**

<a id="get_repository17"></a>

> SimpleApiProxyRepository get_repository17(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.simple_api_proxy_repository import SimpleApiProxyRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository17(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository17: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository17.ApiResponseFor200) | successful operation                                        |

#### get_repository17.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                     | Description | Notes |
| ------------------------------------------------------------------------ | ----------- | ----- |
| [**SimpleApiProxyRepository**](../../models/SimpleApiProxyRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository18**

<a id="get_repository18"></a>

> SimpleApiGroupRepository get_repository18(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.simple_api_group_repository import SimpleApiGroupRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository18(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository18: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository18.ApiResponseFor200) | successful operation                                        |

#### get_repository18.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                     | Description | Notes |
| ------------------------------------------------------------------------ | ----------- | ----- |
| [**SimpleApiGroupRepository**](../../models/SimpleApiGroupRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository19**

<a id="get_repository19"></a>

> YumHostedApiRepository get_repository19(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.yum_hosted_api_repository import YumHostedApiRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository19(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository19: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository19.ApiResponseFor200) | successful operation                                        |

#### get_repository19.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                 | Description | Notes |
| -------------------------------------------------------------------- | ----------- | ----- |
| [**YumHostedApiRepository**](../../models/YumHostedApiRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository2**

<a id="get_repository2"></a>

> MavenHostedApiRepository get_repository2(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.maven_hosted_api_repository import MavenHostedApiRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository2(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository2: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                   | Description                                                 |
| ---- | ------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization            | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository2.ApiResponseFor200) | successful operation                                        |

#### get_repository2.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                     | Description | Notes |
| ------------------------------------------------------------------------ | ----------- | ----- |
| [**MavenHostedApiRepository**](../../models/MavenHostedApiRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository20**

<a id="get_repository20"></a>

> SimpleApiProxyRepository get_repository20(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.simple_api_proxy_repository import SimpleApiProxyRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository20(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository20: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository20.ApiResponseFor200) | successful operation                                        |

#### get_repository20.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                     | Description | Notes |
| ------------------------------------------------------------------------ | ----------- | ----- |
| [**SimpleApiProxyRepository**](../../models/SimpleApiProxyRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository21**

<a id="get_repository21"></a>

> DockerGroupApiRepository get_repository21(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.docker_group_api_repository import DockerGroupApiRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository21(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository21: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository21.ApiResponseFor200) | successful operation                                        |

#### get_repository21.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                     | Description | Notes |
| ------------------------------------------------------------------------ | ----------- | ----- |
| [**DockerGroupApiRepository**](../../models/DockerGroupApiRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository22**

<a id="get_repository22"></a>

> DockerHostedApiRepository get_repository22(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.docker_hosted_api_repository import DockerHostedApiRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository22(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository22: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository22.ApiResponseFor200) | successful operation                                        |

#### get_repository22.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                       | Description | Notes |
| -------------------------------------------------------------------------- | ----------- | ----- |
| [**DockerHostedApiRepository**](../../models/DockerHostedApiRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository23**

<a id="get_repository23"></a>

> DockerProxyApiRepository get_repository23(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.docker_proxy_api_repository import DockerProxyApiRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository23(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository23: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository23.ApiResponseFor200) | successful operation                                        |

#### get_repository23.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                     | Description | Notes |
| ------------------------------------------------------------------------ | ----------- | ----- |
| [**DockerProxyApiRepository**](../../models/DockerProxyApiRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository24**

<a id="get_repository24"></a>

> SimpleApiGroupRepository get_repository24(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.simple_api_group_repository import SimpleApiGroupRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository24(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository24: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository24.ApiResponseFor200) | successful operation                                        |

#### get_repository24.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                     | Description | Notes |
| ------------------------------------------------------------------------ | ----------- | ----- |
| [**SimpleApiGroupRepository**](../../models/SimpleApiGroupRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository25**

<a id="get_repository25"></a>

> SimpleApiHostedRepository get_repository25(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.simple_api_hosted_repository import SimpleApiHostedRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository25(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository25: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository25.ApiResponseFor200) | successful operation                                        |

#### get_repository25.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                       | Description | Notes |
| -------------------------------------------------------------------------- | ----------- | ----- |
| [**SimpleApiHostedRepository**](../../models/SimpleApiHostedRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository26**

<a id="get_repository26"></a>

> SimpleApiProxyRepository get_repository26(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.simple_api_proxy_repository import SimpleApiProxyRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository26(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository26: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository26.ApiResponseFor200) | successful operation                                        |

#### get_repository26.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                     | Description | Notes |
| ------------------------------------------------------------------------ | ----------- | ----- |
| [**SimpleApiProxyRepository**](../../models/SimpleApiProxyRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository27**

<a id="get_repository27"></a>

> SimpleApiProxyRepository get_repository27(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.simple_api_proxy_repository import SimpleApiProxyRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository27(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository27: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository27.ApiResponseFor200) | successful operation                                        |

#### get_repository27.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                     | Description | Notes |
| ------------------------------------------------------------------------ | ----------- | ----- |
| [**SimpleApiProxyRepository**](../../models/SimpleApiProxyRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository28**

<a id="get_repository28"></a>

> SimpleApiProxyRepository get_repository28(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.simple_api_proxy_repository import SimpleApiProxyRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository28(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository28: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository28.ApiResponseFor200) | successful operation                                        |

#### get_repository28.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                     | Description | Notes |
| ------------------------------------------------------------------------ | ----------- | ----- |
| [**SimpleApiProxyRepository**](../../models/SimpleApiProxyRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository29**

<a id="get_repository29"></a>

> SimpleApiHostedRepository get_repository29(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.simple_api_hosted_repository import SimpleApiHostedRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository29(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository29: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository29.ApiResponseFor200) | successful operation                                        |

#### get_repository29.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                       | Description | Notes |
| -------------------------------------------------------------------------- | ----------- | ----- |
| [**SimpleApiHostedRepository**](../../models/SimpleApiHostedRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository3**

<a id="get_repository3"></a>

> MavenProxyApiRepository get_repository3(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.maven_proxy_api_repository import MavenProxyApiRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository3(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository3: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                   | Description                                                 |
| ---- | ------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization            | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository3.ApiResponseFor200) | successful operation                                        |

#### get_repository3.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                   | Description | Notes |
| ---------------------------------------------------------------------- | ----------- | ----- |
| [**MavenProxyApiRepository**](../../models/MavenProxyApiRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository30**

<a id="get_repository30"></a>

> SimpleApiGroupRepository get_repository30(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.simple_api_group_repository import SimpleApiGroupRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository30(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository30: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository30.ApiResponseFor200) | successful operation                                        |

#### get_repository30.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                     | Description | Notes |
| ------------------------------------------------------------------------ | ----------- | ----- |
| [**SimpleApiGroupRepository**](../../models/SimpleApiGroupRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository31**

<a id="get_repository31"></a>

> SimpleApiHostedRepository get_repository31(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.simple_api_hosted_repository import SimpleApiHostedRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository31(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository31: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository31.ApiResponseFor200) | successful operation                                        |

#### get_repository31.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                       | Description | Notes |
| -------------------------------------------------------------------------- | ----------- | ----- |
| [**SimpleApiHostedRepository**](../../models/SimpleApiHostedRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository32**

<a id="get_repository32"></a>

> SimpleApiProxyRepository get_repository32(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.simple_api_proxy_repository import SimpleApiProxyRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository32(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository32: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository32.ApiResponseFor200) | successful operation                                        |

#### get_repository32.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                     | Description | Notes |
| ------------------------------------------------------------------------ | ----------- | ----- |
| [**SimpleApiProxyRepository**](../../models/SimpleApiProxyRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository33**

<a id="get_repository33"></a>

> SimpleApiProxyRepository get_repository33(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.simple_api_proxy_repository import SimpleApiProxyRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository33(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository33: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository33.ApiResponseFor200) | successful operation                                        |

#### get_repository33.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                     | Description | Notes |
| ------------------------------------------------------------------------ | ----------- | ----- |
| [**SimpleApiProxyRepository**](../../models/SimpleApiProxyRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository34**

<a id="get_repository34"></a>

> SimpleApiGroupRepository get_repository34(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.simple_api_group_repository import SimpleApiGroupRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository34(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository34: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository34.ApiResponseFor200) | successful operation                                        |

#### get_repository34.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                     | Description | Notes |
| ------------------------------------------------------------------------ | ----------- | ----- |
| [**SimpleApiGroupRepository**](../../models/SimpleApiGroupRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository35**

<a id="get_repository35"></a>

> SimpleApiProxyRepository get_repository35(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.simple_api_proxy_repository import SimpleApiProxyRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository35(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository35: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository35.ApiResponseFor200) | successful operation                                        |

#### get_repository35.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                     | Description | Notes |
| ------------------------------------------------------------------------ | ----------- | ----- |
| [**SimpleApiProxyRepository**](../../models/SimpleApiProxyRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository36**

<a id="get_repository36"></a>

> SimpleApiProxyRepository get_repository36(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.simple_api_proxy_repository import SimpleApiProxyRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository36(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository36: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository36.ApiResponseFor200) | successful operation                                        |

#### get_repository36.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                     | Description | Notes |
| ------------------------------------------------------------------------ | ----------- | ----- |
| [**SimpleApiProxyRepository**](../../models/SimpleApiProxyRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository37**

<a id="get_repository37"></a>

> SimpleApiHostedRepository get_repository37(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.simple_api_hosted_repository import SimpleApiHostedRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository37(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository37: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository37.ApiResponseFor200) | successful operation                                        |

#### get_repository37.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                       | Description | Notes |
| -------------------------------------------------------------------------- | ----------- | ----- |
| [**SimpleApiHostedRepository**](../../models/SimpleApiHostedRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository38**

<a id="get_repository38"></a>

> SimpleApiProxyRepository get_repository38(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.simple_api_proxy_repository import SimpleApiProxyRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository38(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository38: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository38.ApiResponseFor200) | successful operation                                        |

#### get_repository38.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                     | Description | Notes |
| ------------------------------------------------------------------------ | ----------- | ----- |
| [**SimpleApiProxyRepository**](../../models/SimpleApiProxyRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository39**

<a id="get_repository39"></a>

> SimpleApiGroupRepository get_repository39(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.simple_api_group_repository import SimpleApiGroupRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository39(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository39: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository39.ApiResponseFor200) | successful operation                                        |

#### get_repository39.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                     | Description | Notes |
| ------------------------------------------------------------------------ | ----------- | ----- |
| [**SimpleApiGroupRepository**](../../models/SimpleApiGroupRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository4**

<a id="get_repository4"></a>

> AptHostedApiRepository get_repository4(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.apt_hosted_api_repository import AptHostedApiRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository4(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository4: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                   | Description                                                 |
| ---- | ------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization            | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository4.ApiResponseFor200) | successful operation                                        |

#### get_repository4.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                 | Description | Notes |
| -------------------------------------------------------------------- | ----------- | ----- |
| [**AptHostedApiRepository**](../../models/AptHostedApiRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository40**

<a id="get_repository40"></a>

> SimpleApiHostedRepository get_repository40(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.simple_api_hosted_repository import SimpleApiHostedRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository40(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository40: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository40.ApiResponseFor200) | successful operation                                        |

#### get_repository40.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                       | Description | Notes |
| -------------------------------------------------------------------------- | ----------- | ----- |
| [**SimpleApiHostedRepository**](../../models/SimpleApiHostedRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository41**

<a id="get_repository41"></a>

> BowerProxyApiRepository get_repository41(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.bower_proxy_api_repository import BowerProxyApiRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository41(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository41: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository41.ApiResponseFor200) | successful operation                                        |

#### get_repository41.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                   | Description | Notes |
| ---------------------------------------------------------------------- | ----------- | ----- |
| [**BowerProxyApiRepository**](../../models/BowerProxyApiRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository5**

<a id="get_repository5"></a>

> AptProxyApiRepository get_repository5(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.apt_proxy_api_repository import AptProxyApiRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository5(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository5: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                   | Description                                                 |
| ---- | ------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization            | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository5.ApiResponseFor200) | successful operation                                        |

#### get_repository5.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                               | Description | Notes |
| ------------------------------------------------------------------ | ----------- | ----- |
| [**AptProxyApiRepository**](../../models/AptProxyApiRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository6**

<a id="get_repository6"></a>

> SimpleApiGroupRepository get_repository6(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.simple_api_group_repository import SimpleApiGroupRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository6(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository6: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                   | Description                                                 |
| ---- | ------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization            | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository6.ApiResponseFor200) | successful operation                                        |

#### get_repository6.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                     | Description | Notes |
| ------------------------------------------------------------------------ | ----------- | ----- |
| [**SimpleApiGroupRepository**](../../models/SimpleApiGroupRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository7**

<a id="get_repository7"></a>

> SimpleApiHostedRepository get_repository7(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.simple_api_hosted_repository import SimpleApiHostedRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository7(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository7: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                   | Description                                                 |
| ---- | ------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization            | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository7.ApiResponseFor200) | successful operation                                        |

#### get_repository7.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                       | Description | Notes |
| -------------------------------------------------------------------------- | ----------- | ----- |
| [**SimpleApiHostedRepository**](../../models/SimpleApiHostedRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository8**

<a id="get_repository8"></a>

> SimpleApiProxyRepository get_repository8(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.simple_api_proxy_repository import SimpleApiProxyRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository8(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository8: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                   | Description                                                 |
| ---- | ------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization            | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository8.ApiResponseFor200) | successful operation                                        |

#### get_repository8.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                     | Description | Notes |
| ------------------------------------------------------------------------ | ----------- | ----- |
| [**SimpleApiProxyRepository**](../../models/SimpleApiProxyRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_repository9**

<a id="get_repository9"></a>

> SimpleApiGroupDeployRepository get_repository9(repository_name)

Get repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.simple_api_group_deploy_repository import SimpleApiGroupDeployRepository
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Get repository
        api_response = api_instance.get_repository9(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repository9: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                   | Description                                                 |
| ---- | ------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization            | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_repository9.ApiResponseFor200) | successful operation                                        |

#### get_repository9.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                                 | Description | Notes |
| ------------------------------------------------------------------------------------ | ----------- | ----- |
| [**SimpleApiGroupDeployRepository**](../../models/SimpleApiGroupDeployRepository.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **invalidate_cache**

<a id="invalidate_cache"></a>

> invalidate_cache(repository_name)

Invalidate repository cache. Proxy or group repositories only.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Invalidate repository cache. Proxy or group repositories only.
        api_response = api_instance.invalidate_cache(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->invalidate_cache: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description      | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                  |
| stream               | bool                                             | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None  | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#invalidate_cache.ApiResponseFor204) | Repository cache invalidated                                |
| 400  | [ApiResponseFor400](#invalidate_cache.ApiResponseFor400) | Repository is not of proxy or group type                    |
| 401  | [ApiResponseFor401](#invalidate_cache.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#invalidate_cache.ApiResponseFor403) | Insufficient permissions                                    |
| 404  | [ApiResponseFor404](#invalidate_cache.ApiResponseFor404) | Repository not found                                        |

#### invalidate_cache.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### invalidate_cache.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### invalidate_cache.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### invalidate_cache.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### invalidate_cache.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **rebuild_index**

<a id="rebuild_index"></a>

> rebuild_index(repository_name)

Schedule a 'Repair - Rebuild repository search' Task. Hosted or proxy repositories only.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Schedule a 'Repair - Rebuild repository search' Task. Hosted or proxy repositories only.
        api_response = api_instance.rebuild_index(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->rebuild_index: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description      | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                  |
| stream               | bool                                             | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None  | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                 | Description                                                 |
| ---- | ----------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization          | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#rebuild_index.ApiResponseFor204) | Repository search index rebuild has been scheduled          |
| 400  | [ApiResponseFor400](#rebuild_index.ApiResponseFor400) | Repository is not of hosted or proxy type                   |
| 401  | [ApiResponseFor401](#rebuild_index.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#rebuild_index.ApiResponseFor403) | Insufficient permissions                                    |
| 404  | [ApiResponseFor404](#rebuild_index.ApiResponseFor404) | Repository not found                                        |

#### rebuild_index.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### rebuild_index.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### rebuild_index.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### rebuild_index.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### rebuild_index.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository**

<a id="update_repository"></a>

> update_repository(repository_name)

Update Maven group repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.maven_group_repository_api_request import MavenGroupRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update Maven group repository
        api_response = api_instance.update_repository(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = MavenGroupRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        group=GroupAttributes(
            member_names=[
                "member_names_example"
            ],
        ),
    )
    try:
        # Update Maven group repository
        api_response = api_instance.update_repository(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                 | Description | Notes |
| ------------------------------------------------------------------------------------ | ----------- | ----- |
| [**MavenGroupRepositoryApiRequest**](../../models/MavenGroupRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                     | Description                                                 |
| ---- | --------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization              | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository.ApiResponseFor403) | Insufficient permissions                                    |

#### update_repository.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository1**

<a id="update_repository1"></a>

> update_repository1(repository_name)

Update Maven hosted repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.maven_hosted_repository_api_request import MavenHostedRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update Maven hosted repository
        api_response = api_instance.update_repository1(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository1: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = MavenHostedRepositoryApiRequest(
        name="internal",
        online=True,
        storage=HostedStorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
            write_policy="allow_once",
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        component=ComponentAttributes(
            proprietary_components=True,
        ),
        maven=MavenAttributes(
            version_policy="MIXED",
            layout_policy="STRICT",
            content_disposition="ATTACHMENT",
        ),
    )
    try:
        # Update Maven hosted repository
        api_response = api_instance.update_repository1(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository1: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                   | Description | Notes |
| -------------------------------------------------------------------------------------- | ----------- | ----- |
| [**MavenHostedRepositoryApiRequest**](../../models/MavenHostedRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                      | Description                                                 |
| ---- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization               | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository1.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository1.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository1.ApiResponseFor403) | Insufficient permissions                                    |

#### update_repository1.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository1.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository1.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository10**

<a id="update_repository10"></a>

> update_repository10(repository_name)

Update npm proxy repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.npm_proxy_repository_api_request import NpmProxyRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update npm proxy repository
        api_response = api_instance.update_repository10(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository10: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = NpmProxyRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        proxy=ProxyAttributes(
            remote_url="https://remote.repository.com",
            content_max_age=1440,
            metadata_max_age=1440,
        ),
        negative_cache=NegativeCacheAttributes(
            enabled=True,
            time_to_live=1440,
        ),
        http_client=HttpClientAttributes(
            blocked=False,
            auto_block=True,
            connection=HttpClientConnectionAttributes(
                retries=0,
                user_agent_suffix="user_agent_suffix_example",
                timeout=60,
                enable_circular_redirects=False,
                enable_cookies=False,
                use_trust_store=False,
            ),
            authentication=HttpClientConnectionAuthenticationAttributes(
                type="username",
                username="username_example",
                password="password_example",
                ntlm_host="ntlm_host_example",
                ntlm_domain="ntlm_domain_example",
            ),
        ),
        routing_rule="routing_rule_example",
        replication=ReplicationAttributes(
            preemptive_pull_enabled=True,
            asset_path_regex="asset_path_regex_example",
        ),
        npm=NpmAttributes(
            remove_non_cataloged=True,
            remove_quarantined=True,
        ),
    )
    try:
        # Update npm proxy repository
        api_response = api_instance.update_repository10(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository10: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                             | Description | Notes |
| -------------------------------------------------------------------------------- | ----------- | ----- |
| [**NpmProxyRepositoryApiRequest**](../../models/NpmProxyRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository10.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository10.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository10.ApiResponseFor403) | Insufficient permissions                                    |

#### update_repository10.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository10.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository10.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository11**

<a id="update_repository11"></a>

> update_repository11(repository_name)

Update NuGet group repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.nuget_group_repository_api_request import NugetGroupRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update NuGet group repository
        api_response = api_instance.update_repository11(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository11: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = NugetGroupRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        group=GroupAttributes(
            member_names=[
                "member_names_example"
            ],
        ),
    )
    try:
        # Update NuGet group repository
        api_response = api_instance.update_repository11(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository11: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                 | Description | Notes |
| ------------------------------------------------------------------------------------ | ----------- | ----- |
| [**NugetGroupRepositoryApiRequest**](../../models/NugetGroupRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository11.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository11.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository11.ApiResponseFor403) | Insufficient permissions                                    |

#### update_repository11.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository11.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository11.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository12**

<a id="update_repository12"></a>

> update_repository12(repository_name)

Update NuGet hosted repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.nuget_hosted_repository_api_request import NugetHostedRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update NuGet hosted repository
        api_response = api_instance.update_repository12(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository12: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = NugetHostedRepositoryApiRequest(
        name="internal",
        online=True,
        storage=HostedStorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
            write_policy="allow_once",
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        component=ComponentAttributes(
            proprietary_components=True,
        ),
    )
    try:
        # Update NuGet hosted repository
        api_response = api_instance.update_repository12(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository12: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                   | Description | Notes |
| -------------------------------------------------------------------------------------- | ----------- | ----- |
| [**NugetHostedRepositoryApiRequest**](../../models/NugetHostedRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository12.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository12.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository12.ApiResponseFor403) | Insufficient permissions                                    |

#### update_repository12.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository12.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository12.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository13**

<a id="update_repository13"></a>

> update_repository13(repository_name)

Update NuGet proxy repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.nuget_proxy_repository_api_request import NugetProxyRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update NuGet proxy repository
        api_response = api_instance.update_repository13(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository13: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = NugetProxyRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        proxy=ProxyAttributes(
            remote_url="https://remote.repository.com",
            content_max_age=1440,
            metadata_max_age=1440,
        ),
        negative_cache=NegativeCacheAttributes(
            enabled=True,
            time_to_live=1440,
        ),
        http_client=HttpClientAttributes(
            blocked=False,
            auto_block=True,
            connection=HttpClientConnectionAttributes(
                retries=0,
                user_agent_suffix="user_agent_suffix_example",
                timeout=60,
                enable_circular_redirects=False,
                enable_cookies=False,
                use_trust_store=False,
            ),
            authentication=HttpClientConnectionAuthenticationAttributes(
                type="username",
                username="username_example",
                password="password_example",
                ntlm_host="ntlm_host_example",
                ntlm_domain="ntlm_domain_example",
            ),
        ),
        routing_rule="routing_rule_example",
        replication=ReplicationAttributes(
            preemptive_pull_enabled=True,
            asset_path_regex="asset_path_regex_example",
        ),
        nuget_proxy=NugetAttributes(
            query_cache_item_max_age=3600,
            nuget_version="V3",
        ),
    )
    try:
        # Update NuGet proxy repository
        api_response = api_instance.update_repository13(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository13: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                 | Description | Notes |
| ------------------------------------------------------------------------------------ | ----------- | ----- |
| [**NugetProxyRepositoryApiRequest**](../../models/NugetProxyRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository13.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository13.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository13.ApiResponseFor403) | Insufficient permissions                                    |

#### update_repository13.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository13.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository13.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository14**

<a id="update_repository14"></a>

> update_repository14(repository_name)

Update RubyGems group repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.ruby_gems_group_repository_api_request import RubyGemsGroupRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update RubyGems group repository
        api_response = api_instance.update_repository14(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository14: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = RubyGemsGroupRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        group=GroupAttributes(
            member_names=[
                "member_names_example"
            ],
        ),
    )
    try:
        # Update RubyGems group repository
        api_response = api_instance.update_repository14(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository14: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                       | Description | Notes |
| ------------------------------------------------------------------------------------------ | ----------- | ----- |
| [**RubyGemsGroupRepositoryApiRequest**](../../models/RubyGemsGroupRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository14.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository14.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository14.ApiResponseFor403) | Insufficient permissions                                    |

#### update_repository14.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository14.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository14.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository15**

<a id="update_repository15"></a>

> update_repository15(repository_name)

Update RubyGems hosted repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.ruby_gems_hosted_repository_api_request import RubyGemsHostedRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update RubyGems hosted repository
        api_response = api_instance.update_repository15(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository15: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = RubyGemsHostedRepositoryApiRequest(
        name="internal",
        online=True,
        storage=HostedStorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
            write_policy="allow_once",
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        component=ComponentAttributes(
            proprietary_components=True,
        ),
    )
    try:
        # Update RubyGems hosted repository
        api_response = api_instance.update_repository15(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository15: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                         | Description | Notes |
| -------------------------------------------------------------------------------------------- | ----------- | ----- |
| [**RubyGemsHostedRepositoryApiRequest**](../../models/RubyGemsHostedRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository15.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository15.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository15.ApiResponseFor403) | Insufficient permissions                                    |

#### update_repository15.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository15.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository15.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository16**

<a id="update_repository16"></a>

> update_repository16(repository_name)

Update RubyGems proxy repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.ruby_gems_proxy_repository_api_request import RubyGemsProxyRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update RubyGems proxy repository
        api_response = api_instance.update_repository16(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository16: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = RubyGemsProxyRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        proxy=ProxyAttributes(
            remote_url="https://remote.repository.com",
            content_max_age=1440,
            metadata_max_age=1440,
        ),
        negative_cache=NegativeCacheAttributes(
            enabled=True,
            time_to_live=1440,
        ),
        http_client=HttpClientAttributes(
            blocked=False,
            auto_block=True,
            connection=HttpClientConnectionAttributes(
                retries=0,
                user_agent_suffix="user_agent_suffix_example",
                timeout=60,
                enable_circular_redirects=False,
                enable_cookies=False,
                use_trust_store=False,
            ),
            authentication=HttpClientConnectionAuthenticationAttributes(
                type="username",
                username="username_example",
                password="password_example",
                ntlm_host="ntlm_host_example",
                ntlm_domain="ntlm_domain_example",
            ),
        ),
        routing_rule="routing_rule_example",
        replication=ReplicationAttributes(
            preemptive_pull_enabled=True,
            asset_path_regex="asset_path_regex_example",
        ),
    )
    try:
        # Update RubyGems proxy repository
        api_response = api_instance.update_repository16(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository16: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                       | Description | Notes |
| ------------------------------------------------------------------------------------------ | ----------- | ----- |
| [**RubyGemsProxyRepositoryApiRequest**](../../models/RubyGemsProxyRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository16.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository16.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository16.ApiResponseFor403) | Insufficient permissions                                    |

#### update_repository16.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository16.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository16.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository17**

<a id="update_repository17"></a>

> update_repository17(repository_name)

Update Yum group repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.yum_group_repository_api_request import YumGroupRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update Yum group repository
        api_response = api_instance.update_repository17(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository17: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = YumGroupRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        group=GroupAttributes(
            member_names=[
                "member_names_example"
            ],
        ),
        yum_signing=YumSigningRepositoriesAttributes(
            keypair="keypair_example",
            passphrase="passphrase_example",
        ),
    )
    try:
        # Update Yum group repository
        api_response = api_instance.update_repository17(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository17: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                             | Description | Notes |
| -------------------------------------------------------------------------------- | ----------- | ----- |
| [**YumGroupRepositoryApiRequest**](../../models/YumGroupRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository17.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository17.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository17.ApiResponseFor403) | Insufficient permissions                                    |

#### update_repository17.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository17.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository17.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository18**

<a id="update_repository18"></a>

> update_repository18(repository_name)

Update Yum hosted repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.yum_hosted_repository_api_request import YumHostedRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update Yum hosted repository
        api_response = api_instance.update_repository18(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository18: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = YumHostedRepositoryApiRequest(
        name="internal",
        online=True,
        storage=HostedStorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
            write_policy="allow_once",
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        component=ComponentAttributes(
            proprietary_components=True,
        ),
        yum=YumAttributes(
            repodata_depth=5,
            deploy_policy="STRICT",
        ),
    )
    try:
        # Update Yum hosted repository
        api_response = api_instance.update_repository18(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository18: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                               | Description | Notes |
| ---------------------------------------------------------------------------------- | ----------- | ----- |
| [**YumHostedRepositoryApiRequest**](../../models/YumHostedRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository18.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository18.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository18.ApiResponseFor403) | Insufficient permissions                                    |

#### update_repository18.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository18.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository18.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository19**

<a id="update_repository19"></a>

> update_repository19(repository_name)

Update Yum proxy repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.yum_proxy_repository_api_request import YumProxyRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update Yum proxy repository
        api_response = api_instance.update_repository19(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository19: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = YumProxyRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        proxy=ProxyAttributes(
            remote_url="https://remote.repository.com",
            content_max_age=1440,
            metadata_max_age=1440,
        ),
        negative_cache=NegativeCacheAttributes(
            enabled=True,
            time_to_live=1440,
        ),
        http_client=HttpClientAttributes(
            blocked=False,
            auto_block=True,
            connection=HttpClientConnectionAttributes(
                retries=0,
                user_agent_suffix="user_agent_suffix_example",
                timeout=60,
                enable_circular_redirects=False,
                enable_cookies=False,
                use_trust_store=False,
            ),
            authentication=HttpClientConnectionAuthenticationAttributes(
                type="username",
                username="username_example",
                password="password_example",
                ntlm_host="ntlm_host_example",
                ntlm_domain="ntlm_domain_example",
            ),
        ),
        routing_rule="routing_rule_example",
        replication=ReplicationAttributes(
            preemptive_pull_enabled=True,
            asset_path_regex="asset_path_regex_example",
        ),
        yum_signing=YumSigningRepositoriesAttributes(
            keypair="keypair_example",
            passphrase="passphrase_example",
        ),
    )
    try:
        # Update Yum proxy repository
        api_response = api_instance.update_repository19(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository19: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                             | Description | Notes |
| -------------------------------------------------------------------------------- | ----------- | ----- |
| [**YumProxyRepositoryApiRequest**](../../models/YumProxyRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository19.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository19.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository19.ApiResponseFor403) | Insufficient permissions                                    |

#### update_repository19.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository19.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository19.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository2**

<a id="update_repository2"></a>

> update_repository2(repository_name)

Update Maven proxy repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.maven_proxy_repository_api_request import MavenProxyRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update Maven proxy repository
        api_response = api_instance.update_repository2(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository2: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = MavenProxyRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        proxy=ProxyAttributes(
            remote_url="https://remote.repository.com",
            content_max_age=1440,
            metadata_max_age=1440,
        ),
        negative_cache=NegativeCacheAttributes(
            enabled=True,
            time_to_live=1440,
        ),
        http_client=HttpClientAttributesWithPreemptiveAuth(
            blocked=False,
            auto_block=True,
            connection=HttpClientConnectionAttributes(
                retries=0,
                user_agent_suffix="user_agent_suffix_example",
                timeout=60,
                enable_circular_redirects=False,
                enable_cookies=False,
                use_trust_store=False,
            ),
            authentication=HttpClientConnectionAuthenticationAttributesWithPreemptive(
                type="username",
                username="username_example",
                password="password_example",
                ntlm_host="ntlm_host_example",
                ntlm_domain="ntlm_domain_example",
                preemptive=False,
            ),
        ),
        routing_rule="routing_rule_example",
        replication=ReplicationAttributes(
            preemptive_pull_enabled=True,
            asset_path_regex="asset_path_regex_example",
        ),
        maven=MavenAttributes(
            version_policy="MIXED",
            layout_policy="STRICT",
            content_disposition="ATTACHMENT",
        ),
    )
    try:
        # Update Maven proxy repository
        api_response = api_instance.update_repository2(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository2: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                 | Description | Notes |
| ------------------------------------------------------------------------------------ | ----------- | ----- |
| [**MavenProxyRepositoryApiRequest**](../../models/MavenProxyRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                      | Description                                                 |
| ---- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization               | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository2.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository2.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository2.ApiResponseFor403) | Insufficient permissions                                    |

#### update_repository2.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository2.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository2.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository20**

<a id="update_repository20"></a>

> update_repository20(repository_name)

Update Docker group repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.docker_group_repository_api_request import DockerGroupRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update Docker group repository
        api_response = api_instance.update_repository20(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository20: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = DockerGroupRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        group=GroupDeployAttributes(
            member_names=[
                "member_names_example"
            ],
            writable_member="writable_member_example",
        ),
        docker=DockerAttributes(
            v1_enabled=False,
            force_basic_auth=True,
            http_port=8082,
            https_port=8083,
            subdomain="docker-a",
        ),
    )
    try:
        # Update Docker group repository
        api_response = api_instance.update_repository20(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository20: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                   | Description | Notes |
| -------------------------------------------------------------------------------------- | ----------- | ----- |
| [**DockerGroupRepositoryApiRequest**](../../models/DockerGroupRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository20.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository20.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository20.ApiResponseFor403) | Insufficient permissions                                    |
| 404  | [ApiResponseFor404](#update_repository20.ApiResponseFor404) | Repository not found                                        |

#### update_repository20.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository20.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository20.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository20.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository21**

<a id="update_repository21"></a>

> update_repository21(repository_name)

Update Docker hosted repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.docker_hosted_repository_api_request import DockerHostedRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update Docker hosted repository
        api_response = api_instance.update_repository21(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository21: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = DockerHostedRepositoryApiRequest(
        name="internal",
        online=True,
        storage=DockerHostedStorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
            write_policy="allow_once",
            latest_policy=True,
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        component=ComponentAttributes(
            proprietary_components=True,
        ),
        docker=DockerAttributes(
            v1_enabled=False,
            force_basic_auth=True,
            http_port=8082,
            https_port=8083,
            subdomain="docker-a",
        ),
    )
    try:
        # Update Docker hosted repository
        api_response = api_instance.update_repository21(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository21: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                     | Description | Notes |
| ---------------------------------------------------------------------------------------- | ----------- | ----- |
| [**DockerHostedRepositoryApiRequest**](../../models/DockerHostedRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository21.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository21.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository21.ApiResponseFor403) | Insufficient permissions                                    |
| 404  | [ApiResponseFor404](#update_repository21.ApiResponseFor404) | Repository not found                                        |

#### update_repository21.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository21.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository21.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository21.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository22**

<a id="update_repository22"></a>

> update_repository22(repository_name)

Update Docker group repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.docker_proxy_repository_api_request import DockerProxyRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update Docker group repository
        api_response = api_instance.update_repository22(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository22: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = DockerProxyRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        proxy=ProxyAttributes(
            remote_url="https://remote.repository.com",
            content_max_age=1440,
            metadata_max_age=1440,
        ),
        negative_cache=NegativeCacheAttributes(
            enabled=True,
            time_to_live=1440,
        ),
        http_client=HttpClientAttributes(
            blocked=False,
            auto_block=True,
            connection=HttpClientConnectionAttributes(
                retries=0,
                user_agent_suffix="user_agent_suffix_example",
                timeout=60,
                enable_circular_redirects=False,
                enable_cookies=False,
                use_trust_store=False,
            ),
            authentication=HttpClientConnectionAuthenticationAttributes(
                type="username",
                username="username_example",
                password="password_example",
                ntlm_host="ntlm_host_example",
                ntlm_domain="ntlm_domain_example",
            ),
        ),
        routing_rule="routing_rule_example",
        replication=ReplicationAttributes(
            preemptive_pull_enabled=True,
            asset_path_regex="asset_path_regex_example",
        ),
        docker=DockerAttributes(
            v1_enabled=False,
            force_basic_auth=True,
            http_port=8082,
            https_port=8083,
            subdomain="docker-a",
        ),
        docker_proxy=DockerProxyAttributes(
            index_type="HUB",
            index_url="index_url_example",
            cache_foreign_layers=True,
            foreign_layer_url_whitelist=[
                "foreign_layer_url_whitelist_example"
            ],
        ),
    )
    try:
        # Update Docker group repository
        api_response = api_instance.update_repository22(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository22: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                   | Description | Notes |
| -------------------------------------------------------------------------------------- | ----------- | ----- |
| [**DockerProxyRepositoryApiRequest**](../../models/DockerProxyRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository22.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository22.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository22.ApiResponseFor403) | Insufficient permissions                                    |
| 404  | [ApiResponseFor404](#update_repository22.ApiResponseFor404) | Repository not found                                        |

#### update_repository22.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository22.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository22.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository22.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository23**

<a id="update_repository23"></a>

> update_repository23(repository_name)

Update PyPI group repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.pypi_group_repository_api_request import PypiGroupRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update PyPI group repository
        api_response = api_instance.update_repository23(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository23: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = PypiGroupRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        group=GroupAttributes(
            member_names=[
                "member_names_example"
            ],
        ),
    )
    try:
        # Update PyPI group repository
        api_response = api_instance.update_repository23(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository23: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                               | Description | Notes |
| ---------------------------------------------------------------------------------- | ----------- | ----- |
| [**PypiGroupRepositoryApiRequest**](../../models/PypiGroupRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository23.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository23.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository23.ApiResponseFor403) | Insufficient permissions                                    |

#### update_repository23.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository23.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository23.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository24**

<a id="update_repository24"></a>

> update_repository24(repository_name)

Update PyPI hosted repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.pypi_hosted_repository_api_request import PypiHostedRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update PyPI hosted repository
        api_response = api_instance.update_repository24(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository24: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = PypiHostedRepositoryApiRequest(
        name="internal",
        online=True,
        storage=HostedStorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
            write_policy="allow_once",
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        component=ComponentAttributes(
            proprietary_components=True,
        ),
    )
    try:
        # Update PyPI hosted repository
        api_response = api_instance.update_repository24(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository24: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                 | Description | Notes |
| ------------------------------------------------------------------------------------ | ----------- | ----- |
| [**PypiHostedRepositoryApiRequest**](../../models/PypiHostedRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository24.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository24.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository24.ApiResponseFor403) | Insufficient permissions                                    |

#### update_repository24.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository24.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository24.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository25**

<a id="update_repository25"></a>

> update_repository25(repository_name)

Update PyPI proxy repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.pypi_proxy_repository_api_request import PypiProxyRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update PyPI proxy repository
        api_response = api_instance.update_repository25(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository25: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = PypiProxyRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        proxy=ProxyAttributes(
            remote_url="https://remote.repository.com",
            content_max_age=1440,
            metadata_max_age=1440,
        ),
        negative_cache=NegativeCacheAttributes(
            enabled=True,
            time_to_live=1440,
        ),
        http_client=HttpClientAttributes(
            blocked=False,
            auto_block=True,
            connection=HttpClientConnectionAttributes(
                retries=0,
                user_agent_suffix="user_agent_suffix_example",
                timeout=60,
                enable_circular_redirects=False,
                enable_cookies=False,
                use_trust_store=False,
            ),
            authentication=HttpClientConnectionAuthenticationAttributes(
                type="username",
                username="username_example",
                password="password_example",
                ntlm_host="ntlm_host_example",
                ntlm_domain="ntlm_domain_example",
            ),
        ),
        routing_rule="routing_rule_example",
        replication=ReplicationAttributes(
            preemptive_pull_enabled=True,
            asset_path_regex="asset_path_regex_example",
        ),
    )
    try:
        # Update PyPI proxy repository
        api_response = api_instance.update_repository25(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository25: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                               | Description | Notes |
| ---------------------------------------------------------------------------------- | ----------- | ----- |
| [**PypiProxyRepositoryApiRequest**](../../models/PypiProxyRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository25.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository25.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository25.ApiResponseFor403) | Insufficient permissions                                    |

#### update_repository25.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository25.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository25.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository26**

<a id="update_repository26"></a>

> update_repository26(repository_name)

Update conda proxy repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.conda_proxy_repository_api_request import CondaProxyRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update conda proxy repository
        api_response = api_instance.update_repository26(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository26: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = CondaProxyRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        proxy=ProxyAttributes(
            remote_url="https://remote.repository.com",
            content_max_age=1440,
            metadata_max_age=1440,
        ),
        negative_cache=NegativeCacheAttributes(
            enabled=True,
            time_to_live=1440,
        ),
        http_client=HttpClientAttributes(
            blocked=False,
            auto_block=True,
            connection=HttpClientConnectionAttributes(
                retries=0,
                user_agent_suffix="user_agent_suffix_example",
                timeout=60,
                enable_circular_redirects=False,
                enable_cookies=False,
                use_trust_store=False,
            ),
            authentication=HttpClientConnectionAuthenticationAttributes(
                type="username",
                username="username_example",
                password="password_example",
                ntlm_host="ntlm_host_example",
                ntlm_domain="ntlm_domain_example",
            ),
        ),
        routing_rule="routing_rule_example",
        replication=ReplicationAttributes(
            preemptive_pull_enabled=True,
            asset_path_regex="asset_path_regex_example",
        ),
    )
    try:
        # Update conda proxy repository
        api_response = api_instance.update_repository26(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository26: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                 | Description | Notes |
| ------------------------------------------------------------------------------------ | ----------- | ----- |
| [**CondaProxyRepositoryApiRequest**](../../models/CondaProxyRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository26.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository26.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository26.ApiResponseFor403) | Insufficient permissions                                    |

#### update_repository26.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository26.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository26.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository27**

<a id="update_repository27"></a>

> update_repository27(repository_name)

Update Conan proxy repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.conan_proxy_repository_api_request import ConanProxyRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update Conan proxy repository
        api_response = api_instance.update_repository27(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository27: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = ConanProxyRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        proxy=ProxyAttributes(
            remote_url="https://remote.repository.com",
            content_max_age=1440,
            metadata_max_age=1440,
        ),
        negative_cache=NegativeCacheAttributes(
            enabled=True,
            time_to_live=1440,
        ),
        http_client=HttpClientAttributes(
            blocked=False,
            auto_block=True,
            connection=HttpClientConnectionAttributes(
                retries=0,
                user_agent_suffix="user_agent_suffix_example",
                timeout=60,
                enable_circular_redirects=False,
                enable_cookies=False,
                use_trust_store=False,
            ),
            authentication=HttpClientConnectionAuthenticationAttributes(
                type="username",
                username="username_example",
                password="password_example",
                ntlm_host="ntlm_host_example",
                ntlm_domain="ntlm_domain_example",
            ),
        ),
        routing_rule="routing_rule_example",
        replication=ReplicationAttributes(
            preemptive_pull_enabled=True,
            asset_path_regex="asset_path_regex_example",
        ),
    )
    try:
        # Update Conan proxy repository
        api_response = api_instance.update_repository27(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository27: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                 | Description | Notes |
| ------------------------------------------------------------------------------------ | ----------- | ----- |
| [**ConanProxyRepositoryApiRequest**](../../models/ConanProxyRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository27.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository27.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository27.ApiResponseFor403) | Insufficient permissions                                    |
| 404  | [ApiResponseFor404](#update_repository27.ApiResponseFor404) | Repository not found                                        |

#### update_repository27.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository27.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository27.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository27.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository28**

<a id="update_repository28"></a>

> update_repository28(repository_name)

Update Git LFS hosted repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.git_lfs_hosted_repository_api_request import GitLfsHostedRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update Git LFS hosted repository
        api_response = api_instance.update_repository28(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository28: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = GitLfsHostedRepositoryApiRequest(
        name="internal",
        online=True,
        storage=HostedStorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
            write_policy="allow_once",
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        component=ComponentAttributes(
            proprietary_components=True,
        ),
    )
    try:
        # Update Git LFS hosted repository
        api_response = api_instance.update_repository28(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository28: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                     | Description | Notes |
| ---------------------------------------------------------------------------------------- | ----------- | ----- |
| [**GitLfsHostedRepositoryApiRequest**](../../models/GitLfsHostedRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository28.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository28.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository28.ApiResponseFor403) | Insufficient permissions                                    |

#### update_repository28.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository28.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository28.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository29**

<a id="update_repository29"></a>

> update_repository29(repository_name)

Update R group repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.r_group_repository_api_request import RGroupRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update R group repository
        api_response = api_instance.update_repository29(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository29: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = RGroupRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        group=GroupAttributes(
            member_names=[
                "member_names_example"
            ],
        ),
    )
    try:
        # Update R group repository
        api_response = api_instance.update_repository29(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository29: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                         | Description | Notes |
| ---------------------------------------------------------------------------- | ----------- | ----- |
| [**RGroupRepositoryApiRequest**](../../models/RGroupRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository29.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository29.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository29.ApiResponseFor403) | Insufficient permissions                                    |

#### update_repository29.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository29.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository29.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository3**

<a id="update_repository3"></a>

> update_repository3(repository_name)

Update APT hosted repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.apt_hosted_repository_api_request import AptHostedRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update APT hosted repository
        api_response = api_instance.update_repository3(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository3: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = AptHostedRepositoryApiRequest(
        name="internal",
        online=True,
        storage=HostedStorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
            write_policy="allow_once",
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        component=ComponentAttributes(
            proprietary_components=True,
        ),
        apt=AptHostedRepositoriesAttributes(
            distribution="bionic",
        ),
        apt_signing=AptSigningRepositoriesAttributes(
            keypair="keypair_example",
            passphrase="passphrase_example",
        ),
    )
    try:
        # Update APT hosted repository
        api_response = api_instance.update_repository3(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository3: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                               | Description | Notes |
| ---------------------------------------------------------------------------------- | ----------- | ----- |
| [**AptHostedRepositoryApiRequest**](../../models/AptHostedRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                      | Description                                                 |
| ---- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization               | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository3.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository3.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository3.ApiResponseFor403) | Insufficient permissions                                    |
| 404  | [ApiResponseFor404](#update_repository3.ApiResponseFor404) | Repository not found                                        |

#### update_repository3.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository3.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository3.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository3.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository30**

<a id="update_repository30"></a>

> update_repository30(repository_name)

Update R hosted repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.r_hosted_repository_api_request import RHostedRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update R hosted repository
        api_response = api_instance.update_repository30(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository30: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = RHostedRepositoryApiRequest(
        name="internal",
        online=True,
        storage=HostedStorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
            write_policy="allow_once",
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        component=ComponentAttributes(
            proprietary_components=True,
        ),
    )
    try:
        # Update R hosted repository
        api_response = api_instance.update_repository30(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository30: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                           | Description | Notes |
| ------------------------------------------------------------------------------ | ----------- | ----- |
| [**RHostedRepositoryApiRequest**](../../models/RHostedRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository30.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository30.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository30.ApiResponseFor403) | Insufficient permissions                                    |

#### update_repository30.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository30.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository30.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository31**

<a id="update_repository31"></a>

> update_repository31(repository_name)

Update R proxy repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.r_proxy_repository_api_request import RProxyRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update R proxy repository
        api_response = api_instance.update_repository31(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository31: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = RProxyRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        proxy=ProxyAttributes(
            remote_url="https://remote.repository.com",
            content_max_age=1440,
            metadata_max_age=1440,
        ),
        negative_cache=NegativeCacheAttributes(
            enabled=True,
            time_to_live=1440,
        ),
        http_client=HttpClientAttributes(
            blocked=False,
            auto_block=True,
            connection=HttpClientConnectionAttributes(
                retries=0,
                user_agent_suffix="user_agent_suffix_example",
                timeout=60,
                enable_circular_redirects=False,
                enable_cookies=False,
                use_trust_store=False,
            ),
            authentication=HttpClientConnectionAuthenticationAttributes(
                type="username",
                username="username_example",
                password="password_example",
                ntlm_host="ntlm_host_example",
                ntlm_domain="ntlm_domain_example",
            ),
        ),
        routing_rule="routing_rule_example",
        replication=ReplicationAttributes(
            preemptive_pull_enabled=True,
            asset_path_regex="asset_path_regex_example",
        ),
    )
    try:
        # Update R proxy repository
        api_response = api_instance.update_repository31(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository31: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                         | Description | Notes |
| ---------------------------------------------------------------------------- | ----------- | ----- |
| [**RProxyRepositoryApiRequest**](../../models/RProxyRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository31.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository31.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository31.ApiResponseFor403) | Insufficient permissions                                    |
| 404  | [ApiResponseFor404](#update_repository31.ApiResponseFor404) | Repository not found                                        |

#### update_repository31.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository31.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository31.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository31.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository32**

<a id="update_repository32"></a>

> update_repository32(repository_name)

Update Cocoapods proxy repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.cocoapods_proxy_repository_api_request import CocoapodsProxyRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update Cocoapods proxy repository
        api_response = api_instance.update_repository32(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository32: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = CocoapodsProxyRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        proxy=ProxyAttributes(
            remote_url="https://remote.repository.com",
            content_max_age=1440,
            metadata_max_age=1440,
        ),
        negative_cache=NegativeCacheAttributes(
            enabled=True,
            time_to_live=1440,
        ),
        http_client=HttpClientAttributes(
            blocked=False,
            auto_block=True,
            connection=HttpClientConnectionAttributes(
                retries=0,
                user_agent_suffix="user_agent_suffix_example",
                timeout=60,
                enable_circular_redirects=False,
                enable_cookies=False,
                use_trust_store=False,
            ),
            authentication=HttpClientConnectionAuthenticationAttributes(
                type="username",
                username="username_example",
                password="password_example",
                ntlm_host="ntlm_host_example",
                ntlm_domain="ntlm_domain_example",
            ),
        ),
        routing_rule="routing_rule_example",
        replication=ReplicationAttributes(
            preemptive_pull_enabled=True,
            asset_path_regex="asset_path_regex_example",
        ),
    )
    try:
        # Update Cocoapods proxy repository
        api_response = api_instance.update_repository32(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository32: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                         | Description | Notes |
| -------------------------------------------------------------------------------------------- | ----------- | ----- |
| [**CocoapodsProxyRepositoryApiRequest**](../../models/CocoapodsProxyRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository32.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository32.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository32.ApiResponseFor403) | Insufficient permissions                                    |

#### update_repository32.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository32.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository32.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository33**

<a id="update_repository33"></a>

> update_repository33(repository_name)

Update a Go group repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.golang_group_repository_api_request import GolangGroupRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update a Go group repository
        api_response = api_instance.update_repository33(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository33: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = GolangGroupRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        group=GroupAttributes(
            member_names=[
                "member_names_example"
            ],
        ),
    )
    try:
        # Update a Go group repository
        api_response = api_instance.update_repository33(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository33: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                   | Description | Notes |
| -------------------------------------------------------------------------------------- | ----------- | ----- |
| [**GolangGroupRepositoryApiRequest**](../../models/GolangGroupRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository33.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository33.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository33.ApiResponseFor403) | Insufficient permissions                                    |
| 404  | [ApiResponseFor404](#update_repository33.ApiResponseFor404) | Repository not found                                        |

#### update_repository33.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository33.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository33.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository33.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository34**

<a id="update_repository34"></a>

> update_repository34(repository_name)

Update a Go proxy repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.golang_proxy_repository_api_request import GolangProxyRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update a Go proxy repository
        api_response = api_instance.update_repository34(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository34: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = GolangProxyRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        proxy=ProxyAttributes(
            remote_url="https://remote.repository.com",
            content_max_age=1440,
            metadata_max_age=1440,
        ),
        negative_cache=NegativeCacheAttributes(
            enabled=True,
            time_to_live=1440,
        ),
        http_client=HttpClientAttributes(
            blocked=False,
            auto_block=True,
            connection=HttpClientConnectionAttributes(
                retries=0,
                user_agent_suffix="user_agent_suffix_example",
                timeout=60,
                enable_circular_redirects=False,
                enable_cookies=False,
                use_trust_store=False,
            ),
            authentication=HttpClientConnectionAuthenticationAttributes(
                type="username",
                username="username_example",
                password="password_example",
                ntlm_host="ntlm_host_example",
                ntlm_domain="ntlm_domain_example",
            ),
        ),
        routing_rule="routing_rule_example",
        replication=ReplicationAttributes(
            preemptive_pull_enabled=True,
            asset_path_regex="asset_path_regex_example",
        ),
    )
    try:
        # Update a Go proxy repository
        api_response = api_instance.update_repository34(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository34: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                   | Description | Notes |
| -------------------------------------------------------------------------------------- | ----------- | ----- |
| [**GolangProxyRepositoryApiRequest**](../../models/GolangProxyRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository34.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository34.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository34.ApiResponseFor403) | Insufficient permissions                                    |
| 404  | [ApiResponseFor404](#update_repository34.ApiResponseFor404) | Repository not found                                        |

#### update_repository34.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository34.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository34.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository34.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository35**

<a id="update_repository35"></a>

> update_repository35(repository_name)

Update p2 proxy repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.p2_proxy_repository_api_request import P2ProxyRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update p2 proxy repository
        api_response = api_instance.update_repository35(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository35: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = P2ProxyRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        proxy=ProxyAttributes(
            remote_url="https://remote.repository.com",
            content_max_age=1440,
            metadata_max_age=1440,
        ),
        negative_cache=NegativeCacheAttributes(
            enabled=True,
            time_to_live=1440,
        ),
        http_client=HttpClientAttributes(
            blocked=False,
            auto_block=True,
            connection=HttpClientConnectionAttributes(
                retries=0,
                user_agent_suffix="user_agent_suffix_example",
                timeout=60,
                enable_circular_redirects=False,
                enable_cookies=False,
                use_trust_store=False,
            ),
            authentication=HttpClientConnectionAuthenticationAttributes(
                type="username",
                username="username_example",
                password="password_example",
                ntlm_host="ntlm_host_example",
                ntlm_domain="ntlm_domain_example",
            ),
        ),
        routing_rule="routing_rule_example",
        replication=ReplicationAttributes(
            preemptive_pull_enabled=True,
            asset_path_regex="asset_path_regex_example",
        ),
    )
    try:
        # Update p2 proxy repository
        api_response = api_instance.update_repository35(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository35: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                           | Description | Notes |
| ------------------------------------------------------------------------------ | ----------- | ----- |
| [**P2ProxyRepositoryApiRequest**](../../models/P2ProxyRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository35.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository35.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository35.ApiResponseFor403) | Insufficient permissions                                    |

#### update_repository35.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository35.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository35.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository36**

<a id="update_repository36"></a>

> update_repository36(repository_name)

Update Helm hosted repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.helm_hosted_repository_api_request import HelmHostedRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update Helm hosted repository
        api_response = api_instance.update_repository36(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository36: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = HelmHostedRepositoryApiRequest(
        name="internal",
        online=True,
        storage=HostedStorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
            write_policy="allow_once",
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        component=ComponentAttributes(
            proprietary_components=True,
        ),
    )
    try:
        # Update Helm hosted repository
        api_response = api_instance.update_repository36(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository36: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                 | Description | Notes |
| ------------------------------------------------------------------------------------ | ----------- | ----- |
| [**HelmHostedRepositoryApiRequest**](../../models/HelmHostedRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository36.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository36.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository36.ApiResponseFor403) | Insufficient permissions                                    |

#### update_repository36.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository36.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository36.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository37**

<a id="update_repository37"></a>

> update_repository37(repository_name)

Update Helm proxy repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.helm_proxy_repository_api_request import HelmProxyRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update Helm proxy repository
        api_response = api_instance.update_repository37(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository37: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = HelmProxyRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        proxy=ProxyAttributes(
            remote_url="https://remote.repository.com",
            content_max_age=1440,
            metadata_max_age=1440,
        ),
        negative_cache=NegativeCacheAttributes(
            enabled=True,
            time_to_live=1440,
        ),
        http_client=HttpClientAttributes(
            blocked=False,
            auto_block=True,
            connection=HttpClientConnectionAttributes(
                retries=0,
                user_agent_suffix="user_agent_suffix_example",
                timeout=60,
                enable_circular_redirects=False,
                enable_cookies=False,
                use_trust_store=False,
            ),
            authentication=HttpClientConnectionAuthenticationAttributes(
                type="username",
                username="username_example",
                password="password_example",
                ntlm_host="ntlm_host_example",
                ntlm_domain="ntlm_domain_example",
            ),
        ),
        routing_rule="routing_rule_example",
        replication=ReplicationAttributes(
            preemptive_pull_enabled=True,
            asset_path_regex="asset_path_regex_example",
        ),
    )
    try:
        # Update Helm proxy repository
        api_response = api_instance.update_repository37(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository37: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                               | Description | Notes |
| ---------------------------------------------------------------------------------- | ----------- | ----- |
| [**HelmProxyRepositoryApiRequest**](../../models/HelmProxyRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository37.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository37.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository37.ApiResponseFor403) | Insufficient permissions                                    |

#### update_repository37.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository37.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository37.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository38**

<a id="update_repository38"></a>

> update_repository38(repository_name)

Update Bower group repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.bower_group_repository_api_request import BowerGroupRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update Bower group repository
        api_response = api_instance.update_repository38(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository38: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = BowerGroupRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        group=GroupAttributes(
            member_names=[
                "member_names_example"
            ],
        ),
    )
    try:
        # Update Bower group repository
        api_response = api_instance.update_repository38(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository38: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                 | Description | Notes |
| ------------------------------------------------------------------------------------ | ----------- | ----- |
| [**BowerGroupRepositoryApiRequest**](../../models/BowerGroupRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository38.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository38.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository38.ApiResponseFor403) | Insufficient permissions                                    |

#### update_repository38.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository38.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository38.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository39**

<a id="update_repository39"></a>

> update_repository39(repository_name)

Update Bower hosted repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.bower_hosted_repository_api_request import BowerHostedRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update Bower hosted repository
        api_response = api_instance.update_repository39(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository39: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = BowerHostedRepositoryApiRequest(
        name="internal",
        online=True,
        storage=HostedStorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
            write_policy="allow_once",
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        component=ComponentAttributes(
            proprietary_components=True,
        ),
    )
    try:
        # Update Bower hosted repository
        api_response = api_instance.update_repository39(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository39: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                   | Description | Notes |
| -------------------------------------------------------------------------------------- | ----------- | ----- |
| [**BowerHostedRepositoryApiRequest**](../../models/BowerHostedRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository39.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository39.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository39.ApiResponseFor403) | Insufficient permissions                                    |

#### update_repository39.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository39.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository39.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository4**

<a id="update_repository4"></a>

> update_repository4(repository_name)

Update APT proxy repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.apt_proxy_repository_api_request import AptProxyRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update APT proxy repository
        api_response = api_instance.update_repository4(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository4: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = AptProxyRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        proxy=ProxyAttributes(
            remote_url="https://remote.repository.com",
            content_max_age=1440,
            metadata_max_age=1440,
        ),
        negative_cache=NegativeCacheAttributes(
            enabled=True,
            time_to_live=1440,
        ),
        http_client=HttpClientAttributes(
            blocked=False,
            auto_block=True,
            connection=HttpClientConnectionAttributes(
                retries=0,
                user_agent_suffix="user_agent_suffix_example",
                timeout=60,
                enable_circular_redirects=False,
                enable_cookies=False,
                use_trust_store=False,
            ),
            authentication=HttpClientConnectionAuthenticationAttributes(
                type="username",
                username="username_example",
                password="password_example",
                ntlm_host="ntlm_host_example",
                ntlm_domain="ntlm_domain_example",
            ),
        ),
        routing_rule="routing_rule_example",
        replication=ReplicationAttributes(
            preemptive_pull_enabled=True,
            asset_path_regex="asset_path_regex_example",
        ),
        apt=AptProxyRepositoriesAttributes(
            distribution="bionic",
            flat=False,
        ),
    )
    try:
        # Update APT proxy repository
        api_response = api_instance.update_repository4(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository4: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                             | Description | Notes |
| -------------------------------------------------------------------------------- | ----------- | ----- |
| [**AptProxyRepositoryApiRequest**](../../models/AptProxyRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                      | Description                                                 |
| ---- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization               | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository4.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository4.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository4.ApiResponseFor403) | Insufficient permissions                                    |
| 404  | [ApiResponseFor404](#update_repository4.ApiResponseFor404) | Repository not found                                        |

#### update_repository4.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository4.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository4.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository4.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository40**

<a id="update_repository40"></a>

> update_repository40(repository_name)

Update Bower proxy repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.bower_proxy_repository_api_request import BowerProxyRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update Bower proxy repository
        api_response = api_instance.update_repository40(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository40: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = BowerProxyRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        proxy=ProxyAttributes(
            remote_url="https://remote.repository.com",
            content_max_age=1440,
            metadata_max_age=1440,
        ),
        negative_cache=NegativeCacheAttributes(
            enabled=True,
            time_to_live=1440,
        ),
        http_client=HttpClientAttributes(
            blocked=False,
            auto_block=True,
            connection=HttpClientConnectionAttributes(
                retries=0,
                user_agent_suffix="user_agent_suffix_example",
                timeout=60,
                enable_circular_redirects=False,
                enable_cookies=False,
                use_trust_store=False,
            ),
            authentication=HttpClientConnectionAuthenticationAttributes(
                type="username",
                username="username_example",
                password="password_example",
                ntlm_host="ntlm_host_example",
                ntlm_domain="ntlm_domain_example",
            ),
        ),
        routing_rule="routing_rule_example",
        replication=ReplicationAttributes(
            preemptive_pull_enabled=True,
            asset_path_regex="asset_path_regex_example",
        ),
        bower=BowerAttributes(
            rewrite_package_urls=True,
        ),
    )
    try:
        # Update Bower proxy repository
        api_response = api_instance.update_repository40(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository40: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                 | Description | Notes |
| ------------------------------------------------------------------------------------ | ----------- | ----- |
| [**BowerProxyRepositoryApiRequest**](../../models/BowerProxyRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository40.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository40.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository40.ApiResponseFor403) | Insufficient permissions                                    |

#### update_repository40.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository40.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository40.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository5**

<a id="update_repository5"></a>

> update_repository5(repository_name)

Update raw group repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.raw_group_repository_api_request import RawGroupRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update raw group repository
        api_response = api_instance.update_repository5(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository5: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = RawGroupRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        group=GroupAttributes(
            member_names=[
                "member_names_example"
            ],
        ),
        raw=RawAttributes(
            content_disposition="ATTACHMENT",
        ),
    )
    try:
        # Update raw group repository
        api_response = api_instance.update_repository5(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository5: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                             | Description | Notes |
| -------------------------------------------------------------------------------- | ----------- | ----- |
| [**RawGroupRepositoryApiRequest**](../../models/RawGroupRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                      | Description                                                 |
| ---- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization               | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository5.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository5.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository5.ApiResponseFor403) | Insufficient permissions                                    |

#### update_repository5.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository5.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository5.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository6**

<a id="update_repository6"></a>

> update_repository6(repository_name)

Update raw hosted repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.raw_hosted_repository_api_request import RawHostedRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update raw hosted repository
        api_response = api_instance.update_repository6(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository6: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = RawHostedRepositoryApiRequest(
        name="internal",
        online=True,
        storage=HostedStorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
            write_policy="allow_once",
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        component=ComponentAttributes(
            proprietary_components=True,
        ),
        raw=RawAttributes(
            content_disposition="ATTACHMENT",
        ),
    )
    try:
        # Update raw hosted repository
        api_response = api_instance.update_repository6(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository6: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                               | Description | Notes |
| ---------------------------------------------------------------------------------- | ----------- | ----- |
| [**RawHostedRepositoryApiRequest**](../../models/RawHostedRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                      | Description                                                 |
| ---- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization               | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository6.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository6.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository6.ApiResponseFor403) | Insufficient permissions                                    |

#### update_repository6.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository6.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository6.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository7**

<a id="update_repository7"></a>

> update_repository7(repository_name)

Update raw proxy repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.raw_proxy_repository_api_request import RawProxyRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update raw proxy repository
        api_response = api_instance.update_repository7(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository7: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = RawProxyRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        proxy=ProxyAttributes(
            remote_url="https://remote.repository.com",
            content_max_age=1440,
            metadata_max_age=1440,
        ),
        negative_cache=NegativeCacheAttributes(
            enabled=True,
            time_to_live=1440,
        ),
        http_client=HttpClientAttributes(
            blocked=False,
            auto_block=True,
            connection=HttpClientConnectionAttributes(
                retries=0,
                user_agent_suffix="user_agent_suffix_example",
                timeout=60,
                enable_circular_redirects=False,
                enable_cookies=False,
                use_trust_store=False,
            ),
            authentication=HttpClientConnectionAuthenticationAttributes(
                type="username",
                username="username_example",
                password="password_example",
                ntlm_host="ntlm_host_example",
                ntlm_domain="ntlm_domain_example",
            ),
        ),
        routing_rule="routing_rule_example",
        replication=ReplicationAttributes(
            preemptive_pull_enabled=True,
            asset_path_regex="asset_path_regex_example",
        ),
        raw=RawAttributes(
            content_disposition="ATTACHMENT",
        ),
    )
    try:
        # Update raw proxy repository
        api_response = api_instance.update_repository7(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository7: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                             | Description | Notes |
| -------------------------------------------------------------------------------- | ----------- | ----- |
| [**RawProxyRepositoryApiRequest**](../../models/RawProxyRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                      | Description                                                 |
| ---- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization               | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository7.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository7.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository7.ApiResponseFor403) | Insufficient permissions                                    |

#### update_repository7.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository7.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository7.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository8**

<a id="update_repository8"></a>

> update_repository8(repository_name)

Update npm group repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.npm_group_repository_api_request import NpmGroupRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update npm group repository
        api_response = api_instance.update_repository8(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository8: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = NpmGroupRepositoryApiRequest(
        name="internal",
        online=True,
        storage=StorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
        ),
        group=GroupDeployAttributes(
            member_names=[
                "member_names_example"
            ],
            writable_member="writable_member_example",
        ),
    )
    try:
        # Update npm group repository
        api_response = api_instance.update_repository8(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository8: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                             | Description | Notes |
| -------------------------------------------------------------------------------- | ----------- | ----- |
| [**NpmGroupRepositoryApiRequest**](../../models/NpmGroupRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                      | Description                                                 |
| ---- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization               | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository8.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository8.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository8.ApiResponseFor403) | Insufficient permissions                                    |

#### update_repository8.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository8.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository8.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_repository9**

<a id="update_repository9"></a>

> update_repository9(repository_name)

Update npm hosted repository

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import repository_management_api
from nexus_sdk.model.npm_hosted_repository_api_request import NpmHostedRepositoryApiRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_management_api.RepositoryManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    try:
        # Update npm hosted repository
        api_response = api_instance.update_repository9(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository9: %s\n" % e)

    # example passing only optional values
    path_params = {
        'repositoryName': "repositoryName_example",
    }
    body = NpmHostedRepositoryApiRequest(
        name="internal",
        online=True,
        storage=HostedStorageAttributes(
            blob_store_name="default",
            strict_content_type_validation=True,
            write_policy="allow_once",
        ),
        cleanup=CleanupPolicyAttributes(
            policy_names=[
                "policy_names_example"
            ],
        ),
        component=ComponentAttributes(
            proprietary_components=True,
        ),
    )
    try:
        # Update npm hosted repository
        api_response = api_instance.update_repository9(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository9: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                               | Description | Notes |
| ---------------------------------------------------------------------------------- | ----------- | ----- |
| [**NpmHostedRepositoryApiRequest**](../../models/NpmHostedRepositoryApiRequest.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| repositoryName | RepositoryNameSchema |             |

# RepositoryNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                      | Description                                                 |
| ---- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization               | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_repository9.ApiResponseFor204) | Repository updated                                          |
| 401  | [ApiResponseFor401](#update_repository9.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_repository9.ApiResponseFor403) | Insufficient permissions                                    |

#### update_repository9.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository9.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_repository9.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
