# swagger_client.StagingApi

All URIs are relative to */service/rest/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete4**](StagingApi.md#delete4) | **POST** /v1/staging/delete | Delete components
[**move**](StagingApi.md#move) | **POST** /v1/staging/move/{destination} | Move components

# **delete4**
> delete4(q=q, repository=repository, format=format, group=group, name=name, version=version, prerelease=prerelease, md5=md5, sha1=sha1, sha256=sha256, sha512=sha512, conan_base_version=conan_base_version, conan_channel=conan_channel, docker_image_name=docker_image_name, docker_image_tag=docker_image_tag, docker_layer_id=docker_layer_id, docker_content_digest=docker_content_digest, maven_group_id=maven_group_id, maven_artifact_id=maven_artifact_id, maven_base_version=maven_base_version, maven_extension=maven_extension, maven_classifier=maven_classifier, npm_scope=npm_scope, nuget_id=nuget_id, nuget_tags=nuget_tags, p2_plugin_name=p2_plugin_name, pypi_classifiers=pypi_classifiers, pypi_description=pypi_description, pypi_keywords=pypi_keywords, pypi_summary=pypi_summary, rubygems_description=rubygems_description, rubygems_platform=rubygems_platform, rubygems_summary=rubygems_summary, tag=tag, yum_architecture=yum_architecture)

Delete components

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StagingApi()
q = 'q_example' # str | Query by keyword (optional)
repository = 'repository_example' # str | Repository name (optional)
format = 'format_example' # str | Query by format (optional)
group = 'group_example' # str | Component group (optional)
name = 'name_example' # str | Component name (optional)
version = 'version_example' # str | Component version (optional)
prerelease = 'prerelease_example' # str | Prerelease version flag (optional)
md5 = 'md5_example' # str | Specific MD5 hash of component's asset (optional)
sha1 = 'sha1_example' # str | Specific SHA-1 hash of component's asset (optional)
sha256 = 'sha256_example' # str | Specific SHA-256 hash of component's asset (optional)
sha512 = 'sha512_example' # str | Specific SHA-512 hash of component's asset (optional)
conan_base_version = 'conan_base_version_example' # str | Conan base version (optional)
conan_channel = 'conan_channel_example' # str | Conan channel (optional)
docker_image_name = 'docker_image_name_example' # str | Docker image name (optional)
docker_image_tag = 'docker_image_tag_example' # str | Docker image tag (optional)
docker_layer_id = 'docker_layer_id_example' # str | Docker layer ID (optional)
docker_content_digest = 'docker_content_digest_example' # str | Docker content digest (optional)
maven_group_id = 'maven_group_id_example' # str | Maven groupId (optional)
maven_artifact_id = 'maven_artifact_id_example' # str | Maven artifactId (optional)
maven_base_version = 'maven_base_version_example' # str | Maven base version (optional)
maven_extension = 'maven_extension_example' # str | Maven extension of component's asset (optional)
maven_classifier = 'maven_classifier_example' # str | Maven classifier of component's asset (optional)
npm_scope = 'npm_scope_example' # str | npm scope (optional)
nuget_id = 'nuget_id_example' # str | NuGet id (optional)
nuget_tags = 'nuget_tags_example' # str | NuGet tags (optional)
p2_plugin_name = 'p2_plugin_name_example' # str | p2 plugin name (optional)
pypi_classifiers = 'pypi_classifiers_example' # str | PyPI classifiers (optional)
pypi_description = 'pypi_description_example' # str | PyPI description (optional)
pypi_keywords = 'pypi_keywords_example' # str | PyPI keywords (optional)
pypi_summary = 'pypi_summary_example' # str | PyPI summary (optional)
rubygems_description = 'rubygems_description_example' # str | RubyGems description (optional)
rubygems_platform = 'rubygems_platform_example' # str | RubyGems platform (optional)
rubygems_summary = 'rubygems_summary_example' # str | RubyGems summary (optional)
tag = 'tag_example' # str | Component tag (optional)
yum_architecture = 'yum_architecture_example' # str | Yum architecture (optional)

try:
    # Delete components
    api_instance.delete4(q=q, repository=repository, format=format, group=group, name=name, version=version, prerelease=prerelease, md5=md5, sha1=sha1, sha256=sha256, sha512=sha512, conan_base_version=conan_base_version, conan_channel=conan_channel, docker_image_name=docker_image_name, docker_image_tag=docker_image_tag, docker_layer_id=docker_layer_id, docker_content_digest=docker_content_digest, maven_group_id=maven_group_id, maven_artifact_id=maven_artifact_id, maven_base_version=maven_base_version, maven_extension=maven_extension, maven_classifier=maven_classifier, npm_scope=npm_scope, nuget_id=nuget_id, nuget_tags=nuget_tags, p2_plugin_name=p2_plugin_name, pypi_classifiers=pypi_classifiers, pypi_description=pypi_description, pypi_keywords=pypi_keywords, pypi_summary=pypi_summary, rubygems_description=rubygems_description, rubygems_platform=rubygems_platform, rubygems_summary=rubygems_summary, tag=tag, yum_architecture=yum_architecture)
except ApiException as e:
    print("Exception when calling StagingApi->delete4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Query by keyword | [optional] 
 **repository** | **str**| Repository name | [optional] 
 **format** | **str**| Query by format | [optional] 
 **group** | **str**| Component group | [optional] 
 **name** | **str**| Component name | [optional] 
 **version** | **str**| Component version | [optional] 
 **prerelease** | **str**| Prerelease version flag | [optional] 
 **md5** | **str**| Specific MD5 hash of component&#x27;s asset | [optional] 
 **sha1** | **str**| Specific SHA-1 hash of component&#x27;s asset | [optional] 
 **sha256** | **str**| Specific SHA-256 hash of component&#x27;s asset | [optional] 
 **sha512** | **str**| Specific SHA-512 hash of component&#x27;s asset | [optional] 
 **conan_base_version** | **str**| Conan base version | [optional] 
 **conan_channel** | **str**| Conan channel | [optional] 
 **docker_image_name** | **str**| Docker image name | [optional] 
 **docker_image_tag** | **str**| Docker image tag | [optional] 
 **docker_layer_id** | **str**| Docker layer ID | [optional] 
 **docker_content_digest** | **str**| Docker content digest | [optional] 
 **maven_group_id** | **str**| Maven groupId | [optional] 
 **maven_artifact_id** | **str**| Maven artifactId | [optional] 
 **maven_base_version** | **str**| Maven base version | [optional] 
 **maven_extension** | **str**| Maven extension of component&#x27;s asset | [optional] 
 **maven_classifier** | **str**| Maven classifier of component&#x27;s asset | [optional] 
 **npm_scope** | **str**| npm scope | [optional] 
 **nuget_id** | **str**| NuGet id | [optional] 
 **nuget_tags** | **str**| NuGet tags | [optional] 
 **p2_plugin_name** | **str**| p2 plugin name | [optional] 
 **pypi_classifiers** | **str**| PyPI classifiers | [optional] 
 **pypi_description** | **str**| PyPI description | [optional] 
 **pypi_keywords** | **str**| PyPI keywords | [optional] 
 **pypi_summary** | **str**| PyPI summary | [optional] 
 **rubygems_description** | **str**| RubyGems description | [optional] 
 **rubygems_platform** | **str**| RubyGems platform | [optional] 
 **rubygems_summary** | **str**| RubyGems summary | [optional] 
 **tag** | **str**| Component tag | [optional] 
 **yum_architecture** | **str**| Yum architecture | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move**
> move(destination, q=q, repository=repository, format=format, group=group, name=name, version=version, prerelease=prerelease, md5=md5, sha1=sha1, sha256=sha256, sha512=sha512, conan_base_version=conan_base_version, conan_channel=conan_channel, docker_image_name=docker_image_name, docker_image_tag=docker_image_tag, docker_layer_id=docker_layer_id, docker_content_digest=docker_content_digest, maven_group_id=maven_group_id, maven_artifact_id=maven_artifact_id, maven_base_version=maven_base_version, maven_extension=maven_extension, maven_classifier=maven_classifier, npm_scope=npm_scope, nuget_id=nuget_id, nuget_tags=nuget_tags, p2_plugin_name=p2_plugin_name, pypi_classifiers=pypi_classifiers, pypi_description=pypi_description, pypi_keywords=pypi_keywords, pypi_summary=pypi_summary, rubygems_description=rubygems_description, rubygems_platform=rubygems_platform, rubygems_summary=rubygems_summary, tag=tag, yum_architecture=yum_architecture)

Move components

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StagingApi()
destination = 'destination_example' # str | 
q = 'q_example' # str | Query by keyword (optional)
repository = 'repository_example' # str | Repository name (optional)
format = 'format_example' # str | Query by format (optional)
group = 'group_example' # str | Component group (optional)
name = 'name_example' # str | Component name (optional)
version = 'version_example' # str | Component version (optional)
prerelease = 'prerelease_example' # str | Prerelease version flag (optional)
md5 = 'md5_example' # str | Specific MD5 hash of component's asset (optional)
sha1 = 'sha1_example' # str | Specific SHA-1 hash of component's asset (optional)
sha256 = 'sha256_example' # str | Specific SHA-256 hash of component's asset (optional)
sha512 = 'sha512_example' # str | Specific SHA-512 hash of component's asset (optional)
conan_base_version = 'conan_base_version_example' # str | Conan base version (optional)
conan_channel = 'conan_channel_example' # str | Conan channel (optional)
docker_image_name = 'docker_image_name_example' # str | Docker image name (optional)
docker_image_tag = 'docker_image_tag_example' # str | Docker image tag (optional)
docker_layer_id = 'docker_layer_id_example' # str | Docker layer ID (optional)
docker_content_digest = 'docker_content_digest_example' # str | Docker content digest (optional)
maven_group_id = 'maven_group_id_example' # str | Maven groupId (optional)
maven_artifact_id = 'maven_artifact_id_example' # str | Maven artifactId (optional)
maven_base_version = 'maven_base_version_example' # str | Maven base version (optional)
maven_extension = 'maven_extension_example' # str | Maven extension of component's asset (optional)
maven_classifier = 'maven_classifier_example' # str | Maven classifier of component's asset (optional)
npm_scope = 'npm_scope_example' # str | npm scope (optional)
nuget_id = 'nuget_id_example' # str | NuGet id (optional)
nuget_tags = 'nuget_tags_example' # str | NuGet tags (optional)
p2_plugin_name = 'p2_plugin_name_example' # str | p2 plugin name (optional)
pypi_classifiers = 'pypi_classifiers_example' # str | PyPI classifiers (optional)
pypi_description = 'pypi_description_example' # str | PyPI description (optional)
pypi_keywords = 'pypi_keywords_example' # str | PyPI keywords (optional)
pypi_summary = 'pypi_summary_example' # str | PyPI summary (optional)
rubygems_description = 'rubygems_description_example' # str | RubyGems description (optional)
rubygems_platform = 'rubygems_platform_example' # str | RubyGems platform (optional)
rubygems_summary = 'rubygems_summary_example' # str | RubyGems summary (optional)
tag = 'tag_example' # str | Component tag (optional)
yum_architecture = 'yum_architecture_example' # str | Yum architecture (optional)

try:
    # Move components
    api_instance.move(destination, q=q, repository=repository, format=format, group=group, name=name, version=version, prerelease=prerelease, md5=md5, sha1=sha1, sha256=sha256, sha512=sha512, conan_base_version=conan_base_version, conan_channel=conan_channel, docker_image_name=docker_image_name, docker_image_tag=docker_image_tag, docker_layer_id=docker_layer_id, docker_content_digest=docker_content_digest, maven_group_id=maven_group_id, maven_artifact_id=maven_artifact_id, maven_base_version=maven_base_version, maven_extension=maven_extension, maven_classifier=maven_classifier, npm_scope=npm_scope, nuget_id=nuget_id, nuget_tags=nuget_tags, p2_plugin_name=p2_plugin_name, pypi_classifiers=pypi_classifiers, pypi_description=pypi_description, pypi_keywords=pypi_keywords, pypi_summary=pypi_summary, rubygems_description=rubygems_description, rubygems_platform=rubygems_platform, rubygems_summary=rubygems_summary, tag=tag, yum_architecture=yum_architecture)
except ApiException as e:
    print("Exception when calling StagingApi->move: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination** | **str**|  | 
 **q** | **str**| Query by keyword | [optional] 
 **repository** | **str**| Repository name | [optional] 
 **format** | **str**| Query by format | [optional] 
 **group** | **str**| Component group | [optional] 
 **name** | **str**| Component name | [optional] 
 **version** | **str**| Component version | [optional] 
 **prerelease** | **str**| Prerelease version flag | [optional] 
 **md5** | **str**| Specific MD5 hash of component&#x27;s asset | [optional] 
 **sha1** | **str**| Specific SHA-1 hash of component&#x27;s asset | [optional] 
 **sha256** | **str**| Specific SHA-256 hash of component&#x27;s asset | [optional] 
 **sha512** | **str**| Specific SHA-512 hash of component&#x27;s asset | [optional] 
 **conan_base_version** | **str**| Conan base version | [optional] 
 **conan_channel** | **str**| Conan channel | [optional] 
 **docker_image_name** | **str**| Docker image name | [optional] 
 **docker_image_tag** | **str**| Docker image tag | [optional] 
 **docker_layer_id** | **str**| Docker layer ID | [optional] 
 **docker_content_digest** | **str**| Docker content digest | [optional] 
 **maven_group_id** | **str**| Maven groupId | [optional] 
 **maven_artifact_id** | **str**| Maven artifactId | [optional] 
 **maven_base_version** | **str**| Maven base version | [optional] 
 **maven_extension** | **str**| Maven extension of component&#x27;s asset | [optional] 
 **maven_classifier** | **str**| Maven classifier of component&#x27;s asset | [optional] 
 **npm_scope** | **str**| npm scope | [optional] 
 **nuget_id** | **str**| NuGet id | [optional] 
 **nuget_tags** | **str**| NuGet tags | [optional] 
 **p2_plugin_name** | **str**| p2 plugin name | [optional] 
 **pypi_classifiers** | **str**| PyPI classifiers | [optional] 
 **pypi_description** | **str**| PyPI description | [optional] 
 **pypi_keywords** | **str**| PyPI keywords | [optional] 
 **pypi_summary** | **str**| PyPI summary | [optional] 
 **rubygems_description** | **str**| RubyGems description | [optional] 
 **rubygems_platform** | **str**| RubyGems platform | [optional] 
 **rubygems_summary** | **str**| RubyGems summary | [optional] 
 **tag** | **str**| Component tag | [optional] 
 **yum_architecture** | **str**| Yum architecture | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

