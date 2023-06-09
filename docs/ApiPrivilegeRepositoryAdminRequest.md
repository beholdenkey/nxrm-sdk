# ApiPrivilegeRepositoryAdminRequest

## Properties

| Name            | Type          | Description                                                                                                                                                     | Notes      |
| --------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **name**        | **str**       | The name of the privilege. This value cannot be changed.                                                                                                        | [optional] |
| **description** | **str**       |                                                                                                                                                                 | [optional] |
| **actions**     | **list[str]** | A collection of actions to associate with the privilege, using BREAD syntax (browse,read,edit,add,delete,all) as well as &#x27;run&#x27; for script privileges. | [optional] |
| **format**      | **str**       | The repository format (i.e &#x27;nuget&#x27;, &#x27;npm&#x27;) this privilege will grant access to (or \* for all).                                             | [optional] |
| **repository**  | **str**       | The name of the repository this privilege will grant access to (or \* for all).                                                                                 | [optional] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
