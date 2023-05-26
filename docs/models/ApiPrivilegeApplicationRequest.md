# nexus_sdk.model.api_privilege_application_request.ApiPrivilegeApplicationRequest

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
**domain** | str,  | str,  | The domain (i.e. &#x27;blobstores&#x27;, &#x27;capabilities&#x27; or even &#x27;*&#x27; for all) that this privilege is granting access to.  Note that creating new privileges with a domain is only necessary when using plugins that define their own domain(s). | [optional] 
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

