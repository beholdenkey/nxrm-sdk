from nexus_sdk.paths.v1_security_content_selectors_name.get import ApiForget
from nexus_sdk.paths.v1_security_content_selectors_name.put import ApiForput
from nexus_sdk.paths.v1_security_content_selectors_name.delete import ApiFordelete


class V1SecurityContentSelectorsName(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass