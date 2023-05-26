# nexus_sdk.model.docker_attributes.DockerAttributes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**v1Enabled** | bool,  | BoolClass,  | Whether to allow clients to use the V1 API to interact with this repository | 
**forceBasicAuth** | bool,  | BoolClass,  | Whether to force authentication (Docker Bearer Token Realm required if false) | 
**httpPort** | decimal.Decimal, int,  | decimal.Decimal,  | Create an HTTP connector at specified port | [optional] value must be a 32 bit integer
**httpsPort** | decimal.Decimal, int,  | decimal.Decimal,  | Create an HTTPS connector at specified port | [optional] value must be a 32 bit integer
**subdomain** | str,  | str,  | Allows to use subdomain | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

