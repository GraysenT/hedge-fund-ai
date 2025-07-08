from explainability.shap_explainer import explain_latest_prediction
from analytics.causal_inference import run_causal_inference

def show_explainability_dashboard():
    print("\n🧠 Explainability Dashboard:")
    print("1. SHAP model feature impact")
    explain_latest_prediction()

    print("\n2. Causal impact of features on PnL")
    run_causal_inference("logs/signal_feature_log.csv")

if __name__ == "__main__":
    show_explainability_dashboard()