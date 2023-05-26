<a id="__pageTop"></a>
# nexus_sdk.apis.tags.security_management_users_api.SecurityManagementUsersApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_password**](#change_password) | **put** /v1/security/users/{userId}/change-password | Change a user&#x27;s password.
[**create_user**](#create_user) | **post** /v1/security/users | Create a new user in the default source.
[**delete_user**](#delete_user) | **delete** /v1/security/users/{userId} | Delete a user.
[**get_users**](#get_users) | **get** /v1/security/users | Retrieve a list of users. Note if the source is not &#x27;default&#x27; the response is limited to 100 users.
[**reset**](#reset) | **delete** /v1/security/users/{userId}/{realm}/user-token-reset | Reset the user token for the given user.
[**update_user**](#update_user) | **put** /v1/security/users/{userId} | Update an existing user.

# **change_password**
<a id="change_password"></a>
> change_password(user_id)

Change a user's password.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_users_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_users_api.SecurityManagementUsersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'userId': "userId_example",
    }
    try:
        # Change a user's password.
        api_response = api_instance.change_password(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementUsersApi->change_password: %s\n" % e)

    # example passing only optional values
    path_params = {
        'userId': "userId_example",
    }
    body = "body_example"
    try:
        # Change a user's password.
        api_response = api_instance.change_password(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementUsersApi->change_password: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyTextPlain, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'text/plain' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
userId | UserIdSchema | | 

# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
400 | [ApiResponseFor400](#change_password.ApiResponseFor400) | Password was not supplied in the body of the request
403 | [ApiResponseFor403](#change_password.ApiResponseFor403) | The user does not have permission to perform the operation.
404 | [ApiResponseFor404](#change_password.ApiResponseFor404) | User not found in the system.

#### change_password.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### change_password.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### change_password.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_user**
<a id="create_user"></a>
> ApiUser create_user()

Create a new user in the default source.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_users_api
from nexus_sdk.model.api_create_user import ApiCreateUser
from nexus_sdk.model.api_user import ApiUser
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_users_api.SecurityManagementUsersApi(api_client)

    # example passing only optional values
    body = ApiCreateUser(
        user_id="user_id_example",
        first_name="first_name_example",
        last_name="last_name_example",
        email_address="email_address_example",
        password="password_example",
        status="active",
        roles=[
            "roles_example"
        ],
    )
    try:
        # Create a new user in the default source.
        api_response = api_instance.create_user(
            body=body,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementUsersApi->create_user: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiCreateUser**](../../models/ApiCreateUser.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_user.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#create_user.ApiResponseFor400) | Password was not supplied in the body of the request
403 | [ApiResponseFor403](#create_user.ApiResponseFor403) | The user does not have permission to perform the operation.

#### create_user.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiUser**](../../models/ApiUser.md) |  | 


#### create_user.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_user.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_user**
<a id="delete_user"></a>
> delete_user(user_id)

Delete a user.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_users_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_users_api.SecurityManagementUsersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'userId': "userId_example",
    }
    try:
        # Delete a user.
        api_response = api_instance.delete_user(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementUsersApi->delete_user: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
userId | UserIdSchema | | 

# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
400 | [ApiResponseFor400](#delete_user.ApiResponseFor400) | There was problem deleting a user. Consult the response body for more details
403 | [ApiResponseFor403](#delete_user.ApiResponseFor403) | The user does not have permission to perform the operation.
404 | [ApiResponseFor404](#delete_user.ApiResponseFor404) | User or user source not found in the system.

#### delete_user.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_user.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_user.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_users**
<a id="get_users"></a>
> [ApiUser] get_users()

Retrieve a list of users. Note if the source is not 'default' the response is limited to 100 users.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_users_api
from nexus_sdk.model.api_user import ApiUser
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_users_api.SecurityManagementUsersApi(api_client)

    # example passing only optional values
    query_params = {
        'userId': "userId_example",
        'source': "source_example",
    }
    try:
        # Retrieve a list of users. Note if the source is not 'default' the response is limited to 100 users.
        api_response = api_instance.get_users(
            query_params=query_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementUsersApi->get_users: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
userId | UserIdSchema | | optional
source | SourceSchema | | optional


# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SourceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_users.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_users.ApiResponseFor400) | Password was not supplied in the body of the request
403 | [ApiResponseFor403](#get_users.ApiResponseFor403) | The user does not have permission to perform the operation.

#### get_users.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ApiUser**]({{complexTypePrefix}}ApiUser.md) | [**ApiUser**]({{complexTypePrefix}}ApiUser.md) | [**ApiUser**]({{complexTypePrefix}}ApiUser.md) |  | 

#### get_users.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_users.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **reset**
<a id="reset"></a>
> reset(user_idrealm)

Reset the user token for the given user.

Resetting the user token will invalidate the current token and force a new token to be created the next time it is accessed.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_users_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_users_api.SecurityManagementUsersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'userId': "userId_example",
        'realm': "realm_example",
    }
    try:
        # Reset the user token for the given user.
        api_response = api_instance.reset(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementUsersApi->reset: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
userId | UserIdSchema | | 
realm | RealmSchema | | 

# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RealmSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#reset.ApiResponseFor204) | User token successfully reset
400 | [ApiResponseFor400](#reset.ApiResponseFor400) | User tokens are not enabled
403 | [ApiResponseFor403](#reset.ApiResponseFor403) | Insufficient permissions to reset user token
404 | [ApiResponseFor404](#reset.ApiResponseFor404) | User not found

#### reset.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### reset.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### reset.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### reset.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_user**
<a id="update_user"></a>
> update_user(user_id)

Update an existing user.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_users_api
from nexus_sdk.model.api_user import ApiUser
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_users_api.SecurityManagementUsersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'userId': "userId_example",
    }
    try:
        # Update an existing user.
        api_response = api_instance.update_user(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementUsersApi->update_user: %s\n" % e)

    # example passing only optional values
    path_params = {
        'userId': "userId_example",
    }
    body = ApiUser(
        user_id="user_id_example",
        first_name="first_name_example",
        last_name="last_name_example",
        email_address="email_address_example",
        source="source_example",
        status="active",
        read_only=True,
        roles=[
            "roles_example"
        ],
        external_roles=[
            "external_roles_example"
        ],
    )
    try:
        # Update an existing user.
        api_response = api_instance.update_user(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementUsersApi->update_user: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiUser**](../../models/ApiUser.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
userId | UserIdSchema | | 

# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
400 | [ApiResponseFor400](#update_user.ApiResponseFor400) | Password was not supplied in the body of the request
403 | [ApiResponseFor403](#update_user.ApiResponseFor403) | The user does not have permission to perform the operation.
404 | [ApiResponseFor404](#update_user.ApiResponseFor404) | User or user source not found in the system.

#### update_user.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_user.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_user.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

