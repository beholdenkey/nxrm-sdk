<a id="__pageTop"></a>

# nexus_sdk.apis.tags.staging_api.StagingApi

All URIs are relative to _http://localhost/service/rest_

| Method                  | HTTP request                            | Description       |
| ----------------------- | --------------------------------------- | ----------------- |
| [**delete4**](#delete4) | **post** /v1/staging/delete             | Delete components |
| [**move**](#move)       | **post** /v1/staging/move/{destination} | Move components   |

# **delete4**

<a id="delete4"></a>

> delete4()

Delete components

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import staging_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = staging_api.StagingApi(api_client)

    # example passing only optional values
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
        # Delete components
        api_response = api_instance.delete4(
            query_params=query_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling StagingApi->delete4: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description      | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| query_params         | RequestQueryParams                               |                  |
| stream               | bool                                             | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None  | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### query_params

#### RequestQueryParams

| Name                 | Type                      | Description | Notes    |
| -------------------- | ------------------------- | ----------- | -------- |
| q                    | QSchema                   |             | optional |
| repository           | RepositorySchema          |             | optional |
| format               | FormatSchema              |             | optional |
| group                | GroupSchema               |             | optional |
| name                 | NameSchema                |             | optional |
| version              | VersionSchema             |             | optional |
| prerelease           | PrereleaseSchema          |             | optional |
| md5                  | Md5Schema                 |             | optional |
| sha1                 | Sha1Schema                |             | optional |
| sha256               | Sha256Schema              |             | optional |
| sha512               | Sha512Schema              |             | optional |
| conan.baseVersion    | ConanBaseVersionSchema    |             | optional |
| conan.channel        | ConanChannelSchema        |             | optional |
| docker.imageName     | DockerImageNameSchema     |             | optional |
| docker.imageTag      | DockerImageTagSchema      |             | optional |
| docker.layerId       | DockerLayerIdSchema       |             | optional |
| docker.contentDigest | DockerContentDigestSchema |             | optional |
| maven.groupId        | MavenGroupIdSchema        |             | optional |
| maven.artifactId     | MavenArtifactIdSchema     |             | optional |
| maven.baseVersion    | MavenBaseVersionSchema    |             | optional |
| maven.extension      | MavenExtensionSchema      |             | optional |
| maven.classifier     | MavenClassifierSchema     |             | optional |
| npm.scope            | NpmScopeSchema            |             | optional |
| nuget.id             | NugetIdSchema             |             | optional |
| nuget.tags           | NugetTagsSchema           |             | optional |
| p2.pluginName        | P2PluginNameSchema        |             | optional |
| pypi.classifiers     | PypiClassifiersSchema     |             | optional |
| pypi.description     | PypiDescriptionSchema     |             | optional |
| pypi.keywords        | PypiKeywordsSchema        |             | optional |
| pypi.summary         | PypiSummarySchema         |             | optional |
| rubygems.description | RubygemsDescriptionSchema |             | optional |
| rubygems.platform    | RubygemsPlatformSchema    |             | optional |
| rubygems.summary     | RubygemsSummarySchema     |             | optional |
| tag                  | TagSchema                 |             | optional |
| yum.architecture     | YumArchitectureSchema     |             | optional |

# QSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# RepositorySchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# FormatSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# GroupSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# NameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# VersionSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# PrereleaseSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# Md5Schema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# Sha1Schema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# Sha256Schema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# Sha512Schema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# ConanBaseVersionSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# ConanChannelSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# DockerImageNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# DockerImageTagSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# DockerLayerIdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# DockerContentDigestSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# MavenGroupIdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# MavenArtifactIdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# MavenBaseVersionSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# MavenExtensionSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# MavenClassifierSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# NpmScopeSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# NugetIdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# NugetTagsSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# P2PluginNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# PypiClassifiersSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# PypiDescriptionSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# PypiKeywordsSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# PypiSummarySchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# RubygemsDescriptionSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# RubygemsPlatformSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# RubygemsSummarySchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# TagSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# YumArchitectureSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                           | Description                                                 |
| ---- | ----------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization    | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#delete4.ApiResponseFor200) | Delete Successful                                           |
| 400  | [ApiResponseFor400](#delete4.ApiResponseFor400) | Invalid client request                                      |
| 401  | [ApiResponseFor401](#delete4.ApiResponseFor401) | Unauthorized                                                |
| 403  | [ApiResponseFor403](#delete4.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#delete4.ApiResponseFor404) | No components found                                         |

#### delete4.ApiResponseFor200

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete4.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete4.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete4.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete4.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **move**

<a id="move"></a>

> move(destination)

Move components

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import staging_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = staging_api.StagingApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'destination': "destination_example",
    }
    query_params = {
    }
    try:
        # Move components
        api_response = api_instance.move(
            path_params=path_params,
            query_params=query_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling StagingApi->move: %s\n" % e)

    # example passing only optional values
    path_params = {
        'destination': "destination_example",
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
        # Move components
        api_response = api_instance.move(
            path_params=path_params,
            query_params=query_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling StagingApi->move: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description      | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| query_params         | RequestQueryParams                               |                  |
| path_params          | RequestPathParams                                |                  |
| stream               | bool                                             | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None  | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### query_params

#### RequestQueryParams

| Name                 | Type                      | Description | Notes    |
| -------------------- | ------------------------- | ----------- | -------- |
| q                    | QSchema                   |             | optional |
| repository           | RepositorySchema          |             | optional |
| format               | FormatSchema              |             | optional |
| group                | GroupSchema               |             | optional |
| name                 | NameSchema                |             | optional |
| version              | VersionSchema             |             | optional |
| prerelease           | PrereleaseSchema          |             | optional |
| md5                  | Md5Schema                 |             | optional |
| sha1                 | Sha1Schema                |             | optional |
| sha256               | Sha256Schema              |             | optional |
| sha512               | Sha512Schema              |             | optional |
| conan.baseVersion    | ConanBaseVersionSchema    |             | optional |
| conan.channel        | ConanChannelSchema        |             | optional |
| docker.imageName     | DockerImageNameSchema     |             | optional |
| docker.imageTag      | DockerImageTagSchema      |             | optional |
| docker.layerId       | DockerLayerIdSchema       |             | optional |
| docker.contentDigest | DockerContentDigestSchema |             | optional |
| maven.groupId        | MavenGroupIdSchema        |             | optional |
| maven.artifactId     | MavenArtifactIdSchema     |             | optional |
| maven.baseVersion    | MavenBaseVersionSchema    |             | optional |
| maven.extension      | MavenExtensionSchema      |             | optional |
| maven.classifier     | MavenClassifierSchema     |             | optional |
| npm.scope            | NpmScopeSchema            |             | optional |
| nuget.id             | NugetIdSchema             |             | optional |
| nuget.tags           | NugetTagsSchema           |             | optional |
| p2.pluginName        | P2PluginNameSchema        |             | optional |
| pypi.classifiers     | PypiClassifiersSchema     |             | optional |
| pypi.description     | PypiDescriptionSchema     |             | optional |
| pypi.keywords        | PypiKeywordsSchema        |             | optional |
| pypi.summary         | PypiSummarySchema         |             | optional |
| rubygems.description | RubygemsDescriptionSchema |             | optional |
| rubygems.platform    | RubygemsPlatformSchema    |             | optional |
| rubygems.summary     | RubygemsSummarySchema     |             | optional |
| tag                  | TagSchema                 |             | optional |
| yum.architecture     | YumArchitectureSchema     |             | optional |

# QSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# RepositorySchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# FormatSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# GroupSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# NameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# VersionSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# PrereleaseSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# Md5Schema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# Sha1Schema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# Sha256Schema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# Sha512Schema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# ConanBaseVersionSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# ConanChannelSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# DockerImageNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# DockerImageTagSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# DockerLayerIdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# DockerContentDigestSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# MavenGroupIdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# MavenArtifactIdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# MavenBaseVersionSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# MavenExtensionSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# MavenClassifierSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# NpmScopeSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# NugetIdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# NugetTagsSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# P2PluginNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# PypiClassifiersSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# PypiDescriptionSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# PypiKeywordsSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# PypiSummarySchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# RubygemsDescriptionSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# RubygemsPlatformSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# RubygemsSummarySchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# TagSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# YumArchitectureSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### path_params

#### RequestPathParams

| Name        | Type              | Description | Notes |
| ----------- | ----------------- | ----------- | ----- |
| destination | DestinationSchema |             |

# DestinationSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                        | Description                                                 |
| ---- | -------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#move.ApiResponseFor200) | Move Successful                                             |
| 400  | [ApiResponseFor400](#move.ApiResponseFor400) | Invalid client request                                      |
| 401  | [ApiResponseFor401](#move.ApiResponseFor401) | Unauthorized                                                |
| 403  | [ApiResponseFor403](#move.ApiResponseFor403) | Authentication required                                     |
| 404  | [ApiResponseFor404](#move.ApiResponseFor404) | No components found                                         |

#### move.ApiResponseFor200

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### move.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### move.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### move.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### move.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
