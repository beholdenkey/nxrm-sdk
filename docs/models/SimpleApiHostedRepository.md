# nexus_sdk.model.simple_api_hosted_repository.SimpleApiHostedRepository

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                 | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes      |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------- |
| **online**          | bool,                                                                                                                                       | BoolClass,                                                                              | Whether this repository accepts incoming requests                  |
| **storage**         | [**HostedStorageAttributes**](HostedStorageAttributes.md)                                                                                   | [**HostedStorageAttributes**](HostedStorageAttributes.md)                               |                                                                    |
| **name**            | str,                                                                                                                                        | str,                                                                                    | A unique identifier for this repository                            | [optional] |
| **cleanup**         | [**CleanupPolicyAttributes**](CleanupPolicyAttributes.md)                                                                                   | [**CleanupPolicyAttributes**](CleanupPolicyAttributes.md)                               |                                                                    | [optional] |
| **component**       | [**ComponentAttributes**](ComponentAttributes.md)                                                                                           | [**ComponentAttributes**](ComponentAttributes.md)                                       |                                                                    | [optional] |
| **any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional] |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
