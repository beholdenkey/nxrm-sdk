<a id="__pageTop"></a>
# nexus_sdk.apis.tags.search_api.SearchApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search**](#search) | **get** /v1/search | Search components
[**search_and_download_assets**](#search_and_download_assets) | **get** /v1/search/assets/download | Search and download asset
[**search_assets**](#search_assets) | **get** /v1/search/assets | Search assets

# **search**
<a id="search"></a>
> PageComponentXO search()

Search components

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import search_api
from nexus_sdk.model.page_component_xo import PageComponentXO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    query_params = {
        'continuationToken': "continuationToken_example",
        'sort': "group",
        'direction': "asc",
        'timeout': 1,
        'q': "q_example",
        'repository': "repository_example",
        'format': "format_example",
        'group': "group_example",
        'name': "name_example",
        'version': "version_example",
        'prerelease': "prerelease_example",
        'md5': "md5_example",
        'sha1': "sha1_example",
        'sha256': "sha256_example",
        'sha512': "sha512_example",
        'conan.baseVersion': "conan.baseVersion_example",
        'conan.channel': "conan.channel_example",
        'docker.imageName': "docker.imageName_example",
        'docker.imageTag': "docker.imageTag_example",
        'docker.layerId': "docker.layerId_example",
        'docker.contentDigest': "docker.contentDigest_example",
        'maven.groupId': "maven.groupId_example",
        'maven.artifactId': "maven.artifactId_example",
        'maven.baseVersion': "maven.baseVersion_example",
        'maven.extension': "maven.extension_example",
        'maven.classifier': "maven.classifier_example",
        'npm.scope': "npm.scope_example",
        'nuget.id': "nuget.id_example",
        'nuget.tags': "nuget.tags_example",
        'p2.pluginName': "p2.pluginName_example",
        'pypi.classifiers': "pypi.classifiers_example",
        'pypi.description': "pypi.description_example",
        'pypi.keywords': "pypi.keywords_example",
        'pypi.summary': "pypi.summary_example",
        'rubygems.description': "rubygems.description_example",
        'rubygems.platform': "rubygems.platform_example",
        'rubygems.summary': "rubygems.summary_example",
        'tag': "tag_example",
        'yum.architecture': "yum.architecture_example",
    }
    try:
        # Search components
        api_response = api_instance.search(
            query_params=query_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling SearchApi->search: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
continuationToken | ContinuationTokenSchema | | optional
sort | SortSchema | | optional
direction | DirectionSchema | | optional
timeout | TimeoutSchema | | optional
q | QSchema | | optional
repository | RepositorySchema | | optional
format | FormatSchema | | optional
group | GroupSchema | | optional
name | NameSchema | | optional
version | VersionSchema | | optional
prerelease | PrereleaseSchema | | optional
md5 | Md5Schema | | optional
sha1 | Sha1Schema | | optional
sha256 | Sha256Schema | | optional
sha512 | Sha512Schema | | optional
conan.baseVersion | ConanBaseVersionSchema | | optional
conan.channel | ConanChannelSchema | | optional
docker.imageName | DockerImageNameSchema | | optional
docker.imageTag | DockerImageTagSchema | | optional
docker.layerId | DockerLayerIdSchema | | optional
docker.contentDigest | DockerContentDigestSchema | | optional
maven.groupId | MavenGroupIdSchema | | optional
maven.artifactId | MavenArtifactIdSchema | | optional
maven.baseVersion | MavenBaseVersionSchema | | optional
maven.extension | MavenExtensionSchema | | optional
maven.classifier | MavenClassifierSchema | | optional
npm.scope | NpmScopeSchema | | optional
nuget.id | NugetIdSchema | | optional
nuget.tags | NugetTagsSchema | | optional
p2.pluginName | P2PluginNameSchema | | optional
pypi.classifiers | PypiClassifiersSchema | | optional
pypi.description | PypiDescriptionSchema | | optional
pypi.keywords | PypiKeywordsSchema | | optional
pypi.summary | PypiSummarySchema | | optional
rubygems.description | RubygemsDescriptionSchema | | optional
rubygems.platform | RubygemsPlatformSchema | | optional
rubygems.summary | RubygemsSummarySchema | | optional
tag | TagSchema | | optional
yum.architecture | YumArchitectureSchema | | optional


# ContinuationTokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["group", "name", "version", "repository", ] 

# DirectionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["asc", "desc", ] 

# TimeoutSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# QSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RepositorySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FormatSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GroupSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PrereleaseSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# Md5Schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# Sha1Schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# Sha256Schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# Sha512Schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ConanBaseVersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ConanChannelSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DockerImageNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DockerImageTagSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DockerLayerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DockerContentDigestSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MavenGroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MavenArtifactIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MavenBaseVersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MavenExtensionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MavenClassifierSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NpmScopeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NugetIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NugetTagsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# P2PluginNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PypiClassifiersSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PypiDescriptionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PypiKeywordsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PypiSummarySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RubygemsDescriptionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RubygemsPlatformSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RubygemsSummarySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TagSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# YumArchitectureSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search.ApiResponseFor200) | successful operation

#### search.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PageComponentXO**](../../models/PageComponentXO.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **search_and_download_assets**
<a id="search_and_download_assets"></a>
> search_and_download_assets()

Search and download asset

Returns a 302 Found with location header field set to download URL. Unless a sort parameter is supplied, the search must return a single asset to receive download URL.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import search_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    query_params = {
        'sort': "group",
        'direction': "asc",
        'timeout': 1,
        'q': "q_example",
        'repository': "repository_example",
        'format': "format_example",
        'group': "group_example",
        'name': "name_example",
        'version': "version_example",
        'prerelease': "prerelease_example",
        'md5': "md5_example",
        'sha1': "sha1_example",
        'sha256': "sha256_example",
        'sha512': "sha512_example",
        'conan.baseVersion': "conan.baseVersion_example",
        'conan.channel': "conan.channel_example",
        'docker.imageName': "docker.imageName_example",
        'docker.imageTag': "docker.imageTag_example",
        'docker.layerId': "docker.layerId_example",
        'docker.contentDigest': "docker.contentDigest_example",
        'maven.groupId': "maven.groupId_example",
        'maven.artifactId': "maven.artifactId_example",
        'maven.baseVersion': "maven.baseVersion_example",
        'maven.extension': "maven.extension_example",
        'maven.classifier': "maven.classifier_example",
        'npm.scope': "npm.scope_example",
        'nuget.id': "nuget.id_example",
        'nuget.tags': "nuget.tags_example",
        'p2.pluginName': "p2.pluginName_example",
        'pypi.classifiers': "pypi.classifiers_example",
        'pypi.description': "pypi.description_example",
        'pypi.keywords': "pypi.keywords_example",
        'pypi.summary': "pypi.summary_example",
        'rubygems.description': "rubygems.description_example",
        'rubygems.platform': "rubygems.platform_example",
        'rubygems.summary': "rubygems.summary_example",
        'tag': "tag_example",
        'yum.architecture': "yum.architecture_example",
    }
    try:
        # Search and download asset
        api_response = api_instance.search_and_download_assets(
            query_params=query_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SearchApi->search_and_download_assets: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
sort | SortSchema | | optional
direction | DirectionSchema | | optional
timeout | TimeoutSchema | | optional
q | QSchema | | optional
repository | RepositorySchema | | optional
format | FormatSchema | | optional
group | GroupSchema | | optional
name | NameSchema | | optional
version | VersionSchema | | optional
prerelease | PrereleaseSchema | | optional
md5 | Md5Schema | | optional
sha1 | Sha1Schema | | optional
sha256 | Sha256Schema | | optional
sha512 | Sha512Schema | | optional
conan.baseVersion | ConanBaseVersionSchema | | optional
conan.channel | ConanChannelSchema | | optional
docker.imageName | DockerImageNameSchema | | optional
docker.imageTag | DockerImageTagSchema | | optional
docker.layerId | DockerLayerIdSchema | | optional
docker.contentDigest | DockerContentDigestSchema | | optional
maven.groupId | MavenGroupIdSchema | | optional
maven.artifactId | MavenArtifactIdSchema | | optional
maven.baseVersion | MavenBaseVersionSchema | | optional
maven.extension | MavenExtensionSchema | | optional
maven.classifier | MavenClassifierSchema | | optional
npm.scope | NpmScopeSchema | | optional
nuget.id | NugetIdSchema | | optional
nuget.tags | NugetTagsSchema | | optional
p2.pluginName | P2PluginNameSchema | | optional
pypi.classifiers | PypiClassifiersSchema | | optional
pypi.description | PypiDescriptionSchema | | optional
pypi.keywords | PypiKeywordsSchema | | optional
pypi.summary | PypiSummarySchema | | optional
rubygems.description | RubygemsDescriptionSchema | | optional
rubygems.platform | RubygemsPlatformSchema | | optional
rubygems.summary | RubygemsSummarySchema | | optional
tag | TagSchema | | optional
yum.architecture | YumArchitectureSchema | | optional


# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["group", "name", "version", "repository", ] 

# DirectionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["asc", "desc", ] 

# TimeoutSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# QSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RepositorySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FormatSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GroupSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PrereleaseSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# Md5Schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# Sha1Schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# Sha256Schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# Sha512Schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ConanBaseVersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ConanChannelSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DockerImageNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DockerImageTagSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DockerLayerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DockerContentDigestSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MavenGroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MavenArtifactIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MavenBaseVersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MavenExtensionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MavenClassifierSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NpmScopeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NugetIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NugetTagsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# P2PluginNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PypiClassifiersSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PypiDescriptionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PypiKeywordsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PypiSummarySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RubygemsDescriptionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RubygemsPlatformSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RubygemsSummarySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TagSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# YumArchitectureSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
400 | [ApiResponseFor400](#search_and_download_assets.ApiResponseFor400) | Search returned multiple assets, please refine search criteria to find a single asset or use the sort query parameter to retrieve the first result.
404 | [ApiResponseFor404](#search_and_download_assets.ApiResponseFor404) | Asset search returned no results

#### search_and_download_assets.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_and_download_assets.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **search_assets**
<a id="search_assets"></a>
> PageAssetXO search_assets()

Search assets

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import search_api
from nexus_sdk.model.page_asset_xo import PageAssetXO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    query_params = {
        'continuationToken': "continuationToken_example",
        'sort': "group",
        'direction': "asc",
        'timeout': 1,
        'q': "q_example",
        'repository': "repository_example",
        'format': "format_example",
        'group': "group_example",
        'name': "name_example",
        'version': "version_example",
        'prerelease': "prerelease_example",
        'md5': "md5_example",
        'sha1': "sha1_example",
        'sha256': "sha256_example",
        'sha512': "sha512_example",
        'conan.baseVersion': "conan.baseVersion_example",
        'conan.channel': "conan.channel_example",
        'docker.imageName': "docker.imageName_example",
        'docker.imageTag': "docker.imageTag_example",
        'docker.layerId': "docker.layerId_example",
        'docker.contentDigest': "docker.contentDigest_example",
        'maven.groupId': "maven.groupId_example",
        'maven.artifactId': "maven.artifactId_example",
        'maven.baseVersion': "maven.baseVersion_example",
        'maven.extension': "maven.extension_example",
        'maven.classifier': "maven.classifier_example",
        'npm.scope': "npm.scope_example",
        'nuget.id': "nuget.id_example",
        'nuget.tags': "nuget.tags_example",
        'p2.pluginName': "p2.pluginName_example",
        'pypi.classifiers': "pypi.classifiers_example",
        'pypi.description': "pypi.description_example",
        'pypi.keywords': "pypi.keywords_example",
        'pypi.summary': "pypi.summary_example",
        'rubygems.description': "rubygems.description_example",
        'rubygems.platform': "rubygems.platform_example",
        'rubygems.summary': "rubygems.summary_example",
        'tag': "tag_example",
        'yum.architecture': "yum.architecture_example",
    }
    try:
        # Search assets
        api_response = api_instance.search_assets(
            query_params=query_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling SearchApi->search_assets: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
continuationToken | ContinuationTokenSchema | | optional
sort | SortSchema | | optional
direction | DirectionSchema | | optional
timeout | TimeoutSchema | | optional
q | QSchema | | optional
repository | RepositorySchema | | optional
format | FormatSchema | | optional
group | GroupSchema | | optional
name | NameSchema | | optional
version | VersionSchema | | optional
prerelease | PrereleaseSchema | | optional
md5 | Md5Schema | | optional
sha1 | Sha1Schema | | optional
sha256 | Sha256Schema | | optional
sha512 | Sha512Schema | | optional
conan.baseVersion | ConanBaseVersionSchema | | optional
conan.channel | ConanChannelSchema | | optional
docker.imageName | DockerImageNameSchema | | optional
docker.imageTag | DockerImageTagSchema | | optional
docker.layerId | DockerLayerIdSchema | | optional
docker.contentDigest | DockerContentDigestSchema | | optional
maven.groupId | MavenGroupIdSchema | | optional
maven.artifactId | MavenArtifactIdSchema | | optional
maven.baseVersion | MavenBaseVersionSchema | | optional
maven.extension | MavenExtensionSchema | | optional
maven.classifier | MavenClassifierSchema | | optional
npm.scope | NpmScopeSchema | | optional
nuget.id | NugetIdSchema | | optional
nuget.tags | NugetTagsSchema | | optional
p2.pluginName | P2PluginNameSchema | | optional
pypi.classifiers | PypiClassifiersSchema | | optional
pypi.description | PypiDescriptionSchema | | optional
pypi.keywords | PypiKeywordsSchema | | optional
pypi.summary | PypiSummarySchema | | optional
rubygems.description | RubygemsDescriptionSchema | | optional
rubygems.platform | RubygemsPlatformSchema | | optional
rubygems.summary | RubygemsSummarySchema | | optional
tag | TagSchema | | optional
yum.architecture | YumArchitectureSchema | | optional


# ContinuationTokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["group", "name", "version", "repository", ] 

# DirectionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["asc", "desc", ] 

# TimeoutSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# QSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RepositorySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FormatSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GroupSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PrereleaseSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# Md5Schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# Sha1Schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# Sha256Schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# Sha512Schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ConanBaseVersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ConanChannelSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DockerImageNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DockerImageTagSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DockerLayerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DockerContentDigestSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MavenGroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MavenArtifactIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MavenBaseVersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MavenExtensionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MavenClassifierSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NpmScopeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NugetIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NugetTagsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# P2PluginNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PypiClassifiersSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PypiDescriptionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PypiKeywordsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PypiSummarySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RubygemsDescriptionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RubygemsPlatformSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RubygemsSummarySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TagSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# YumArchitectureSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search_assets.ApiResponseFor200) | successful operation

#### search_assets.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PageAssetXO**](../../models/PageAssetXO.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

