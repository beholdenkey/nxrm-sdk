from nexus_sdk.paths.v1_security_ldap_name.delete import ApiFordelete
from nexus_sdk.paths.v1_security_ldap_name.get import ApiForget
from nexus_sdk.paths.v1_security_ldap_name.put import ApiForput


class V1SecurityLdapName(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
