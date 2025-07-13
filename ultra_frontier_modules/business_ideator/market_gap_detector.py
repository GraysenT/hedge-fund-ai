import pandas as pd
import json
from data.alt_feed_integrator import fetch_global_sentiment_data

def detect_unmet_needs(sentiment_df: pd.DataFrame, threshold: float = -0.3):
    """
    Detect topics with persistent negative sentiment and low current solution presence.
    """
    sentiment_df["need_score"] = sentiment_df["negativity"] - sentiment_df["solution_coverage"]
    opportunities = sentiment_df[sentiment_df["need_score"] < threshold]
    return opportunities.sort_values(by="need_score")

def generate_business_ideas():
    sentiment_data = fetch_global_sentiment_data()
    needs = detect_unmet_needs(sentiment_data)
    ideas = []
    for _, row in needs.iterrows():
        idea = {
            "topic": row["topic"],
            "need_score": row["need_score"],
            "proposed_business": f"A platform to address {row['topic']} via novel approach."
        }
        ideas.append(idea)
    return ideas

if __name__ == "__main__":
    ideas = generate_business_ideas()
    print(json.dumps(ideas, indent=2))