<a id="__pageTop"></a>
# nexus_sdk.apis.tags.security_management_jwt_api.SecurityManagementJWTApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reset_secret**](#reset_secret) | **put** /v1/security/jwt | Reset JWT secret (note that session will be expired for the all logged-in users)

# **reset_secret**
<a id="reset_secret"></a>
> reset_secret()

Reset JWT secret (note that session will be expired for the all logged-in users)

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_jwt_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_jwt_api.SecurityManagementJWTApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Reset JWT secret (note that session will be expired for the all logged-in users)
        api_response = api_instance.reset_secret()
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementJWTApi->reset_secret: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
401 | [ApiResponseFor401](#reset_secret.ApiResponseFor401) | Authentication required
403 | [ApiResponseFor403](#reset_secret.ApiResponseFor403) | Insufficient permissions

#### reset_secret.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### reset_secret.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

