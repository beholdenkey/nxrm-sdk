# nexus_sdk.model.role_xo_request.RoleXORequest

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                           | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes      |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------- |
| **id**                        | str,                                                                                                                                        | str,                                                                                    | The id of the role.                                                | [optional] |
| **name**                      | str,                                                                                                                                        | str,                                                                                    | The name of the role.                                              | [optional] |
| **description**               | str,                                                                                                                                        | str,                                                                                    | The description of this role.                                      | [optional] |
| **[privileges](#privileges)** | list, tuple,                                                                                                                                | tuple,                                                                                  | The list of privileges assigned to this role.                      | [optional] |
| **[roles](#roles)**           | list, tuple,                                                                                                                                | tuple,                                                                                  | The list of roles assigned to this role.                           | [optional] |
| **any_string_name**           | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional] |

# privileges

The list of privileges assigned to this role.

## Model Type Info

| Input Type   | Accessed Type | Description                                   | Notes |
| ------------ | ------------- | --------------------------------------------- | ----- |
| list, tuple, | tuple,        | The list of privileges assigned to this role. |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes |
| ---------- | ---------- | ------------- | ----------- | ----- |
| items      | str,       | str,          |             |

# roles

The list of roles assigned to this role.

## Model Type Info

| Input Type   | Accessed Type | Description                              | Notes |
| ------------ | ------------- | ---------------------------------------- | ----- |
| list, tuple, | tuple,        | The list of roles assigned to this role. |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes |
| ---------- | ---------- | ------------- | ----------- | ----- |
| items      | str,       | str,          |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
