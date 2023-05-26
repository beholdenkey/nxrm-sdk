<a id="__pageTop"></a>

# nexus_sdk.apis.tags.security_management_saml_api.SecurityManagementSAMLApi

All URIs are relative to _http://localhost/service/rest_

| Method                                                                            | HTTP request                       | Description                                            |
| --------------------------------------------------------------------------------- | ---------------------------------- | ------------------------------------------------------ |
| [**delete_saml_configuration**](#delete_saml_configuration)                       | **delete** /v1/security/saml       | Delete SAML configuration                              |
| [**get_metadata**](#get_metadata)                                                 | **get** /v1/security/saml/metadata | Get service provider metadata XML document             |
| [**get_public_certificate_in_pem_format**](#get_public_certificate_in_pem_format) | **get** /v1/security/saml/pem      | Get service provider signing certificate in PEM format |
| [**get_saml_configuration**](#get_saml_configuration)                             | **get** /v1/security/saml          | Get SAML configuration                                 |
| [**put_saml_configuration**](#put_saml_configuration)                             | **put** /v1/security/saml          | Create or update SAML configuration                    |

# **delete_saml_configuration**

<a id="delete_saml_configuration"></a>

> delete_saml_configuration()

Delete SAML configuration

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_saml_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_saml_api.SecurityManagementSAMLApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Delete SAML configuration
        api_response = api_instance.delete_saml_configuration()
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementSAMLApi->delete_saml_configuration: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return Types, Responses

| Code | Class                                                             | Description                                                 |
| ---- | ----------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                      | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#delete_saml_configuration.ApiResponseFor204) | SAML configuration deleted                                  |
| 401  | [ApiResponseFor401](#delete_saml_configuration.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#delete_saml_configuration.ApiResponseFor403) | Insufficient permissions                                    |

#### delete_saml_configuration.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_saml_configuration.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_saml_configuration.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_metadata**

<a id="get_metadata"></a>

> get_metadata()

Get service provider metadata XML document

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_saml_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_saml_api.SecurityManagementSAMLApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get service provider metadata XML document
        api_response = api_instance.get_metadata()
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementSAMLApi->get_metadata: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return Types, Responses

| Code | Class                                                | Description                                                 |
| ---- | ---------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization         | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_metadata.ApiResponseFor200) | Metadata Returned                                           |
| 401  | [ApiResponseFor401](#get_metadata.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#get_metadata.ApiResponseFor403) | Insufficient permissions                                    |
| 404  | [ApiResponseFor404](#get_metadata.ApiResponseFor404) | Metadata not found                                          |

#### get_metadata.ApiResponseFor200

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_metadata.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_metadata.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_metadata.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_public_certificate_in_pem_format**

<a id="get_public_certificate_in_pem_format"></a>

> get_public_certificate_in_pem_format()

Get service provider signing certificate in PEM format

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_saml_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_saml_api.SecurityManagementSAMLApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get service provider signing certificate in PEM format
        api_response = api_instance.get_public_certificate_in_pem_format()
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementSAMLApi->get_public_certificate_in_pem_format: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return Types, Responses

| Code | Class                                                                        | Description                                                 |
| ---- | ---------------------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                                 | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_public_certificate_in_pem_format.ApiResponseFor200) | PEM file Returned                                           |
| 401  | [ApiResponseFor401](#get_public_certificate_in_pem_format.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#get_public_certificate_in_pem_format.ApiResponseFor403) | Insufficient permissions                                    |
| 404  | [ApiResponseFor404](#get_public_certificate_in_pem_format.ApiResponseFor404) | PEM file not found                                          |

#### get_public_certificate_in_pem_format.ApiResponseFor200

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_public_certificate_in_pem_format.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_public_certificate_in_pem_format.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_public_certificate_in_pem_format.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_saml_configuration**

<a id="get_saml_configuration"></a>

> get_saml_configuration()

Get SAML configuration

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_saml_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_saml_api.SecurityManagementSAMLApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get SAML configuration
        api_response = api_instance.get_saml_configuration()
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementSAMLApi->get_saml_configuration: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return Types, Responses

| Code | Class                                                          | Description                                                 |
| ---- | -------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                   | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_saml_configuration.ApiResponseFor200) | SAML configuration returned                                 |
| 401  | [ApiResponseFor401](#get_saml_configuration.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#get_saml_configuration.ApiResponseFor403) | Insufficient permissions                                    |
| 404  | [ApiResponseFor404](#get_saml_configuration.ApiResponseFor404) | SAML configuration not found                                |

#### get_saml_configuration.ApiResponseFor200

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_saml_configuration.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_saml_configuration.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_saml_configuration.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **put_saml_configuration**

<a id="put_saml_configuration"></a>

> put_saml_configuration()

Create or update SAML configuration

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_management_saml_api
from nexus_sdk.model.saml_configuration_xo import SamlConfigurationXO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_management_saml_api.SecurityManagementSAMLApi(api_client)

    # example passing only optional values
    body = SamlConfigurationXO(
        entity_id="entity_id_example",
        idp_metadata="idp_metadata_example",
        username_attribute="username_attribute_example",
        first_name_attribute="first_name_attribute_example",
        last_name_attribute="last_name_attribute_example",
        email_attribute="email_attribute_example",
        groups_attribute="groups_attribute_example",
        validate_response_signature=True,
        validate_assertion_signature=True,
    )
    try:
        # Create or update SAML configuration
        api_response = api_instance.put_saml_configuration(
            body=body,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityManagementSAMLApi->put_saml_configuration: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                           | Description | Notes |
| -------------------------------------------------------------- | ----------- | ----- |
| [**SamlConfigurationXO**](../../models/SamlConfigurationXO.md) |             |

### Return Types, Responses

| Code | Class                                                          | Description                                                 |
| ---- | -------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                   | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#put_saml_configuration.ApiResponseFor201) | SAML configuration created                                  |
| 204  | [ApiResponseFor204](#put_saml_configuration.ApiResponseFor204) | SAML configuration updated                                  |
| 401  | [ApiResponseFor401](#put_saml_configuration.ApiResponseFor401) | Authentication required                                     |
| 403  | [ApiResponseFor403](#put_saml_configuration.ApiResponseFor403) | Insufficient permissions                                    |
| 404  | [ApiResponseFor404](#put_saml_configuration.ApiResponseFor404) | SAML configuration not found                                |

#### put_saml_configuration.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### put_saml_configuration.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### put_saml_configuration.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### put_saml_configuration.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### put_saml_configuration.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
