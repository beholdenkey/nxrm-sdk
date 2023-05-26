# nexus_sdk.model.http_client_attributes_with_preemptive_auth.HttpClientAttributesWithPreemptiveAuth

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**blocked** | bool,  | BoolClass,  | Whether to block outbound connections on the repository | 
**autoBlock** | bool,  | BoolClass,  | Whether to auto-block outbound connections if remote peer is detected as unreachable/unresponsive | 
**connection** | [**HttpClientConnectionAttributes**](HttpClientConnectionAttributes.md) | [**HttpClientConnectionAttributes**](HttpClientConnectionAttributes.md) |  | [optional] 
**authentication** | [**HttpClientConnectionAuthenticationAttributesWithPreemptive**](HttpClientConnectionAuthenticationAttributesWithPreemptive.md) | [**HttpClientConnectionAuthenticationAttributesWithPreemptive**](HttpClientConnectionAuthenticationAttributesWithPreemptive.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

