import pandas as pd
import json

def load_data(path):
    df = pd.read_csv(path, encoding="latin1")
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    return df

def get_summary(df):
    summary = {}

    summary["total_sales"] = round(df["Sales"].sum(), 2)
    summary["total_profit"] = round(df["Profit"].sum(), 2)
    summary["total_orders"] = df["Order ID"].nunique()
    summary["avg_discount"] = round(df["Discount"].mean(), 3)
    summary["profit_margin_pct"] = round((df["Profit"].sum() / df["Sales"].sum()) * 100, 2)

    region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
    summary["sales_by_region"] = region_sales.round(2).to_dict()

    category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
    summary["sales_by_category"] = category_sales.round(2).to_dict()

    category_profit = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)
    summary["profit_by_category"] = category_profit.round(2).to_dict()

    subcat_profit = df.groupby("Sub-Category")["Profit"].sum().sort_values()
    summary["least_profitable_subcategories"] = subcat_profit.head(5).round(2).to_dict()
    summary["most_profitable_subcategories"] = subcat_profit.tail(5).round(2).to_dict()

    top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False)
    summary["top_5_products"] = top_products.head(5).round(2).to_dict()

    df["Month"] = df["Order Date"].dt.to_period("M").astype(str)
    monthly_sales = df.groupby("Month")["Sales"].sum()
    summary["monthly_sales_trend"] = monthly_sales.round(2).to_dict()

    segment_sales = df.groupby("Segment")["Sales"].sum().sort_values(ascending=False)
    summary["sales_by_segment"] = segment_sales.round(2).to_dict()

    high_discount_orders = df[df["Discount"] >= 0.3]
    summary["high_discount_order_count"] = int(len(high_discount_orders))
    summary["high_discount_avg_profit"] = round(high_discount_orders["Profit"].mean(), 2) if len(high_discount_orders) > 0 else 0

    return summary

if __name__ == "__main__":
    df = load_data("data/sales_data.csv")
    summary = get_summary(df)

    with open("reports/summary_stats.json", "w") as f:
        json.dump(summary, f, indent=2)

    print("Analysis complete. Summary saved to reports/summary_stats.json")
    print(f"Total Sales: {summary['total_sales']}")
    print(f"Total Profit: {summary['total_profit']}")
    print(f"Profit Margin: {summary['profit_margin_pct']}%")