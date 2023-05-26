# nexus_sdk.model.api_privilege_repository_view_request.ApiPrivilegeRepositoryViewRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The name of the privilege.  This value cannot be changed. | [optional] 
**description** | str,  | str,  |  | [optional] 
**[actions](#actions)** | list, tuple,  | tuple,  | A collection of actions to associate with the privilege, using BREAD syntax (browse,read,edit,add,delete,all) as well as &#x27;run&#x27; for script privileges. | [optional] 
**format** | str,  | str,  | The repository format (i.e &#x27;nuget&#x27;, &#x27;npm&#x27;) this privilege will grant access to (or * for all). | [optional] 
**repository** | str,  | str,  | The name of the repository this privilege will grant access to (or * for all). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# actions

A collection of actions to associate with the privilege, using BREAD syntax (browse,read,edit,add,delete,all) as well as 'run' for script privileges.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A collection of actions to associate with the privilege, using BREAD syntax (browse,read,edit,add,delete,all) as well as &#x27;run&#x27; for script privileges. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["READ", "BROWSE", "EDIT", "ADD", "DELETE", "RUN", "ASSOCIATE", "DISASSOCIATE", "ALL", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

