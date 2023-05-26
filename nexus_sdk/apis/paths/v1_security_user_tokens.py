from nexus_sdk.paths.v1_security_user_tokens.get import ApiForget
from nexus_sdk.paths.v1_security_user_tokens.put import ApiForput
from nexus_sdk.paths.v1_security_user_tokens.delete import ApiFordelete


class V1SecurityUserTokens(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
