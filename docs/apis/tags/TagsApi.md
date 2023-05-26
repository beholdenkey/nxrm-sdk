<a id="__pageTop"></a>
# nexus_sdk.apis.tags.tags_api.TagsApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associate**](#associate) | **post** /v1/tags/associate/{tagName} | Associate components with a tag
[**create1**](#create1) | **post** /v1/tags | Create a tag
[**delete2**](#delete2) | **delete** /v1/tags/{name} | Delete a tag
[**disassociate**](#disassociate) | **delete** /v1/tags/associate/{tagName} | Disassociate components from a tag
[**get3**](#get3) | **get** /v1/tags/{name} | Get a tag
[**get_tags**](#get_tags) | **get** /v1/tags | List tags
[**replace**](#replace) | **put** /v1/tags/{name} | Update a tags attributes

# **associate**
<a id="associate"></a>
> associate(tag_name)

Associate components with a tag

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import tags_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tags_api.TagsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'tagName': "tagName_example",
    }
    query_params = {
    }
    try:
        # Associate components with a tag
        api_response = api_instance.associate(
            path_params=path_params,
            query_params=query_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling TagsApi->associate: %s\n" % e)

    # example passing only optional values
    path_params = {
        'tagName': "tagName_example",
    }
    query_params = {
        'wait': True,
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
        # Associate components with a tag
        api_response = api_instance.associate(
            path_params=path_params,
            query_params=query_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling TagsApi->associate: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
wait | WaitSchema | | optional
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


# WaitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of True

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

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
tagName | TagNameSchema | | 

# TagNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#associate.ApiResponseFor200) | Associate was successful
404 | [ApiResponseFor404](#associate.ApiResponseFor404) | Tag or components not found

#### associate.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### associate.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create1**
<a id="create1"></a>
> create1()

Create a tag

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import tags_api
from nexus_sdk.model.tag_xo import TagXO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tags_api.TagsApi(api_client)

    # example passing only optional values
    body = TagXO(
        name="e6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        attributes=dict(
            "key": dict(),
        ),
        first_created="1970-01-01T00:00:00.00Z",
        last_updated="1970-01-01T00:00:00.00Z",
    )
    try:
        # Create a tag
        api_response = api_instance.create1(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling TagsApi->create1: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TagXO**](../../models/TagXO.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create1.ApiResponseFor200) | Tag was added
400 | [ApiResponseFor400](#create1.ApiResponseFor400) | Bad request. Check tag name and attributes. Name can only contain letters, numbers, underscores, hyphens and dots and cannot start with an underscore or dot. The name cannot exceed 256 characters. The attributes is a JSON document which cannot exceed 20k.

#### create1.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create1.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete2**
<a id="delete2"></a>
> delete2(name)

Delete a tag

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import tags_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tags_api.TagsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    try:
        # Delete a tag
        api_response = api_instance.delete2(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling TagsApi->delete2: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete2.ApiResponseFor204) | Tag was deleted
404 | [ApiResponseFor404](#delete2.ApiResponseFor404) | Tag not found

#### delete2.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete2.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **disassociate**
<a id="disassociate"></a>
> disassociate(tag_name)

Disassociate components from a tag

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import tags_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tags_api.TagsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'tagName': "tagName_example",
    }
    query_params = {
    }
    try:
        # Disassociate components from a tag
        api_response = api_instance.disassociate(
            path_params=path_params,
            query_params=query_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling TagsApi->disassociate: %s\n" % e)

    # example passing only optional values
    path_params = {
        'tagName': "tagName_example",
    }
    query_params = {
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
        # Disassociate components from a tag
        api_response = api_instance.disassociate(
            path_params=path_params,
            query_params=query_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling TagsApi->disassociate: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
tagName | TagNameSchema | | 

# TagNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#disassociate.ApiResponseFor200) | Disassociation was successful
404 | [ApiResponseFor404](#disassociate.ApiResponseFor404) | Tag or components not found

#### disassociate.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### disassociate.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get3**
<a id="get3"></a>
> TagXO get3(name)

Get a tag

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import tags_api
from nexus_sdk.model.tag_xo import TagXO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tags_api.TagsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    try:
        # Get a tag
        api_response = api_instance.get3(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling TagsApi->get3: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get3.ApiResponseFor200) | successful operation
404 | [ApiResponseFor404](#get3.ApiResponseFor404) | Tag not found

#### get3.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TagXO**](../../models/TagXO.md) |  | 


#### get3.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_tags**
<a id="get_tags"></a>
> PageTagXO get_tags()

List tags

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import tags_api
from nexus_sdk.model.page_tag_xo import PageTagXO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tags_api.TagsApi(api_client)

    # example passing only optional values
    query_params = {
        'continuationToken': "continuationToken_example",
    }
    try:
        # List tags
        api_response = api_instance.get_tags(
            query_params=query_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling TagsApi->get_tags: %s\n" % e)
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


# ContinuationTokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_tags.ApiResponseFor200) | successful operation

#### get_tags.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PageTagXO**](../../models/PageTagXO.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **replace**
<a id="replace"></a>
> TagXO replace(name)

Update a tags attributes

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import tags_api
from nexus_sdk.model.base_tag_xo import BaseTagXO
from nexus_sdk.model.tag_xo import TagXO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tags_api.TagsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    try:
        # Update a tags attributes
        api_response = api_instance.replace(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling TagsApi->replace: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
    }
    body = BaseTagXO(
        attributes=dict(
            "key": dict(),
        ),
    )
    try:
        # Update a tags attributes
        api_response = api_instance.replace(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling TagsApi->replace: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BaseTagXO**](../../models/BaseTagXO.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#replace.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#replace.ApiResponseFor400) | Bad request. Check tag attributes. The attributes is a JSON document which cannot exceed 20k
404 | [ApiResponseFor404](#replace.ApiResponseFor404) | Tag not found

#### replace.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TagXO**](../../models/TagXO.md) |  | 


#### replace.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### replace.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

