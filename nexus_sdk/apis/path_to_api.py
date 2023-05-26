import typing_extensions

from nexus_sdk.apis.paths.beta_replication_connection import BetaReplicationConnection
from nexus_sdk.apis.paths.beta_replication_connection_name import (
    BetaReplicationConnectionName,
)
from nexus_sdk.apis.paths.beta_replicationtarget_repository_enable import (
    BetaReplicationtargetRepositoryEnable,
)
from nexus_sdk.apis.paths.beta_replicationtarget_repository_repository_name_enable import (
    BetaReplicationtargetRepositoryRepositoryNameEnable,
)
from nexus_sdk.apis.paths.v1_assets import V1Assets
from nexus_sdk.apis.paths.v1_assets_id import V1AssetsId
from nexus_sdk.apis.paths.v1_azureblobstore_test_connection import (
    V1AzureblobstoreTestConnection,
)
from nexus_sdk.apis.paths.v1_blobstores import V1Blobstores
from nexus_sdk.apis.paths.v1_blobstores_azure import V1BlobstoresAzure
from nexus_sdk.apis.paths.v1_blobstores_azure_name import V1BlobstoresAzureName
from nexus_sdk.apis.paths.v1_blobstores_file import V1BlobstoresFile
from nexus_sdk.apis.paths.v1_blobstores_file_name import V1BlobstoresFileName
from nexus_sdk.apis.paths.v1_blobstores_group import V1BlobstoresGroup
from nexus_sdk.apis.paths.v1_blobstores_group_convert_name_new_name_for_original import (
    V1BlobstoresGroupConvertNameNewNameForOriginal,
)
from nexus_sdk.apis.paths.v1_blobstores_group_name import V1BlobstoresGroupName
from nexus_sdk.apis.paths.v1_blobstores_name import V1BlobstoresName
from nexus_sdk.apis.paths.v1_blobstores_name_quota_status import (
    V1BlobstoresNameQuotaStatus,
)
from nexus_sdk.apis.paths.v1_blobstores_s3 import V1BlobstoresS3
from nexus_sdk.apis.paths.v1_blobstores_s3_name import V1BlobstoresS3Name
from nexus_sdk.apis.paths.v1_components import V1Components
from nexus_sdk.apis.paths.v1_components_id import V1ComponentsId
from nexus_sdk.apis.paths.v1_email import V1Email
from nexus_sdk.apis.paths.v1_email_verify import V1EmailVerify
from nexus_sdk.apis.paths.v1_formats_format_upload_specs import (
    V1FormatsFormatUploadSpecs,
)
from nexus_sdk.apis.paths.v1_formats_upload_specs import V1FormatsUploadSpecs
from nexus_sdk.apis.paths.v1_iq import V1Iq
from nexus_sdk.apis.paths.v1_iq_disable import V1IqDisable
from nexus_sdk.apis.paths.v1_iq_enable import V1IqEnable
from nexus_sdk.apis.paths.v1_iq_verify_connection import V1IqVerifyConnection
from nexus_sdk.apis.paths.v1_lifecycle_bounce import V1LifecycleBounce
from nexus_sdk.apis.paths.v1_lifecycle_phase import V1LifecyclePhase
from nexus_sdk.apis.paths.v1_read_only import V1ReadOnly
from nexus_sdk.apis.paths.v1_read_only_force_release import V1ReadOnlyForceRelease
from nexus_sdk.apis.paths.v1_read_only_freeze import V1ReadOnlyFreeze
from nexus_sdk.apis.paths.v1_read_only_release import V1ReadOnlyRelease
from nexus_sdk.apis.paths.v1_repositories import V1Repositories
from nexus_sdk.apis.paths.v1_repositories_apt_hosted import V1RepositoriesAptHosted
from nexus_sdk.apis.paths.v1_repositories_apt_hosted_repository_name import (
    V1RepositoriesAptHostedRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_apt_proxy import V1RepositoriesAptProxy
from nexus_sdk.apis.paths.v1_repositories_apt_proxy_repository_name import (
    V1RepositoriesAptProxyRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_bower_group import V1RepositoriesBowerGroup
from nexus_sdk.apis.paths.v1_repositories_bower_group_repository_name import (
    V1RepositoriesBowerGroupRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_bower_hosted import V1RepositoriesBowerHosted
from nexus_sdk.apis.paths.v1_repositories_bower_hosted_repository_name import (
    V1RepositoriesBowerHostedRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_bower_proxy import V1RepositoriesBowerProxy
from nexus_sdk.apis.paths.v1_repositories_bower_proxy_repository_name import (
    V1RepositoriesBowerProxyRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_cocoapods_proxy import (
    V1RepositoriesCocoapodsProxy,
)
from nexus_sdk.apis.paths.v1_repositories_cocoapods_proxy_repository_name import (
    V1RepositoriesCocoapodsProxyRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_conan_proxy import V1RepositoriesConanProxy
from nexus_sdk.apis.paths.v1_repositories_conan_proxy_repository_name import (
    V1RepositoriesConanProxyRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_conda_proxy import V1RepositoriesCondaProxy
from nexus_sdk.apis.paths.v1_repositories_conda_proxy_repository_name import (
    V1RepositoriesCondaProxyRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_docker_group import V1RepositoriesDockerGroup
from nexus_sdk.apis.paths.v1_repositories_docker_group_repository_name import (
    V1RepositoriesDockerGroupRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_docker_hosted import (
    V1RepositoriesDockerHosted,
)
from nexus_sdk.apis.paths.v1_repositories_docker_hosted_repository_name import (
    V1RepositoriesDockerHostedRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_docker_proxy import V1RepositoriesDockerProxy
from nexus_sdk.apis.paths.v1_repositories_docker_proxy_repository_name import (
    V1RepositoriesDockerProxyRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_gitlfs_hosted import (
    V1RepositoriesGitlfsHosted,
)
from nexus_sdk.apis.paths.v1_repositories_gitlfs_hosted_repository_name import (
    V1RepositoriesGitlfsHostedRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_go_group import V1RepositoriesGoGroup
from nexus_sdk.apis.paths.v1_repositories_go_group_repository_name import (
    V1RepositoriesGoGroupRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_go_proxy import V1RepositoriesGoProxy
from nexus_sdk.apis.paths.v1_repositories_go_proxy_repository_name import (
    V1RepositoriesGoProxyRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_helm_hosted import V1RepositoriesHelmHosted
from nexus_sdk.apis.paths.v1_repositories_helm_hosted_repository_name import (
    V1RepositoriesHelmHostedRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_helm_proxy import V1RepositoriesHelmProxy
from nexus_sdk.apis.paths.v1_repositories_helm_proxy_repository_name import (
    V1RepositoriesHelmProxyRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_maven_group import V1RepositoriesMavenGroup
from nexus_sdk.apis.paths.v1_repositories_maven_group_repository_name import (
    V1RepositoriesMavenGroupRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_maven_hosted import V1RepositoriesMavenHosted
from nexus_sdk.apis.paths.v1_repositories_maven_hosted_repository_name import (
    V1RepositoriesMavenHostedRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_maven_proxy import V1RepositoriesMavenProxy
from nexus_sdk.apis.paths.v1_repositories_maven_proxy_repository_name import (
    V1RepositoriesMavenProxyRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_npm_group import V1RepositoriesNpmGroup
from nexus_sdk.apis.paths.v1_repositories_npm_group_repository_name import (
    V1RepositoriesNpmGroupRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_npm_hosted import V1RepositoriesNpmHosted
from nexus_sdk.apis.paths.v1_repositories_npm_hosted_repository_name import (
    V1RepositoriesNpmHostedRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_npm_proxy import V1RepositoriesNpmProxy
from nexus_sdk.apis.paths.v1_repositories_npm_proxy_repository_name import (
    V1RepositoriesNpmProxyRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_nuget_group import V1RepositoriesNugetGroup
from nexus_sdk.apis.paths.v1_repositories_nuget_group_repository_name import (
    V1RepositoriesNugetGroupRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_nuget_hosted import V1RepositoriesNugetHosted
from nexus_sdk.apis.paths.v1_repositories_nuget_hosted_repository_name import (
    V1RepositoriesNugetHostedRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_nuget_proxy import V1RepositoriesNugetProxy
from nexus_sdk.apis.paths.v1_repositories_nuget_proxy_repository_name import (
    V1RepositoriesNugetProxyRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_p2_proxy import V1RepositoriesP2Proxy
from nexus_sdk.apis.paths.v1_repositories_p2_proxy_repository_name import (
    V1RepositoriesP2ProxyRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_pypi_group import V1RepositoriesPypiGroup
from nexus_sdk.apis.paths.v1_repositories_pypi_group_repository_name import (
    V1RepositoriesPypiGroupRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_pypi_hosted import V1RepositoriesPypiHosted
from nexus_sdk.apis.paths.v1_repositories_pypi_hosted_repository_name import (
    V1RepositoriesPypiHostedRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_pypi_proxy import V1RepositoriesPypiProxy
from nexus_sdk.apis.paths.v1_repositories_pypi_proxy_repository_name import (
    V1RepositoriesPypiProxyRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_r_group import V1RepositoriesRGroup
from nexus_sdk.apis.paths.v1_repositories_r_group_repository_name import (
    V1RepositoriesRGroupRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_r_hosted import V1RepositoriesRHosted
from nexus_sdk.apis.paths.v1_repositories_r_hosted_repository_name import (
    V1RepositoriesRHostedRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_r_proxy import V1RepositoriesRProxy
from nexus_sdk.apis.paths.v1_repositories_r_proxy_repository_name import (
    V1RepositoriesRProxyRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_raw_group import V1RepositoriesRawGroup
from nexus_sdk.apis.paths.v1_repositories_raw_group_repository_name import (
    V1RepositoriesRawGroupRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_raw_hosted import V1RepositoriesRawHosted
from nexus_sdk.apis.paths.v1_repositories_raw_hosted_repository_name import (
    V1RepositoriesRawHostedRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_raw_proxy import V1RepositoriesRawProxy
from nexus_sdk.apis.paths.v1_repositories_raw_proxy_repository_name import (
    V1RepositoriesRawProxyRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_repository_name import (
    V1RepositoriesRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_repository_name_health_check import (
    V1RepositoriesRepositoryNameHealthCheck,
)
from nexus_sdk.apis.paths.v1_repositories_repository_name_invalidate_cache import (
    V1RepositoriesRepositoryNameInvalidateCache,
)
from nexus_sdk.apis.paths.v1_repositories_repository_name_rebuild_index import (
    V1RepositoriesRepositoryNameRebuildIndex,
)
from nexus_sdk.apis.paths.v1_repositories_rubygems_group import (
    V1RepositoriesRubygemsGroup,
)
from nexus_sdk.apis.paths.v1_repositories_rubygems_group_repository_name import (
    V1RepositoriesRubygemsGroupRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_rubygems_hosted import (
    V1RepositoriesRubygemsHosted,
)
from nexus_sdk.apis.paths.v1_repositories_rubygems_hosted_repository_name import (
    V1RepositoriesRubygemsHostedRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_rubygems_proxy import (
    V1RepositoriesRubygemsProxy,
)
from nexus_sdk.apis.paths.v1_repositories_rubygems_proxy_repository_name import (
    V1RepositoriesRubygemsProxyRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_yum_group import V1RepositoriesYumGroup
from nexus_sdk.apis.paths.v1_repositories_yum_group_repository_name import (
    V1RepositoriesYumGroupRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_yum_hosted import V1RepositoriesYumHosted
from nexus_sdk.apis.paths.v1_repositories_yum_hosted_repository_name import (
    V1RepositoriesYumHostedRepositoryName,
)
from nexus_sdk.apis.paths.v1_repositories_yum_proxy import V1RepositoriesYumProxy
from nexus_sdk.apis.paths.v1_repositories_yum_proxy_repository_name import (
    V1RepositoriesYumProxyRepositoryName,
)
from nexus_sdk.apis.paths.v1_repository_settings import V1RepositorySettings
from nexus_sdk.apis.paths.v1_routing_rules import V1RoutingRules
from nexus_sdk.apis.paths.v1_routing_rules_name import V1RoutingRulesName
from nexus_sdk.apis.paths.v1_script import V1Script
from nexus_sdk.apis.paths.v1_script_name import V1ScriptName
from nexus_sdk.apis.paths.v1_script_name_run import V1ScriptNameRun
from nexus_sdk.apis.paths.v1_search import V1Search
from nexus_sdk.apis.paths.v1_search_assets import V1SearchAssets
from nexus_sdk.apis.paths.v1_search_assets_download import V1SearchAssetsDownload
from nexus_sdk.apis.paths.v1_security_anonymous import V1SecurityAnonymous
from nexus_sdk.apis.paths.v1_security_atlassian_crowd import V1SecurityAtlassianCrowd
from nexus_sdk.apis.paths.v1_security_atlassian_crowd_clear_cache import (
    V1SecurityAtlassianCrowdClearCache,
)
from nexus_sdk.apis.paths.v1_security_atlassian_crowd_verify_connection import (
    V1SecurityAtlassianCrowdVerifyConnection,
)
from nexus_sdk.apis.paths.v1_security_content_selectors import (
    V1SecurityContentSelectors,
)
from nexus_sdk.apis.paths.v1_security_content_selectors_name import (
    V1SecurityContentSelectorsName,
)
from nexus_sdk.apis.paths.v1_security_jwt import V1SecurityJwt
from nexus_sdk.apis.paths.v1_security_ldap import V1SecurityLdap
from nexus_sdk.apis.paths.v1_security_ldap_change_order import V1SecurityLdapChangeOrder
from nexus_sdk.apis.paths.v1_security_ldap_name import V1SecurityLdapName
from nexus_sdk.apis.paths.v1_security_privileges import V1SecurityPrivileges
from nexus_sdk.apis.paths.v1_security_privileges_application import (
    V1SecurityPrivilegesApplication,
)
from nexus_sdk.apis.paths.v1_security_privileges_application_privilege_name import (
    V1SecurityPrivilegesApplicationPrivilegeName,
)
from nexus_sdk.apis.paths.v1_security_privileges_privilege_name import (
    V1SecurityPrivilegesPrivilegeName,
)
from nexus_sdk.apis.paths.v1_security_privileges_repository_admin import (
    V1SecurityPrivilegesRepositoryAdmin,
)
from nexus_sdk.apis.paths.v1_security_privileges_repository_admin_privilege_name import (
    V1SecurityPrivilegesRepositoryAdminPrivilegeName,
)
from nexus_sdk.apis.paths.v1_security_privileges_repository_content_selector import (
    V1SecurityPrivilegesRepositoryContentSelector,
)
from nexus_sdk.apis.paths.v1_security_privileges_repository_content_selector_privilege_name import (
    V1SecurityPrivilegesRepositoryContentSelectorPrivilegeName,
)
from nexus_sdk.apis.paths.v1_security_privileges_repository_view import (
    V1SecurityPrivilegesRepositoryView,
)
from nexus_sdk.apis.paths.v1_security_privileges_repository_view_privilege_name import (
    V1SecurityPrivilegesRepositoryViewPrivilegeName,
)
from nexus_sdk.apis.paths.v1_security_privileges_script import (
    V1SecurityPrivilegesScript,
)
from nexus_sdk.apis.paths.v1_security_privileges_script_privilege_name import (
    V1SecurityPrivilegesScriptPrivilegeName,
)
from nexus_sdk.apis.paths.v1_security_privileges_wildcard import (
    V1SecurityPrivilegesWildcard,
)
from nexus_sdk.apis.paths.v1_security_privileges_wildcard_privilege_name import (
    V1SecurityPrivilegesWildcardPrivilegeName,
)
from nexus_sdk.apis.paths.v1_security_realms_active import V1SecurityRealmsActive
from nexus_sdk.apis.paths.v1_security_realms_available import V1SecurityRealmsAvailable
from nexus_sdk.apis.paths.v1_security_roles import V1SecurityRoles
from nexus_sdk.apis.paths.v1_security_roles_id import V1SecurityRolesId
from nexus_sdk.apis.paths.v1_security_saml import V1SecuritySaml
from nexus_sdk.apis.paths.v1_security_saml_metadata import V1SecuritySamlMetadata
from nexus_sdk.apis.paths.v1_security_saml_pem import V1SecuritySamlPem
from nexus_sdk.apis.paths.v1_security_ssl import V1SecuritySsl
from nexus_sdk.apis.paths.v1_security_ssl_truststore import V1SecuritySslTruststore
from nexus_sdk.apis.paths.v1_security_ssl_truststore_id import V1SecuritySslTruststoreId
from nexus_sdk.apis.paths.v1_security_user_sources import V1SecurityUserSources
from nexus_sdk.apis.paths.v1_security_user_tokens import V1SecurityUserTokens
from nexus_sdk.apis.paths.v1_security_users import V1SecurityUsers
from nexus_sdk.apis.paths.v1_security_users_user_id import V1SecurityUsersUserId
from nexus_sdk.apis.paths.v1_security_users_user_id_change_password import (
    V1SecurityUsersUserIdChangePassword,
)
from nexus_sdk.apis.paths.v1_security_users_user_id_realm_user_token_reset import (
    V1SecurityUsersUserIdRealmUserTokenReset,
)
from nexus_sdk.apis.paths.v1_staging_delete import V1StagingDelete
from nexus_sdk.apis.paths.v1_staging_move_destination import V1StagingMoveDestination
from nexus_sdk.apis.paths.v1_status import V1Status
from nexus_sdk.apis.paths.v1_status_check import V1StatusCheck
from nexus_sdk.apis.paths.v1_status_writable import V1StatusWritable
from nexus_sdk.apis.paths.v1_support_supportzip import V1SupportSupportzip
from nexus_sdk.apis.paths.v1_support_supportzippath import V1SupportSupportzippath
from nexus_sdk.apis.paths.v1_system_license import V1SystemLicense
from nexus_sdk.apis.paths.v1_tags import V1Tags
from nexus_sdk.apis.paths.v1_tags_associate_tag_name import V1TagsAssociateTagName
from nexus_sdk.apis.paths.v1_tags_name import V1TagsName
from nexus_sdk.apis.paths.v1_tasks import V1Tasks
from nexus_sdk.apis.paths.v1_tasks_id import V1TasksId
from nexus_sdk.apis.paths.v1_tasks_id_run import V1TasksIdRun
from nexus_sdk.apis.paths.v1_tasks_id_stop import V1TasksIdStop
from nexus_sdk.paths import PathValues

PathToApi = typing_extensions.TypedDict(
    "PathToApi",
    {
        PathValues.V1_SECURITY_ANONYMOUS: V1SecurityAnonymous,
        PathValues.V1_SECURITY_USERSOURCES: V1SecurityUserSources,
        PathValues.V1_SECURITY_USERS_USER_ID: V1SecurityUsersUserId,
        PathValues.V1_SECURITY_USERS_USER_ID_CHANGEPASSWORD: V1SecurityUsersUserIdChangePassword,
        PathValues.V1_SECURITY_USERS: V1SecurityUsers,
        PathValues.V1_SECURITY_JWT: V1SecurityJwt,
        PathValues.V1_SECURITY_PRIVILEGES: V1SecurityPrivileges,
        PathValues.V1_SECURITY_PRIVILEGES_PRIVILEGE_NAME: V1SecurityPrivilegesPrivilegeName,
        PathValues.V1_SECURITY_PRIVILEGES_WILDCARD: V1SecurityPrivilegesWildcard,
        PathValues.V1_SECURITY_PRIVILEGES_APPLICATION: V1SecurityPrivilegesApplication,
        PathValues.V1_SECURITY_PRIVILEGES_WILDCARD_PRIVILEGE_NAME: V1SecurityPrivilegesWildcardPrivilegeName,
        PathValues.V1_SECURITY_PRIVILEGES_APPLICATION_PRIVILEGE_NAME: V1SecurityPrivilegesApplicationPrivilegeName,
        PathValues.V1_SECURITY_REALMS_ACTIVE: V1SecurityRealmsActive,
        PathValues.V1_SECURITY_REALMS_AVAILABLE: V1SecurityRealmsAvailable,
        PathValues.V1_SECURITY_ROLES: V1SecurityRoles,
        PathValues.V1_SECURITY_ROLES_ID: V1SecurityRolesId,
        PathValues.V1_TASKS_ID: V1TasksId,
        PathValues.V1_TASKS: V1Tasks,
        PathValues.V1_TASKS_ID_RUN: V1TasksIdRun,
        PathValues.V1_TASKS_ID_STOP: V1TasksIdStop,
        PathValues.V1_BLOBSTORES_NAME: V1BlobstoresName,
        PathValues.V1_BLOBSTORES_NAME_QUOTASTATUS: V1BlobstoresNameQuotaStatus,
        PathValues.V1_BLOBSTORES: V1Blobstores,
        PathValues.V1_BLOBSTORES_FILE: V1BlobstoresFile,
        PathValues.V1_BLOBSTORES_FILE_NAME: V1BlobstoresFileName,
        PathValues.V1_LIFECYCLE_BOUNCE: V1LifecycleBounce,
        PathValues.V1_LIFECYCLE_PHASE: V1LifecyclePhase,
        PathValues.V1_READONLY_FREEZE: V1ReadOnlyFreeze,
        PathValues.V1_READONLY_FORCERELEASE: V1ReadOnlyForceRelease,
        PathValues.V1_READONLY_RELEASE: V1ReadOnlyRelease,
        PathValues.V1_READONLY: V1ReadOnly,
        PathValues.V1_SECURITY_SSL: V1SecuritySsl,
        PathValues.V1_SECURITY_SSL_TRUSTSTORE: V1SecuritySslTruststore,
        PathValues.V1_SECURITY_SSL_TRUSTSTORE_ID: V1SecuritySslTruststoreId,
        PathValues.V1_ASSETS_ID: V1AssetsId,
        PathValues.V1_ASSETS: V1Assets,
        PathValues.V1_COMPONENTS_ID: V1ComponentsId,
        PathValues.V1_COMPONENTS: V1Components,
        PathValues.V1_REPOSITORIES_REPOSITORY_NAME_REBUILDINDEX: V1RepositoriesRepositoryNameRebuildIndex,
        PathValues.V1_REPOSITORIES_REPOSITORY_NAME_INVALIDATECACHE: V1RepositoriesRepositoryNameInvalidateCache,
        PathValues.V1_REPOSITORIES_REPOSITORY_NAME: V1RepositoriesRepositoryName,
        PathValues.V1_REPOSITORY_SETTINGS: V1RepositorySettings,
        PathValues.V1_SECURITY_CONTENTSELECTORS: V1SecurityContentSelectors,
        PathValues.V1_SECURITY_CONTENTSELECTORS_NAME: V1SecurityContentSelectorsName,
        PathValues.V1_REPOSITORIES: V1Repositories,
        PathValues.V1_ROUTINGRULES_NAME: V1RoutingRulesName,
        PathValues.V1_ROUTINGRULES: V1RoutingRules,
        PathValues.V1_SEARCH_ASSETS_DOWNLOAD: V1SearchAssetsDownload,
        PathValues.V1_SEARCH_ASSETS: V1SearchAssets,
        PathValues.V1_SEARCH: V1Search,
        PathValues.V1_FORMATS_FORMAT_UPLOADSPECS: V1FormatsFormatUploadSpecs,
        PathValues.V1_FORMATS_UPLOADSPECS: V1FormatsUploadSpecs,
        PathValues.V1_SECURITY_PRIVILEGES_REPOSITORYCONTENTSELECTOR: V1SecurityPrivilegesRepositoryContentSelector,
        PathValues.V1_SECURITY_PRIVILEGES_REPOSITORYADMIN: V1SecurityPrivilegesRepositoryAdmin,
        PathValues.V1_SECURITY_PRIVILEGES_REPOSITORYVIEW: V1SecurityPrivilegesRepositoryView,
        PathValues.V1_SECURITY_PRIVILEGES_REPOSITORYVIEW_PRIVILEGE_NAME: V1SecurityPrivilegesRepositoryViewPrivilegeName,
        PathValues.V1_SECURITY_PRIVILEGES_REPOSITORYCONTENTSELECTOR_PRIVILEGE_NAME: V1SecurityPrivilegesRepositoryContentSelectorPrivilegeName,
        PathValues.V1_SECURITY_PRIVILEGES_REPOSITORYADMIN_PRIVILEGE_NAME: V1SecurityPrivilegesRepositoryAdminPrivilegeName,
        PathValues.V1_REPOSITORIES_MAVEN_GROUP: V1RepositoriesMavenGroup,
        PathValues.V1_REPOSITORIES_MAVEN_GROUP_REPOSITORY_NAME: V1RepositoriesMavenGroupRepositoryName,
        PathValues.V1_REPOSITORIES_MAVEN_HOSTED_REPOSITORY_NAME: V1RepositoriesMavenHostedRepositoryName,
        PathValues.V1_REPOSITORIES_MAVEN_HOSTED: V1RepositoriesMavenHosted,
        PathValues.V1_REPOSITORIES_MAVEN_PROXY_REPOSITORY_NAME: V1RepositoriesMavenProxyRepositoryName,
        PathValues.V1_REPOSITORIES_MAVEN_PROXY: V1RepositoriesMavenProxy,
        PathValues.V1_SECURITY_PRIVILEGES_SCRIPT: V1SecurityPrivilegesScript,
        PathValues.V1_SECURITY_PRIVILEGES_SCRIPT_PRIVILEGE_NAME: V1SecurityPrivilegesScriptPrivilegeName,
        PathValues.V1_SCRIPT: V1Script,
        PathValues.V1_SCRIPT_NAME: V1ScriptName,
        PathValues.V1_SCRIPT_NAME_RUN: V1ScriptNameRun,
        PathValues.V1_BLOBSTORES_S3: V1BlobstoresS3,
        PathValues.V1_BLOBSTORES_S3_NAME: V1BlobstoresS3Name,
        PathValues.V1_REPOSITORIES_APT_HOSTED_REPOSITORY_NAME: V1RepositoriesAptHostedRepositoryName,
        PathValues.V1_REPOSITORIES_APT_HOSTED: V1RepositoriesAptHosted,
        PathValues.V1_REPOSITORIES_APT_PROXY_REPOSITORY_NAME: V1RepositoriesAptProxyRepositoryName,
        PathValues.V1_REPOSITORIES_APT_PROXY: V1RepositoriesAptProxy,
        PathValues.V1_REPOSITORIES_RAW_GROUP: V1RepositoriesRawGroup,
        PathValues.V1_REPOSITORIES_RAW_GROUP_REPOSITORY_NAME: V1RepositoriesRawGroupRepositoryName,
        PathValues.V1_REPOSITORIES_RAW_HOSTED: V1RepositoriesRawHosted,
        PathValues.V1_REPOSITORIES_RAW_HOSTED_REPOSITORY_NAME: V1RepositoriesRawHostedRepositoryName,
        PathValues.V1_REPOSITORIES_RAW_PROXY: V1RepositoriesRawProxy,
        PathValues.V1_REPOSITORIES_RAW_PROXY_REPOSITORY_NAME: V1RepositoriesRawProxyRepositoryName,
        PathValues.V1_EMAIL: V1Email,
        PathValues.V1_EMAIL_VERIFY: V1EmailVerify,
        PathValues.V1_STATUS_CHECK: V1StatusCheck,
        PathValues.V1_STATUS: V1Status,
        PathValues.V1_STATUS_WRITABLE: V1StatusWritable,
        PathValues.V1_SUPPORT_SUPPORTZIP: V1SupportSupportzip,
        PathValues.V1_SUPPORT_SUPPORTZIPPATH: V1SupportSupportzippath,
        PathValues.V1_SECURITY_LDAP: V1SecurityLdap,
        PathValues.V1_SECURITY_LDAP_NAME: V1SecurityLdapName,
        PathValues.V1_SECURITY_LDAP_CHANGEORDER: V1SecurityLdapChangeOrder,
        PathValues.V1_TAGS: V1Tags,
        PathValues.V1_TAGS_ASSOCIATE_TAG_NAME: V1TagsAssociateTagName,
        PathValues.V1_TAGS_NAME: V1TagsName,
        PathValues.V1_IQ_VERIFYCONNECTION: V1IqVerifyConnection,
        PathValues.V1_IQ: V1Iq,
        PathValues.V1_IQ_ENABLE: V1IqEnable,
        PathValues.V1_IQ_DISABLE: V1IqDisable,
        PathValues.V1_REPOSITORIES_REPOSITORY_NAME_HEALTHCHECK: V1RepositoriesRepositoryNameHealthCheck,
        PathValues.V1_SYSTEM_LICENSE: V1SystemLicense,
        PathValues.V1_SECURITY_ATLASSIANCROWD_VERIFYCONNECTION: V1SecurityAtlassianCrowdVerifyConnection,
        PathValues.V1_SECURITY_ATLASSIANCROWD: V1SecurityAtlassianCrowd,
        PathValues.V1_SECURITY_ATLASSIANCROWD_CLEARCACHE: V1SecurityAtlassianCrowdClearCache,
        PathValues.V1_REPOSITORIES_NPM_GROUP_REPOSITORY_NAME: V1RepositoriesNpmGroupRepositoryName,
        PathValues.V1_REPOSITORIES_NPM_GROUP: V1RepositoriesNpmGroup,
        PathValues.V1_REPOSITORIES_NPM_HOSTED: V1RepositoriesNpmHosted,
        PathValues.V1_REPOSITORIES_NPM_HOSTED_REPOSITORY_NAME: V1RepositoriesNpmHostedRepositoryName,
        PathValues.V1_REPOSITORIES_NPM_PROXY_REPOSITORY_NAME: V1RepositoriesNpmProxyRepositoryName,
        PathValues.V1_REPOSITORIES_NPM_PROXY: V1RepositoriesNpmProxy,
        PathValues.V1_REPOSITORIES_NUGET_GROUP: V1RepositoriesNugetGroup,
        PathValues.V1_REPOSITORIES_NUGET_GROUP_REPOSITORY_NAME: V1RepositoriesNugetGroupRepositoryName,
        PathValues.V1_REPOSITORIES_NUGET_HOSTED: V1RepositoriesNugetHosted,
        PathValues.V1_REPOSITORIES_NUGET_HOSTED_REPOSITORY_NAME: V1RepositoriesNugetHostedRepositoryName,
        PathValues.V1_REPOSITORIES_NUGET_PROXY_REPOSITORY_NAME: V1RepositoriesNugetProxyRepositoryName,
        PathValues.V1_REPOSITORIES_NUGET_PROXY: V1RepositoriesNugetProxy,
        PathValues.V1_SECURITY_USERTOKENS: V1SecurityUserTokens,
        PathValues.V1_SECURITY_USERS_USER_ID_REALM_USERTOKENRESET: V1SecurityUsersUserIdRealmUserTokenReset,
        PathValues.V1_REPOSITORIES_RUBYGEMS_GROUP: V1RepositoriesRubygemsGroup,
        PathValues.V1_REPOSITORIES_RUBYGEMS_GROUP_REPOSITORY_NAME: V1RepositoriesRubygemsGroupRepositoryName,
        PathValues.V1_REPOSITORIES_RUBYGEMS_HOSTED: V1RepositoriesRubygemsHosted,
        PathValues.V1_REPOSITORIES_RUBYGEMS_HOSTED_REPOSITORY_NAME: V1RepositoriesRubygemsHostedRepositoryName,
        PathValues.V1_REPOSITORIES_RUBYGEMS_PROXY: V1RepositoriesRubygemsProxy,
        PathValues.V1_REPOSITORIES_RUBYGEMS_PROXY_REPOSITORY_NAME: V1RepositoriesRubygemsProxyRepositoryName,
        PathValues.V1_REPOSITORIES_YUM_GROUP: V1RepositoriesYumGroup,
        PathValues.V1_REPOSITORIES_YUM_GROUP_REPOSITORY_NAME: V1RepositoriesYumGroupRepositoryName,
        PathValues.V1_REPOSITORIES_YUM_HOSTED_REPOSITORY_NAME: V1RepositoriesYumHostedRepositoryName,
        PathValues.V1_REPOSITORIES_YUM_HOSTED: V1RepositoriesYumHosted,
        PathValues.V1_REPOSITORIES_YUM_PROXY: V1RepositoriesYumProxy,
        PathValues.V1_REPOSITORIES_YUM_PROXY_REPOSITORY_NAME: V1RepositoriesYumProxyRepositoryName,
        PathValues.V1_REPOSITORIES_DOCKER_GROUP_REPOSITORY_NAME: V1RepositoriesDockerGroupRepositoryName,
        PathValues.V1_REPOSITORIES_DOCKER_GROUP: V1RepositoriesDockerGroup,
        PathValues.V1_REPOSITORIES_DOCKER_HOSTED_REPOSITORY_NAME: V1RepositoriesDockerHostedRepositoryName,
        PathValues.V1_REPOSITORIES_DOCKER_HOSTED: V1RepositoriesDockerHosted,
        PathValues.V1_REPOSITORIES_DOCKER_PROXY_REPOSITORY_NAME: V1RepositoriesDockerProxyRepositoryName,
        PathValues.V1_REPOSITORIES_DOCKER_PROXY: V1RepositoriesDockerProxy,
        PathValues.V1_REPOSITORIES_PYPI_GROUP: V1RepositoriesPypiGroup,
        PathValues.V1_REPOSITORIES_PYPI_GROUP_REPOSITORY_NAME: V1RepositoriesPypiGroupRepositoryName,
        PathValues.V1_REPOSITORIES_PYPI_HOSTED: V1RepositoriesPypiHosted,
        PathValues.V1_REPOSITORIES_PYPI_HOSTED_REPOSITORY_NAME: V1RepositoriesPypiHostedRepositoryName,
        PathValues.V1_REPOSITORIES_PYPI_PROXY: V1RepositoriesPypiProxy,
        PathValues.V1_REPOSITORIES_PYPI_PROXY_REPOSITORY_NAME: V1RepositoriesPypiProxyRepositoryName,
        PathValues.V1_REPOSITORIES_CONDA_PROXY: V1RepositoriesCondaProxy,
        PathValues.V1_REPOSITORIES_CONDA_PROXY_REPOSITORY_NAME: V1RepositoriesCondaProxyRepositoryName,
        PathValues.V1_REPOSITORIES_CONAN_PROXY: V1RepositoriesConanProxy,
        PathValues.V1_REPOSITORIES_CONAN_PROXY_REPOSITORY_NAME: V1RepositoriesConanProxyRepositoryName,
        PathValues.V1_REPOSITORIES_GITLFS_HOSTED: V1RepositoriesGitlfsHosted,
        PathValues.V1_REPOSITORIES_GITLFS_HOSTED_REPOSITORY_NAME: V1RepositoriesGitlfsHostedRepositoryName,
        PathValues.V1_REPOSITORIES_R_GROUP: V1RepositoriesRGroup,
        PathValues.V1_REPOSITORIES_R_GROUP_REPOSITORY_NAME: V1RepositoriesRGroupRepositoryName,
        PathValues.V1_REPOSITORIES_R_HOSTED: V1RepositoriesRHosted,
        PathValues.V1_REPOSITORIES_R_HOSTED_REPOSITORY_NAME: V1RepositoriesRHostedRepositoryName,
        PathValues.V1_REPOSITORIES_R_PROXY: V1RepositoriesRProxy,
        PathValues.V1_REPOSITORIES_R_PROXY_REPOSITORY_NAME: V1RepositoriesRProxyRepositoryName,
        PathValues.V1_BLOBSTORES_GROUP: V1BlobstoresGroup,
        PathValues.V1_BLOBSTORES_GROUP_NAME: V1BlobstoresGroupName,
        PathValues.V1_BLOBSTORES_GROUP_CONVERT_NAME_NEW_NAME_FOR_ORIGINAL: V1BlobstoresGroupConvertNameNewNameForOriginal,
        PathValues.BETA_REPLICATION_CONNECTION_NAME: BetaReplicationConnectionName,
        PathValues.BETA_REPLICATION_CONNECTION: BetaReplicationConnection,
        PathValues.BETA_REPLICATIONTARGET_REPOSITORY_ENABLE: BetaReplicationtargetRepositoryEnable,
        PathValues.BETA_REPLICATIONTARGET_REPOSITORY_REPOSITORY_NAME_ENABLE: BetaReplicationtargetRepositoryRepositoryNameEnable,
        PathValues.V1_REPOSITORIES_COCOAPODS_PROXY: V1RepositoriesCocoapodsProxy,
        PathValues.V1_REPOSITORIES_COCOAPODS_PROXY_REPOSITORY_NAME: V1RepositoriesCocoapodsProxyRepositoryName,
        PathValues.V1_REPOSITORIES_GO_GROUP: V1RepositoriesGoGroup,
        PathValues.V1_REPOSITORIES_GO_GROUP_REPOSITORY_NAME: V1RepositoriesGoGroupRepositoryName,
        PathValues.V1_REPOSITORIES_GO_PROXY: V1RepositoriesGoProxy,
        PathValues.V1_REPOSITORIES_GO_PROXY_REPOSITORY_NAME: V1RepositoriesGoProxyRepositoryName,
        PathValues.V1_REPOSITORIES_P2_PROXY: V1RepositoriesP2Proxy,
        PathValues.V1_REPOSITORIES_P2_PROXY_REPOSITORY_NAME: V1RepositoriesP2ProxyRepositoryName,
        PathValues.V1_STAGING_MOVE_DESTINATION: V1StagingMoveDestination,
        PathValues.V1_STAGING_DELETE: V1StagingDelete,
        PathValues.V1_AZUREBLOBSTORE_TESTCONNECTION: V1AzureblobstoreTestConnection,
        PathValues.V1_BLOBSTORES_AZURE: V1BlobstoresAzure,
        PathValues.V1_BLOBSTORES_AZURE_NAME: V1BlobstoresAzureName,
        PathValues.V1_SECURITY_SAML_METADATA: V1SecuritySamlMetadata,
        PathValues.V1_SECURITY_SAML: V1SecuritySaml,
        PathValues.V1_SECURITY_SAML_PEM: V1SecuritySamlPem,
        PathValues.V1_REPOSITORIES_HELM_HOSTED: V1RepositoriesHelmHosted,
        PathValues.V1_REPOSITORIES_HELM_HOSTED_REPOSITORY_NAME: V1RepositoriesHelmHostedRepositoryName,
        PathValues.V1_REPOSITORIES_HELM_PROXY: V1RepositoriesHelmProxy,
        PathValues.V1_REPOSITORIES_HELM_PROXY_REPOSITORY_NAME: V1RepositoriesHelmProxyRepositoryName,
        PathValues.V1_REPOSITORIES_BOWER_GROUP: V1RepositoriesBowerGroup,
        PathValues.V1_REPOSITORIES_BOWER_GROUP_REPOSITORY_NAME: V1RepositoriesBowerGroupRepositoryName,
        PathValues.V1_REPOSITORIES_BOWER_HOSTED: V1RepositoriesBowerHosted,
        PathValues.V1_REPOSITORIES_BOWER_HOSTED_REPOSITORY_NAME: V1RepositoriesBowerHostedRepositoryName,
        PathValues.V1_REPOSITORIES_BOWER_PROXY_REPOSITORY_NAME: V1RepositoriesBowerProxyRepositoryName,
        PathValues.V1_REPOSITORIES_BOWER_PROXY: V1RepositoriesBowerProxy,
    },
)

path_to_api = PathToApi(
    {
        PathValues.V1_SECURITY_ANONYMOUS: V1SecurityAnonymous,
        PathValues.V1_SECURITY_USERSOURCES: V1SecurityUserSources,
        PathValues.V1_SECURITY_USERS_USER_ID: V1SecurityUsersUserId,
        PathValues.V1_SECURITY_USERS_USER_ID_CHANGEPASSWORD: V1SecurityUsersUserIdChangePassword,
        PathValues.V1_SECURITY_USERS: V1SecurityUsers,
        PathValues.V1_SECURITY_JWT: V1SecurityJwt,
        PathValues.V1_SECURITY_PRIVILEGES: V1SecurityPrivileges,
        PathValues.V1_SECURITY_PRIVILEGES_PRIVILEGE_NAME: V1SecurityPrivilegesPrivilegeName,
        PathValues.V1_SECURITY_PRIVILEGES_WILDCARD: V1SecurityPrivilegesWildcard,
        PathValues.V1_SECURITY_PRIVILEGES_APPLICATION: V1SecurityPrivilegesApplication,
        PathValues.V1_SECURITY_PRIVILEGES_WILDCARD_PRIVILEGE_NAME: V1SecurityPrivilegesWildcardPrivilegeName,
        PathValues.V1_SECURITY_PRIVILEGES_APPLICATION_PRIVILEGE_NAME: V1SecurityPrivilegesApplicationPrivilegeName,
        PathValues.V1_SECURITY_REALMS_ACTIVE: V1SecurityRealmsActive,
        PathValues.V1_SECURITY_REALMS_AVAILABLE: V1SecurityRealmsAvailable,
        PathValues.V1_SECURITY_ROLES: V1SecurityRoles,
        PathValues.V1_SECURITY_ROLES_ID: V1SecurityRolesId,
        PathValues.V1_TASKS_ID: V1TasksId,
        PathValues.V1_TASKS: V1Tasks,
        PathValues.V1_TASKS_ID_RUN: V1TasksIdRun,
        PathValues.V1_TASKS_ID_STOP: V1TasksIdStop,
        PathValues.V1_BLOBSTORES_NAME: V1BlobstoresName,
        PathValues.V1_BLOBSTORES_NAME_QUOTASTATUS: V1BlobstoresNameQuotaStatus,
        PathValues.V1_BLOBSTORES: V1Blobstores,
        PathValues.V1_BLOBSTORES_FILE: V1BlobstoresFile,
        PathValues.V1_BLOBSTORES_FILE_NAME: V1BlobstoresFileName,
        PathValues.V1_LIFECYCLE_BOUNCE: V1LifecycleBounce,
        PathValues.V1_LIFECYCLE_PHASE: V1LifecyclePhase,
        PathValues.V1_READONLY_FREEZE: V1ReadOnlyFreeze,
        PathValues.V1_READONLY_FORCERELEASE: V1ReadOnlyForceRelease,
        PathValues.V1_READONLY_RELEASE: V1ReadOnlyRelease,
        PathValues.V1_READONLY: V1ReadOnly,
        PathValues.V1_SECURITY_SSL: V1SecuritySsl,
        PathValues.V1_SECURITY_SSL_TRUSTSTORE: V1SecuritySslTruststore,
        PathValues.V1_SECURITY_SSL_TRUSTSTORE_ID: V1SecuritySslTruststoreId,
        PathValues.V1_ASSETS_ID: V1AssetsId,
        PathValues.V1_ASSETS: V1Assets,
        PathValues.V1_COMPONENTS_ID: V1ComponentsId,
        PathValues.V1_COMPONENTS: V1Components,
        PathValues.V1_REPOSITORIES_REPOSITORY_NAME_REBUILDINDEX: V1RepositoriesRepositoryNameRebuildIndex,
        PathValues.V1_REPOSITORIES_REPOSITORY_NAME_INVALIDATECACHE: V1RepositoriesRepositoryNameInvalidateCache,
        PathValues.V1_REPOSITORIES_REPOSITORY_NAME: V1RepositoriesRepositoryName,
        PathValues.V1_REPOSITORY_SETTINGS: V1RepositorySettings,
        PathValues.V1_SECURITY_CONTENTSELECTORS: V1SecurityContentSelectors,
        PathValues.V1_SECURITY_CONTENTSELECTORS_NAME: V1SecurityContentSelectorsName,
        PathValues.V1_REPOSITORIES: V1Repositories,
        PathValues.V1_ROUTINGRULES_NAME: V1RoutingRulesName,
        PathValues.V1_ROUTINGRULES: V1RoutingRules,
        PathValues.V1_SEARCH_ASSETS_DOWNLOAD: V1SearchAssetsDownload,
        PathValues.V1_SEARCH_ASSETS: V1SearchAssets,
        PathValues.V1_SEARCH: V1Search,
        PathValues.V1_FORMATS_FORMAT_UPLOADSPECS: V1FormatsFormatUploadSpecs,
        PathValues.V1_FORMATS_UPLOADSPECS: V1FormatsUploadSpecs,
        PathValues.V1_SECURITY_PRIVILEGES_REPOSITORYCONTENTSELECTOR: V1SecurityPrivilegesRepositoryContentSelector,
        PathValues.V1_SECURITY_PRIVILEGES_REPOSITORYADMIN: V1SecurityPrivilegesRepositoryAdmin,
        PathValues.V1_SECURITY_PRIVILEGES_REPOSITORYVIEW: V1SecurityPrivilegesRepositoryView,
        PathValues.V1_SECURITY_PRIVILEGES_REPOSITORYVIEW_PRIVILEGE_NAME: V1SecurityPrivilegesRepositoryViewPrivilegeName,
        PathValues.V1_SECURITY_PRIVILEGES_REPOSITORYCONTENTSELECTOR_PRIVILEGE_NAME: V1SecurityPrivilegesRepositoryContentSelectorPrivilegeName,
        PathValues.V1_SECURITY_PRIVILEGES_REPOSITORYADMIN_PRIVILEGE_NAME: V1SecurityPrivilegesRepositoryAdminPrivilegeName,
        PathValues.V1_REPOSITORIES_MAVEN_GROUP: V1RepositoriesMavenGroup,
        PathValues.V1_REPOSITORIES_MAVEN_GROUP_REPOSITORY_NAME: V1RepositoriesMavenGroupRepositoryName,
        PathValues.V1_REPOSITORIES_MAVEN_HOSTED_REPOSITORY_NAME: V1RepositoriesMavenHostedRepositoryName,
        PathValues.V1_REPOSITORIES_MAVEN_HOSTED: V1RepositoriesMavenHosted,
        PathValues.V1_REPOSITORIES_MAVEN_PROXY_REPOSITORY_NAME: V1RepositoriesMavenProxyRepositoryName,
        PathValues.V1_REPOSITORIES_MAVEN_PROXY: V1RepositoriesMavenProxy,
        PathValues.V1_SECURITY_PRIVILEGES_SCRIPT: V1SecurityPrivilegesScript,
        PathValues.V1_SECURITY_PRIVILEGES_SCRIPT_PRIVILEGE_NAME: V1SecurityPrivilegesScriptPrivilegeName,
        PathValues.V1_SCRIPT: V1Script,
        PathValues.V1_SCRIPT_NAME: V1ScriptName,
        PathValues.V1_SCRIPT_NAME_RUN: V1ScriptNameRun,
        PathValues.V1_BLOBSTORES_S3: V1BlobstoresS3,
        PathValues.V1_BLOBSTORES_S3_NAME: V1BlobstoresS3Name,
        PathValues.V1_REPOSITORIES_APT_HOSTED_REPOSITORY_NAME: V1RepositoriesAptHostedRepositoryName,
        PathValues.V1_REPOSITORIES_APT_HOSTED: V1RepositoriesAptHosted,
        PathValues.V1_REPOSITORIES_APT_PROXY_REPOSITORY_NAME: V1RepositoriesAptProxyRepositoryName,
        PathValues.V1_REPOSITORIES_APT_PROXY: V1RepositoriesAptProxy,
        PathValues.V1_REPOSITORIES_RAW_GROUP: V1RepositoriesRawGroup,
        PathValues.V1_REPOSITORIES_RAW_GROUP_REPOSITORY_NAME: V1RepositoriesRawGroupRepositoryName,
        PathValues.V1_REPOSITORIES_RAW_HOSTED: V1RepositoriesRawHosted,
        PathValues.V1_REPOSITORIES_RAW_HOSTED_REPOSITORY_NAME: V1RepositoriesRawHostedRepositoryName,
        PathValues.V1_REPOSITORIES_RAW_PROXY: V1RepositoriesRawProxy,
        PathValues.V1_REPOSITORIES_RAW_PROXY_REPOSITORY_NAME: V1RepositoriesRawProxyRepositoryName,
        PathValues.V1_EMAIL: V1Email,
        PathValues.V1_EMAIL_VERIFY: V1EmailVerify,
        PathValues.V1_STATUS_CHECK: V1StatusCheck,
        PathValues.V1_STATUS: V1Status,
        PathValues.V1_STATUS_WRITABLE: V1StatusWritable,
        PathValues.V1_SUPPORT_SUPPORTZIP: V1SupportSupportzip,
        PathValues.V1_SUPPORT_SUPPORTZIPPATH: V1SupportSupportzippath,
        PathValues.V1_SECURITY_LDAP: V1SecurityLdap,
        PathValues.V1_SECURITY_LDAP_NAME: V1SecurityLdapName,
        PathValues.V1_SECURITY_LDAP_CHANGEORDER: V1SecurityLdapChangeOrder,
        PathValues.V1_TAGS: V1Tags,
        PathValues.V1_TAGS_ASSOCIATE_TAG_NAME: V1TagsAssociateTagName,
        PathValues.V1_TAGS_NAME: V1TagsName,
        PathValues.V1_IQ_VERIFYCONNECTION: V1IqVerifyConnection,
        PathValues.V1_IQ: V1Iq,
        PathValues.V1_IQ_ENABLE: V1IqEnable,
        PathValues.V1_IQ_DISABLE: V1IqDisable,
        PathValues.V1_REPOSITORIES_REPOSITORY_NAME_HEALTHCHECK: V1RepositoriesRepositoryNameHealthCheck,
        PathValues.V1_SYSTEM_LICENSE: V1SystemLicense,
        PathValues.V1_SECURITY_ATLASSIANCROWD_VERIFYCONNECTION: V1SecurityAtlassianCrowdVerifyConnection,
        PathValues.V1_SECURITY_ATLASSIANCROWD: V1SecurityAtlassianCrowd,
        PathValues.V1_SECURITY_ATLASSIANCROWD_CLEARCACHE: V1SecurityAtlassianCrowdClearCache,
        PathValues.V1_REPOSITORIES_NPM_GROUP_REPOSITORY_NAME: V1RepositoriesNpmGroupRepositoryName,
        PathValues.V1_REPOSITORIES_NPM_GROUP: V1RepositoriesNpmGroup,
        PathValues.V1_REPOSITORIES_NPM_HOSTED: V1RepositoriesNpmHosted,
        PathValues.V1_REPOSITORIES_NPM_HOSTED_REPOSITORY_NAME: V1RepositoriesNpmHostedRepositoryName,
        PathValues.V1_REPOSITORIES_NPM_PROXY_REPOSITORY_NAME: V1RepositoriesNpmProxyRepositoryName,
        PathValues.V1_REPOSITORIES_NPM_PROXY: V1RepositoriesNpmProxy,
        PathValues.V1_REPOSITORIES_NUGET_GROUP: V1RepositoriesNugetGroup,
        PathValues.V1_REPOSITORIES_NUGET_GROUP_REPOSITORY_NAME: V1RepositoriesNugetGroupRepositoryName,
        PathValues.V1_REPOSITORIES_NUGET_HOSTED: V1RepositoriesNugetHosted,
        PathValues.V1_REPOSITORIES_NUGET_HOSTED_REPOSITORY_NAME: V1RepositoriesNugetHostedRepositoryName,
        PathValues.V1_REPOSITORIES_NUGET_PROXY_REPOSITORY_NAME: V1RepositoriesNugetProxyRepositoryName,
        PathValues.V1_REPOSITORIES_NUGET_PROXY: V1RepositoriesNugetProxy,
        PathValues.V1_SECURITY_USERTOKENS: V1SecurityUserTokens,
        PathValues.V1_SECURITY_USERS_USER_ID_REALM_USERTOKENRESET: V1SecurityUsersUserIdRealmUserTokenReset,
        PathValues.V1_REPOSITORIES_RUBYGEMS_GROUP: V1RepositoriesRubygemsGroup,
        PathValues.V1_REPOSITORIES_RUBYGEMS_GROUP_REPOSITORY_NAME: V1RepositoriesRubygemsGroupRepositoryName,
        PathValues.V1_REPOSITORIES_RUBYGEMS_HOSTED: V1RepositoriesRubygemsHosted,
        PathValues.V1_REPOSITORIES_RUBYGEMS_HOSTED_REPOSITORY_NAME: V1RepositoriesRubygemsHostedRepositoryName,
        PathValues.V1_REPOSITORIES_RUBYGEMS_PROXY: V1RepositoriesRubygemsProxy,
        PathValues.V1_REPOSITORIES_RUBYGEMS_PROXY_REPOSITORY_NAME: V1RepositoriesRubygemsProxyRepositoryName,
        PathValues.V1_REPOSITORIES_YUM_GROUP: V1RepositoriesYumGroup,
        PathValues.V1_REPOSITORIES_YUM_GROUP_REPOSITORY_NAME: V1RepositoriesYumGroupRepositoryName,
        PathValues.V1_REPOSITORIES_YUM_HOSTED_REPOSITORY_NAME: V1RepositoriesYumHostedRepositoryName,
        PathValues.V1_REPOSITORIES_YUM_HOSTED: V1RepositoriesYumHosted,
        PathValues.V1_REPOSITORIES_YUM_PROXY: V1RepositoriesYumProxy,
        PathValues.V1_REPOSITORIES_YUM_PROXY_REPOSITORY_NAME: V1RepositoriesYumProxyRepositoryName,
        PathValues.V1_REPOSITORIES_DOCKER_GROUP_REPOSITORY_NAME: V1RepositoriesDockerGroupRepositoryName,
        PathValues.V1_REPOSITORIES_DOCKER_GROUP: V1RepositoriesDockerGroup,
        PathValues.V1_REPOSITORIES_DOCKER_HOSTED_REPOSITORY_NAME: V1RepositoriesDockerHostedRepositoryName,
        PathValues.V1_REPOSITORIES_DOCKER_HOSTED: V1RepositoriesDockerHosted,
        PathValues.V1_REPOSITORIES_DOCKER_PROXY_REPOSITORY_NAME: V1RepositoriesDockerProxyRepositoryName,
        PathValues.V1_REPOSITORIES_DOCKER_PROXY: V1RepositoriesDockerProxy,
        PathValues.V1_REPOSITORIES_PYPI_GROUP: V1RepositoriesPypiGroup,
        PathValues.V1_REPOSITORIES_PYPI_GROUP_REPOSITORY_NAME: V1RepositoriesPypiGroupRepositoryName,
        PathValues.V1_REPOSITORIES_PYPI_HOSTED: V1RepositoriesPypiHosted,
        PathValues.V1_REPOSITORIES_PYPI_HOSTED_REPOSITORY_NAME: V1RepositoriesPypiHostedRepositoryName,
        PathValues.V1_REPOSITORIES_PYPI_PROXY: V1RepositoriesPypiProxy,
        PathValues.V1_REPOSITORIES_PYPI_PROXY_REPOSITORY_NAME: V1RepositoriesPypiProxyRepositoryName,
        PathValues.V1_REPOSITORIES_CONDA_PROXY: V1RepositoriesCondaProxy,
        PathValues.V1_REPOSITORIES_CONDA_PROXY_REPOSITORY_NAME: V1RepositoriesCondaProxyRepositoryName,
        PathValues.V1_REPOSITORIES_CONAN_PROXY: V1RepositoriesConanProxy,
        PathValues.V1_REPOSITORIES_CONAN_PROXY_REPOSITORY_NAME: V1RepositoriesConanProxyRepositoryName,
        PathValues.V1_REPOSITORIES_GITLFS_HOSTED: V1RepositoriesGitlfsHosted,
        PathValues.V1_REPOSITORIES_GITLFS_HOSTED_REPOSITORY_NAME: V1RepositoriesGitlfsHostedRepositoryName,
        PathValues.V1_REPOSITORIES_R_GROUP: V1RepositoriesRGroup,
        PathValues.V1_REPOSITORIES_R_GROUP_REPOSITORY_NAME: V1RepositoriesRGroupRepositoryName,
        PathValues.V1_REPOSITORIES_R_HOSTED: V1RepositoriesRHosted,
        PathValues.V1_REPOSITORIES_R_HOSTED_REPOSITORY_NAME: V1RepositoriesRHostedRepositoryName,
        PathValues.V1_REPOSITORIES_R_PROXY: V1RepositoriesRProxy,
        PathValues.V1_REPOSITORIES_R_PROXY_REPOSITORY_NAME: V1RepositoriesRProxyRepositoryName,
        PathValues.V1_BLOBSTORES_GROUP: V1BlobstoresGroup,
        PathValues.V1_BLOBSTORES_GROUP_NAME: V1BlobstoresGroupName,
        PathValues.V1_BLOBSTORES_GROUP_CONVERT_NAME_NEW_NAME_FOR_ORIGINAL: V1BlobstoresGroupConvertNameNewNameForOriginal,
        PathValues.BETA_REPLICATION_CONNECTION_NAME: BetaReplicationConnectionName,
        PathValues.BETA_REPLICATION_CONNECTION: BetaReplicationConnection,
        PathValues.BETA_REPLICATIONTARGET_REPOSITORY_ENABLE: BetaReplicationtargetRepositoryEnable,
        PathValues.BETA_REPLICATIONTARGET_REPOSITORY_REPOSITORY_NAME_ENABLE: BetaReplicationtargetRepositoryRepositoryNameEnable,
        PathValues.V1_REPOSITORIES_COCOAPODS_PROXY: V1RepositoriesCocoapodsProxy,
        PathValues.V1_REPOSITORIES_COCOAPODS_PROXY_REPOSITORY_NAME: V1RepositoriesCocoapodsProxyRepositoryName,
        PathValues.V1_REPOSITORIES_GO_GROUP: V1RepositoriesGoGroup,
        PathValues.V1_REPOSITORIES_GO_GROUP_REPOSITORY_NAME: V1RepositoriesGoGroupRepositoryName,
        PathValues.V1_REPOSITORIES_GO_PROXY: V1RepositoriesGoProxy,
        PathValues.V1_REPOSITORIES_GO_PROXY_REPOSITORY_NAME: V1RepositoriesGoProxyRepositoryName,
        PathValues.V1_REPOSITORIES_P2_PROXY: V1RepositoriesP2Proxy,
        PathValues.V1_REPOSITORIES_P2_PROXY_REPOSITORY_NAME: V1RepositoriesP2ProxyRepositoryName,
        PathValues.V1_STAGING_MOVE_DESTINATION: V1StagingMoveDestination,
        PathValues.V1_STAGING_DELETE: V1StagingDelete,
        PathValues.V1_AZUREBLOBSTORE_TESTCONNECTION: V1AzureblobstoreTestConnection,
        PathValues.V1_BLOBSTORES_AZURE: V1BlobstoresAzure,
        PathValues.V1_BLOBSTORES_AZURE_NAME: V1BlobstoresAzureName,
        PathValues.V1_SECURITY_SAML_METADATA: V1SecuritySamlMetadata,
        PathValues.V1_SECURITY_SAML: V1SecuritySaml,
        PathValues.V1_SECURITY_SAML_PEM: V1SecuritySamlPem,
        PathValues.V1_REPOSITORIES_HELM_HOSTED: V1RepositoriesHelmHosted,
        PathValues.V1_REPOSITORIES_HELM_HOSTED_REPOSITORY_NAME: V1RepositoriesHelmHostedRepositoryName,
        PathValues.V1_REPOSITORIES_HELM_PROXY: V1RepositoriesHelmProxy,
        PathValues.V1_REPOSITORIES_HELM_PROXY_REPOSITORY_NAME: V1RepositoriesHelmProxyRepositoryName,
        PathValues.V1_REPOSITORIES_BOWER_GROUP: V1RepositoriesBowerGroup,
        PathValues.V1_REPOSITORIES_BOWER_GROUP_REPOSITORY_NAME: V1RepositoriesBowerGroupRepositoryName,
        PathValues.V1_REPOSITORIES_BOWER_HOSTED: V1RepositoriesBowerHosted,
        PathValues.V1_REPOSITORIES_BOWER_HOSTED_REPOSITORY_NAME: V1RepositoriesBowerHostedRepositoryName,
        PathValues.V1_REPOSITORIES_BOWER_PROXY_REPOSITORY_NAME: V1RepositoriesBowerProxyRepositoryName,
        PathValues.V1_REPOSITORIES_BOWER_PROXY: V1RepositoriesBowerProxy,
    }
)
