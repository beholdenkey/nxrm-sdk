# nexus_sdk.model.s3_blob_store_api_model.S3BlobStoreApiModel

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                     | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes      |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------- |
| **name**                | str,                                                                                                                                        | str,                                                                                    | The name of the S3 blob store.                                     |
| **bucketConfiguration** | [**S3BlobStoreApiBucketConfiguration**](S3BlobStoreApiBucketConfiguration.md)                                                               | [**S3BlobStoreApiBucketConfiguration**](S3BlobStoreApiBucketConfiguration.md)           |                                                                    |
| **softQuota**           | [**BlobStoreApiSoftQuota**](BlobStoreApiSoftQuota.md)                                                                                       | [**BlobStoreApiSoftQuota**](BlobStoreApiSoftQuota.md)                                   |                                                                    | [optional] |
| **type**                | str,                                                                                                                                        | str,                                                                                    | The blob store type.                                               | [optional] |
| **any_string_name**     | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional] |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
