from nexus_sdk.paths.v1_security_roles_id.delete import ApiFordelete
from nexus_sdk.paths.v1_security_roles_id.get import ApiForget
from nexus_sdk.paths.v1_security_roles_id.put import ApiForput


class V1SecurityRolesId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
