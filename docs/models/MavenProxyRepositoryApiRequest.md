# nexus_sdk.model.maven_proxy_repository_api_request.MavenProxyRepositoryApiRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**httpClient** | [**HttpClientAttributesWithPreemptiveAuth**](HttpClientAttributesWithPreemptiveAuth.md) | [**HttpClientAttributesWithPreemptiveAuth**](HttpClientAttributesWithPreemptiveAuth.md) |  | 
**proxy** | [**ProxyAttributes**](ProxyAttributes.md) | [**ProxyAttributes**](ProxyAttributes.md) |  | 
**negativeCache** | [**NegativeCacheAttributes**](NegativeCacheAttributes.md) | [**NegativeCacheAttributes**](NegativeCacheAttributes.md) |  | 
**maven** | [**MavenAttributes**](MavenAttributes.md) | [**MavenAttributes**](MavenAttributes.md) |  | 
**name** | str,  | str,  | A unique identifier for this repository | 
**online** | bool,  | BoolClass,  | Whether this repository accepts incoming requests | 
**storage** | [**StorageAttributes**](StorageAttributes.md) | [**StorageAttributes**](StorageAttributes.md) |  | 
**cleanup** | [**CleanupPolicyAttributes**](CleanupPolicyAttributes.md) | [**CleanupPolicyAttributes**](CleanupPolicyAttributes.md) |  | [optional] 
**routingRule** | str,  | str,  |  | [optional] 
**replication** | [**ReplicationAttributes**](ReplicationAttributes.md) | [**ReplicationAttributes**](ReplicationAttributes.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

