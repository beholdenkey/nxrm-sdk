# nexus_sdk.model.group_blob_store_api_model.GroupBlobStoreApiModel

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**softQuota** | [**BlobStoreApiSoftQuota**](BlobStoreApiSoftQuota.md) | [**BlobStoreApiSoftQuota**](BlobStoreApiSoftQuota.md) |  | [optional] 
**[members](#members)** | list, tuple,  | tuple,  | List of the names of blob stores that are members of this group | [optional] 
**fillPolicy** | str,  | str,  |  | [optional] must be one of ["roundRobin", "writeToFirst", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# members

List of the names of blob stores that are members of this group

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of the names of blob stores that are members of this group | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
