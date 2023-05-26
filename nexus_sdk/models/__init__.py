# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from nexus_sdk.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from nexus_sdk.model.abstract_api_repository import AbstractApiRepository
from nexus_sdk.model.anonymous_access_settings_xo import AnonymousAccessSettingsXO
from nexus_sdk.model.api_certificate import ApiCertificate
from nexus_sdk.model.api_create_user import ApiCreateUser
from nexus_sdk.model.api_email_configuration import ApiEmailConfiguration
from nexus_sdk.model.api_email_validation import ApiEmailValidation
from nexus_sdk.model.api_license_details_xo import ApiLicenseDetailsXO
from nexus_sdk.model.api_privilege import ApiPrivilege
from nexus_sdk.model.api_privilege_application_request import (
    ApiPrivilegeApplicationRequest,
)
from nexus_sdk.model.api_privilege_repository_admin_request import (
    ApiPrivilegeRepositoryAdminRequest,
)
from nexus_sdk.model.api_privilege_repository_content_selector_request import (
    ApiPrivilegeRepositoryContentSelectorRequest,
)
from nexus_sdk.model.api_privilege_repository_view_request import (
    ApiPrivilegeRepositoryViewRequest,
)
from nexus_sdk.model.api_privilege_script_request import ApiPrivilegeScriptRequest
from nexus_sdk.model.api_privilege_wildcard_request import ApiPrivilegeWildcardRequest
from nexus_sdk.model.api_user import ApiUser
from nexus_sdk.model.api_user_source import ApiUserSource
from nexus_sdk.model.apt_hosted_api_repository import AptHostedApiRepository
from nexus_sdk.model.apt_hosted_repositories_attributes import (
    AptHostedRepositoriesAttributes,
)
from nexus_sdk.model.apt_hosted_repository_api_request import (
    AptHostedRepositoryApiRequest,
)
from nexus_sdk.model.apt_proxy_api_repository import AptProxyApiRepository
from nexus_sdk.model.apt_proxy_repositories_attributes import (
    AptProxyRepositoriesAttributes,
)
from nexus_sdk.model.apt_proxy_repository_api_request import (
    AptProxyRepositoryApiRequest,
)
from nexus_sdk.model.apt_signing_repositories_attributes import (
    AptSigningRepositoriesAttributes,
)
from nexus_sdk.model.asset_xo import AssetXO
from nexus_sdk.model.azure_blob_store_api_authentication import (
    AzureBlobStoreApiAuthentication,
)
from nexus_sdk.model.azure_blob_store_api_bucket_configuration import (
    AzureBlobStoreApiBucketConfiguration,
)
from nexus_sdk.model.azure_blob_store_api_model import AzureBlobStoreApiModel
from nexus_sdk.model.azure_connection_xo import AzureConnectionXO
from nexus_sdk.model.base_tag_xo import BaseTagXO
from nexus_sdk.model.blob_store_api_soft_quota import BlobStoreApiSoftQuota
from nexus_sdk.model.blob_store_quota_result_xo import BlobStoreQuotaResultXO
from nexus_sdk.model.bower_attributes import BowerAttributes
from nexus_sdk.model.bower_group_repository_api_request import (
    BowerGroupRepositoryApiRequest,
)
from nexus_sdk.model.bower_hosted_repository_api_request import (
    BowerHostedRepositoryApiRequest,
)
from nexus_sdk.model.bower_proxy_api_repository import BowerProxyApiRepository
from nexus_sdk.model.bower_proxy_repository_api_request import (
    BowerProxyRepositoryApiRequest,
)
from nexus_sdk.model.cleanup_policy_attributes import CleanupPolicyAttributes
from nexus_sdk.model.cocoapods_proxy_repository_api_request import (
    CocoapodsProxyRepositoryApiRequest,
)
from nexus_sdk.model.component_attributes import ComponentAttributes
from nexus_sdk.model.component_xo import ComponentXO
from nexus_sdk.model.conan_proxy_repository_api_request import (
    ConanProxyRepositoryApiRequest,
)
from nexus_sdk.model.conda_proxy_repository_api_request import (
    CondaProxyRepositoryApiRequest,
)
from nexus_sdk.model.content_selector_api_create_request import (
    ContentSelectorApiCreateRequest,
)
from nexus_sdk.model.content_selector_api_response import ContentSelectorApiResponse
from nexus_sdk.model.content_selector_api_update_request import (
    ContentSelectorApiUpdateRequest,
)
from nexus_sdk.model.create_ldap_server_xo import CreateLdapServerXo
from nexus_sdk.model.crowd_api_xo import CrowdApiXO
from nexus_sdk.model.docker_attributes import DockerAttributes
from nexus_sdk.model.docker_group_api_repository import DockerGroupApiRepository
from nexus_sdk.model.docker_group_repository_api_request import (
    DockerGroupRepositoryApiRequest,
)
from nexus_sdk.model.docker_hosted_api_repository import DockerHostedApiRepository
from nexus_sdk.model.docker_hosted_repository_api_request import (
    DockerHostedRepositoryApiRequest,
)
from nexus_sdk.model.docker_hosted_storage_attributes import (
    DockerHostedStorageAttributes,
)
from nexus_sdk.model.docker_proxy_api_repository import DockerProxyApiRepository
from nexus_sdk.model.docker_proxy_attributes import DockerProxyAttributes
from nexus_sdk.model.docker_proxy_repository_api_request import (
    DockerProxyRepositoryApiRequest,
)
from nexus_sdk.model.file_blob_store_api_create_request import (
    FileBlobStoreApiCreateRequest,
)
from nexus_sdk.model.file_blob_store_api_model import FileBlobStoreApiModel
from nexus_sdk.model.file_blob_store_api_update_request import (
    FileBlobStoreApiUpdateRequest,
)
from nexus_sdk.model.generic_blob_store_api_response import GenericBlobStoreApiResponse
from nexus_sdk.model.git_lfs_hosted_repository_api_request import (
    GitLfsHostedRepositoryApiRequest,
)
from nexus_sdk.model.golang_group_repository_api_request import (
    GolangGroupRepositoryApiRequest,
)
from nexus_sdk.model.golang_proxy_repository_api_request import (
    GolangProxyRepositoryApiRequest,
)
from nexus_sdk.model.group_attributes import GroupAttributes
from nexus_sdk.model.group_blob_store_api_create_request import (
    GroupBlobStoreApiCreateRequest,
)
from nexus_sdk.model.group_blob_store_api_model import GroupBlobStoreApiModel
from nexus_sdk.model.group_blob_store_api_response import GroupBlobStoreApiResponse
from nexus_sdk.model.group_blob_store_api_update_request import (
    GroupBlobStoreApiUpdateRequest,
)
from nexus_sdk.model.group_deploy_attributes import GroupDeployAttributes
from nexus_sdk.model.helm_hosted_repository_api_request import (
    HelmHostedRepositoryApiRequest,
)
from nexus_sdk.model.helm_proxy_repository_api_request import (
    HelmProxyRepositoryApiRequest,
)
from nexus_sdk.model.hosted_storage_attributes import HostedStorageAttributes
from nexus_sdk.model.http_client_attributes import HttpClientAttributes
from nexus_sdk.model.http_client_attributes_with_preemptive_auth import (
    HttpClientAttributesWithPreemptiveAuth,
)
from nexus_sdk.model.http_client_connection_attributes import (
    HttpClientConnectionAttributes,
)
from nexus_sdk.model.http_client_connection_authentication_attributes import (
    HttpClientConnectionAuthenticationAttributes,
)
from nexus_sdk.model.http_client_connection_authentication_attributes_with_preemptive import (
    HttpClientConnectionAuthenticationAttributesWithPreemptive,
)
from nexus_sdk.model.iq_connection_verification_xo import IqConnectionVerificationXo
from nexus_sdk.model.iq_connection_xo import IqConnectionXo
from nexus_sdk.model.maven_attributes import MavenAttributes
from nexus_sdk.model.maven_group_repository_api_request import (
    MavenGroupRepositoryApiRequest,
)
from nexus_sdk.model.maven_hosted_api_repository import MavenHostedApiRepository
from nexus_sdk.model.maven_hosted_repository_api_request import (
    MavenHostedRepositoryApiRequest,
)
from nexus_sdk.model.maven_proxy_api_repository import MavenProxyApiRepository
from nexus_sdk.model.maven_proxy_repository_api_request import (
    MavenProxyRepositoryApiRequest,
)
from nexus_sdk.model.negative_cache_attributes import NegativeCacheAttributes
from nexus_sdk.model.npm_attributes import NpmAttributes
from nexus_sdk.model.npm_group_repository_api_request import (
    NpmGroupRepositoryApiRequest,
)
from nexus_sdk.model.npm_hosted_repository_api_request import (
    NpmHostedRepositoryApiRequest,
)
from nexus_sdk.model.npm_proxy_api_repository import NpmProxyApiRepository
from nexus_sdk.model.npm_proxy_repository_api_request import (
    NpmProxyRepositoryApiRequest,
)
from nexus_sdk.model.nuget_attributes import NugetAttributes
from nexus_sdk.model.nuget_group_repository_api_request import (
    NugetGroupRepositoryApiRequest,
)
from nexus_sdk.model.nuget_hosted_repository_api_request import (
    NugetHostedRepositoryApiRequest,
)
from nexus_sdk.model.nuget_proxy_api_repository import NugetProxyApiRepository
from nexus_sdk.model.nuget_proxy_repository_api_request import (
    NugetProxyRepositoryApiRequest,
)
from nexus_sdk.model.p2_proxy_repository_api_request import P2ProxyRepositoryApiRequest
from nexus_sdk.model.page import Page
from nexus_sdk.model.page_asset_xo import PageAssetXO
from nexus_sdk.model.page_component_xo import PageComponentXO
from nexus_sdk.model.page_tag_xo import PageTagXO
from nexus_sdk.model.page_task_xo import PageTaskXO
from nexus_sdk.model.proxy_attributes import ProxyAttributes
from nexus_sdk.model.pypi_group_repository_api_request import (
    PypiGroupRepositoryApiRequest,
)
from nexus_sdk.model.pypi_hosted_repository_api_request import (
    PypiHostedRepositoryApiRequest,
)
from nexus_sdk.model.pypi_proxy_repository_api_request import (
    PypiProxyRepositoryApiRequest,
)
from nexus_sdk.model.r_group_repository_api_request import RGroupRepositoryApiRequest
from nexus_sdk.model.r_hosted_repository_api_request import RHostedRepositoryApiRequest
from nexus_sdk.model.r_proxy_repository_api_request import RProxyRepositoryApiRequest
from nexus_sdk.model.raw_attributes import RawAttributes
from nexus_sdk.model.raw_group_repository_api_request import (
    RawGroupRepositoryApiRequest,
)
from nexus_sdk.model.raw_hosted_repository_api_request import (
    RawHostedRepositoryApiRequest,
)
from nexus_sdk.model.raw_proxy_repository_api_request import (
    RawProxyRepositoryApiRequest,
)
from nexus_sdk.model.read_ldap_server_xo import ReadLdapServerXo
from nexus_sdk.model.read_only_state import ReadOnlyState
from nexus_sdk.model.realm_api_xo import RealmApiXO
from nexus_sdk.model.replication_attributes import ReplicationAttributes
from nexus_sdk.model.replication_connection_xo import ReplicationConnectionXO
from nexus_sdk.model.replication_enable_xo import ReplicationEnableXO
from nexus_sdk.model.repository_xo import RepositoryXO
from nexus_sdk.model.result import Result
from nexus_sdk.model.role_xo_request import RoleXORequest
from nexus_sdk.model.role_xo_response import RoleXOResponse
from nexus_sdk.model.routing_rule_xo import RoutingRuleXO
from nexus_sdk.model.ruby_gems_group_repository_api_request import (
    RubyGemsGroupRepositoryApiRequest,
)
from nexus_sdk.model.ruby_gems_hosted_repository_api_request import (
    RubyGemsHostedRepositoryApiRequest,
)
from nexus_sdk.model.ruby_gems_proxy_repository_api_request import (
    RubyGemsProxyRepositoryApiRequest,
)
from nexus_sdk.model.s3_blob_store_api_advanced_bucket_connection import (
    S3BlobStoreApiAdvancedBucketConnection,
)
from nexus_sdk.model.s3_blob_store_api_bucket import S3BlobStoreApiBucket
from nexus_sdk.model.s3_blob_store_api_bucket_configuration import (
    S3BlobStoreApiBucketConfiguration,
)
from nexus_sdk.model.s3_blob_store_api_bucket_security import (
    S3BlobStoreApiBucketSecurity,
)
from nexus_sdk.model.s3_blob_store_api_encryption import S3BlobStoreApiEncryption
from nexus_sdk.model.s3_blob_store_api_model import S3BlobStoreApiModel
from nexus_sdk.model.saml_configuration_xo import SamlConfigurationXO
from nexus_sdk.model.script_result_xo import ScriptResultXO
from nexus_sdk.model.script_xo import ScriptXO
from nexus_sdk.model.simple_api_group_deploy_repository import (
    SimpleApiGroupDeployRepository,
)
from nexus_sdk.model.simple_api_group_repository import SimpleApiGroupRepository
from nexus_sdk.model.simple_api_hosted_repository import SimpleApiHostedRepository
from nexus_sdk.model.simple_api_proxy_repository import SimpleApiProxyRepository
from nexus_sdk.model.stack_trace_element import StackTraceElement
from nexus_sdk.model.storage_attributes import StorageAttributes
from nexus_sdk.model.support_zip_generator_request import SupportZipGeneratorRequest
from nexus_sdk.model.support_zip_xo import SupportZipXO
from nexus_sdk.model.tag_xo import TagXO
from nexus_sdk.model.task_xo import TaskXO
from nexus_sdk.model.throwable import Throwable
from nexus_sdk.model.update_ldap_server_xo import UpdateLdapServerXo
from nexus_sdk.model.upload_definition_xo import UploadDefinitionXO
from nexus_sdk.model.upload_field_definition_xo import UploadFieldDefinitionXO
from nexus_sdk.model.user_tokens_api_model import UserTokensApiModel
from nexus_sdk.model.yum_attributes import YumAttributes
from nexus_sdk.model.yum_group_repository_api_request import (
    YumGroupRepositoryApiRequest,
)
from nexus_sdk.model.yum_hosted_api_repository import YumHostedApiRepository
from nexus_sdk.model.yum_hosted_repository_api_request import (
    YumHostedRepositoryApiRequest,
)
from nexus_sdk.model.yum_proxy_repository_api_request import (
    YumProxyRepositoryApiRequest,
)
from nexus_sdk.model.yum_signing_repositories_attributes import (
    YumSigningRepositoriesAttributes,
)
