# nexus_sdk.model.abstract_api_repository.AbstractApiRepository

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**online** | bool,  | BoolClass,  | Whether this repository accepts incoming requests | 
**name** | str,  | str,  | A unique identifier for this repository | [optional] 
**format** | str,  | str,  | Component format held in this repository | [optional] 
**type** | str,  | str,  | Controls if deployments of and updates to artifacts are allowed | [optional] must be one of ["hosted", "proxy", "group", ] 
**url** | str,  | str,  | URL to the repository | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

