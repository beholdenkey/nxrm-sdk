# nexus_sdk.model.replication_connection_xo.ReplicationConnectionXO

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                                   | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                                                      | Notes      |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ---------- |
| **destinationInstanceUrl**            | str,                                                                                                                                        | str,                                                                                    | Destination Instance URL                                                                         |
| **name**                              | str,                                                                                                                                        | str,                                                                                    | Replication Connection Name                                                                      |
| **destinationRepositoryName**         | str,                                                                                                                                        | str,                                                                                    | Destination Repository Name                                                                      |
| **sourceRepositoryName**              | str,                                                                                                                                        | str,                                                                                    | Source Repository Name                                                                           |
| **id**                                | str,                                                                                                                                        | str,                                                                                    | Connection Id                                                                                    | [optional] |
| **destinationInstanceUsername**       | str,                                                                                                                                        | str,                                                                                    | Destination Instance Username                                                                    | [optional] |
| **destinationInstancePassword**       | str,                                                                                                                                        | str,                                                                                    | Destination Instance Password                                                                    | [optional] |
| **[contentRegexes](#contentRegexes)** | list, tuple,                                                                                                                                | tuple,                                                                                  | Regular expressions used to filter the repository content that is replicated                     | [optional] |
| **includeExistingContent**            | bool,                                                                                                                                       | BoolClass,                                                                              | Boolean used to configure if a replication connection should include existing content            | [optional] |
| **useTrustStore**                     | bool,                                                                                                                                       | BoolClass,                                                                              | Boolean used to configure if a replication connection should use the Nexus Repository Truststore | [optional] |
| **any_string_name**                   | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type                               | [optional] |

# contentRegexes

Regular expressions used to filter the repository content that is replicated

## Model Type Info

| Input Type   | Accessed Type | Description                                                                  | Notes |
| ------------ | ------------- | ---------------------------------------------------------------------------- | ----- |
| list, tuple, | tuple,        | Regular expressions used to filter the repository content that is replicated |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes |
| ---------- | ---------- | ------------- | ----------- | ----- |
| items      | str,       | str,          |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
