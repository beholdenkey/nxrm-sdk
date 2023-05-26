# nexus_sdk.model.throwable.Throwable

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                           | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes      |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------- |
| **cause**                     | [**Throwable**](Throwable.md)                                                                                                               | [**Throwable**](Throwable.md)                                                           |                                                                    | [optional] |
| **[stackTrace](#stackTrace)** | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional] |
| **message**                   | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional] |
| **localizedMessage**          | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional] |
| **[suppressed](#suppressed)** | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional] |
| **any_string_name**           | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional] |

# stackTrace

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                                    | Input Type                                    | Accessed Type                                 | Description | Notes |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- | ----------- | ----- |
| [**StackTraceElement**](StackTraceElement.md) | [**StackTraceElement**](StackTraceElement.md) | [**StackTraceElement**](StackTraceElement.md) |             |

# suppressed

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                    | Input Type                    | Accessed Type                 | Description | Notes |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------- | ----- |
| [**Throwable**](Throwable.md) | [**Throwable**](Throwable.md) | [**Throwable**](Throwable.md) |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
