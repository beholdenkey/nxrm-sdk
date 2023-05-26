# nexus_sdk.model.routing_rule_xo.RoutingRuleXO

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                       | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                                                        | Notes                                          |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **name**                  | str,                                                                                                                                        | str,                                                                                    |                                                                                                    | [optional]                                     |
| **description**           | str,                                                                                                                                        | str,                                                                                    |                                                                                                    | [optional]                                     |
| **mode**                  | str,                                                                                                                                        | str,                                                                                    | Determines what should be done with requests when their path matches any of the matchers           | [optional] must be one of ["BLOCK", "ALLOW", ] |
| **[matchers](#matchers)** | list, tuple,                                                                                                                                | tuple,                                                                                  | Regular expressions used to identify request paths that are allowed or blocked (depending on mode) | [optional]                                     |
| **any_string_name**       | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type                                 | [optional]                                     |

# matchers

Regular expressions used to identify request paths that are allowed or blocked (depending on mode)

## Model Type Info

| Input Type   | Accessed Type | Description                                                                                        | Notes |
| ------------ | ------------- | -------------------------------------------------------------------------------------------------- | ----- |
| list, tuple, | tuple,        | Regular expressions used to identify request paths that are allowed or blocked (depending on mode) |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes |
| ---------- | ---------- | ------------- | ----------- | ----- |
| items      | str,       | str,          |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
