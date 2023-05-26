from nexus_sdk.paths.v1_security_user_tokens.delete import ApiFordelete
from nexus_sdk.paths.v1_security_user_tokens.get import ApiForget
from nexus_sdk.paths.v1_security_user_tokens.put import ApiForput


class V1SecurityUserTokens(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
