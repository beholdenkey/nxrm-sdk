# swagger_client.SecurityManagementPrivilegesApi

All URIs are relative to _/service/rest/_

| Method                                                                        | HTTP request                                                                | Description                                          |
| ----------------------------------------------------------------------------- | --------------------------------------------------------------------------- | ---------------------------------------------------- |
| [**create_privilege**](SecurityManagementPrivilegesApi.md#create_privilege)   | **POST** /v1/security/privileges/application                                | Create an application type privilege.                |
| [**create_privilege1**](SecurityManagementPrivilegesApi.md#create_privilege1) | **POST** /v1/security/privileges/wildcard                                   | Create a wildcard type privilege.                    |
| [**create_privilege2**](SecurityManagementPrivilegesApi.md#create_privilege2) | **POST** /v1/security/privileges/repository-content-selector                | Create a repository content selector type privilege. |
| [**create_privilege3**](SecurityManagementPrivilegesApi.md#create_privilege3) | **POST** /v1/security/privileges/repository-admin                           | Create a repository admin type privilege.            |
| [**create_privilege4**](SecurityManagementPrivilegesApi.md#create_privilege4) | **POST** /v1/security/privileges/repository-view                            | Create a repository view type privilege.             |
| [**create_privilege5**](SecurityManagementPrivilegesApi.md#create_privilege5) | **POST** /v1/security/privileges/script                                     | Create a script type privilege.                      |
| [**delete_privilege**](SecurityManagementPrivilegesApi.md#delete_privilege)   | **DELETE** /v1/security/privileges/{privilegeName}                          | Delete a privilege by name.                          |
| [**get_privilege**](SecurityManagementPrivilegesApi.md#get_privilege)         | **GET** /v1/security/privileges/{privilegeName}                             | Retrieve a privilege by name.                        |
| [**get_privileges**](SecurityManagementPrivilegesApi.md#get_privileges)       | **GET** /v1/security/privileges                                             | Retrieve a list of privileges.                       |
| [**update_privilege**](SecurityManagementPrivilegesApi.md#update_privilege)   | **PUT** /v1/security/privileges/application/{privilegeName}                 | Update an application type privilege.                |
| [**update_privilege1**](SecurityManagementPrivilegesApi.md#update_privilege1) | **PUT** /v1/security/privileges/wildcard/{privilegeName}                    | Update a wildcard type privilege.                    |
| [**update_privilege2**](SecurityManagementPrivilegesApi.md#update_privilege2) | **PUT** /v1/security/privileges/repository-view/{privilegeName}             | Update a repository view type privilege.             |
| [**update_privilege3**](SecurityManagementPrivilegesApi.md#update_privilege3) | **PUT** /v1/security/privileges/repository-content-selector/{privilegeName} | Update a repository content selector type privilege. |
| [**update_privilege4**](SecurityManagementPrivilegesApi.md#update_privilege4) | **PUT** /v1/security/privileges/repository-admin/{privilegeName}            | Update a repository admin type privilege.            |
| [**update_privilege5**](SecurityManagementPrivilegesApi.md#update_privilege5) | **PUT** /v1/security/privileges/script/{privilegeName}                      | Update a script type privilege.                      |

# **create_privilege**

> create_privilege(body=body)

Create an application type privilege.

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementPrivilegesApi()
body = swagger_client.ApiPrivilegeApplicationRequest() # ApiPrivilegeApplicationRequest | The privilege to create. (optional)

try:
    # Create an application type privilege.
    api_instance.create_privilege(body=body)
except ApiException as e:
    print("Exception when calling SecurityManagementPrivilegesApi->create_privilege: %s\n" % e)
```

### Parameters

| Name     | Type                                                                    | Description              | Notes      |
| -------- | ----------------------------------------------------------------------- | ------------------------ | ---------- |
| **body** | [**ApiPrivilegeApplicationRequest**](ApiPrivilegeApplicationRequest.md) | The privilege to create. | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_privilege1**

> create_privilege1(body=body)

Create a wildcard type privilege.

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementPrivilegesApi()
body = swagger_client.ApiPrivilegeWildcardRequest() # ApiPrivilegeWildcardRequest | The privilege to create. (optional)

try:
    # Create a wildcard type privilege.
    api_instance.create_privilege1(body=body)
except ApiException as e:
    print("Exception when calling SecurityManagementPrivilegesApi->create_privilege1: %s\n" % e)
```

### Parameters

| Name     | Type                                                              | Description              | Notes      |
| -------- | ----------------------------------------------------------------- | ------------------------ | ---------- |
| **body** | [**ApiPrivilegeWildcardRequest**](ApiPrivilegeWildcardRequest.md) | The privilege to create. | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_privilege2**

> create_privilege2(body=body)

Create a repository content selector type privilege.

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementPrivilegesApi()
body = swagger_client.ApiPrivilegeRepositoryContentSelectorRequest() # ApiPrivilegeRepositoryContentSelectorRequest | The privilege to create. (optional)

try:
    # Create a repository content selector type privilege.
    api_instance.create_privilege2(body=body)
except ApiException as e:
    print("Exception when calling SecurityManagementPrivilegesApi->create_privilege2: %s\n" % e)
```

### Parameters

| Name     | Type                                                                                                | Description              | Notes      |
| -------- | --------------------------------------------------------------------------------------------------- | ------------------------ | ---------- |
| **body** | [**ApiPrivilegeRepositoryContentSelectorRequest**](ApiPrivilegeRepositoryContentSelectorRequest.md) | The privilege to create. | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_privilege3**

> create_privilege3(body=body)

Create a repository admin type privilege.

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementPrivilegesApi()
body = swagger_client.ApiPrivilegeRepositoryAdminRequest() # ApiPrivilegeRepositoryAdminRequest | The privilege to create. (optional)

try:
    # Create a repository admin type privilege.
    api_instance.create_privilege3(body=body)
except ApiException as e:
    print("Exception when calling SecurityManagementPrivilegesApi->create_privilege3: %s\n" % e)
```

### Parameters

| Name     | Type                                                                            | Description              | Notes      |
| -------- | ------------------------------------------------------------------------------- | ------------------------ | ---------- |
| **body** | [**ApiPrivilegeRepositoryAdminRequest**](ApiPrivilegeRepositoryAdminRequest.md) | The privilege to create. | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_privilege4**

> create_privilege4(body=body)

Create a repository view type privilege.

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementPrivilegesApi()
body = swagger_client.ApiPrivilegeRepositoryViewRequest() # ApiPrivilegeRepositoryViewRequest | The privilege to create. (optional)

try:
    # Create a repository view type privilege.
    api_instance.create_privilege4(body=body)
except ApiException as e:
    print("Exception when calling SecurityManagementPrivilegesApi->create_privilege4: %s\n" % e)
```

### Parameters

| Name     | Type                                                                          | Description              | Notes      |
| -------- | ----------------------------------------------------------------------------- | ------------------------ | ---------- |
| **body** | [**ApiPrivilegeRepositoryViewRequest**](ApiPrivilegeRepositoryViewRequest.md) | The privilege to create. | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_privilege5**

> create_privilege5(body=body)

Create a script type privilege.

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementPrivilegesApi()
body = swagger_client.ApiPrivilegeScriptRequest() # ApiPrivilegeScriptRequest | The privilege to create. (optional)

try:
    # Create a script type privilege.
    api_instance.create_privilege5(body=body)
except ApiException as e:
    print("Exception when calling SecurityManagementPrivilegesApi->create_privilege5: %s\n" % e)
```

### Parameters

| Name     | Type                                                          | Description              | Notes      |
| -------- | ------------------------------------------------------------- | ------------------------ | ---------- |
| **body** | [**ApiPrivilegeScriptRequest**](ApiPrivilegeScriptRequest.md) | The privilege to create. | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_privilege**

> delete_privilege(privilege_name)

Delete a privilege by name.

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementPrivilegesApi()
privilege_name = 'privilege_name_example' # str | The name of the privilege to delete.

try:
    # Delete a privilege by name.
    api_instance.delete_privilege(privilege_name)
except ApiException as e:
    print("Exception when calling SecurityManagementPrivilegesApi->delete_privilege: %s\n" % e)
```

### Parameters

| Name               | Type    | Description                          | Notes |
| ------------------ | ------- | ------------------------------------ | ----- |
| **privilege_name** | **str** | The name of the privilege to delete. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_privilege**

> ApiPrivilege get_privilege(privilege_name)

Retrieve a privilege by name.

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementPrivilegesApi()
privilege_name = 'privilege_name_example' # str | The name of the privilege to retrieve.

try:
    # Retrieve a privilege by name.
    api_response = api_instance.get_privilege(privilege_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityManagementPrivilegesApi->get_privilege: %s\n" % e)
```

### Parameters

| Name               | Type    | Description                            | Notes |
| ------------------ | ------- | -------------------------------------- | ----- |
| **privilege_name** | **str** | The name of the privilege to retrieve. |

### Return type

[**ApiPrivilege**](ApiPrivilege.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_privileges**

> list[ApiPrivilege] get_privileges()

Retrieve a list of privileges.

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementPrivilegesApi()

try:
    # Retrieve a list of privileges.
    api_response = api_instance.get_privileges()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityManagementPrivilegesApi->get_privileges: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**list[ApiPrivilege]**](ApiPrivilege.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_privilege**

> update_privilege(privilege_name, body=body)

Update an application type privilege.

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementPrivilegesApi()
privilege_name = 'privilege_name_example' # str | The name of the privilege to update.
body = swagger_client.ApiPrivilegeApplicationRequest() # ApiPrivilegeApplicationRequest | The privilege to update. (optional)

try:
    # Update an application type privilege.
    api_instance.update_privilege(privilege_name, body=body)
except ApiException as e:
    print("Exception when calling SecurityManagementPrivilegesApi->update_privilege: %s\n" % e)
```

### Parameters

| Name               | Type                                                                    | Description                          | Notes      |
| ------------------ | ----------------------------------------------------------------------- | ------------------------------------ | ---------- |
| **privilege_name** | **str**                                                                 | The name of the privilege to update. |
| **body**           | [**ApiPrivilegeApplicationRequest**](ApiPrivilegeApplicationRequest.md) | The privilege to update.             | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_privilege1**

> update_privilege1(privilege_name, body=body)

Update a wildcard type privilege.

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementPrivilegesApi()
privilege_name = 'privilege_name_example' # str | The name of the privilege to update.
body = swagger_client.ApiPrivilegeWildcardRequest() # ApiPrivilegeWildcardRequest | The privilege to update. (optional)

try:
    # Update a wildcard type privilege.
    api_instance.update_privilege1(privilege_name, body=body)
except ApiException as e:
    print("Exception when calling SecurityManagementPrivilegesApi->update_privilege1: %s\n" % e)
```

### Parameters

| Name               | Type                                                              | Description                          | Notes      |
| ------------------ | ----------------------------------------------------------------- | ------------------------------------ | ---------- |
| **privilege_name** | **str**                                                           | The name of the privilege to update. |
| **body**           | [**ApiPrivilegeWildcardRequest**](ApiPrivilegeWildcardRequest.md) | The privilege to update.             | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_privilege2**

> update_privilege2(privilege_name, body=body)

Update a repository view type privilege.

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementPrivilegesApi()
privilege_name = 'privilege_name_example' # str | The name of the privilege to update.
body = swagger_client.ApiPrivilegeRepositoryViewRequest() # ApiPrivilegeRepositoryViewRequest | The privilege to update. (optional)

try:
    # Update a repository view type privilege.
    api_instance.update_privilege2(privilege_name, body=body)
except ApiException as e:
    print("Exception when calling SecurityManagementPrivilegesApi->update_privilege2: %s\n" % e)
```

### Parameters

| Name               | Type                                                                          | Description                          | Notes      |
| ------------------ | ----------------------------------------------------------------------------- | ------------------------------------ | ---------- |
| **privilege_name** | **str**                                                                       | The name of the privilege to update. |
| **body**           | [**ApiPrivilegeRepositoryViewRequest**](ApiPrivilegeRepositoryViewRequest.md) | The privilege to update.             | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_privilege3**

> update_privilege3(privilege_name, body=body)

Update a repository content selector type privilege.

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementPrivilegesApi()
privilege_name = 'privilege_name_example' # str | The name of the privilege to update.
body = swagger_client.ApiPrivilegeRepositoryContentSelectorRequest() # ApiPrivilegeRepositoryContentSelectorRequest | The privilege to update. (optional)

try:
    # Update a repository content selector type privilege.
    api_instance.update_privilege3(privilege_name, body=body)
except ApiException as e:
    print("Exception when calling SecurityManagementPrivilegesApi->update_privilege3: %s\n" % e)
```

### Parameters

| Name               | Type                                                                                                | Description                          | Notes      |
| ------------------ | --------------------------------------------------------------------------------------------------- | ------------------------------------ | ---------- |
| **privilege_name** | **str**                                                                                             | The name of the privilege to update. |
| **body**           | [**ApiPrivilegeRepositoryContentSelectorRequest**](ApiPrivilegeRepositoryContentSelectorRequest.md) | The privilege to update.             | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_privilege4**

> update_privilege4(privilege_name, body=body)

Update a repository admin type privilege.

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementPrivilegesApi()
privilege_name = 'privilege_name_example' # str | The name of the privilege to update.
body = swagger_client.ApiPrivilegeRepositoryAdminRequest() # ApiPrivilegeRepositoryAdminRequest | The privilege to update. (optional)

try:
    # Update a repository admin type privilege.
    api_instance.update_privilege4(privilege_name, body=body)
except ApiException as e:
    print("Exception when calling SecurityManagementPrivilegesApi->update_privilege4: %s\n" % e)
```

### Parameters

| Name               | Type                                                                            | Description                          | Notes      |
| ------------------ | ------------------------------------------------------------------------------- | ------------------------------------ | ---------- |
| **privilege_name** | **str**                                                                         | The name of the privilege to update. |
| **body**           | [**ApiPrivilegeRepositoryAdminRequest**](ApiPrivilegeRepositoryAdminRequest.md) | The privilege to update.             | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_privilege5**

> update_privilege5(privilege_name, body=body)

Update a script type privilege.

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementPrivilegesApi()
privilege_name = 'privilege_name_example' # str | The name of the privilege to update.
body = swagger_client.ApiPrivilegeScriptRequest() # ApiPrivilegeScriptRequest | The privilege to update. (optional)

try:
    # Update a script type privilege.
    api_instance.update_privilege5(privilege_name, body=body)
except ApiException as e:
    print("Exception when calling SecurityManagementPrivilegesApi->update_privilege5: %s\n" % e)
```

### Parameters

| Name               | Type                                                          | Description                          | Notes      |
| ------------------ | ------------------------------------------------------------- | ------------------------------------ | ---------- |
| **privilege_name** | **str**                                                       | The name of the privilege to update. |
| **body**           | [**ApiPrivilegeScriptRequest**](ApiPrivilegeScriptRequest.md) | The privilege to update.             | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
