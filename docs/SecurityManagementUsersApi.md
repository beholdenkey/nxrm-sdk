# swagger_client.SecurityManagementUsersApi

All URIs are relative to _/service/rest/_

| Method                                                               | HTTP request                                                    | Description                                                                                                   |
| -------------------------------------------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| [**change_password**](SecurityManagementUsersApi.md#change_password) | **PUT** /v1/security/users/{userId}/change-password             | Change a user&#x27;s password.                                                                                |
| [**create_user**](SecurityManagementUsersApi.md#create_user)         | **POST** /v1/security/users                                     | Create a new user in the default source.                                                                      |
| [**delete_user**](SecurityManagementUsersApi.md#delete_user)         | **DELETE** /v1/security/users/{userId}                          | Delete a user.                                                                                                |
| [**get_users**](SecurityManagementUsersApi.md#get_users)             | **GET** /v1/security/users                                      | Retrieve a list of users. Note if the source is not &#x27;default&#x27; the response is limited to 100 users. |
| [**reset**](SecurityManagementUsersApi.md#reset)                     | **DELETE** /v1/security/users/{userId}/{realm}/user-token-reset | Reset the user token for the given user.                                                                      |
| [**update_user**](SecurityManagementUsersApi.md#update_user)         | **PUT** /v1/security/users/{userId}                             | Update an existing user.                                                                                      |

# **change_password**

> change_password(user_id, body=body)

Change a user's password.

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementUsersApi()
user_id = 'user_id_example' # str | The userid the request should apply to.
body = 'body_example' # str | The new password to use. (optional)

try:
    # Change a user's password.
    api_instance.change_password(user_id, body=body)
except ApiException as e:
    print("Exception when calling SecurityManagementUsersApi->change_password: %s\n" % e)
```

### Parameters

| Name        | Type              | Description                             | Notes      |
| ----------- | ----------------- | --------------------------------------- | ---------- |
| **user_id** | **str**           | The userid the request should apply to. |
| **body**    | [**str**](str.md) | The new password to use.                | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**

> ApiUser create_user(body=body)

Create a new user in the default source.

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementUsersApi()
body = swagger_client.ApiCreateUser() # ApiCreateUser | A representation of the user to create. (optional)

try:
    # Create a new user in the default source.
    api_response = api_instance.create_user(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityManagementUsersApi->create_user: %s\n" % e)
```

### Parameters

| Name     | Type                                  | Description                             | Notes      |
| -------- | ------------------------------------- | --------------------------------------- | ---------- |
| **body** | [**ApiCreateUser**](ApiCreateUser.md) | A representation of the user to create. | [optional] |

### Return type

[**ApiUser**](ApiUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**

> delete_user(user_id)

Delete a user.

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementUsersApi()
user_id = 'user_id_example' # str | The userid the request should apply to.

try:
    # Delete a user.
    api_instance.delete_user(user_id)
except ApiException as e:
    print("Exception when calling SecurityManagementUsersApi->delete_user: %s\n" % e)
```

### Parameters

| Name        | Type    | Description                             | Notes |
| ----------- | ------- | --------------------------------------- | ----- |
| **user_id** | **str** | The userid the request should apply to. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**

> list[ApiUser] get_users(user_id=user_id, source=source)

Retrieve a list of users. Note if the source is not 'default' the response is limited to 100 users.

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementUsersApi()
user_id = 'user_id_example' # str | An optional term to search userids for. (optional)
source = 'source_example' # str | An optional user source to restrict the search to. (optional)

try:
    # Retrieve a list of users. Note if the source is not 'default' the response is limited to 100 users.
    api_response = api_instance.get_users(user_id=user_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityManagementUsersApi->get_users: %s\n" % e)
```

### Parameters

| Name        | Type    | Description                                        | Notes      |
| ----------- | ------- | -------------------------------------------------- | ---------- |
| **user_id** | **str** | An optional term to search userids for.            | [optional] |
| **source**  | **str** | An optional user source to restrict the search to. | [optional] |

### Return type

[**list[ApiUser]**](ApiUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset**

> reset(user_id, realm)

Reset the user token for the given user.

Resetting the user token will invalidate the current token and force a new token to be created the next time it is accessed.

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementUsersApi()
user_id = 'user_id_example' # str | The userId of the user to reset the token for
realm = 'realm_example' # str | The realm of the user to reset the token for

try:
    # Reset the user token for the given user.
    api_instance.reset(user_id, realm)
except ApiException as e:
    print("Exception when calling SecurityManagementUsersApi->reset: %s\n" % e)
```

### Parameters

| Name        | Type    | Description                                   | Notes |
| ----------- | ------- | --------------------------------------------- | ----- |
| **user_id** | **str** | The userId of the user to reset the token for |
| **realm**   | **str** | The realm of the user to reset the token for  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**

> update_user(user_id, body=body)

Update an existing user.

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityManagementUsersApi()
user_id = 'user_id_example' # str | The userid the request should apply to.
body = swagger_client.ApiUser() # ApiUser | A representation of the user to update. (optional)

try:
    # Update an existing user.
    api_instance.update_user(user_id, body=body)
except ApiException as e:
    print("Exception when calling SecurityManagementUsersApi->update_user: %s\n" % e)
```

### Parameters

| Name        | Type                      | Description                             | Notes      |
| ----------- | ------------------------- | --------------------------------------- | ---------- |
| **user_id** | **str**                   | The userid the request should apply to. |
| **body**    | [**ApiUser**](ApiUser.md) | A representation of the user to update. | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
