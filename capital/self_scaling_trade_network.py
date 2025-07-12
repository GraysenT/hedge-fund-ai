class SelfScalingTradeNetwork:
    def __init__(self):
        self.trade_networks = []

    def scale_trade_network(self, universe_name, scale_factor):
        """Scale the trade network in the multiverse."""
        scaling = {"universe": universe_name, "scale_factor": scale_factor}
        self.trade_networks.append(scaling)
        print(f"Scaled trade network in {universe_name} with factor: {scale_factor}")
    
    def get_scaled_networks(self):
        return self.trade_networks