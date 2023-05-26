from nexus_sdk.paths.v1_routing_rules_name.get import ApiForget
from nexus_sdk.paths.v1_routing_rules_name.put import ApiForput
from nexus_sdk.paths.v1_routing_rules_name.delete import ApiFordelete


class V1RoutingRulesName(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
