<a id="__pageTop"></a>
# nexus_sdk.apis.tags.routing_rules_api.RoutingRulesApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_routing_rule**](#create_routing_rule) | **post** /v1/routing-rules | Create a single routing rule
[**delete_routing_rule**](#delete_routing_rule) | **delete** /v1/routing-rules/{name} | Delete a single routing rule
[**get_routing_rule**](#get_routing_rule) | **get** /v1/routing-rules/{name} | Get a single routing rule
[**get_routing_rules**](#get_routing_rules) | **get** /v1/routing-rules | List routing rules
[**update_routing_rule**](#update_routing_rule) | **put** /v1/routing-rules/{name} | Update a single routing rule

# **create_routing_rule**
<a id="create_routing_rule"></a>
> create_routing_rule(body)

Create a single routing rule

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import routing_rules_api
from nexus_sdk.model.routing_rule_xo import RoutingRuleXO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = routing_rules_api.RoutingRulesApi(api_client)

    # example passing only required values which don't have defaults set
    body = RoutingRuleXO(
        name="e6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        description="description_example",
        mode="BLOCK",
        matchers=[
            "matchers_example"
        ],
    )
    try:
        # Create a single routing rule
        api_response = api_instance.create_routing_rule(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RoutingRulesApi->create_routing_rule: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RoutingRuleXO**](../../models/RoutingRuleXO.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#create_routing_rule.ApiResponseFor204) | Routing rule was successfully created
400 | [ApiResponseFor400](#create_routing_rule.ApiResponseFor400) | A routing rule with the same name already exists or required parameters missing
403 | [ApiResponseFor403](#create_routing_rule.ApiResponseFor403) | Insufficient permissions to create routing rule

#### create_routing_rule.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_routing_rule.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_routing_rule.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_routing_rule**
<a id="delete_routing_rule"></a>
> delete_routing_rule(name)

Delete a single routing rule

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import routing_rules_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = routing_rules_api.RoutingRulesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    try:
        # Delete a single routing rule
        api_response = api_instance.delete_routing_rule(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RoutingRulesApi->delete_routing_rule: %s\n" % e)
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
name | NameSchema | | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_routing_rule.ApiResponseFor204) | Routing rule was successfully deleted
403 | [ApiResponseFor403](#delete_routing_rule.ApiResponseFor403) | Insufficient permissions to delete routing rules
404 | [ApiResponseFor404](#delete_routing_rule.ApiResponseFor404) | Routing rule not found

#### delete_routing_rule.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_routing_rule.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_routing_rule.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_routing_rule**
<a id="get_routing_rule"></a>
> RoutingRuleXO get_routing_rule(name)

Get a single routing rule

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import routing_rules_api
from nexus_sdk.model.routing_rule_xo import RoutingRuleXO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = routing_rules_api.RoutingRulesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    try:
        # Get a single routing rule
        api_response = api_instance.get_routing_rule(
            path_params=path_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RoutingRulesApi->get_routing_rule: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_routing_rule.ApiResponseFor200) | successful operation
403 | [ApiResponseFor403](#get_routing_rule.ApiResponseFor403) | Insufficient permissions to read routing rules
404 | [ApiResponseFor404](#get_routing_rule.ApiResponseFor404) | Routing rule not found

#### get_routing_rule.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RoutingRuleXO**](../../models/RoutingRuleXO.md) |  | 


#### get_routing_rule.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_routing_rule.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_routing_rules**
<a id="get_routing_rules"></a>
> [RoutingRuleXO] get_routing_rules()

List routing rules

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import routing_rules_api
from nexus_sdk.model.routing_rule_xo import RoutingRuleXO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = routing_rules_api.RoutingRulesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List routing rules
        api_response = api_instance.get_routing_rules()
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling RoutingRulesApi->get_routing_rules: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_routing_rules.ApiResponseFor200) | successful operation
403 | [ApiResponseFor403](#get_routing_rules.ApiResponseFor403) | Insufficient permissions to read routing rules

#### get_routing_rules.ApiResponseFor200
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
[**RoutingRuleXO**]({{complexTypePrefix}}RoutingRuleXO.md) | [**RoutingRuleXO**]({{complexTypePrefix}}RoutingRuleXO.md) | [**RoutingRuleXO**]({{complexTypePrefix}}RoutingRuleXO.md) |  | 

#### get_routing_rules.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_routing_rule**
<a id="update_routing_rule"></a>
> update_routing_rule(namebody)

Update a single routing rule

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import routing_rules_api
from nexus_sdk.model.routing_rule_xo import RoutingRuleXO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = routing_rules_api.RoutingRulesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    body = RoutingRuleXO(
        name="e6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        description="description_example",
        mode="BLOCK",
        matchers=[
            "matchers_example"
        ],
    )
    try:
        # Update a single routing rule
        api_response = api_instance.update_routing_rule(
            path_params=path_params,
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling RoutingRulesApi->update_routing_rule: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RoutingRuleXO**](../../models/RoutingRuleXO.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#update_routing_rule.ApiResponseFor204) | Routing rule was successfully updated
400 | [ApiResponseFor400](#update_routing_rule.ApiResponseFor400) | Another routing rule with the same name already exists or required parameters missing
403 | [ApiResponseFor403](#update_routing_rule.ApiResponseFor403) | Insufficient permissions to edit routing rules
404 | [ApiResponseFor404](#update_routing_rule.ApiResponseFor404) | Routing rule not found

#### update_routing_rule.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_routing_rule.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_routing_rule.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_routing_rule.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

