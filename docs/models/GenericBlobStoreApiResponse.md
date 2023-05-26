# nexus_sdk.model.generic_blob_store_api_response.GenericBlobStoreApiResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**softQuota** | [**BlobStoreApiSoftQuota**](BlobStoreApiSoftQuota.md) | [**BlobStoreApiSoftQuota**](BlobStoreApiSoftQuota.md) |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**unavailable** | bool,  | BoolClass,  |  | [optional] 
**blobCount** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**totalSizeInBytes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**availableSpaceInBytes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

