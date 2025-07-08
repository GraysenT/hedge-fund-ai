from evolve import EvolutionRunner

# Replace this with dynamic weights if needed
base_weights = {
    "US_Trend": 0.3,
    "UK_Value": 0.2,
    "Crypto_RSI": 0.5
}

runner = EvolutionRunner()
result = runner.run(base_weights)

print("✅ Daily Evolution Run Complete")
print("Muted:", result["muted"])
print("Alerts:")
for alert in result["alerts"]:
    print(" •", alert)
print("Saved to:", result["snapshot_file"])
