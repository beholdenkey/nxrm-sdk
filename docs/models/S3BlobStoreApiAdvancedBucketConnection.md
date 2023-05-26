# nexus_sdk.model.s3_blob_store_api_advanced_bucket_connection.S3BlobStoreApiAdvancedBucketConnection

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**endpoint** | str,  | str,  | A custom endpoint URL for third party object stores using the S3 API. | [optional] 
**signerType** | str,  | str,  | An API signature version which may be required for third party object stores using the S3 API. | [optional] 
**forcePathStyle** | bool,  | BoolClass,  | Setting this flag will result in path-style access being used for all requests. | [optional] 
**maxConnectionPoolSize** | decimal.Decimal, int,  | decimal.Decimal,  | Setting this value will override the default connection pool size of Nexus of the s3 client for this blobstore. | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

