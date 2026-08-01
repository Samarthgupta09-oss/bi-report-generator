import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_style("whitegrid")
plt.rcParams["figure.dpi"] = 120

def load_data(path):
    df = pd.read_csv(path, encoding="latin1")
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    return df

def plot_sales_by_region(df, output_dir):
    region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
    plt.figure(figsize=(8, 5))
    sns.barplot(x=region_sales.index, y=region_sales.values, hue=region_sales.index, palette="viridis", legend=False)
    plt.title("Total Sales by Region")
    plt.ylabel("Sales ($)")
    plt.xlabel("Region")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/sales_by_region.png")
    plt.close()

def plot_profit_by_category(df, output_dir):
    cat_profit = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)
    colors = ["#2ecc71" if v >= 0 else "#e74c3c" for v in cat_profit.values]
    plt.figure(figsize=(8, 5))
    sns.barplot(x=cat_profit.index, y=cat_profit.values, hue=cat_profit.index, palette=colors, legend=False)
    plt.title("Total Profit by Category")
    plt.ylabel("Profit ($)")
    plt.xlabel("Category")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/profit_by_category.png")
    plt.close()

def plot_monthly_trend(df, output_dir):
    df["Month"] = df["Order Date"].dt.to_period("M").astype(str)
    monthly = df.groupby("Month")["Sales"].sum()
    plt.figure(figsize=(12, 5))
    plt.plot(monthly.index, monthly.values, marker="o", color="#3498db", linewidth=2)
    plt.title("Monthly Sales Trend")
    plt.ylabel("Sales ($)")
    plt.xlabel("Month")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/monthly_sales_trend.png")
    plt.close()

def plot_top_products(df, output_dir):
    top = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)
    plt.figure(figsize=(9, 6))
    sns.barplot(x=top.values, y=top.index, hue=top.index, palette="mako", legend=False)
    plt.title("Top 10 Products by Sales")
    plt.xlabel("Sales ($)")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/top_products.png")
    plt.close()

if __name__ == "__main__":
    output_dir = "reports/charts"
    os.makedirs(output_dir, exist_ok=True)

    df = load_data("data/sales_data.csv")

    plot_sales_by_region(df, output_dir)
    plot_profit_by_category(df, output_dir)
    plot_monthly_trend(df, output_dir)
    plot_top_products(df, output_dir)

    print(f"Charts generated in {output_dir}/")