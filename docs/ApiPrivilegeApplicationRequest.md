# ApiPrivilegeApplicationRequest

## Properties

| Name            | Type          | Description                                                                                                                                                                                                                                                        | Notes      |
| --------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| **name**        | **str**       | The name of the privilege. This value cannot be changed.                                                                                                                                                                                                           | [optional] |
| **description** | **str**       |                                                                                                                                                                                                                                                                    | [optional] |
| **actions**     | **list[str]** | A collection of actions to associate with the privilege, using BREAD syntax (browse,read,edit,add,delete,all) as well as &#x27;run&#x27; for script privileges.                                                                                                    | [optional] |
| **domain**      | **str**       | The domain (i.e. &#x27;blobstores&#x27;, &#x27;capabilities&#x27; or even &#x27;\*&#x27; for all) that this privilege is granting access to. Note that creating new privileges with a domain is only necessary when using plugins that define their own domain(s). | [optional] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
