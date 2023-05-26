from nexus_sdk.paths.v1_email.delete import ApiFordelete
from nexus_sdk.paths.v1_email.get import ApiForget
from nexus_sdk.paths.v1_email.put import ApiForput


class V1Email(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
