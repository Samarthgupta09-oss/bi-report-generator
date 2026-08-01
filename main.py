import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from analyze import load_data, get_summary
from visualize import (
    plot_sales_by_region,
    plot_profit_by_category,
    plot_monthly_trend,
    plot_top_products,
)
from generate_report import generate_report
import json
from datetime import datetime

DATA_PATH = "data/sales_data.csv"
REPORTS_DIR = "reports"
CHARTS_DIR = "reports/charts"

def run_pipeline():
    os.makedirs(REPORTS_DIR, exist_ok=True)
    os.makedirs(CHARTS_DIR, exist_ok=True)

    print("Step 1/3: Analyzing data...")
    df = load_data(DATA_PATH)
    summary = get_summary(df)

    with open(f"{REPORTS_DIR}/summary_stats.json", "w") as f:
        json.dump(summary, f, indent=2)
    print("  Analysis complete.")

    print("Step 2/3: Generating charts...")
    plot_sales_by_region(df, CHARTS_DIR)
    plot_profit_by_category(df, CHARTS_DIR)
    plot_monthly_trend(df, CHARTS_DIR)
    plot_top_products(df, CHARTS_DIR)
    print("  Charts saved to reports/charts/")

    print("Step 3/3: Generating AI report...")
    report_text = generate_report(summary)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f"{REPORTS_DIR}/bi_report_{timestamp}.md"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# Business Intelligence Report\n")
        f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        f.write(report_text)

    print(f"  Report saved to {output_path}")
    print("\nPipeline finished successfully.")

if __name__ == "__main__":
    run_pipeline()