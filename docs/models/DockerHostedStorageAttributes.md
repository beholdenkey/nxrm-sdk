# nexus_sdk.model.docker_hosted_storage_attributes.DockerHostedStorageAttributes

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                             | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                                                                   | Notes                                            |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| **strictContentTypeValidation** | bool,                                                                                                                                       | BoolClass,                                                                              | Whether to validate uploaded content&#x27;s MIME type appropriate for the repository format                   |
| **writePolicy**                 | str,                                                                                                                                        | str,                                                                                    | Controls if deployments of and updates to assets are allowed                                                  | must be one of ["allow", "allow_once", "deny", ] |
| **blobStoreName**               | str,                                                                                                                                        | str,                                                                                    | Blob store used to store repository contents                                                                  | [optional]                                       |
| **latestPolicy**                | bool,                                                                                                                                       | BoolClass,                                                                              | Whether to allow redeploying the &#x27;latest&#x27; tag but defer to the Deployment Policy for all other tags | [optional]                                       |
| **any_string_name**             | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type                                            | [optional]                                       |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
