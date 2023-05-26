# nexus_sdk.model.api_create_user.ApiCreateUser

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                 | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                           | Notes                                                               |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **status**          | str,                                                                                                                                        | str,                                                                                    | The user&#x27;s status, e.g. active or disabled.                      | must be one of ["active", "locked", "disabled", "changepassword", ] |
| **userId**          | str,                                                                                                                                        | str,                                                                                    | The userid which is required for login. This value cannot be changed. | [optional]                                                          |
| **firstName**       | str,                                                                                                                                        | str,                                                                                    | The first name of the user.                                           | [optional]                                                          |
| **lastName**        | str,                                                                                                                                        | str,                                                                                    | The last name of the user.                                            | [optional]                                                          |
| **emailAddress**    | str,                                                                                                                                        | str,                                                                                    | The email address associated with the user.                           | [optional]                                                          |
| **password**        | str,                                                                                                                                        | str,                                                                                    | The password for the new user.                                        | [optional]                                                          |
| **[roles](#roles)** | list, tuple,                                                                                                                                | tuple,                                                                                  | The roles which the user has been assigned within Nexus.              | [optional]                                                          |
| **any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type    | [optional]                                                          |

# roles

The roles which the user has been assigned within Nexus.

## Model Type Info

| Input Type   | Accessed Type | Description                                              | Notes |
| ------------ | ------------- | -------------------------------------------------------- | ----- |
| list, tuple, | tuple,        | The roles which the user has been assigned within Nexus. |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes |
| ---------- | ---------- | ------------- | ----------- | ----- |
| items      | str,       | str,          |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
