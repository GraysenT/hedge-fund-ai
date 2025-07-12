# risk_control/patch_macro_sentiment.py

import macro_sentiment

def patch_macro_sentiment(data):
    try:
        result = macro_sentiment.analyze(data)
    except Exception as e:
        print(f"Error in macro_sentiment module: {e}")
        result = None

    if result is None or not isinstance(result, dict):
        print("Applying patch to macro_sentiment module...")
        result = {
            "sentiment": "neutral",
            "confidence": 0.5
        }

    return result