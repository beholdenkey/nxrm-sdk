# MavenProxyRepositoryApiRequest

## Properties

| Name               | Type                                                                                    | Description                                       | Notes      |
| ------------------ | --------------------------------------------------------------------------------------- | ------------------------------------------------- | ---------- |
| **name**           | **str**                                                                                 | A unique identifier for this repository           |
| **online**         | **bool**                                                                                | Whether this repository accepts incoming requests |
| **storage**        | [**StorageAttributes**](StorageAttributes.md)                                           |                                                   |
| **cleanup**        | [**CleanupPolicyAttributes**](CleanupPolicyAttributes.md)                               |                                                   | [optional] |
| **proxy**          | [**ProxyAttributes**](ProxyAttributes.md)                                               |                                                   |
| **negative_cache** | [**NegativeCacheAttributes**](NegativeCacheAttributes.md)                               |                                                   |
| **http_client**    | [**HttpClientAttributesWithPreemptiveAuth**](HttpClientAttributesWithPreemptiveAuth.md) |                                                   |
| **routing_rule**   | **str**                                                                                 |                                                   | [optional] |
| **replication**    | [**ReplicationAttributes**](ReplicationAttributes.md)                                   |                                                   | [optional] |
| **maven**          | [**MavenAttributes**](MavenAttributes.md)                                               |                                                   |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
