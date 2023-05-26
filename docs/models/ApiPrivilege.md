# nexus_sdk.model.api_privilege.ApiPrivilege

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | The type of privilege, each type covers different portions of the system. External values supplied to this will be ignored by the system. | [optional] 
**name** | str,  | str,  | The name of the privilege.  This value cannot be changed. | [optional] 
**description** | str,  | str,  |  | [optional] 
**readOnly** | bool,  | BoolClass,  | Indicates whether the privilege can be changed. External values supplied to this will be ignored by the system. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

