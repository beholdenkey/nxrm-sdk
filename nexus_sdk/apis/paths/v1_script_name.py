from nexus_sdk.paths.v1_script_name.get import ApiForget
from nexus_sdk.paths.v1_script_name.put import ApiForput
from nexus_sdk.paths.v1_script_name.delete import ApiFordelete


class V1ScriptName(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
