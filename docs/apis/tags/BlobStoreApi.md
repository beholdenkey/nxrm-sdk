<a id="__pageTop"></a>

# nexus_sdk.apis.tags.blob_store_api.BlobStoreApi

All URIs are relative to _http://localhost/service/rest_

| Method                                                                        | HTTP request                                                      | Description                                      |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------ |
| [**convert_blob_store_to_group**](#convert_blob_store_to_group)               | **post** /v1/blobstores/group/convert/{name}/{newNameForOriginal} | Convert a blob store to a group blob store       |
| [**create_blob_store**](#create_blob_store)                                   | **post** /v1/blobstores/s3                                        | Create an S3 blob store                          |
| [**create_blob_store1**](#create_blob_store1)                                 | **post** /v1/blobstores/azure                                     | Create an Azure blob store                       |
| [**create_file_blob_store**](#create_file_blob_store)                         | **post** /v1/blobstores/file                                      | Create a file blob store                         |
| [**create_group_blob_store**](#create_group_blob_store)                       | **post** /v1/blobstores/group                                     | Create a group blob store                        |
| [**delete_blob_store**](#delete_blob_store)                                   | **delete** /v1/blobstores/{name}                                  | Delete a blob store by name                      |
| [**get_blob_store**](#get_blob_store)                                         | **get** /v1/blobstores/s3/{name}                                  | Get a S3 blob store configuration by name        |
| [**get_blob_store1**](#get_blob_store1)                                       | **get** /v1/blobstores/azure/{name}                               | Get an Azure blob store configuration by name    |
| [**get_file_blob_store_configuration**](#get_file_blob_store_configuration)   | **get** /v1/blobstores/file/{name}                                | Get a file blob store configuration by name      |
| [**get_group_blob_store_configuration**](#get_group_blob_store_configuration) | **get** /v1/blobstores/group/{name}                               | Get a group blob store configuration by name     |
| [**list_blob_stores**](#list_blob_stores)                                     | **get** /v1/blobstores                                            | List the blob stores                             |
| [**quota_status**](#quota_status)                                             | **get** /v1/blobstores/{name}/quota-status                        | Get quota status for a given blob store          |
| [**update_blob_store**](#update_blob_store)                                   | **put** /v1/blobstores/s3/{name}                                  | Update an S3 blob store configuration by name    |
| [**update_blob_store1**](#update_blob_store1)                                 | **put** /v1/blobstores/azure/{name}                               | Update an Azure blob store configuration by name |
| [**update_file_blob_store**](#update_file_blob_store)                         | **put** /v1/blobstores/file/{name}                                | Update a file blob store configuration by name   |
| [**update_group_blob_store**](#update_group_blob_store)                       | **put** /v1/blobstores/group/{name}                               | Update a group blob store configuration by name  |

# **convert_blob_store_to_group**

<a id="convert_blob_store_to_group"></a>

> GroupBlobStoreApiModel convert_blob_store_to_group(namenew_name_for_original)

Convert a blob store to a group blob store

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import blob_store_api
from nexus_sdk.model.group_blob_store_api_model import GroupBlobStoreApiModel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = blob_store_api.BlobStoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
        'newNameForOriginal': "newNameForOriginal_example",
    }
    try:
        # Convert a blob store to a group blob store
        api_response = api_instance.convert_blob_store_to_group(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling BlobStoreApi->convert_blob_store_to_group: %s\n" % e)
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

| Name               | Type                     | Description | Notes |
| ------------------ | ------------------------ | ----------- | ----- |
| name               | NameSchema               |             |
| newNameForOriginal | NewNameForOriginalSchema |             |

# NameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# NewNameForOriginalSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                               | Description                                                 |
| ---- | ------------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                        | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#convert_blob_store_to_group.ApiResponseFor200) | Success                                                     |
| 403  | [ApiResponseFor403](#convert_blob_store_to_group.ApiResponseFor403) | Insufficient permissions                                    |
| 404  | [ApiResponseFor404](#convert_blob_store_to_group.ApiResponseFor404) | Blob store not found                                        |

#### convert_blob_store_to_group.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                 | Description | Notes |
| -------------------------------------------------------------------- | ----------- | ----- |
| [**GroupBlobStoreApiModel**](../../models/GroupBlobStoreApiModel.md) |             |

#### convert_blob_store_to_group.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### convert_blob_store_to_group.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_blob_store**

<a id="create_blob_store"></a>

> create_blob_store()

Create an S3 blob store

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import blob_store_api
from nexus_sdk.model.s3_blob_store_api_model import S3BlobStoreApiModel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = blob_store_api.BlobStoreApi(api_client)

    # example passing only optional values
    body = S3BlobStoreApiModel(
        name="s3",
        soft_quota=BlobStoreApiSoftQuota(
            type="spaceRemainingQuota",
            limit=0,
        ),
        bucket_configuration=S3BlobStoreApiBucketConfiguration(
            bucket=S3BlobStoreApiBucket(
                region="DEFAULT",
                name="name_example",
                prefix="prefix_example",
                expiration=3,
            ),
            encryption=S3BlobStoreApiEncryption(
                encryption_type="s3ManagedEncryption",
                encryption_key="encryption_key_example",
            ),
            bucket_security=S3BlobStoreApiBucketSecurity(
                access_key_id="access_key_id_example",
                secret_access_key="secret_access_key_example",
                role="role_example",
                session_token="session_token_example",
            ),
            advanced_bucket_connection=S3BlobStoreApiAdvancedBucketConnection(
                endpoint="endpoint_example",
                signer_type="signer_type_example",
                force_path_style=True,
                max_connection_pool_size=1,
            ),
        ),
        type="S3",
    )
    try:
        # Create an S3 blob store
        api_response = api_instance.create_blob_store(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling BlobStoreApi->create_blob_store: %s\n" % e)
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

| Type                                                           | Description | Notes |
| -------------------------------------------------------------- | ----------- | ----- |
| [**S3BlobStoreApiModel**](../../models/S3BlobStoreApiModel.md) |             |

### Return Types, Responses

| Code | Class                                                     | Description                                                 |
| ---- | --------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization              | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_blob_store.ApiResponseFor201) | S3 blob store created                                       |
| 401  | [ApiResponseFor401](#create_blob_store.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_blob_store.ApiResponseFor403) | Insufficient permissions                                    |

#### create_blob_store.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_blob_store.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_blob_store.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_blob_store1**

<a id="create_blob_store1"></a>

> create_blob_store1()

Create an Azure blob store

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import blob_store_api
from nexus_sdk.model.azure_blob_store_api_model import AzureBlobStoreApiModel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = blob_store_api.BlobStoreApi(api_client)

    # example passing only optional values
    body = AzureBlobStoreApiModel(
        name="name_example",
        soft_quota=BlobStoreApiSoftQuota(
            type="spaceRemainingQuota",
            limit=0,
        ),
        bucket_configuration=AzureBlobStoreApiBucketConfiguration(
            account_name="account_name_example",
            container_name="wr1c2v7s6djuy1zmeto",
            authentication=AzureBlobStoreApiAuthentication(
                authentication_method="ACCOUNTKEY",
                account_key="account_key_example",
            ),
        ),
    )
    try:
        # Create an Azure blob store
        api_response = api_instance.create_blob_store1(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling BlobStoreApi->create_blob_store1: %s\n" % e)
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

| Type                                                                 | Description | Notes |
| -------------------------------------------------------------------- | ----------- | ----- |
| [**AzureBlobStoreApiModel**](../../models/AzureBlobStoreApiModel.md) |             |

### Return Types, Responses

| Code | Class                                                      | Description                                                 |
| ---- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization               | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_blob_store1.ApiResponseFor201) | Azure blob store created                                    |
| 401  | [ApiResponseFor401](#create_blob_store1.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#create_blob_store1.ApiResponseFor403) | Insufficient permissions                                    |

#### create_blob_store1.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_blob_store1.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_blob_store1.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_file_blob_store**

<a id="create_file_blob_store"></a>

> create_file_blob_store()

Create a file blob store

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import blob_store_api
from nexus_sdk.model.file_blob_store_api_create_request import FileBlobStoreApiCreateRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = blob_store_api.BlobStoreApi(api_client)

    # example passing only optional values
    body = FileBlobStoreApiCreateRequest(
        soft_quota=BlobStoreApiSoftQuota(
            type="spaceRemainingQuota",
            limit=0,
        ),
        path="path_example",
        name="name_example",
    )
    try:
        # Create a file blob store
        api_response = api_instance.create_file_blob_store(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling BlobStoreApi->create_file_blob_store: %s\n" % e)
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
| [**FileBlobStoreApiCreateRequest**](../../models/FileBlobStoreApiCreateRequest.md) |             |

### Return Types, Responses

| Code | Class                                                          | Description                                                 |
| ---- | -------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                   | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#create_file_blob_store.ApiResponseFor204) | Success                                                     |
| 403  | [ApiResponseFor403](#create_file_blob_store.ApiResponseFor403) | Insufficient permissions                                    |

#### create_file_blob_store.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_file_blob_store.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_group_blob_store**

<a id="create_group_blob_store"></a>

> create_group_blob_store()

Create a group blob store

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import blob_store_api
from nexus_sdk.model.group_blob_store_api_create_request import GroupBlobStoreApiCreateRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = blob_store_api.BlobStoreApi(api_client)

    # example passing only optional values
    body = GroupBlobStoreApiCreateRequest(
        soft_quota=BlobStoreApiSoftQuota(
            type="spaceRemainingQuota",
            limit=0,
        ),
        members=[
            "members_example"
        ],
        fill_policy="roundRobin",
        name="name_example",
    )
    try:
        # Create a group blob store
        api_response = api_instance.create_group_blob_store(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling BlobStoreApi->create_group_blob_store: %s\n" % e)
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
| [**GroupBlobStoreApiCreateRequest**](../../models/GroupBlobStoreApiCreateRequest.md) |             |

### Return Types, Responses

| Code | Class                                                           | Description                                                 |
| ---- | --------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                    | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#create_group_blob_store.ApiResponseFor204) | Success                                                     |
| 403  | [ApiResponseFor403](#create_group_blob_store.ApiResponseFor403) | Insufficient permissions                                    |

#### create_group_blob_store.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_group_blob_store.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_blob_store**

<a id="delete_blob_store"></a>

> delete_blob_store(name)

Delete a blob store by name

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import blob_store_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = blob_store_api.BlobStoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    try:
        # Delete a blob store by name
        api_response = api_instance.delete_blob_store(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling BlobStoreApi->delete_blob_store: %s\n" % e)
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

| Name | Type       | Description | Notes |
| ---- | ---------- | ----------- | ----- |
| name | NameSchema |             |

# NameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code    | Class                                                             | Description                                                 |
| ------- | ----------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a     | api_client.ApiResponseWithoutDeserialization                      | When skip_deserialization is True this response is returned |
| default | [ApiResponseForDefault](#delete_blob_store.ApiResponseForDefault) | successful operation                                        |

#### delete_blob_store.ApiResponseForDefault

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_blob_store**

<a id="get_blob_store"></a>

> S3BlobStoreApiModel get_blob_store(name)

Get a S3 blob store configuration by name

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import blob_store_api
from nexus_sdk.model.s3_blob_store_api_model import S3BlobStoreApiModel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = blob_store_api.BlobStoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    try:
        # Get a S3 blob store configuration by name
        api_response = api_instance.get_blob_store(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling BlobStoreApi->get_blob_store: %s\n" % e)
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

| Name | Type       | Description | Notes |
| ---- | ---------- | ----------- | ----- |
| name | NameSchema |             |

# NameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                  | Description                                                 |
| ---- | ------------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization           | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_blob_store.ApiResponseFor200) | Success                                                     |
| 400  | [ApiResponseFor400](#get_blob_store.ApiResponseFor400) | Specified S3 blob store doesn&#x27;t exist                  |
| 401  | [ApiResponseFor401](#get_blob_store.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#get_blob_store.ApiResponseFor403) | Insufficient permissions                                    |

#### get_blob_store.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                           | Description | Notes |
| -------------------------------------------------------------- | ----------- | ----- |
| [**S3BlobStoreApiModel**](../../models/S3BlobStoreApiModel.md) |             |

#### get_blob_store.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_blob_store.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_blob_store.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_blob_store1**

<a id="get_blob_store1"></a>

> AzureBlobStoreApiModel get_blob_store1(name)

Get an Azure blob store configuration by name

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import blob_store_api
from nexus_sdk.model.azure_blob_store_api_model import AzureBlobStoreApiModel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = blob_store_api.BlobStoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    try:
        # Get an Azure blob store configuration by name
        api_response = api_instance.get_blob_store1(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling BlobStoreApi->get_blob_store1: %s\n" % e)
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

| Name | Type       | Description | Notes |
| ---- | ---------- | ----------- | ----- |
| name | NameSchema |             |

# NameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                   | Description                                                 |
| ---- | ------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization            | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_blob_store1.ApiResponseFor200) | Success                                                     |
| 400  | [ApiResponseFor400](#get_blob_store1.ApiResponseFor400) | Specified Azure blob store doesn&#x27;t exist               |
| 401  | [ApiResponseFor401](#get_blob_store1.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#get_blob_store1.ApiResponseFor403) | Insufficient permissions                                    |

#### get_blob_store1.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                 | Description | Notes |
| -------------------------------------------------------------------- | ----------- | ----- |
| [**AzureBlobStoreApiModel**](../../models/AzureBlobStoreApiModel.md) |             |

#### get_blob_store1.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_blob_store1.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_blob_store1.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_file_blob_store_configuration**

<a id="get_file_blob_store_configuration"></a>

> FileBlobStoreApiModel get_file_blob_store_configuration(name)

Get a file blob store configuration by name

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import blob_store_api
from nexus_sdk.model.file_blob_store_api_model import FileBlobStoreApiModel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = blob_store_api.BlobStoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "default",
    }
    try:
        # Get a file blob store configuration by name
        api_response = api_instance.get_file_blob_store_configuration(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling BlobStoreApi->get_file_blob_store_configuration: %s\n" % e)
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

| Name | Type       | Description | Notes |
| ---- | ---------- | ----------- | ----- |
| name | NameSchema |             |

# NameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                                     | Description                                                 |
| ---- | ------------------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                              | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_file_blob_store_configuration.ApiResponseFor200) | Success                                                     |
| 403  | [ApiResponseFor403](#get_file_blob_store_configuration.ApiResponseFor403) | Insufficient permissions                                    |
| 404  | [ApiResponseFor404](#get_file_blob_store_configuration.ApiResponseFor404) | Blob store not found                                        |

#### get_file_blob_store_configuration.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                               | Description | Notes |
| ------------------------------------------------------------------ | ----------- | ----- |
| [**FileBlobStoreApiModel**](../../models/FileBlobStoreApiModel.md) |             |

#### get_file_blob_store_configuration.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_file_blob_store_configuration.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_group_blob_store_configuration**

<a id="get_group_blob_store_configuration"></a>

> GroupBlobStoreApiModel get_group_blob_store_configuration(name)

Get a group blob store configuration by name

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import blob_store_api
from nexus_sdk.model.group_blob_store_api_model import GroupBlobStoreApiModel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = blob_store_api.BlobStoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    try:
        # Get a group blob store configuration by name
        api_response = api_instance.get_group_blob_store_configuration(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling BlobStoreApi->get_group_blob_store_configuration: %s\n" % e)
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

| Name | Type       | Description | Notes |
| ---- | ---------- | ----------- | ----- |
| name | NameSchema |             |

# NameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                                      | Description                                                 |
| ---- | -------------------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                               | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_group_blob_store_configuration.ApiResponseFor200) | Success                                                     |
| 403  | [ApiResponseFor403](#get_group_blob_store_configuration.ApiResponseFor403) | Insufficient permissions                                    |
| 404  | [ApiResponseFor404](#get_group_blob_store_configuration.ApiResponseFor404) | Blob store not found                                        |

#### get_group_blob_store_configuration.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                 | Description | Notes |
| -------------------------------------------------------------------- | ----------- | ----- |
| [**GroupBlobStoreApiModel**](../../models/GroupBlobStoreApiModel.md) |             |

#### get_group_blob_store_configuration.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_group_blob_store_configuration.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_blob_stores**

<a id="list_blob_stores"></a>

> [GenericBlobStoreApiResponse] list_blob_stores()

List the blob stores

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import blob_store_api
from nexus_sdk.model.generic_blob_store_api_response import GenericBlobStoreApiResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = blob_store_api.BlobStoreApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List the blob stores
        api_response = api_instance.list_blob_stores()
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling BlobStoreApi->list_blob_stores: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#list_blob_stores.ApiResponseFor200) | successful operation                                        |

#### list_blob_stores.ApiResponseFor200

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

| Class Name                                                                             | Input Type                                                                             | Accessed Type                                                                          | Description | Notes |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ----------- | ----- |
| [**GenericBlobStoreApiResponse**]({{complexTypePrefix}}GenericBlobStoreApiResponse.md) | [**GenericBlobStoreApiResponse**]({{complexTypePrefix}}GenericBlobStoreApiResponse.md) | [**GenericBlobStoreApiResponse**]({{complexTypePrefix}}GenericBlobStoreApiResponse.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **quota_status**

<a id="quota_status"></a>

> BlobStoreQuotaResultXO quota_status(name)

Get quota status for a given blob store

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import blob_store_api
from nexus_sdk.model.blob_store_quota_result_xo import BlobStoreQuotaResultXO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = blob_store_api.BlobStoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    try:
        # Get quota status for a given blob store
        api_response = api_instance.quota_status(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling BlobStoreApi->quota_status: %s\n" % e)
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

| Name | Type       | Description | Notes |
| ---- | ---------- | ----------- | ----- |
| name | NameSchema |             |

# NameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                | Description                                                 |
| ---- | ---------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization         | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#quota_status.ApiResponseFor200) | successful operation                                        |

#### quota_status.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                 | Description | Notes |
| -------------------------------------------------------------------- | ----------- | ----- |
| [**BlobStoreQuotaResultXO**](../../models/BlobStoreQuotaResultXO.md) |             |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_blob_store**

<a id="update_blob_store"></a>

> update_blob_store(name)

Update an S3 blob store configuration by name

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import blob_store_api
from nexus_sdk.model.s3_blob_store_api_model import S3BlobStoreApiModel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = blob_store_api.BlobStoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    try:
        # Update an S3 blob store configuration by name
        api_response = api_instance.update_blob_store(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling BlobStoreApi->update_blob_store: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
    }
    body = S3BlobStoreApiModel(
        name="s3",
        soft_quota=BlobStoreApiSoftQuota(
            type="spaceRemainingQuota",
            limit=0,
        ),
        bucket_configuration=S3BlobStoreApiBucketConfiguration(
            bucket=S3BlobStoreApiBucket(
                region="DEFAULT",
                name="name_example",
                prefix="prefix_example",
                expiration=3,
            ),
            encryption=S3BlobStoreApiEncryption(
                encryption_type="s3ManagedEncryption",
                encryption_key="encryption_key_example",
            ),
            bucket_security=S3BlobStoreApiBucketSecurity(
                access_key_id="access_key_id_example",
                secret_access_key="secret_access_key_example",
                role="role_example",
                session_token="session_token_example",
            ),
            advanced_bucket_connection=S3BlobStoreApiAdvancedBucketConnection(
                endpoint="endpoint_example",
                signer_type="signer_type_example",
                force_path_style=True,
                max_connection_pool_size=1,
            ),
        ),
        type="S3",
    )
    try:
        # Update an S3 blob store configuration by name
        api_response = api_instance.update_blob_store(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling BlobStoreApi->update_blob_store: %s\n" % e)
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

| Type                                                           | Description | Notes |
| -------------------------------------------------------------- | ----------- | ----- |
| [**S3BlobStoreApiModel**](../../models/S3BlobStoreApiModel.md) |             |

### path_params

#### RequestPathParams

| Name | Type       | Description | Notes |
| ---- | ---------- | ----------- | ----- |
| name | NameSchema |             |

# NameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                     | Description                                                 |
| ---- | --------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization              | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_blob_store.ApiResponseFor204) | S3 blob store updated                                       |
| 400  | [ApiResponseFor400](#update_blob_store.ApiResponseFor400) | Specified S3 blob store doesn&#x27;t exist                  |
| 401  | [ApiResponseFor401](#update_blob_store.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_blob_store.ApiResponseFor403) | Insufficient permissions                                    |

#### update_blob_store.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_blob_store.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_blob_store.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_blob_store.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_blob_store1**

<a id="update_blob_store1"></a>

> update_blob_store1(name)

Update an Azure blob store configuration by name

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import blob_store_api
from nexus_sdk.model.azure_blob_store_api_model import AzureBlobStoreApiModel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = blob_store_api.BlobStoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    try:
        # Update an Azure blob store configuration by name
        api_response = api_instance.update_blob_store1(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling BlobStoreApi->update_blob_store1: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
    }
    body = AzureBlobStoreApiModel(
        name="name_example",
        soft_quota=BlobStoreApiSoftQuota(
            type="spaceRemainingQuota",
            limit=0,
        ),
        bucket_configuration=AzureBlobStoreApiBucketConfiguration(
            account_name="account_name_example",
            container_name="wr1c2v7s6djuy1zmeto",
            authentication=AzureBlobStoreApiAuthentication(
                authentication_method="ACCOUNTKEY",
                account_key="account_key_example",
            ),
        ),
    )
    try:
        # Update an Azure blob store configuration by name
        api_response = api_instance.update_blob_store1(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling BlobStoreApi->update_blob_store1: %s\n" % e)
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

| Type                                                                 | Description | Notes |
| -------------------------------------------------------------------- | ----------- | ----- |
| [**AzureBlobStoreApiModel**](../../models/AzureBlobStoreApiModel.md) |             |

### path_params

#### RequestPathParams

| Name | Type       | Description | Notes |
| ---- | ---------- | ----------- | ----- |
| name | NameSchema |             |

# NameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                      | Description                                                 |
| ---- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization               | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_blob_store1.ApiResponseFor204) | Azure blob store updated                                    |
| 400  | [ApiResponseFor400](#update_blob_store1.ApiResponseFor400) | Specified Azure blob store doesn&#x27;t exist               |
| 401  | [ApiResponseFor401](#update_blob_store1.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#update_blob_store1.ApiResponseFor403) | Insufficient permissions                                    |

#### update_blob_store1.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_blob_store1.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_blob_store1.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_blob_store1.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_file_blob_store**

<a id="update_file_blob_store"></a>

> update_file_blob_store(name)

Update a file blob store configuration by name

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import blob_store_api
from nexus_sdk.model.file_blob_store_api_update_request import FileBlobStoreApiUpdateRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = blob_store_api.BlobStoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    try:
        # Update a file blob store configuration by name
        api_response = api_instance.update_file_blob_store(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling BlobStoreApi->update_file_blob_store: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
    }
    body = FileBlobStoreApiUpdateRequest(
        soft_quota=BlobStoreApiSoftQuota(
            type="spaceRemainingQuota",
            limit=0,
        ),
        path="path_example",
    )
    try:
        # Update a file blob store configuration by name
        api_response = api_instance.update_file_blob_store(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling BlobStoreApi->update_file_blob_store: %s\n" % e)
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
| [**FileBlobStoreApiUpdateRequest**](../../models/FileBlobStoreApiUpdateRequest.md) |             |

### path_params

#### RequestPathParams

| Name | Type       | Description | Notes |
| ---- | ---------- | ----------- | ----- |
| name | NameSchema |             |

# NameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                          | Description                                                 |
| ---- | -------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                   | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_file_blob_store.ApiResponseFor204) | Success                                                     |
| 403  | [ApiResponseFor403](#update_file_blob_store.ApiResponseFor403) | Insufficient permissions                                    |
| 404  | [ApiResponseFor404](#update_file_blob_store.ApiResponseFor404) | Blob store not found                                        |

#### update_file_blob_store.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_file_blob_store.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_file_blob_store.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_group_blob_store**

<a id="update_group_blob_store"></a>

> update_group_blob_store(name)

Update a group blob store configuration by name

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import blob_store_api
from nexus_sdk.model.group_blob_store_api_update_request import GroupBlobStoreApiUpdateRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = blob_store_api.BlobStoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    try:
        # Update a group blob store configuration by name
        api_response = api_instance.update_group_blob_store(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling BlobStoreApi->update_group_blob_store: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
    }
    body = GroupBlobStoreApiUpdateRequest(
        soft_quota=BlobStoreApiSoftQuota(
            type="spaceRemainingQuota",
            limit=0,
        ),
        members=[
            "members_example"
        ],
        fill_policy="roundRobin",
    )
    try:
        # Update a group blob store configuration by name
        api_response = api_instance.update_group_blob_store(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling BlobStoreApi->update_group_blob_store: %s\n" % e)
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
| [**GroupBlobStoreApiUpdateRequest**](../../models/GroupBlobStoreApiUpdateRequest.md) |             |

### path_params

#### RequestPathParams

| Name | Type       | Description | Notes |
| ---- | ---------- | ----------- | ----- |
| name | NameSchema |             |

# NameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                           | Description                                                 |
| ---- | --------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                    | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_group_blob_store.ApiResponseFor204) | Success                                                     |
| 403  | [ApiResponseFor403](#update_group_blob_store.ApiResponseFor403) | Insufficient permissions                                    |
| 404  | [ApiResponseFor404](#update_group_blob_store.ApiResponseFor404) | Blob store not found                                        |

#### update_group_blob_store.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_group_blob_store.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_group_blob_store.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
