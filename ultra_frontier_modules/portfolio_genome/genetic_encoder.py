import hashlib
import json

def encode_strategy_to_gene(strategy_config: dict) -> str:
    """
    Turns a strategy's configuration into a fixed-length genetic string.
    """
    serialized = json.dumps(strategy_config, sort_keys=True)
    hashed = hashlib.sha256(serialized.encode()).hexdigest()
    return hashed[:32]  # Shorter gene representation

def decode_gene_to_signature(gene: str):
    """
    Simulate metadata attached to gene (for mock decoding/display).
    """
    return {
        "risk_profile": gene[:4],
        "signal_entropy": gene[4:8],
        "architecture_hint": gene[8:12],
        "historical_fitness": gene[12:16]
    }