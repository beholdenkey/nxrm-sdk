# RoleXOResponse

## Properties

| Name            | Type          | Description                                                                                     | Notes      |
| --------------- | ------------- | ----------------------------------------------------------------------------------------------- | ---------- |
| **id**          | **str**       | The id of the role.                                                                             | [optional] |
| **source**      | **str**       | The user source which is the origin of this role.                                               | [optional] |
| **name**        | **str**       | The name of the role.                                                                           | [optional] |
| **description** | **str**       | The description of this role.                                                                   | [optional] |
| **read_only**   | **bool**      | Indicates whether the role can be changed. The system will ignore any supplied external values. | [optional] |
| **privileges**  | **list[str]** | The list of privileges assigned to this role.                                                   | [optional] |
| **roles**       | **list[str]** | The list of roles assigned to this role.                                                        | [optional] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
