# nexus_sdk.model.http_client_connection_attributes.HttpClientConnectionAttributes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**retries** | decimal.Decimal, int,  | decimal.Decimal,  | Total retries if the initial connection attempt suffers a timeout | [optional] value must be a 32 bit integer
**userAgentSuffix** | str,  | str,  | Custom fragment to append to User-Agent header in HTTP requests | [optional] 
**timeout** | decimal.Decimal, int,  | decimal.Decimal,  | Seconds to wait for activity before stopping and retrying the connection | [optional] value must be a 32 bit integer
**enableCircularRedirects** | bool,  | BoolClass,  | Whether to enable redirects to the same location (may be required by some servers) | [optional] 
**enableCookies** | bool,  | BoolClass,  | Whether to allow cookies to be stored and used | [optional] 
**useTrustStore** | bool,  | BoolClass,  | Use certificates stored in the Nexus Repository Manager truststore to connect to external systems | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
