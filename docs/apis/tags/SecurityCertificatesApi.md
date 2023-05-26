<a id="__pageTop"></a>

# nexus_sdk.apis.tags.security_certificates_api.SecurityCertificatesApi

All URIs are relative to _http://localhost/service/rest_

| Method                                                            | HTTP request                                | Description                                                         |
| ----------------------------------------------------------------- | ------------------------------------------- | ------------------------------------------------------------------- |
| [**add_certificate**](#add_certificate)                           | **post** /v1/security/ssl/truststore        | Add a certificate to the trust store.                               |
| [**get_trust_store_certificates**](#get_trust_store_certificates) | **get** /v1/security/ssl/truststore         | Retrieve a list of certificates added to the trust store.           |
| [**remove_certificate**](#remove_certificate)                     | **delete** /v1/security/ssl/truststore/{id} | Remove a certificate in the trust store.                            |
| [**retrieve_certificate**](#retrieve_certificate)                 | **get** /v1/security/ssl                    | Helper method to retrieve certificate details from a remote system. |

# **add_certificate**

<a id="add_certificate"></a>

> ApiCertificate add_certificate()

Add a certificate to the trust store.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_certificates_api
from nexus_sdk.model.api_certificate import ApiCertificate
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_certificates_api.SecurityCertificatesApi(api_client)

    # example passing only optional values
    body = "body_example"
    try:
        # Add a certificate to the trust store.
        api_response = api_instance.add_certificate(
            body=body,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityCertificatesApi->add_certificate: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBody, Unset]        | optional, default is unset        |
| content_type         | str                                              | optional, default is '_/_'        | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBody

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                   | Description                                                     |
| ---- | ------------------------------------------------------- | --------------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization            | When skip_deserialization is True this response is returned     |
| 201  | [ApiResponseFor201](#add_certificate.ApiResponseFor201) | The certificate was successfully added.                         |
| 403  | [ApiResponseFor403](#add_certificate.ApiResponseFor403) | Insufficient permissions to add certificate to the trust store. |
| 409  | [ApiResponseFor409](#add_certificate.ApiResponseFor409) | The certificate already exists in the system.                   |

#### add_certificate.ApiResponseFor201

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson

| Type                                                 | Description | Notes |
| ---------------------------------------------------- | ----------- | ----- |
| [**ApiCertificate**](../../models/ApiCertificate.md) |             |

#### add_certificate.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### add_certificate.ApiResponseFor409

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_trust_store_certificates**

<a id="get_trust_store_certificates"></a>

> [ApiCertificate] get_trust_store_certificates()

Retrieve a list of certificates added to the trust store.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_certificates_api
from nexus_sdk.model.api_certificate import ApiCertificate
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_certificates_api.SecurityCertificatesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve a list of certificates added to the trust store.
        api_response = api_instance.get_trust_store_certificates()
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityCertificatesApi->get_trust_store_certificates: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return Types, Responses

| Code | Class                                                                | Description                                                       |
| ---- | -------------------------------------------------------------------- | ----------------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                         | When skip_deserialization is True this response is returned       |
| 200  | [ApiResponseFor200](#get_trust_store_certificates.ApiResponseFor200) | successful operation                                              |
| 403  | [ApiResponseFor403](#get_trust_store_certificates.ApiResponseFor403) | Insufficient permissions to list certificates in the trust store. |

#### get_trust_store_certificates.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                                                   | Input Type                                                   | Accessed Type                                                | Description | Notes |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ----------- | ----- |
| [**ApiCertificate**]({{complexTypePrefix}}ApiCertificate.md) | [**ApiCertificate**]({{complexTypePrefix}}ApiCertificate.md) | [**ApiCertificate**]({{complexTypePrefix}}ApiCertificate.md) |             |

#### get_trust_store_certificates.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **remove_certificate**

<a id="remove_certificate"></a>

> remove_certificate(id)

Remove a certificate in the trust store.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_certificates_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_certificates_api.SecurityCertificatesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Remove a certificate in the trust store.
        api_response = api_instance.remove_certificate(
            path_params=path_params,
        )
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityCertificatesApi->remove_certificate: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description      | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                  |
| stream               | bool                                             | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None  | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name | Type     | Description | Notes |
| ---- | -------- | ----------- | ----- |
| id   | IdSchema |             |

# IdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                      | Description                                                         |
| ---- | ---------------------------------------------------------- | ------------------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization               | When skip_deserialization is True this response is returned         |
| 403  | [ApiResponseFor403](#remove_certificate.ApiResponseFor403) | Insufficient permissions to remove certificate from the trust store |

#### remove_certificate.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **retrieve_certificate**

<a id="retrieve_certificate"></a>

> ApiCertificate retrieve_certificate(host)

Helper method to retrieve certificate details from a remote system.

### Example

```python
import nexus_sdk
from nexus_sdk.apis.tags import security_certificates_api
from nexus_sdk.model.api_certificate import ApiCertificate
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/service/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "http://localhost/service/rest"
)

# Enter a context with an instance of the API client
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_certificates_api.SecurityCertificatesApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'host': "host_example",
    }
    try:
        # Helper method to retrieve certificate details from a remote system.
        api_response = api_instance.retrieve_certificate(
            query_params=query_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityCertificatesApi->retrieve_certificate: %s\n" % e)

    # example passing only optional values
    query_params = {
        'host': "host_example",
        'port': 443,
        'protocolHint': "protocolHint_example",
    }
    try:
        # Helper method to retrieve certificate details from a remote system.
        api_response = api_instance.retrieve_certificate(
            query_params=query_params,
        )
        pprint(api_response)
    except nexus_sdk.ApiException as e:
        print("Exception when calling SecurityCertificatesApi->retrieve_certificate: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| query_params         | RequestQueryParams                               |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### query_params

#### RequestQueryParams

| Name         | Type               | Description | Notes    |
| ------------ | ------------------ | ----------- | -------- |
| host         | HostSchema         |             |
| port         | PortSchema         |             | optional |
| protocolHint | ProtocolHintSchema |             | optional |

# HostSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# PortSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                                                                                 |
| --------------------- | ---------------- | ----------- | ------------------------------------------------------------------------------------- |
| decimal.Decimal, int, | decimal.Decimal, |             | if omitted the server will use the default value of 443value must be a 32 bit integer |

# ProtocolHintSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                        | Description                                                        |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------------ |
| n/a  | api_client.ApiResponseWithoutDeserialization                 | When skip_deserialization is True this response is returned        |
| 200  | [ApiResponseFor200](#retrieve_certificate.ApiResponseFor200) | successful operation                                               |
| 400  | [ApiResponseFor400](#retrieve_certificate.ApiResponseFor400) | A certificate could not be retrieved, see the message for details. |
| 403  | [ApiResponseFor403](#retrieve_certificate.ApiResponseFor403) | Insufficient permissions to retrieve remote certificate.           |

#### retrieve_certificate.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                 | Description | Notes |
| ---------------------------------------------------- | ----------- | ----- |
| [**ApiCertificate**](../../models/ApiCertificate.md) |             |

#### retrieve_certificate.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### retrieve_certificate.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
