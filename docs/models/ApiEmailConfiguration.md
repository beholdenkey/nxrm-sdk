# nexus_sdk.model.api_email_configuration.ApiEmailConfiguration

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**port** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer
**enabled** | bool,  | BoolClass,  |  | [optional] 
**host** | str,  | str,  |  | [optional] 
**username** | str,  | str,  |  | [optional] 
**password** | str,  | str,  |  | [optional] 
**fromAddress** | str,  | str,  |  | [optional] 
**subjectPrefix** | str,  | str,  | A prefix to add to all email subjects to aid in identifying automated emails | [optional] 
**startTlsEnabled** | bool,  | BoolClass,  | Enable STARTTLS Support for Insecure Connections | [optional] 
**startTlsRequired** | bool,  | BoolClass,  | Require STARTTLS Support | [optional] 
**sslOnConnectEnabled** | bool,  | BoolClass,  | Enable SSL/TLS Encryption upon Connection | [optional] 
**sslServerIdentityCheckEnabled** | bool,  | BoolClass,  | Verify the server certificate when using TLS or SSL | [optional] 
**nexusTrustStoreEnabled** | bool,  | BoolClass,  | Use the Nexus Repository Manager&#x27;s certificate truststore | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

