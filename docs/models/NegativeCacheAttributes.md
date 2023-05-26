# nexus_sdk.model.negative_cache_attributes.NegativeCacheAttributes

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                 | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                                         | Notes                          |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ------------------------------ |
| **timeToLive**      | decimal.Decimal, int,                                                                                                                       | decimal.Decimal,                                                                        | How long to cache the fact that a file was not found in the repository (in minutes) | value must be a 32 bit integer |
| **enabled**         | bool,                                                                                                                                       | BoolClass,                                                                              | Whether to cache responses for content not present in the proxied repository        |
| **any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type                  | [optional]                     |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
