# swagger_client.TagsApi

All URIs are relative to _/service/rest/_

| Method                                      | HTTP request                            | Description                        |
| ------------------------------------------- | --------------------------------------- | ---------------------------------- |
| [**associate**](TagsApi.md#associate)       | **POST** /v1/tags/associate/{tagName}   | Associate components with a tag    |
| [**create1**](TagsApi.md#create1)           | **POST** /v1/tags                       | Create a tag                       |
| [**delete2**](TagsApi.md#delete2)           | **DELETE** /v1/tags/{name}              | Delete a tag                       |
| [**disassociate**](TagsApi.md#disassociate) | **DELETE** /v1/tags/associate/{tagName} | Disassociate components from a tag |
| [**get3**](TagsApi.md#get3)                 | **GET** /v1/tags/{name}                 | Get a tag                          |
| [**get_tags**](TagsApi.md#get_tags)         | **GET** /v1/tags                        | List tags                          |
| [**replace**](TagsApi.md#replace)           | **PUT** /v1/tags/{name}                 | Update a tags attributes           |

# **associate**

> associate(tag_name, wait=wait, q=q, repository=repository, format=format, group=group, name=name, version=version, prerelease=prerelease, md5=md5, sha1=sha1, sha256=sha256, sha512=sha512, conan_base_version=conan_base_version, conan_channel=conan_channel, docker_image_name=docker_image_name, docker_image_tag=docker_image_tag, docker_layer_id=docker_layer_id, docker_content_digest=docker_content_digest, maven_group_id=maven_group_id, maven_artifact_id=maven_artifact_id, maven_base_version=maven_base_version, maven_extension=maven_extension, maven_classifier=maven_classifier, npm_scope=npm_scope, nuget_id=nuget_id, nuget_tags=nuget_tags, p2_plugin_name=p2_plugin_name, pypi_classifiers=pypi_classifiers, pypi_description=pypi_description, pypi_keywords=pypi_keywords, pypi_summary=pypi_summary, rubygems_description=rubygems_description, rubygems_platform=rubygems_platform, rubygems_summary=rubygems_summary, tag=tag, yum_architecture=yum_architecture)

Associate components with a tag

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TagsApi()
tag_name = 'tag_name_example' # str | Tag to associate to the matched components
wait = true # bool | The query waits until the indexing is complete (optional) (default to true)
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
    # Associate components with a tag
    api_instance.associate(tag_name, wait=wait, q=q, repository=repository, format=format, group=group, name=name, version=version, prerelease=prerelease, md5=md5, sha1=sha1, sha256=sha256, sha512=sha512, conan_base_version=conan_base_version, conan_channel=conan_channel, docker_image_name=docker_image_name, docker_image_tag=docker_image_tag, docker_layer_id=docker_layer_id, docker_content_digest=docker_content_digest, maven_group_id=maven_group_id, maven_artifact_id=maven_artifact_id, maven_base_version=maven_base_version, maven_extension=maven_extension, maven_classifier=maven_classifier, npm_scope=npm_scope, nuget_id=nuget_id, nuget_tags=nuget_tags, p2_plugin_name=p2_plugin_name, pypi_classifiers=pypi_classifiers, pypi_description=pypi_description, pypi_keywords=pypi_keywords, pypi_summary=pypi_summary, rubygems_description=rubygems_description, rubygems_platform=rubygems_platform, rubygems_summary=rubygems_summary, tag=tag, yum_architecture=yum_architecture)
except ApiException as e:
    print("Exception when calling TagsApi->associate: %s\n" % e)
```

### Parameters

| Name                      | Type     | Description                                     | Notes                        |
| ------------------------- | -------- | ----------------------------------------------- | ---------------------------- |
| **tag_name**              | **str**  | Tag to associate to the matched components      |
| **wait**                  | **bool** | The query waits until the indexing is complete  | [optional] [default to true] |
| **q**                     | **str**  | Query by keyword                                | [optional]                   |
| **repository**            | **str**  | Repository name                                 | [optional]                   |
| **format**                | **str**  | Query by format                                 | [optional]                   |
| **group**                 | **str**  | Component group                                 | [optional]                   |
| **name**                  | **str**  | Component name                                  | [optional]                   |
| **version**               | **str**  | Component version                               | [optional]                   |
| **prerelease**            | **str**  | Prerelease version flag                         | [optional]                   |
| **md5**                   | **str**  | Specific MD5 hash of component&#x27;s asset     | [optional]                   |
| **sha1**                  | **str**  | Specific SHA-1 hash of component&#x27;s asset   | [optional]                   |
| **sha256**                | **str**  | Specific SHA-256 hash of component&#x27;s asset | [optional]                   |
| **sha512**                | **str**  | Specific SHA-512 hash of component&#x27;s asset | [optional]                   |
| **conan_base_version**    | **str**  | Conan base version                              | [optional]                   |
| **conan_channel**         | **str**  | Conan channel                                   | [optional]                   |
| **docker_image_name**     | **str**  | Docker image name                               | [optional]                   |
| **docker_image_tag**      | **str**  | Docker image tag                                | [optional]                   |
| **docker_layer_id**       | **str**  | Docker layer ID                                 | [optional]                   |
| **docker_content_digest** | **str**  | Docker content digest                           | [optional]                   |
| **maven_group_id**        | **str**  | Maven groupId                                   | [optional]                   |
| **maven_artifact_id**     | **str**  | Maven artifactId                                | [optional]                   |
| **maven_base_version**    | **str**  | Maven base version                              | [optional]                   |
| **maven_extension**       | **str**  | Maven extension of component&#x27;s asset       | [optional]                   |
| **maven_classifier**      | **str**  | Maven classifier of component&#x27;s asset      | [optional]                   |
| **npm_scope**             | **str**  | npm scope                                       | [optional]                   |
| **nuget_id**              | **str**  | NuGet id                                        | [optional]                   |
| **nuget_tags**            | **str**  | NuGet tags                                      | [optional]                   |
| **p2_plugin_name**        | **str**  | p2 plugin name                                  | [optional]                   |
| **pypi_classifiers**      | **str**  | PyPI classifiers                                | [optional]                   |
| **pypi_description**      | **str**  | PyPI description                                | [optional]                   |
| **pypi_keywords**         | **str**  | PyPI keywords                                   | [optional]                   |
| **pypi_summary**          | **str**  | PyPI summary                                    | [optional]                   |
| **rubygems_description**  | **str**  | RubyGems description                            | [optional]                   |
| **rubygems_platform**     | **str**  | RubyGems platform                               | [optional]                   |
| **rubygems_summary**      | **str**  | RubyGems summary                                | [optional]                   |
| **tag**                   | **str**  | Component tag                                   | [optional]                   |
| **yum_architecture**      | **str**  | Yum architecture                                | [optional]                   |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create1**

> create1(body=body)

Create a tag

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TagsApi()
body = swagger_client.TagXO() # TagXO |  (optional)

try:
    # Create a tag
    api_instance.create1(body=body)
except ApiException as e:
    print("Exception when calling TagsApi->create1: %s\n" % e)
```

### Parameters

| Name     | Type                  | Description | Notes      |
| -------- | --------------------- | ----------- | ---------- |
| **body** | [**TagXO**](TagXO.md) |             | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete2**

> delete2(name)

Delete a tag

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TagsApi()
name = 'name_example' # str | Name of the tag to delete

try:
    # Delete a tag
    api_instance.delete2(name)
except ApiException as e:
    print("Exception when calling TagsApi->delete2: %s\n" % e)
```

### Parameters

| Name     | Type    | Description               | Notes |
| -------- | ------- | ------------------------- | ----- |
| **name** | **str** | Name of the tag to delete |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disassociate**

> disassociate(tag_name, q=q, repository=repository, format=format, group=group, name=name, version=version, prerelease=prerelease, md5=md5, sha1=sha1, sha256=sha256, sha512=sha512, conan_base_version=conan_base_version, conan_channel=conan_channel, docker_image_name=docker_image_name, docker_image_tag=docker_image_tag, docker_layer_id=docker_layer_id, docker_content_digest=docker_content_digest, maven_group_id=maven_group_id, maven_artifact_id=maven_artifact_id, maven_base_version=maven_base_version, maven_extension=maven_extension, maven_classifier=maven_classifier, npm_scope=npm_scope, nuget_id=nuget_id, nuget_tags=nuget_tags, p2_plugin_name=p2_plugin_name, pypi_classifiers=pypi_classifiers, pypi_description=pypi_description, pypi_keywords=pypi_keywords, pypi_summary=pypi_summary, rubygems_description=rubygems_description, rubygems_platform=rubygems_platform, rubygems_summary=rubygems_summary, tag=tag, yum_architecture=yum_architecture)

Disassociate components from a tag

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TagsApi()
tag_name = 'tag_name_example' # str | Tag to associate to the matched components
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
    # Disassociate components from a tag
    api_instance.disassociate(tag_name, q=q, repository=repository, format=format, group=group, name=name, version=version, prerelease=prerelease, md5=md5, sha1=sha1, sha256=sha256, sha512=sha512, conan_base_version=conan_base_version, conan_channel=conan_channel, docker_image_name=docker_image_name, docker_image_tag=docker_image_tag, docker_layer_id=docker_layer_id, docker_content_digest=docker_content_digest, maven_group_id=maven_group_id, maven_artifact_id=maven_artifact_id, maven_base_version=maven_base_version, maven_extension=maven_extension, maven_classifier=maven_classifier, npm_scope=npm_scope, nuget_id=nuget_id, nuget_tags=nuget_tags, p2_plugin_name=p2_plugin_name, pypi_classifiers=pypi_classifiers, pypi_description=pypi_description, pypi_keywords=pypi_keywords, pypi_summary=pypi_summary, rubygems_description=rubygems_description, rubygems_platform=rubygems_platform, rubygems_summary=rubygems_summary, tag=tag, yum_architecture=yum_architecture)
except ApiException as e:
    print("Exception when calling TagsApi->disassociate: %s\n" % e)
```

### Parameters

| Name                      | Type    | Description                                     | Notes      |
| ------------------------- | ------- | ----------------------------------------------- | ---------- |
| **tag_name**              | **str** | Tag to associate to the matched components      |
| **q**                     | **str** | Query by keyword                                | [optional] |
| **repository**            | **str** | Repository name                                 | [optional] |
| **format**                | **str** | Query by format                                 | [optional] |
| **group**                 | **str** | Component group                                 | [optional] |
| **name**                  | **str** | Component name                                  | [optional] |
| **version**               | **str** | Component version                               | [optional] |
| **prerelease**            | **str** | Prerelease version flag                         | [optional] |
| **md5**                   | **str** | Specific MD5 hash of component&#x27;s asset     | [optional] |
| **sha1**                  | **str** | Specific SHA-1 hash of component&#x27;s asset   | [optional] |
| **sha256**                | **str** | Specific SHA-256 hash of component&#x27;s asset | [optional] |
| **sha512**                | **str** | Specific SHA-512 hash of component&#x27;s asset | [optional] |
| **conan_base_version**    | **str** | Conan base version                              | [optional] |
| **conan_channel**         | **str** | Conan channel                                   | [optional] |
| **docker_image_name**     | **str** | Docker image name                               | [optional] |
| **docker_image_tag**      | **str** | Docker image tag                                | [optional] |
| **docker_layer_id**       | **str** | Docker layer ID                                 | [optional] |
| **docker_content_digest** | **str** | Docker content digest                           | [optional] |
| **maven_group_id**        | **str** | Maven groupId                                   | [optional] |
| **maven_artifact_id**     | **str** | Maven artifactId                                | [optional] |
| **maven_base_version**    | **str** | Maven base version                              | [optional] |
| **maven_extension**       | **str** | Maven extension of component&#x27;s asset       | [optional] |
| **maven_classifier**      | **str** | Maven classifier of component&#x27;s asset      | [optional] |
| **npm_scope**             | **str** | npm scope                                       | [optional] |
| **nuget_id**              | **str** | NuGet id                                        | [optional] |
| **nuget_tags**            | **str** | NuGet tags                                      | [optional] |
| **p2_plugin_name**        | **str** | p2 plugin name                                  | [optional] |
| **pypi_classifiers**      | **str** | PyPI classifiers                                | [optional] |
| **pypi_description**      | **str** | PyPI description                                | [optional] |
| **pypi_keywords**         | **str** | PyPI keywords                                   | [optional] |
| **pypi_summary**          | **str** | PyPI summary                                    | [optional] |
| **rubygems_description**  | **str** | RubyGems description                            | [optional] |
| **rubygems_platform**     | **str** | RubyGems platform                               | [optional] |
| **rubygems_summary**      | **str** | RubyGems summary                                | [optional] |
| **tag**                   | **str** | Component tag                                   | [optional] |
| **yum_architecture**      | **str** | Yum architecture                                | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get3**

> TagXO get3(name)

Get a tag

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TagsApi()
name = 'name_example' # str | Name of the tag to retrieve

try:
    # Get a tag
    api_response = api_instance.get3(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->get3: %s\n" % e)
```

### Parameters

| Name     | Type    | Description                 | Notes |
| -------- | ------- | --------------------------- | ----- |
| **name** | **str** | Name of the tag to retrieve |

### Return type

[**TagXO**](TagXO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tags**

> PageTagXO get_tags(continuation_token=continuation_token)

List tags

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TagsApi()
continuation_token = 'continuation_token_example' # str | A token returned by a prior request. If present, the next page of results are returned (optional)

try:
    # List tags
    api_response = api_instance.get_tags(continuation_token=continuation_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->get_tags: %s\n" % e)
```

### Parameters

| Name                   | Type    | Description                                                                            | Notes      |
| ---------------------- | ------- | -------------------------------------------------------------------------------------- | ---------- |
| **continuation_token** | **str** | A token returned by a prior request. If present, the next page of results are returned | [optional] |

### Return type

[**PageTagXO**](PageTagXO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace**

> TagXO replace(name, body=body)

Update a tags attributes

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TagsApi()
name = 'name_example' # str |
body = swagger_client.BaseTagXO() # BaseTagXO |  (optional)

try:
    # Update a tags attributes
    api_response = api_instance.replace(name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->replace: %s\n" % e)
```

### Parameters

| Name     | Type                          | Description | Notes      |
| -------- | ----------------------------- | ----------- | ---------- |
| **name** | **str**                       |             |
| **body** | [**BaseTagXO**](BaseTagXO.md) |             | [optional] |

### Return type

[**TagXO**](TagXO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
