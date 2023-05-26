from nexus_sdk.paths.v1_security_ldap_name.get import ApiForget
from nexus_sdk.paths.v1_security_ldap_name.put import ApiForput
from nexus_sdk.paths.v1_security_ldap_name.delete import ApiFordelete


class V1SecurityLdapName(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
