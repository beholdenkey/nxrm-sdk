# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from nexus_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    SECURITY_MANAGEMENT_ANONYMOUS_ACCESS = "Security Management: Anonymous Access"
    SECURITY_MANAGEMENT = "Security management"
    SECURITY_MANAGEMENT_USERS = "Security management: users"
    SECURITY_MANAGEMENT_JWT = "Security management: JWT"
    SECURITY_MANAGEMENT_PRIVILEGES = "Security management: privileges"
    SECURITY_MANAGEMENT_REALMS = "Security management: realms"
    SECURITY_MANAGEMENT_ROLES = "Security management: roles"
    TASKS = "Tasks"
    BLOB_STORE = "Blob store"
    LIFECYCLE = "Lifecycle"
    READONLY = "Read-only"
    SECURITY_CERTIFICATES = "Security: certificates"
    ASSETS = "Assets"
    COMPONENTS = "Components"
    REPOSITORY_MANAGEMENT = "Repository Management"
    CONTENT_SELECTORS = "Content selectors"
    ROUTING_RULES = "Routing rules"
    SEARCH = "Search"
    FORMATS = "Formats"
    SCRIPT = "Script"
    EMAIL = "Email"
    STATUS = "Status"
    SUPPORT = "Support"
    SECURITY_MANAGEMENT_LDAP = "Security management: LDAP"
    TAGS = "Tags"
    MANAGE_IQ_SERVER_CONFIGURATION = "Manage IQ server configuration"
    PRODUCT_LICENSING = "Product licensing"
    SECURITY_ATLASSIAN_CROWD = "Security: Atlassian Crowd"
    SECURITY_MANAGEMENT_USER_TOKENS = "Security management: user tokens"
    REPLICATION = "Replication"
    STAGING = "Staging"
    AZURE_BLOB_STORE = "Azure blob store"
    SECURITY_MANAGEMENT_SAML = "Security management: SAML"
