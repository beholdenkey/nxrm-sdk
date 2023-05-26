import typing_extensions

from nexus_sdk.apis.tags import TagValues
from nexus_sdk.apis.tags.assets_api import AssetsApi
from nexus_sdk.apis.tags.azure_blob_store_api import AzureBlobStoreApi
from nexus_sdk.apis.tags.blob_store_api import BlobStoreApi
from nexus_sdk.apis.tags.components_api import ComponentsApi
from nexus_sdk.apis.tags.content_selectors_api import ContentSelectorsApi
from nexus_sdk.apis.tags.email_api import EmailApi
from nexus_sdk.apis.tags.formats_api import FormatsApi
from nexus_sdk.apis.tags.lifecycle_api import LifecycleApi
from nexus_sdk.apis.tags.manage_iq_server_configuration_api import (
    ManageIQServerConfigurationApi,
)
from nexus_sdk.apis.tags.product_licensing_api import ProductLicensingApi
from nexus_sdk.apis.tags.read_only_api import ReadOnlyApi
from nexus_sdk.apis.tags.replication_api import ReplicationApi
from nexus_sdk.apis.tags.repository_management_api import RepositoryManagementApi
from nexus_sdk.apis.tags.routing_rules_api import RoutingRulesApi
from nexus_sdk.apis.tags.script_api import ScriptApi
from nexus_sdk.apis.tags.search_api import SearchApi
from nexus_sdk.apis.tags.security_atlassian_crowd_api import SecurityAtlassianCrowdApi
from nexus_sdk.apis.tags.security_certificates_api import SecurityCertificatesApi
from nexus_sdk.apis.tags.security_management_anonymous_access_api import (
    SecurityManagementAnonymousAccessApi,
)
from nexus_sdk.apis.tags.security_management_api import SecurityManagementApi
from nexus_sdk.apis.tags.security_management_jwt_api import SecurityManagementJWTApi
from nexus_sdk.apis.tags.security_management_ldap_api import SecurityManagementLDAPApi
from nexus_sdk.apis.tags.security_management_privileges_api import (
    SecurityManagementPrivilegesApi,
)
from nexus_sdk.apis.tags.security_management_realms_api import (
    SecurityManagementRealmsApi,
)
from nexus_sdk.apis.tags.security_management_roles_api import SecurityManagementRolesApi
from nexus_sdk.apis.tags.security_management_saml_api import SecurityManagementSAMLApi
from nexus_sdk.apis.tags.security_management_user_tokens_api import (
    SecurityManagementUserTokensApi,
)
from nexus_sdk.apis.tags.security_management_users_api import SecurityManagementUsersApi
from nexus_sdk.apis.tags.staging_api import StagingApi
from nexus_sdk.apis.tags.status_api import StatusApi
from nexus_sdk.apis.tags.support_api import SupportApi
from nexus_sdk.apis.tags.tags_api import TagsApi
from nexus_sdk.apis.tags.tasks_api import TasksApi

TagToApi = typing_extensions.TypedDict(
    "TagToApi",
    {
        TagValues.SECURITY_MANAGEMENT_ANONYMOUS_ACCESS: SecurityManagementAnonymousAccessApi,
        TagValues.SECURITY_MANAGEMENT: SecurityManagementApi,
        TagValues.SECURITY_MANAGEMENT_USERS: SecurityManagementUsersApi,
        TagValues.SECURITY_MANAGEMENT_JWT: SecurityManagementJWTApi,
        TagValues.SECURITY_MANAGEMENT_PRIVILEGES: SecurityManagementPrivilegesApi,
        TagValues.SECURITY_MANAGEMENT_REALMS: SecurityManagementRealmsApi,
        TagValues.SECURITY_MANAGEMENT_ROLES: SecurityManagementRolesApi,
        TagValues.TASKS: TasksApi,
        TagValues.BLOB_STORE: BlobStoreApi,
        TagValues.LIFECYCLE: LifecycleApi,
        TagValues.READONLY: ReadOnlyApi,
        TagValues.SECURITY_CERTIFICATES: SecurityCertificatesApi,
        TagValues.ASSETS: AssetsApi,
        TagValues.COMPONENTS: ComponentsApi,
        TagValues.REPOSITORY_MANAGEMENT: RepositoryManagementApi,
        TagValues.CONTENT_SELECTORS: ContentSelectorsApi,
        TagValues.ROUTING_RULES: RoutingRulesApi,
        TagValues.SEARCH: SearchApi,
        TagValues.FORMATS: FormatsApi,
        TagValues.SCRIPT: ScriptApi,
        TagValues.EMAIL: EmailApi,
        TagValues.STATUS: StatusApi,
        TagValues.SUPPORT: SupportApi,
        TagValues.SECURITY_MANAGEMENT_LDAP: SecurityManagementLDAPApi,
        TagValues.TAGS: TagsApi,
        TagValues.MANAGE_IQ_SERVER_CONFIGURATION: ManageIQServerConfigurationApi,
        TagValues.PRODUCT_LICENSING: ProductLicensingApi,
        TagValues.SECURITY_ATLASSIAN_CROWD: SecurityAtlassianCrowdApi,
        TagValues.SECURITY_MANAGEMENT_USER_TOKENS: SecurityManagementUserTokensApi,
        TagValues.REPLICATION: ReplicationApi,
        TagValues.STAGING: StagingApi,
        TagValues.AZURE_BLOB_STORE: AzureBlobStoreApi,
        TagValues.SECURITY_MANAGEMENT_SAML: SecurityManagementSAMLApi,
    },
)

tag_to_api = TagToApi(
    {
        TagValues.SECURITY_MANAGEMENT_ANONYMOUS_ACCESS: SecurityManagementAnonymousAccessApi,
        TagValues.SECURITY_MANAGEMENT: SecurityManagementApi,
        TagValues.SECURITY_MANAGEMENT_USERS: SecurityManagementUsersApi,
        TagValues.SECURITY_MANAGEMENT_JWT: SecurityManagementJWTApi,
        TagValues.SECURITY_MANAGEMENT_PRIVILEGES: SecurityManagementPrivilegesApi,
        TagValues.SECURITY_MANAGEMENT_REALMS: SecurityManagementRealmsApi,
        TagValues.SECURITY_MANAGEMENT_ROLES: SecurityManagementRolesApi,
        TagValues.TASKS: TasksApi,
        TagValues.BLOB_STORE: BlobStoreApi,
        TagValues.LIFECYCLE: LifecycleApi,
        TagValues.READONLY: ReadOnlyApi,
        TagValues.SECURITY_CERTIFICATES: SecurityCertificatesApi,
        TagValues.ASSETS: AssetsApi,
        TagValues.COMPONENTS: ComponentsApi,
        TagValues.REPOSITORY_MANAGEMENT: RepositoryManagementApi,
        TagValues.CONTENT_SELECTORS: ContentSelectorsApi,
        TagValues.ROUTING_RULES: RoutingRulesApi,
        TagValues.SEARCH: SearchApi,
        TagValues.FORMATS: FormatsApi,
        TagValues.SCRIPT: ScriptApi,
        TagValues.EMAIL: EmailApi,
        TagValues.STATUS: StatusApi,
        TagValues.SUPPORT: SupportApi,
        TagValues.SECURITY_MANAGEMENT_LDAP: SecurityManagementLDAPApi,
        TagValues.TAGS: TagsApi,
        TagValues.MANAGE_IQ_SERVER_CONFIGURATION: ManageIQServerConfigurationApi,
        TagValues.PRODUCT_LICENSING: ProductLicensingApi,
        TagValues.SECURITY_ATLASSIAN_CROWD: SecurityAtlassianCrowdApi,
        TagValues.SECURITY_MANAGEMENT_USER_TOKENS: SecurityManagementUserTokensApi,
        TagValues.REPLICATION: ReplicationApi,
        TagValues.STAGING: StagingApi,
        TagValues.AZURE_BLOB_STORE: AzureBlobStoreApi,
        TagValues.SECURITY_MANAGEMENT_SAML: SecurityManagementSAMLApi,
    }
)
