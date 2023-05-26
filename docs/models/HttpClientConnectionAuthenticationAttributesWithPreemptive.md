# nexus_sdk.model.http_client_connection_authentication_attributes_with_preemptive.HttpClientConnectionAuthenticationAttributesWithPreemptive

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | Authentication type | [optional] must be one of ["username", "ntlm", ] 
**username** | str,  | str,  |  | [optional] 
**password** | str,  | str,  |  | [optional] 
**ntlmHost** | str,  | str,  |  | [optional] 
**ntlmDomain** | str,  | str,  |  | [optional] 
**preemptive** | bool,  | BoolClass,  | Whether to use pre-emptive authentication. Use with caution. Defaults to false. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
