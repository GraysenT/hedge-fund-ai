import json
import uuid

def export_as_nft(seed):
    data = {
        "id": seed.id,
        "vision": seed.vision,
        "capital": seed.capital,
        "growth_bias": seed.growth_bias,
        "success": seed.success
    }
    filename = f"nfts/{seed.vision.replace(' ', '_')}-{uuid.uuid4().hex[:6]}.json"
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
    print(f"🧬 NFT Exported: {filename}")