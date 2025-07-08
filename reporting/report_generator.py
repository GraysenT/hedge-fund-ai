import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from datetime import datetime

SIGNALS = Path("signal_logs")
PERF = Path("performance_logs")
REPORT_DIR = Path("reports/generated")
REPORT_DIR.mkdir(parents=True, exist_ok=True)

def load_data():
    signals = pd.concat([pd.read_csv(f) for f in SIGNALS.glob("signals_*.csv")], ignore_index=True)
    perf = pd.concat([pd.read_csv(f) for f in PERF.glob("performance_*.csv")], ignore_index=True)

    signals["date"] = pd.to_datetime(signals["date"])
    perf["date"] = pd.to_datetime(perf["date"])
    return signals, perf

def generate_charts(perf):
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=perf.groupby("date")["pnl"].sum().cumsum(), label="Cumulative PnL")
    plt.title("Portfolio Cumulative PnL")
    plt.tight_layout()
    chart_path = REPORT_DIR / "pnl_chart.png"
    plt.savefig(chart_path)
    plt.close()
    return chart_path

def render_html(perf, chart_path):
    env = Environment(loader=FileSystemLoader("reporting/templates"))
    template = env.get_template("report_template.html")

    grouped = perf.groupby("strategy")["pnl"].agg(["sum", "mean", "std", "count"])
    grouped["sharpe"] = grouped["mean"] / grouped["std"].replace(0, 1e-6)

    rendered = template.render(
        timestamp=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        stats=grouped.reset_index().to_dict(orient="records"),
        chart=str(chart_path.name)
    )

    html_path = REPORT_DIR / "report.html"
    with open(html_path, "w") as f:
        f.write(rendered)
    return html_path

def generate_pdf(html_path):
    pdf_path = html_path.with_suffix(".pdf")
    HTML(str(html_path)).write_pdf(str(pdf_path))
    print(f"📄 PDF saved to {pdf_path}")
    return pdf_path

def generate_full_report():
    print("📊 Generating investor-grade report...")
    _, perf = load_data()
    chart_path = generate_charts(perf)
    html_path = render_html(perf, chart_path)
    pdf_path = generate_pdf(html_path)
    print(f"✅ Report complete: {pdf_path}")