# S3BlobStoreApiAdvancedBucketConnection

## Properties

| Name                         | Type     | Description                                                                                                     | Notes      |
| ---------------------------- | -------- | --------------------------------------------------------------------------------------------------------------- | ---------- |
| **endpoint**                 | **str**  | A custom endpoint URL for third party object stores using the S3 API.                                           | [optional] |
| **signer_type**              | **str**  | An API signature version which may be required for third party object stores using the S3 API.                  | [optional] |
| **force_path_style**         | **bool** | Setting this flag will result in path-style access being used for all requests.                                 | [optional] |
| **max_connection_pool_size** | **int**  | Setting this value will override the default connection pool size of Nexus of the s3 client for this blobstore. | [optional] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
