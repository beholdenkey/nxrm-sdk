# NpmProxyApiRepository

## Properties

| Name                  | Type                                                      | Description                                              | Notes      |
| --------------------- | --------------------------------------------------------- | -------------------------------------------------------- | ---------- |
| **name**              | **str**                                                   | A unique identifier for this repository                  | [optional] |
| **online**            | **bool**                                                  | Whether this repository accepts incoming requests        |
| **storage**           | [**StorageAttributes**](StorageAttributes.md)             |                                                          |
| **cleanup**           | [**CleanupPolicyAttributes**](CleanupPolicyAttributes.md) |                                                          | [optional] |
| **proxy**             | [**ProxyAttributes**](ProxyAttributes.md)                 |                                                          |
| **negative_cache**    | [**NegativeCacheAttributes**](NegativeCacheAttributes.md) |                                                          |
| **http_client**       | [**HttpClientAttributes**](HttpClientAttributes.md)       |                                                          |
| **routing_rule_name** | **str**                                                   | The name of the routing rule assigned to this repository | [optional] |
| **replication**       | [**ReplicationAttributes**](ReplicationAttributes.md)     |                                                          | [optional] |
| **npm**               | [**NpmAttributes**](NpmAttributes.md)                     |                                                          | [optional] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
