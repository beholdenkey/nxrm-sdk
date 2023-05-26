# nexus_sdk.model.create_ldap_server_xo.CreateLdapServerXo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**maxIncidentsCount** | decimal.Decimal, int,  | decimal.Decimal,  | How many retry attempts | value must be a 32 bit integer
**groupType** | str,  | str,  | Defines a type of groups used: static (a group contains a list of users) or dynamic (a user contains a list of groups). Required if ldapGroupsAsRoles is true. | must be one of ["static", "dynamic", ] 
**protocol** | str,  | str,  | LDAP server connection Protocol to use | must be one of ["ldap", "ldaps", ] 
**connectionRetryDelaySeconds** | decimal.Decimal, int,  | decimal.Decimal,  | How long to wait before retrying | value must be a 32 bit integer
**port** | decimal.Decimal, int,  | decimal.Decimal,  | LDAP server connection port to use | value must be a 32 bit integer
**searchBase** | str,  | str,  | LDAP location to be added to the connection URL | 
**connectionTimeoutSeconds** | decimal.Decimal, int,  | decimal.Decimal,  | How long to wait before timeout | value must be a 32 bit integer
**host** | str,  | str,  | LDAP server connection hostname | 
**name** | str,  | str,  | LDAP server name | 
**authScheme** | str,  | str,  | Authentication scheme used for connecting to LDAP server | must be one of ["NONE", "SIMPLE", "DIGEST_MD5", "CRAM_MD5", ] 
**authPassword** | str,  | str,  | The password to bind with. Required if authScheme other than none. | 
**useTrustStore** | bool,  | BoolClass,  | Whether to use certificates stored in Nexus Repository Manager&#x27;s truststore | [optional] 
**authRealm** | str,  | str,  | The SASL realm to bind to. Required if authScheme is CRAM_MD5 or DIGEST_MD5 | [optional] 
**authUsername** | str,  | str,  | This must be a fully qualified username if simple authentication is used. Required if authScheme other than none. | [optional] 
**userBaseDn** | str,  | str,  | The relative DN where user objects are found (e.g. ou&#x3D;people). This value will have the Search base DN value appended to form the full User search base DN. | [optional] 
**userSubtree** | bool,  | BoolClass,  | Are users located in structures below the user base DN? | [optional] 
**userObjectClass** | str,  | str,  | LDAP class for user objects | [optional] 
**userLdapFilter** | str,  | str,  | LDAP search filter to limit user search | [optional] 
**userIdAttribute** | str,  | str,  | This is used to find a user given its user ID | [optional] 
**userRealNameAttribute** | str,  | str,  | This is used to find a real name given the user ID | [optional] 
**userEmailAddressAttribute** | str,  | str,  | This is used to find an email address given the user ID | [optional] 
**userPasswordAttribute** | str,  | str,  | If this field is blank the user will be authenticated against a bind with the LDAP server | [optional] 
**ldapGroupsAsRoles** | bool,  | BoolClass,  | Denotes whether LDAP assigned roles are used as Nexus Repository Manager roles | [optional] 
**groupBaseDn** | str,  | str,  | The relative DN where group objects are found (e.g. ou&#x3D;Group). This value will have the Search base DN value appended to form the full Group search base DN. | [optional] 
**groupSubtree** | bool,  | BoolClass,  | Are groups located in structures below the group base DN | [optional] 
**groupObjectClass** | str,  | str,  | LDAP class for group objects. Required if groupType is static | [optional] 
**groupIdAttribute** | str,  | str,  | This field specifies the attribute of the Object class that defines the Group ID. Required if groupType is static | [optional] 
**groupMemberAttribute** | str,  | str,  | LDAP attribute containing the usernames for the group. Required if groupType is static | [optional] 
**groupMemberFormat** | str,  | str,  | The format of user ID stored in the group member attribute. Required if groupType is static | [optional] 
**userMemberOfAttribute** | str,  | str,  | Set this to the attribute used to store the attribute which holds groups DN in the user object. Required if groupType is dynamic | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

