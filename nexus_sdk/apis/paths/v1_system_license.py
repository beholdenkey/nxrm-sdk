from nexus_sdk.paths.v1_system_license.delete import ApiFordelete
from nexus_sdk.paths.v1_system_license.get import ApiForget
from nexus_sdk.paths.v1_system_license.post import ApiForpost


class V1SystemLicense(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
