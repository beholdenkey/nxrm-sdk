from nexus_sdk.paths.v1_system_license.get import ApiForget
from nexus_sdk.paths.v1_system_license.post import ApiForpost
from nexus_sdk.paths.v1_system_license.delete import ApiFordelete


class V1SystemLicense(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
