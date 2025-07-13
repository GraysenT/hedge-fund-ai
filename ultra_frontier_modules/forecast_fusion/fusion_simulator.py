from .fused_forecast import FusedForecast
from .context_blender import blend_context_weights

def simulate_fusion():
    contexts = ["CPI Week", "Tech Breakout"]
    forecast = FusedForecast(
        asset="AAPL",
        short_term_sig=0.8,
        long_term_sig=0.5,
        macro_view=0.3,
        context_tags=contexts
    )
    adjustment = blend_context_weights(contexts)
    adjusted_score = round(forecast.score + adjustment, 4)

    return {
        "base_score": forecast.score,
        "adjustment": adjustment,
        "final_score": adjusted_score,
        "conflict_level": forecast.conflict,
        "contexts": forecast.contexts
    }

if __name__ == "__main__":
    from pprint import pprint
    pprint(simulate_fusion())