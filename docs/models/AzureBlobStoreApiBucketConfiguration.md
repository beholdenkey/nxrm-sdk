# nexus_sdk.model.azure_blob_store_api_bucket_configuration.AzureBlobStoreApiBucketConfiguration

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                 | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes      |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------- |
| **accountName**     | str,                                                                                                                                        | str,                                                                                    | Account name found under Access keys for the storage account.      |
| **containerName**   | str,                                                                                                                                        | str,                                                                                    | The name of an existing container to be used for storage.          |
| **authentication**  | [**AzureBlobStoreApiAuthentication**](AzureBlobStoreApiAuthentication.md)                                                                   | [**AzureBlobStoreApiAuthentication**](AzureBlobStoreApiAuthentication.md)               |                                                                    |
| **any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional] |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
