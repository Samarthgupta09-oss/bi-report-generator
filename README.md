# Automated BI Report Generation from Tabular Data

An end-to-end pipeline that takes raw sales data (CSV) and automatically generates a comprehensive business intelligence report in natural language, complete with charts and actionable recommendations — powered by generative AI.

## Overview

Manually writing business reports from spreadsheets is slow and repetitive. This project automates the entire workflow: it reads a CSV of sales data, computes key business metrics, generates visual charts, and then uses a large language model (Llama 3.3 via Groq) to write a human-readable report with an executive summary, regional analysis, category insights, and recommendations.

## Features

- Automated statistical analysis of sales data (revenue, profit, margins, trends)
- AI-generated natural language business report (Executive Summary, Regional Analysis, Category Insights, Recommendations)
- Auto-generated visual charts (sales by region, profit by category, monthly trend, top products)
- Interactive web app (Streamlit) — upload CSV, get instant report in browser
- No-code interface for non-technical users
- Single-command pipeline execution
- Timestamped report versioning

## Tech Stack

- Python 3.13
- Pandas, NumPy for data processing
- Matplotlib, Seaborn for visualization
- Groq API (Llama 3.3 70B) for natural language report generation
- Streamlit for web app interface
- python-dotenv for environment variable management

## Project Structure
bi-report-generator/
├── data/
│ └── sales_data.csv
├── src/
│ ├── analyze.py
│ ├── visualize.py
│ └── generate_report.py
├── notebooks/
│ └── eda.ipynb
├── reports/
│ ├── charts/
│ └── bi_report_*.md
├── app.py
├── main.py
├── requirements.txt
└── README.md
## Setup

1. Clone the repository
2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Add your Groq API key
Create a `.env` file in the root directory:
GROQ_API_KEY=your_api_key_here
Get a free API key from [console.groq.com/keys](https://console.groq.com/keys)

5. Add your dataset
Place your CSV file in the `data/` folder as `sales_data.csv`. This project is built for the Superstore dataset structure but can be adapted to other tabular sales data.

## Usage

Run the full pipeline:
python main.py
This will:
1. Analyze the dataset and compute summary statistics
2. Generate visual charts in `reports/charts/`
3. Generate a full business intelligence report in `reports/`

You can also run individual stages:
python src/analyze.py
python src/visualize.py
python src/generate_report.py
