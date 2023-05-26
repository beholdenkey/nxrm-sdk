from nexus_sdk.paths.beta_replication_connection_name.get import ApiForget
from nexus_sdk.paths.beta_replication_connection_name.put import ApiForput
from nexus_sdk.paths.beta_replication_connection_name.delete import ApiFordelete


class BetaReplicationConnectionName(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass