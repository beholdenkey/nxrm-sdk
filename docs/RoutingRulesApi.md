# swagger_client.RoutingRulesApi

All URIs are relative to _/service/rest/_

| Method                                                            | HTTP request                        | Description                  |
| ----------------------------------------------------------------- | ----------------------------------- | ---------------------------- |
| [**create_routing_rule**](RoutingRulesApi.md#create_routing_rule) | **POST** /v1/routing-rules          | Create a single routing rule |
| [**delete_routing_rule**](RoutingRulesApi.md#delete_routing_rule) | **DELETE** /v1/routing-rules/{name} | Delete a single routing rule |
| [**get_routing_rule**](RoutingRulesApi.md#get_routing_rule)       | **GET** /v1/routing-rules/{name}    | Get a single routing rule    |
| [**get_routing_rules**](RoutingRulesApi.md#get_routing_rules)     | **GET** /v1/routing-rules           | List routing rules           |
| [**update_routing_rule**](RoutingRulesApi.md#update_routing_rule) | **PUT** /v1/routing-rules/{name}    | Update a single routing rule |

# **create_routing_rule**

> create_routing_rule(body)

Create a single routing rule

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RoutingRulesApi()
body = swagger_client.RoutingRuleXO() # RoutingRuleXO | A routing rule configuration

try:
    # Create a single routing rule
    api_instance.create_routing_rule(body)
except ApiException as e:
    print("Exception when calling RoutingRulesApi->create_routing_rule: %s\n" % e)
```

### Parameters

| Name     | Type                                  | Description                  | Notes |
| -------- | ------------------------------------- | ---------------------------- | ----- |
| **body** | [**RoutingRuleXO**](RoutingRuleXO.md) | A routing rule configuration |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_routing_rule**

> delete_routing_rule(name)

Delete a single routing rule

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RoutingRulesApi()
name = 'name_example' # str | The name of the routing rule to delete

try:
    # Delete a single routing rule
    api_instance.delete_routing_rule(name)
except ApiException as e:
    print("Exception when calling RoutingRulesApi->delete_routing_rule: %s\n" % e)
```

### Parameters

| Name     | Type    | Description                            | Notes |
| -------- | ------- | -------------------------------------- | ----- |
| **name** | **str** | The name of the routing rule to delete |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_routing_rule**

> RoutingRuleXO get_routing_rule(name)

Get a single routing rule

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RoutingRulesApi()
name = 'name_example' # str | The name of the routing rule to get

try:
    # Get a single routing rule
    api_response = api_instance.get_routing_rule(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingRulesApi->get_routing_rule: %s\n" % e)
```

### Parameters

| Name     | Type    | Description                         | Notes |
| -------- | ------- | ----------------------------------- | ----- |
| **name** | **str** | The name of the routing rule to get |

### Return type

[**RoutingRuleXO**](RoutingRuleXO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_routing_rules**

> list[RoutingRuleXO] get_routing_rules()

List routing rules

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RoutingRulesApi()

try:
    # List routing rules
    api_response = api_instance.get_routing_rules()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingRulesApi->get_routing_rules: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**list[RoutingRuleXO]**](RoutingRuleXO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_routing_rule**

> update_routing_rule(body, name)

Update a single routing rule

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RoutingRulesApi()
body = swagger_client.RoutingRuleXO() # RoutingRuleXO | A routing rule configuration
name = 'name_example' # str | The name of the routing rule to update

try:
    # Update a single routing rule
    api_instance.update_routing_rule(body, name)
except ApiException as e:
    print("Exception when calling RoutingRulesApi->update_routing_rule: %s\n" % e)
```

### Parameters

| Name     | Type                                  | Description                            | Notes |
| -------- | ------------------------------------- | -------------------------------------- | ----- |
| **body** | [**RoutingRuleXO**](RoutingRuleXO.md) | A routing rule configuration           |
| **name** | **str**                               | The name of the routing rule to update |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
