# nexus_sdk.model.asset_xo.AssetXO

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                       | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes                                               |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | --------------------------------------------------- |
| **downloadUrl**           | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                          |
| **path**                  | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                          |
| **id**                    | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                          |
| **repository**            | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                          |
| **format**                | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                          |
| **[checksum](#checksum)** | dict, frozendict.frozendict,                                                                                                                | frozendict.frozendict,                                                                  |                                                                    | [optional]                                          |
| **contentType**           | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                          |
| **lastModified**          | str, datetime,                                                                                                                              | str,                                                                                    |                                                                    | [optional] value must conform to RFC-3339 date-time |
| **lastDownloaded**        | str, datetime,                                                                                                                              | str,                                                                                    |                                                                    | [optional] value must conform to RFC-3339 date-time |
| **uploader**              | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                          |
| **uploaderIp**            | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                          |
| **fileSize**              | decimal.Decimal, int,                                                                                                                       | decimal.Decimal,                                                                        |                                                                    | [optional] value must be a 64 bit integer           |
| **any_string_name**       | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]                                          |

# checksum

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                                     | Input Type                   | Accessed Type          | Description                                                        | Notes      |
| --------------------------------------- | ---------------------------- | ---------------------- | ------------------------------------------------------------------ | ---------- |
| **[any_string_name](#any_string_name)** | dict, frozendict.frozendict, | frozendict.frozendict, | any string name can be used but the value must be the correct type | [optional] |

# any_string_name

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
