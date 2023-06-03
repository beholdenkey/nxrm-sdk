# swagger_client.SecurityManagementRolesApi

All URIs are relative to _/service/rest/_

| Method                                                   | HTTP request                       | Description |
| -------------------------------------------------------- | ---------------------------------- | ----------- |
| [**create**](SecurityManagementRolesApi.md#create)       | **POST** /v1/security/roles        | Create role |
| [**delete**](SecurityManagementRolesApi.md#delete)       | **DELETE** /v1/security/roles/{id} | Delete role |
| [**get_role**](SecurityManagementRolesApi.md#get_role)   | **GET** /v1/security/roles/{id}    | Get role    |
| [**get_roles**](SecurityManagementRolesApi.md#get_roles) | **GET** /v1/security/roles         | List roles  |
| [**update1**](SecurityManagementRolesApi.md#update1)     | **PUT** /v1/security/roles/{id}    | Update role |

# **create**

> RoleXOResponse create(body)

Create role

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementRolesApi()
body = swagger_client.RoleXORequest() # RoleXORequest | A role configuration

try:
    # Create role
    api_response = api_instance.create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityManagementRolesApi->create: %s\n" % e)
```

### Parameters

| Name     | Type                                  | Description          | Notes |
| -------- | ------------------------------------- | -------------------- | ----- |
| **body** | [**RoleXORequest**](RoleXORequest.md) | A role configuration |

### Return type

[**RoleXOResponse**](RoleXOResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**

> delete(id)

Delete role

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementRolesApi()
id = 'id_example' # str | The id of the role to delete

try:
    # Delete role
    api_instance.delete(id)
except ApiException as e:
    print("Exception when calling SecurityManagementRolesApi->delete: %s\n" % e)
```

### Parameters

| Name   | Type    | Description                  | Notes |
| ------ | ------- | ---------------------------- | ----- |
| **id** | **str** | The id of the role to delete |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role**

> RoleXOResponse get_role(id, source=source)

Get role

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementRolesApi()
id = 'id_example' # str | The id of the role to get
source = 'default' # str | The id of the user source to filter the roles by. Available sources can be fetched using the 'User Sources' endpoint. (optional) (default to default)

try:
    # Get role
    api_response = api_instance.get_role(id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityManagementRolesApi->get_role: %s\n" % e)
```

### Parameters

| Name       | Type    | Description                                                                                                                     | Notes                           |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| **id**     | **str** | The id of the role to get                                                                                                       |
| **source** | **str** | The id of the user source to filter the roles by. Available sources can be fetched using the &#x27;User Sources&#x27; endpoint. | [optional] [default to default] |

### Return type

[**RoleXOResponse**](RoleXOResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_roles**

> list[RoleXOResponse] get_roles(source=source)

List roles

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementRolesApi()
source = 'source_example' # str | The id of the user source to filter the roles by, if supplied. Otherwise roles from all user sources will be returned. (optional)

try:
    # List roles
    api_response = api_instance.get_roles(source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityManagementRolesApi->get_roles: %s\n" % e)
```

### Parameters

| Name       | Type    | Description                                                                                                            | Notes      |
| ---------- | ------- | ---------------------------------------------------------------------------------------------------------------------- | ---------- |
| **source** | **str** | The id of the user source to filter the roles by, if supplied. Otherwise roles from all user sources will be returned. | [optional] |

### Return type

[**list[RoleXOResponse]**](RoleXOResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update1**

> update1(body, id)

Update role

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementRolesApi()
body = swagger_client.RoleXORequest() # RoleXORequest | A role configuration
id = 'id_example' # str | The id of the role to update

try:
    # Update role
    api_instance.update1(body, id)
except ApiException as e:
    print("Exception when calling SecurityManagementRolesApi->update1: %s\n" % e)
```

### Parameters

| Name     | Type                                  | Description                  | Notes |
| -------- | ------------------------------------- | ---------------------------- | ----- |
| **body** | [**RoleXORequest**](RoleXORequest.md) | A role configuration         |
| **id**   | **str**                               | The id of the role to update |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
