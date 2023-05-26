# nexus_sdk.model.s3_blob_store_api_bucket_security.S3BlobStoreApiBucketSecurity

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                 | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                                                                 | Notes      |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ---------- |
| **accessKeyId**     | str,                                                                                                                                        | str,                                                                                    | An IAM access key ID for granting access to the S3 bucket                                                   | [optional] |
| **secretAccessKey** | str,                                                                                                                                        | str,                                                                                    | The secret access key associated with the specified IAM access key ID                                       | [optional] |
| **role**            | str,                                                                                                                                        | str,                                                                                    | An IAM role to assume in order to access the S3 bucket                                                      | [optional] |
| **sessionToken**    | str,                                                                                                                                        | str,                                                                                    | An AWS STS session token associated with temporary security credentials which grant access to the S3 bucket | [optional] |
| **any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type                                          | [optional] |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
