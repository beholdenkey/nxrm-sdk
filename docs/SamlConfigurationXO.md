# SamlConfigurationXO

## Properties

| Name                             | Type     | Description                                                                                               | Notes      |
| -------------------------------- | -------- | --------------------------------------------------------------------------------------------------------- | ---------- |
| **entity_id**                    | **str**  | SAML Service Provider&#x27;s unique identifying URI                                                       | [optional] |
| **idp_metadata**                 | **str**  | SAML Identity Provider Metadata XML                                                                       |
| **username_attribute**           | **str**  | SAML attribute name for the username                                                                      |
| **first_name_attribute**         | **str**  | SAML attribute name for the first name                                                                    | [optional] |
| **last_name_attribute**          | **str**  | SAML attribute name for the last name                                                                     | [optional] |
| **email_attribute**              | **str**  | SAML attribute name for email                                                                             | [optional] |
| **groups_attribute**             | **str**  | SAML attribute name for groups which maps the Identity Provider groups to a Nexus Repository Manager role | [optional] |
| **validate_response_signature**  | **bool** | Validate signatures on responses from Identity Provider                                                   | [optional] |
| **validate_assertion_signature** | **bool** | Validate signatures on assertions from Identity Provider                                                  | [optional] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
