# swagger_client.SecurityManagementLDAPApi

All URIs are relative to */service/rest/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_order**](SecurityManagementLDAPApi.md#change_order) | **POST** /v1/security/ldap/change-order | Change LDAP server order
[**create_ldap_server**](SecurityManagementLDAPApi.md#create_ldap_server) | **POST** /v1/security/ldap | Create LDAP server
[**delete_ldap_server**](SecurityManagementLDAPApi.md#delete_ldap_server) | **DELETE** /v1/security/ldap/{name} | Delete LDAP server
[**get_ldap_server**](SecurityManagementLDAPApi.md#get_ldap_server) | **GET** /v1/security/ldap/{name} | Get LDAP server
[**get_ldap_servers**](SecurityManagementLDAPApi.md#get_ldap_servers) | **GET** /v1/security/ldap | List LDAP servers
[**update_ldap_server**](SecurityManagementLDAPApi.md#update_ldap_server) | **PUT** /v1/security/ldap/{name} | Update LDAP server

# **change_order**
> change_order(body=body)

Change LDAP server order

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementLDAPApi()
body = ['body_example'] # list[str] | Ordered list of LDAP server names (optional)

try:
    # Change LDAP server order
    api_instance.change_order(body=body)
except ApiException as e:
    print("Exception when calling SecurityManagementLDAPApi->change_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| Ordered list of LDAP server names | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ldap_server**
> create_ldap_server(body=body)

Create LDAP server

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementLDAPApi()
body = swagger_client.CreateLdapServerXo() # CreateLdapServerXo |  (optional)

try:
    # Create LDAP server
    api_instance.create_ldap_server(body=body)
except ApiException as e:
    print("Exception when calling SecurityManagementLDAPApi->create_ldap_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateLdapServerXo**](CreateLdapServerXo.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ldap_server**
> delete_ldap_server(name)

Delete LDAP server

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementLDAPApi()
name = 'name_example' # str | Name of the LDAP server to delete

try:
    # Delete LDAP server
    api_instance.delete_ldap_server(name)
except ApiException as e:
    print("Exception when calling SecurityManagementLDAPApi->delete_ldap_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the LDAP server to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ldap_server**
> get_ldap_server(name)

Get LDAP server

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementLDAPApi()
name = 'name_example' # str | Name of the LDAP server to retrieve

try:
    # Get LDAP server
    api_instance.get_ldap_server(name)
except ApiException as e:
    print("Exception when calling SecurityManagementLDAPApi->get_ldap_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the LDAP server to retrieve | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ldap_servers**
> get_ldap_servers()

List LDAP servers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementLDAPApi()

try:
    # List LDAP servers
    api_instance.get_ldap_servers()
except ApiException as e:
    print("Exception when calling SecurityManagementLDAPApi->get_ldap_servers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ldap_server**
> update_ldap_server(name, body=body)

Update LDAP server

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementLDAPApi()
name = 'name_example' # str | Name of the LDAP server to update
body = swagger_client.UpdateLdapServerXo() # UpdateLdapServerXo | Updated values of LDAP server (optional)

try:
    # Update LDAP server
    api_instance.update_ldap_server(name, body=body)
except ApiException as e:
    print("Exception when calling SecurityManagementLDAPApi->update_ldap_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the LDAP server to update | 
 **body** | [**UpdateLdapServerXo**](UpdateLdapServerXo.md)| Updated values of LDAP server | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

