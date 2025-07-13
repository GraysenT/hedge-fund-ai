from .deployment_order import DeploymentOrder
from .theater_map import get_agents_for_zone
from .deployment_registry import save_deployment

def simulate_theater_deployment():
    zone = "Commodities"
    agents = get_agents_for_zone(zone)

    orders = []
    for a in agents:
        order = DeploymentOrder(
            target_zone=zone,
            agent_id=a,
            operation_type="volatility_monitor",
            conditions={"trigger": "vol > 0.3"}
        )
        save_deployment(order)
        orders.append(order.serialize())

    return orders

if __name__ == "__main__":
    from pprint import pprint
    pprint(simulate_theater_deployment())