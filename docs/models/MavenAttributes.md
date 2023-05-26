# nexus_sdk.model.maven_attributes.MavenAttributes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**versionPolicy** | str,  | str,  | What type of artifacts does this repository store? | [optional] must be one of ["RELEASE", "SNAPSHOT", "MIXED", ] 
**layoutPolicy** | str,  | str,  | Validate that all paths are maven artifact or metadata paths | [optional] must be one of ["STRICT", "PERMISSIVE", ] 
**contentDisposition** | str,  | str,  | Content Disposition | [optional] must be one of ["INLINE", "ATTACHMENT", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

