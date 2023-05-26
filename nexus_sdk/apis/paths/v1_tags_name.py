from nexus_sdk.paths.v1_tags_name.get import ApiForget
from nexus_sdk.paths.v1_tags_name.put import ApiForput
from nexus_sdk.paths.v1_tags_name.delete import ApiFordelete


class V1TagsName(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
