echo "📦 Creating system snapshot export..."

TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
ZIP_NAME="hedge_fund_ai_snapshot_$TIMESTAMP.zip"

zip -r $ZIP_NAME \
  dashboards/ \
  execution/ \
  portfolio_ai/ \
  reinforcement/ \
  simulation/ \
  alerts/ \
  risk_control/ \
  models/ \
  strategies/ \
  cloud/ \
  audit/ \
  memory/ \
  reports/ \
  requirements.txt \
  Dockerfile \
  *.py

echo "✅ Deployment snapshot created: $ZIP_NAME"