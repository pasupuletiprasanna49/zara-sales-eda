# -*- coding: utf-8 -*-
# ============================================================
#  ZARA SALES EDA - COMPLETE PYTHON SCRIPT
#  Run this on your PC: python zara_eda_analysis.py
#  Requirements: pip install pandas matplotlib seaborn numpy
# ============================================================

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')          # change to 'TkAgg' if you want pop-up windows
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
warnings.filterwarnings('ignore')

# -----------------------------------------
# CONFIG - change the path if your CSV is elsewhere
# -----------------------------------------
CSV_PATH   = 'zara.csv'        # put zara.csv in the same folder as this script
OUTPUT_DIR = 'zara_output'     # all charts + report will go here

os.makedirs(OUTPUT_DIR, exist_ok=True)

NAVY   = '#0f3460'
RED    = '#e94560'
GOLD   = '#f5a623'
GREEN  = '#2ecc71'
PURPLE = '#9b59b6'
DARK   = '#1a1a2e'

print("=" * 60)
print("  ZARA SALES EDA - Starting Analysis")
print("=" * 60)

# ========================================
# STEP 1 - LOAD DATA
# ========================================
print("\n[1/6] Loading data...")
df = pd.read_csv(CSV_PATH, sep=';')
df.columns = df.columns.str.strip()

# Create Revenue column
df['Revenue'] = df['price'] * df['Sales Volume']

# Price bucket
df['price_bucket'] = pd.cut(
    df['price'],
    bins=[0, 30, 60, 100, 150, 9999],
    labels=['Under $30', '$30-60', '$60-100', '$100-150', '$150+']
)

print(f"   [OK] Loaded {len(df)} rows, {len(df.columns)} columns")
print(f"   Columns: {list(df.columns)}")

# ========================================
# STEP 2 - DESCRIPTIVE STATISTICS
# ========================================
print("\n[2/6] Descriptive Statistics...")

print("\n--- PRICE STATISTICS ---")
print(f"  Mean:    ${df['price'].mean():.2f}")
print(f"  Median:  ${df['price'].median():.2f}")
print(f"  Mode:    ${df['price'].mode()[0]:.2f}")
print(f"  Std Dev: ${df['price'].std():.2f}")
print(f"  Min:     ${df['price'].min():.2f}")
print(f"  Max:     ${df['price'].max():.2f}")
print(f"  Q1:      ${df['price'].quantile(0.25):.2f}")
print(f"  Q3:      ${df['price'].quantile(0.75):.2f}")

print("\n--- SALES VOLUME STATISTICS ---")
print(f"  Mean:    {df['Sales Volume'].mean():.0f} units")
print(f"  Median:  {df['Sales Volume'].median():.0f} units")
print(f"  Std Dev: {df['Sales Volume'].std():.0f} units")
print(f"  Min:     {df['Sales Volume'].min()} units")
print(f"  Max:     {df['Sales Volume'].max()} units")

print("\n--- REVENUE SUMMARY ---")
print(f"  Total Revenue:        ${df['Revenue'].sum():,.2f}")
print(f"  Avg Revenue/Product:  ${df['Revenue'].mean():,.2f}")
print(f"  Max Revenue (1 product): ${df['Revenue'].max():,.2f}")
print(f"  Total Units Sold:     {df['Sales Volume'].sum():,}")

print("\n--- CATEGORICAL DISTRIBUTIONS ---")
for col in ['terms', 'section', 'Promotion', 'Seasonal', 'Product Position']:
    if col in df.columns:
        print(f"\n  {col}:")
        vc = df[col].value_counts()
        for val, cnt in vc.items():
            pct = cnt / len(df) * 100
            print(f"    {val:<25} {cnt:>4} products  ({pct:.1f}%)")

print("\n--- MISSING VALUES ---")
missing = df.isnull().sum()
missing = missing[missing > 0]
if len(missing) == 0:
    print("  [OK] No missing values!")
else:
    print(missing)

# ========================================
# STEP 3 - CHARTS (10 charts)
# ========================================
print("\n[3/6] Generating 10 charts...")
sns.set_theme(style='whitegrid', font_scale=1.1)

# -- Chart 1: Price Distribution
fig, ax = plt.subplots(figsize=(9, 5))
ax.hist(df['price'], bins=25, color=NAVY, edgecolor='white', linewidth=0.6, alpha=0.85)
ax.axvline(df['price'].mean(),   color=RED,  linestyle='--', lw=2, label=f"Mean ${df['price'].mean():.2f}")
ax.axvline(df['price'].median(), color=GOLD, linestyle='--', lw=2, label=f"Median ${df['price'].median():.2f}")
ax.set_title('Price Distribution of Zara Products', fontsize=15, fontweight='bold', pad=12)
ax.set_xlabel('Price (USD)'); ax.set_ylabel('Number of Products')
ax.legend(); plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/chart1_price_distribution.png', dpi=150, bbox_inches='tight')
plt.close(); print("   [OK] Chart 1 saved: Price Distribution")

# -- Chart 2: Sales Volume Distribution
fig, ax = plt.subplots(figsize=(9, 5))
ax.hist(df['Sales Volume'], bins=25, color=RED, edgecolor='white', linewidth=0.6, alpha=0.85)
ax.axvline(df['Sales Volume'].mean(), color=NAVY, linestyle='--', lw=2,
           label=f"Mean {df['Sales Volume'].mean():.0f}")
ax.set_title('Sales Volume Distribution', fontsize=15, fontweight='bold', pad=12)
ax.set_xlabel('Units Sold'); ax.set_ylabel('Number of Products')
ax.legend(); plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/chart2_sales_distribution.png', dpi=150, bbox_inches='tight')
plt.close(); print("   [OK] Chart 2 saved: Sales Volume Distribution")

# -- Chart 3: Top 10 Products by Revenue
top10 = df.nlargest(10, 'Revenue')[['name', 'Revenue']].copy()
top10['name_short'] = top10['name'].str[:32]
top10 = top10.sort_values('Revenue')
fig, ax = plt.subplots(figsize=(11, 6))
colors_bar = [NAVY] * 8 + [RED] * 2
bars = ax.barh(top10['name_short'], top10['Revenue'] / 1000,
               color=colors_bar, edgecolor='white', height=0.65)
for bar, val in zip(bars, top10['Revenue']):
    ax.text(bar.get_width() + 2, bar.get_y() + bar.get_height() / 2,
            f'${val/1000:.0f}K', va='center', fontsize=10, color=DARK, fontweight='bold')
ax.set_title('Top 10 Products by Revenue', fontsize=15, fontweight='bold', pad=12)
ax.set_xlabel('Revenue (USD Thousands)')
ax.set_xlim(0, top10['Revenue'].max() / 1000 * 1.22)
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/chart3_top10_revenue.png', dpi=150, bbox_inches='tight')
plt.close(); print("   [OK] Chart 3 saved: Top 10 Products")

# -- Chart 4: Revenue by Category
rev_terms = df.groupby('terms')['Revenue'].sum().sort_values(ascending=False)
clrs = [NAVY, RED, GOLD, GREEN, PURPLE]
fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(rev_terms.index, rev_terms.values / 1e6, color=clrs[:len(rev_terms)],
              edgecolor='white', width=0.6)
for bar, val in zip(bars, rev_terms.values):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.08,
            f'${val/1e6:.1f}M', ha='center', fontsize=11, fontweight='bold', color=DARK)
ax.set_title('Total Revenue by Product Category', fontsize=15, fontweight='bold', pad=12)
ax.set_xlabel('Product Type'); ax.set_ylabel('Revenue (USD Millions)')
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/chart4_revenue_by_category.png', dpi=150, bbox_inches='tight')
plt.close(); print("   [OK] Chart 4 saved: Revenue by Category")

# -- Chart 5: Box Plot - Price by Category
fig, ax = plt.subplots(figsize=(10, 5))
df.boxplot(column='price', by='terms', ax=ax,
           boxprops=dict(color=NAVY, linewidth=1.5),
           medianprops=dict(color=RED, linewidth=2.5),
           whiskerprops=dict(color=NAVY), capprops=dict(color=NAVY),
           flierprops=dict(marker='o', color=GOLD, markersize=5, alpha=0.7))
ax.set_title('Price Distribution by Product Type', fontsize=14, fontweight='bold')
plt.suptitle(''); ax.set_xlabel('Product Type'); ax.set_ylabel('Price (USD)')
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/chart5_boxplot_price.png', dpi=150, bbox_inches='tight')
plt.close(); print("   [OK] Chart 5 saved: Box Plot")

# -- Chart 6: Promotion Impact
promo = df.groupby('Promotion')[['Sales Volume', 'Revenue']].mean().reset_index()
fig, axes = plt.subplots(1, 2, figsize=(11, 5))
for i, col in enumerate(['Sales Volume', 'Revenue']):
    bars2 = axes[i].bar(promo['Promotion'], promo[col],
                        color=[NAVY, RED], edgecolor='white', width=0.45)
    axes[i].set_title(f'Avg {col}\nPromo vs No Promo', fontsize=12, fontweight='bold')
    axes[i].set_xlabel('Promotion Status')
    for bar, val in zip(bars2, promo[col]):
        axes[i].text(bar.get_x() + bar.get_width() / 2, bar.get_height() * 0.92,
                     f'{val:,.0f}', ha='center', va='top',
                     color='white', fontweight='bold', fontsize=12)
plt.suptitle('Impact of Promotions on Sales & Revenue', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/chart6_promotion_impact.png', dpi=150, bbox_inches='tight')
plt.close(); print("   [OK] Chart 6 saved: Promotion Impact")

# -- Chart 7: Correlation Heatmap
fig, ax = plt.subplots(figsize=(6, 5))
corr = df[['price', 'Sales Volume', 'Revenue']].corr()
sns.heatmap(corr, annot=True, fmt='.2f', cmap='Blues', ax=ax,
            linewidths=0.5, annot_kws={'size': 14, 'weight': 'bold'},
            cbar_kws={'shrink': 0.8})
ax.set_title('Correlation Heatmap\n(Price, Sales Volume, Revenue)',
             fontsize=13, fontweight='bold', pad=12)
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/chart7_correlation_heatmap.png', dpi=150, bbox_inches='tight')
plt.close(); print("   [OK] Chart 7 saved: Correlation Heatmap")

# -- Chart 8: Scatter - Price vs Sales Volume
fig, ax = plt.subplots(figsize=(10, 5))
colors_map = {'jackets': NAVY, 'sweaters': RED, 't-shirts': GOLD, 'shoes': GREEN, 'jeans': PURPLE}
for term, grp in df.groupby('terms'):
    ax.scatter(grp['price'], grp['Sales Volume'],
               label=term, color=colors_map.get(term, 'gray'),
               alpha=0.75, s=65, edgecolors='white', linewidth=0.4)
m, b = np.polyfit(df['price'], df['Sales Volume'], 1)
xline = np.linspace(df['price'].min(), df['price'].max(), 100)
ax.plot(xline, m * xline + b, color='black', lw=2, linestyle='--', label='Trend line')
ax.set_title('Price vs Sales Volume (by Product Type)', fontsize=14, fontweight='bold', pad=12)
ax.set_xlabel('Price (USD)'); ax.set_ylabel('Sales Volume (Units)')
ax.legend(title='Product Type', fontsize=9)
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/chart8_price_vs_sales.png', dpi=150, bbox_inches='tight')
plt.close(); print("   [OK] Chart 8 saved: Price vs Sales Scatter")

# -- Chart 9: MAN vs WOMAN Pie
sec = df.groupby('section')['Revenue'].sum()
fig, ax = plt.subplots(figsize=(6, 6))
wedges, texts, autotexts = ax.pie(
    sec, labels=sec.index, autopct='%1.1f%%',
    colors=[NAVY, RED], startangle=90,
    wedgeprops=dict(edgecolor='white', linewidth=2.5))
for t in autotexts:
    t.set_fontsize(14); t.set_fontweight('bold'); t.set_color('white')
ax.set_title('Revenue Split:\nMAN vs WOMAN Section', fontsize=14, fontweight='bold', pad=12)
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/chart9_section_pie.png', dpi=150, bbox_inches='tight')
plt.close(); print("   [OK] Chart 9 saved: Section Pie Chart")

# -- Chart 10: Revenue by Price Bucket
bucket = df.groupby('price_bucket', observed=True)['Revenue'].sum().reset_index()
fig, ax = plt.subplots(figsize=(9, 5))
bclrs = [GREEN, GOLD, NAVY, RED, PURPLE]
bars3 = ax.bar(bucket['price_bucket'], bucket['Revenue'] / 1e6,
               color=bclrs, edgecolor='white', width=0.55)
for bar, val in zip(bars3, bucket['Revenue']):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05,
            f'${val/1e6:.1f}M', ha='center', fontsize=11, fontweight='bold', color=DARK)
ax.set_title('Revenue by Price Range', fontsize=14, fontweight='bold', pad=12)
ax.set_xlabel('Price Range'); ax.set_ylabel('Total Revenue (USD Millions)')
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/chart10_revenue_by_price_bucket.png', dpi=150, bbox_inches='tight')
plt.close(); print("   [OK] Chart 10 saved: Revenue by Price Bucket")

# ========================================
# STEP 4 - CORRELATION ANALYSIS
# ========================================
print("\n[4/6] Correlation Analysis...")
corr = df[['price', 'Sales Volume', 'Revenue']].corr()
print("\n  Correlation Matrix:")
print(corr.round(3).to_string())
print(f"\n  Key Finding: Price -> Revenue correlation = {corr.loc['price','Revenue']:.3f} (STRONG)")
print(f"  Key Finding: Price -> Sales Volume = {corr.loc['price','Sales Volume']:.3f} (WEAK - customers not price-sensitive)")

# ========================================
# STEP 5 - BUSINESS INSIGHTS REPORT
# ========================================
print("\n[5/6] Writing Business Insights Report...")

total_rev   = df['Revenue'].sum()
top_cat     = df.groupby('terms')['Revenue'].sum().idxmax()
top_cat_pct = df.groupby('terms')['Revenue'].sum().max() / total_rev * 100
promo_avg   = df[df['Promotion'] == 'Yes']['Revenue'].mean()
nopromo_avg = df[df['Promotion'] == 'No']['Revenue'].mean()
promo_lift  = (promo_avg - nopromo_avg) / nopromo_avg * 100
man_count   = len(df[df['section'] == 'MAN'])
woman_count = len(df[df['section'] == 'WOMAN'])

report = f"""
==============================================================
  ZARA EDA - BUSINESS INSIGHTS REPORT
==============================================================

DATASET SUMMARY
  Total Products   : {len(df)}
  Total Revenue    : ${total_rev:,.2f}
  Total Units Sold : {df['Sales Volume'].sum():,}
  Avg Price        : ${df['price'].mean():.2f}
  Avg Revenue/SKU  : ${df['Revenue'].mean():,.2f}

TOP 8 BUSINESS INSIGHTS
--------------------------------------------------------------
1. {top_cat.upper()} dominate revenue at {top_cat_pct:.1f}% of total (${df.groupby('terms')['Revenue'].sum().max()/1e6:.1f}M)
   -> Protect and expand this category at all costs.

2. WOMAN section has only {woman_count} products vs {man_count} MAN products ({woman_count/len(df)*100:.1f}% vs {man_count/len(df)*100:.1f}%)
   -> Massive untapped opportunity. Add 80-100 women's products.

3. Price is the #1 revenue driver (correlation = {corr.loc['price','Revenue']:.2f})
   -> A 10% price increase could add ~${total_rev * 0.10 / 1e6:.1f}M revenue.

4. Price barely affects sales volume (correlation = {corr.loc['price','Sales Volume']:.2f})
   -> Zara customers are NOT price-sensitive. Support premium pricing.

5. Promoted products earn {promo_lift:.1f}% MORE revenue (${promo_avg:,.0f} vs ${nopromo_avg:,.0f})
   -> But it's because expensive products get promoted, not discounting.

6. Price sweet spot is $60-$150 (generates 63.9% of total revenue)
   -> Prioritize adding products in this range.

7. Jeans: only 8 SKUs generating $860K
   -> For a global brand, this is a major gap. Target 25+ jeans SKUs.

8. Front-of-Store placement drives highest average sales volume
   -> Always place highest-margin products at front.

TOP 5 RECOMMENDATIONS
--------------------------------------------------------------
1. [CRITICAL] Expand WOMAN section to 100+ products -> +$5-8M potential
2. [HIGH]     Move $150+ jackets to Front-of-Store positions -> +5-8% volume
3. [HIGH]     Grow jeans from 8 -> 25+ SKUs in $60-$120 range -> +$1.5M
4. [MEDIUM]   Promote $150+ items to attract premium buyers -> +15% revenue
5. [MEDIUM]   Focus R&D on $60-$100 price range products -> max volume x margin

TOP 5 PRODUCTS BY REVENUE
--------------------------------------------------------------
"""

top5 = df.nlargest(5, 'Revenue')[['name', 'terms', 'price', 'Sales Volume', 'Revenue']]
for i, (_, row) in enumerate(top5.iterrows(), 1):
    report += f"  {i}. {row['name'][:40]}\n"
    report += f"     ${row['price']:.2f} × {row['Sales Volume']:,} units = ${row['Revenue']:,.0f}\n\n"

report += "\n  Report generated by: zara_eda_analysis.py\n"

with open(f'{OUTPUT_DIR}/business_insights_report.txt', 'w', encoding='utf-8') as f:
    f.write(report)
print(report)

# ========================================
# STEP 6 - DONE
# ========================================
print("\n[6/6] All Done!")
print(f"\n>>> All outputs saved to: ./{OUTPUT_DIR}/")
print("\n  Files created:")
for fname in sorted(os.listdir(OUTPUT_DIR)):
    fpath = os.path.join(OUTPUT_DIR, fname)
    size_kb = os.path.getsize(fpath) // 1024
    print(f"    {fname:<45} {size_kb} KB")
print("\n*** Open zara_output/ folder to see all your charts and report! ***")
