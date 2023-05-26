# nexus_sdk.model.docker_hosted_repository_api_request.DockerHostedRepositoryApiRequest

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                 | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes      |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------- |
| **name**            | str,                                                                                                                                        | str,                                                                                    | A unique identifier for this repository                            |
| **online**          | bool,                                                                                                                                       | BoolClass,                                                                              | Whether this repository accepts incoming requests                  |
| **storage**         | [**DockerHostedStorageAttributes**](DockerHostedStorageAttributes.md)                                                                       | [**DockerHostedStorageAttributes**](DockerHostedStorageAttributes.md)                   |                                                                    |
| **docker**          | [**DockerAttributes**](DockerAttributes.md)                                                                                                 | [**DockerAttributes**](DockerAttributes.md)                                             |                                                                    |
| **cleanup**         | [**CleanupPolicyAttributes**](CleanupPolicyAttributes.md)                                                                                   | [**CleanupPolicyAttributes**](CleanupPolicyAttributes.md)                               |                                                                    | [optional] |
| **component**       | [**ComponentAttributes**](ComponentAttributes.md)                                                                                           | [**ComponentAttributes**](ComponentAttributes.md)                                       |                                                                    | [optional] |
| **any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional] |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
