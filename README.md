# 🛍️ Zara Sales Analytics — End-to-End EDA & BI Project

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-EDA-green?logo=pandas)
![SQL](https://img.shields.io/badge/SQL-Analytics-orange?logo=postgresql)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

> A complete Exploratory Data Analysis and Business Intelligence project on **252 Zara fashion products**, uncovering actionable insights around pricing, category performance, promotions, and growth opportunities.

---

## 📌 Project Overview

| Property | Detail |
|---|---|
| **Dataset** | Zara.com scraped product data — Feb 2024 |
| **Records** | 252 products |
| **Columns** | 16 (Product ID, Price, Sales Volume, Category, Section, Promotion, etc.) |
| **Tools Used** | Python (Pandas, Matplotlib, Seaborn), SQL, HTML/CSS |
| **Revenue Analyzed** | $38.99M total across all products |

---

## 📁 Project Structure

```
zara-eda-project/
│
├── data/
│   └── zara.csv                    # Raw dataset
│
├── charts/
│   ├── chart1_price_distribution.png
│   ├── chart2_sales_distribution.png
│   ├── chart3_top10_revenue.png
│   ├── chart4_revenue_by_category.png
│   ├── chart5_boxplot_price.png
│   ├── chart6_promotion_impact.png
│   ├── chart7_correlation_heatmap.png
│   ├── chart8_price_vs_sales.png
│   ├── chart9_section_pie.png
│   └── chart10_revenue_by_price_bucket.png
│
├── zara_dashboard.html             # Interactive BI Dashboard
├── zara_eda_report.md              # Full EDA Report
├── zara_sql_queries.sql            # All SQL Business Queries
└── README.md                       # This file
```

---

## 📊 Key KPIs

| KPI | Value |
|---|---|
| Total Revenue | **$38.99M** |
| Total Units Sold | **459,573** |
| Total Products | **252** |
| Average Price | **$86.25** |
| Avg Revenue per Product | **$154,716** |
| Top Product Revenue | **$651,521** (Vintage Leather Bomber Jacket) |

---

## 🔍 EDA Highlights

### Descriptive Statistics
| Metric | Price (USD) | Sales Volume |
|---|---|---|
| Mean | $86.25 | 1,824 |
| Median | $79.90 | 1,840 |
| Mode | $89.90 | — |
| Std Dev | $52.08 | 697.7 |
| Min | $7.99 | 529 |
| Max | $439.00 | 2,989 |

### Category Performance
| Category | Products | Revenue | Share |
|---|---|---|---|
| Jackets | 140 | $26.6M | 68.2% |
| Sweaters | 41 | $4.1M | 10.5% |
| Shoes | 31 | $3.75M | 9.6% |
| T-Shirts | 32 | $3.7M | 9.5% |
| Jeans | 8 | $0.86M | 2.2% |

### Correlation Analysis
- **Price ↔ Revenue: 0.75** — Strong positive (price is the #1 revenue driver)
- **Sales Volume ↔ Revenue: 0.50** — Moderate positive
- **Price ↔ Sales Volume: -0.07** — No meaningful negative effect

---

## 🗄️ SQL Analysis Summary

10 SQL queries written covering:
1. Top 5 products by revenue
2. Revenue by product category
3. Promotion impact analysis
4. Seasonal vs non-seasonal performance
5. Product placement analysis
6. Price tier segmentation
7. Section (MAN vs WOMAN) comparison
8. Low-performing products detection
9. High price + high volume "best of both worlds" products
10. Revenue ranking with window functions (RANK, NTILE)

---

## 💡 Top Business Insights

1. **Jackets = 68.2% of revenue** — single most important category
2. **WOMAN section critically underserved** — only 13.5% of products, massive growth opportunity
3. **Price is the #1 revenue lever** — 0.75 correlation, raising prices doesn't hurt volume
4. **Promotions lift revenue +15.8%** — driven by higher-priced items being promoted
5. **Jeans heavily underrepresented** — only 8 SKUs for a global fashion brand
6. **Price sweet spot: $60–$150** — 63.9% of total revenue
7. **Front-of-store placement boosts sales** by ~5% vs end-cap

---

## 🚀 Actionable Recommendations

| Priority | Action | Expected Impact |
|---|---|---|
| 🔴 Critical | Expand WOMAN section to 100+ products | +$5–8M revenue |
| 🟡 High | Place premium jackets at front-of-store | +5–8% volume |
| 🟡 High | Grow jeans SKUs from 8 → 25+ | +$1.5M revenue |
| 🟢 Medium | Apply promotions to $150+ items | +15% on flagged SKUs |
| 🟢 Medium | Introduce more $60–$100 products | Optimal volume×margin |

---

## 🛠️ How to Run

```bash
# Clone the repo
git clone https://github.com/yourusername/zara-eda-project.git
cd zara-eda-project

# Install dependencies
pip install pandas matplotlib seaborn numpy

# Run the analysis
python zara_eda.py

# Open the dashboard
open zara_dashboard.html
```

---

## 📸 Sample Visualizations

> Charts available in the `/charts` folder — includes price histogram, revenue bar charts, correlation heatmap, box plots, scatter plots, and more.

---

## 👤 Author

**Your Name**  
📧 your.email@example.com  
🔗 [LinkedIn](https://linkedin.com/in/yourprofile) | [Portfolio](https://yourportfolio.com)

---

## 📄 License

MIT License — free to use for learning and portfolio purposes.

---

*⭐ If you found this project useful, please give it a star!*
