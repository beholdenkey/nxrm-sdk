# nexus_sdk.model.s3_blob_store_api_bucket.S3BlobStoreApiBucket

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                 | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                                              | Notes                          |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ------------------------------ |
| **name**            | str,                                                                                                                                        | str,                                                                                    | The name of the S3 bucket                                                                |
| **expiration**      | decimal.Decimal, int,                                                                                                                       | decimal.Decimal,                                                                        | How many days until deleted blobs are finally removed from the S3 bucket (-1 to disable) | value must be a 32 bit integer |
| **region**          | str,                                                                                                                                        | str,                                                                                    | The AWS region to create a new S3 bucket in or an existing S3 bucket&#x27;s region       |
| **prefix**          | str,                                                                                                                                        | str,                                                                                    | The S3 blob store (i.e S3 object) key prefix                                             | [optional]                     |
| **any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type                       | [optional]                     |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
