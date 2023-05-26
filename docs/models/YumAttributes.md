# nexus_sdk.model.yum_attributes.YumAttributes

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                 | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                         | Notes                                                |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ---------------------------------------------------- |
| **repodataDepth**   | decimal.Decimal, int,                                                                                                                       | decimal.Decimal,                                                                        | Specifies the repository depth where repodata folder(s) are created | value must be a 32 bit integer                       |
| **deployPolicy**    | str,                                                                                                                                        | str,                                                                                    | Validate that all paths are RPMs or yum metadata                    | [optional] must be one of ["PERMISSIVE", "STRICT", ] |
| **any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type  | [optional]                                           |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
