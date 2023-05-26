# nexus_sdk.model.nuget_attributes.NugetAttributes

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                      | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                              | Notes                                     |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | ----------------------------------------- |
| **queryCacheItemMaxAge** | decimal.Decimal, int,                                                                                                                       | decimal.Decimal,                                                                        | How long to cache query results from the proxied repository (in seconds) | [optional] value must be a 32 bit integer |
| **nugetVersion**         | str,                                                                                                                                        | str,                                                                                    | Nuget protocol version                                                   | [optional] must be one of ["V2", "V3", ]  |
| **any_string_name**      | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type       | [optional]                                |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
