# DockerHostedRepositoryApiRequest

## Properties

| Name          | Type                                                                  | Description                                       | Notes      |
| ------------- | --------------------------------------------------------------------- | ------------------------------------------------- | ---------- |
| **name**      | **str**                                                               | A unique identifier for this repository           |
| **online**    | **bool**                                                              | Whether this repository accepts incoming requests |
| **storage**   | [**DockerHostedStorageAttributes**](DockerHostedStorageAttributes.md) |                                                   |
| **cleanup**   | [**CleanupPolicyAttributes**](CleanupPolicyAttributes.md)             |                                                   | [optional] |
| **component** | [**ComponentAttributes**](ComponentAttributes.md)                     |                                                   | [optional] |
| **docker**    | [**DockerAttributes**](DockerAttributes.md)                           |                                                   |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
