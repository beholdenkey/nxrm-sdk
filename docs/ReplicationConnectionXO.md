# ReplicationConnectionXO

## Properties

| Name                              | Type          | Description                                                                                      | Notes      |
| --------------------------------- | ------------- | ------------------------------------------------------------------------------------------------ | ---------- |
| **id**                            | **str**       | Connection Id                                                                                    | [optional] |
| **name**                          | **str**       | Replication Connection Name                                                                      |
| **source_repository_name**        | **str**       | Source Repository Name                                                                           |
| **destination_instance_url**      | **str**       | Destination Instance URL                                                                         |
| **destination_instance_username** | **str**       | Destination Instance Username                                                                    | [optional] |
| **destination_instance_password** | **str**       | Destination Instance Password                                                                    | [optional] |
| **destination_repository_name**   | **str**       | Destination Repository Name                                                                      |
| **content_regexes**               | **list[str]** | Regular expressions used to filter the repository content that is replicated                     | [optional] |
| **include_existing_content**      | **bool**      | Boolean used to configure if a replication connection should include existing content            | [optional] |
| **use_trust_store**               | **bool**      | Boolean used to configure if a replication connection should use the Nexus Repository Truststore | [optional] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
