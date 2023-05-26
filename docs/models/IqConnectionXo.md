# nexus_sdk.model.iq_connection_xo.IqConnectionXo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**authenticationType** | str,  | str,  | Authentication method | must be one of ["USER", "PKI", ] 
**enabled** | bool,  | BoolClass,  | Whether to use IQ Server | [optional] 
**showLink** | bool,  | BoolClass,  | Show IQ Server link in Browse menu when server is enabled | [optional] 
**url** | str,  | str,  | The address of your IQ Server | [optional] 
**username** | str,  | str,  | User with access to IQ Server | [optional] 
**password** | str,  | str,  | Credentials for the IQ Server User | [optional] 
**useTrustStoreForUrl** | bool,  | BoolClass,  | Use certificates stored in the Nexus Repository Manager truststore to connect to IQ Server | [optional] 
**timeoutSeconds** | decimal.Decimal, int,  | decimal.Decimal,  | Seconds to wait for activity before stopping and retrying the connection. Leave blank to use the globally defined HTTP timeout. | [optional] value must be a 32 bit integer
**properties** | str,  | str,  | Additional properties to configure for IQ Server | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

