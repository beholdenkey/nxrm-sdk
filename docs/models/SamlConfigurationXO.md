# nexus_sdk.model.saml_configuration_xo.SamlConfigurationXO

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**idpMetadata** | str,  | str,  | SAML Identity Provider Metadata XML | 
**usernameAttribute** | str,  | str,  | SAML attribute name for the username | 
**entityId** | str,  | str,  | SAML Service Provider&#x27;s unique identifying URI | [optional] 
**firstNameAttribute** | str,  | str,  | SAML attribute name for the first name | [optional] 
**lastNameAttribute** | str,  | str,  | SAML attribute name for the last name | [optional] 
**emailAttribute** | str,  | str,  | SAML attribute name for email | [optional] 
**groupsAttribute** | str,  | str,  | SAML attribute name for groups which maps the Identity Provider groups to a Nexus Repository Manager role | [optional] 
**validateResponseSignature** | bool,  | BoolClass,  | Validate signatures on responses from Identity Provider | [optional] 
**validateAssertionSignature** | bool,  | BoolClass,  | Validate signatures on assertions from Identity Provider | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

