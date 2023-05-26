from nexus_sdk.paths.v1_security_saml.delete import ApiFordelete
from nexus_sdk.paths.v1_security_saml.get import ApiForget
from nexus_sdk.paths.v1_security_saml.put import ApiForput


class V1SecuritySaml(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
