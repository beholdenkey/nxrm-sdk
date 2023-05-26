# nexus_sdk.model.group_attributes.GroupAttributes

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                             | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes      |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------- |
| **[memberNames](#memberNames)** | list, tuple,                                                                                                                                | tuple,                                                                                  | Member repositories&#x27; names                                    | [optional] |
| **any_string_name**             | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional] |

# memberNames

Member repositories' names

## Model Type Info

| Input Type   | Accessed Type | Description                     | Notes |
| ------------ | ------------- | ------------------------------- | ----- |
| list, tuple, | tuple,        | Member repositories&#x27; names |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes |
| ---------- | ---------- | ------------- | ----------- | ----- |
| items      | str,       | str,          |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
