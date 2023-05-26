# nexus_sdk.model.docker_proxy_attributes.DockerProxyAttributes

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                                                       | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                                           | Notes                                                     |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| **indexType**                                             | str,                                                                                                                                        | str,                                                                                    | Type of Docker Index                                                                  | [optional] must be one of ["HUB", "REGISTRY", "CUSTOM", ] |
| **indexUrl**                                              | str,                                                                                                                                        | str,                                                                                    | Url of Docker Index to use                                                            | [optional]                                                |
| **cacheForeignLayers**                                    | bool,                                                                                                                                       | BoolClass,                                                                              | Allow Nexus Repository Manager to download and cache foreign layers                   | [optional]                                                |
| **[foreignLayerUrlWhitelist](#foreignLayerUrlWhitelist)** | list, tuple,                                                                                                                                | tuple,                                                                                  | Regular expressions used to identify URLs that are allowed for foreign layer requests | [optional]                                                |
| **any_string_name**                                       | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type                    | [optional]                                                |

# foreignLayerUrlWhitelist

Regular expressions used to identify URLs that are allowed for foreign layer requests

## Model Type Info

| Input Type   | Accessed Type | Description                                                                           | Notes |
| ------------ | ------------- | ------------------------------------------------------------------------------------- | ----- |
| list, tuple, | tuple,        | Regular expressions used to identify URLs that are allowed for foreign layer requests |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes |
| ---------- | ---------- | ------------- | ----------- | ----- |
| items      | str,       | str,          |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
