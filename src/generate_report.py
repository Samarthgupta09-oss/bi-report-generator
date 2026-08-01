import json
import os
from datetime import datetime
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def build_prompt(summary):
    prompt = f"""
You are a senior business intelligence analyst. Write a clear, professional business report based on the data below. Use natural, human-sounding language, not robotic bullet dumps. Structure the report with these sections: Executive Summary, Sales Performance, Regional Analysis, Category & Product Insights, Discounting Impact, and Recommendations.

Data:
Total Sales: {summary['total_sales']}
Total Profit: {summary['total_profit']}
Total Orders: {summary['total_orders']}
Average Discount: {summary['avg_discount']}
Profit Margin: {summary['profit_margin_pct']}%

Sales by Region: {summary['sales_by_region']}
Sales by Category: {summary['sales_by_category']}
Profit by Category: {summary['profit_by_category']}
Most Profitable Sub-Categories: {summary['most_profitable_subcategories']}
Least Profitable Sub-Categories: {summary['least_profitable_subcategories']}
Top 5 Products by Sales: {summary['top_5_products']}
Monthly Sales Trend: {summary['monthly_sales_trend']}
Sales by Segment: {summary['sales_by_segment']}
High Discount Orders (30%+ discount): {summary['high_discount_order_count']} orders, average profit {summary['high_discount_avg_profit']}

Keep it concise but insightful, around 500-700 words. End with 3-4 actionable recommendations for the business.
"""
    return prompt

def generate_report(summary):
    prompt = build_prompt(summary)
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=2000
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    with open("reports/summary_stats.json", "r") as f:
        summary = json.load(f)

    report_text = generate_report(summary)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f"reports/bi_report_{timestamp}.md"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# Business Intelligence Report\n")
        f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        f.write(report_text)

    print(f"Report generated successfully: {output_path}")