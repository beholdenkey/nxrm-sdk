# swagger_client.SecurityManagementSAMLApi

All URIs are relative to */service/rest/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_saml_configuration**](SecurityManagementSAMLApi.md#delete_saml_configuration) | **DELETE** /v1/security/saml | Delete SAML configuration
[**get_metadata**](SecurityManagementSAMLApi.md#get_metadata) | **GET** /v1/security/saml/metadata | Get service provider metadata XML document
[**get_public_certificate_in_pem_format**](SecurityManagementSAMLApi.md#get_public_certificate_in_pem_format) | **GET** /v1/security/saml/pem | Get service provider signing certificate in PEM format
[**get_saml_configuration**](SecurityManagementSAMLApi.md#get_saml_configuration) | **GET** /v1/security/saml | Get SAML configuration
[**put_saml_configuration**](SecurityManagementSAMLApi.md#put_saml_configuration) | **PUT** /v1/security/saml | Create or update SAML configuration

# **delete_saml_configuration**
> delete_saml_configuration()

Delete SAML configuration

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementSAMLApi()

try:
    # Delete SAML configuration
    api_instance.delete_saml_configuration()
except ApiException as e:
    print("Exception when calling SecurityManagementSAMLApi->delete_saml_configuration: %s\n" % e)
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

# **get_metadata**
> get_metadata()

Get service provider metadata XML document

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementSAMLApi()

try:
    # Get service provider metadata XML document
    api_instance.get_metadata()
except ApiException as e:
    print("Exception when calling SecurityManagementSAMLApi->get_metadata: %s\n" % e)
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

# **get_public_certificate_in_pem_format**
> get_public_certificate_in_pem_format()

Get service provider signing certificate in PEM format

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementSAMLApi()

try:
    # Get service provider signing certificate in PEM format
    api_instance.get_public_certificate_in_pem_format()
except ApiException as e:
    print("Exception when calling SecurityManagementSAMLApi->get_public_certificate_in_pem_format: %s\n" % e)
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

# **get_saml_configuration**
> get_saml_configuration()

Get SAML configuration

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementSAMLApi()

try:
    # Get SAML configuration
    api_instance.get_saml_configuration()
except ApiException as e:
    print("Exception when calling SecurityManagementSAMLApi->get_saml_configuration: %s\n" % e)
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

# **put_saml_configuration**
> put_saml_configuration(body=body)

Create or update SAML configuration

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementSAMLApi()
body = swagger_client.SamlConfigurationXO() # SamlConfigurationXO |  (optional)

try:
    # Create or update SAML configuration
    api_instance.put_saml_configuration(body=body)
except ApiException as e:
    print("Exception when calling SecurityManagementSAMLApi->put_saml_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SamlConfigurationXO**](SamlConfigurationXO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

