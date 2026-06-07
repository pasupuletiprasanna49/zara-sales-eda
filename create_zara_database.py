# -*- coding: utf-8 -*-
# ============================================================
#  STEP 1: Run this script FIRST on your PC
#  It converts zara.csv into a proper SQLite database file
#  
#  Run: python create_zara_database.py
#  Output: zara_database.db  (upload this to sqliteonline.com)
# ============================================================

import sqlite3
import pandas as pd
import os

CSV_PATH = 'zara.csv'       # must be in same folder as this script
DB_PATH  = 'zara_database.db'

print("=" * 55)
print("  Creating Zara SQLite Database from CSV")
print("=" * 55)

# --- Load CSV ---
print("\n[1/4] Loading CSV...")
df = pd.read_csv(CSV_PATH, sep=';')
df.columns = df.columns.str.strip()
print(f"   Loaded {len(df)} rows, {len(df.columns)} columns")
print(f"   Columns found: {list(df.columns)}")

# --- Add Revenue column ---
print("\n[2/4] Adding Revenue column...")
df['Revenue'] = df['price'] * df['Sales Volume']
print(f"   Revenue added. Total = ${df['Revenue'].sum():,.2f}")

# --- Write to SQLite ---
print("\n[3/4] Creating SQLite database...")
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

conn = sqlite3.connect(DB_PATH)

# Write the main table
df.to_sql('zara_products', conn, index=False, if_exists='replace')

# Verify it worked
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM zara_products")
count = cursor.fetchone()[0]
cursor.execute("PRAGMA table_info(zara_products)")
columns = cursor.fetchall()

print(f"   Table 'zara_products' created with {count} rows")
print(f"   Columns in database:")
for col in columns:
    print(f"     - {col[1]} ({col[2]})")

conn.close()
print("\n[4/4] Done!")
print(f"\n   File created: {DB_PATH}")
print(f"   Size: {os.path.getsize(DB_PATH) / 1024:.1f} KB")
print("\n" + "=" * 55)
print("  NEXT STEP:")
print("  1. Go to sqliteonline.com")
print("  2. Click 'Open DB' (top left folder icon)")
print("  3. Upload 'zara_database.db'")
print("  4. You will see 'zara_products' table on the left")
print("  5. Run your SQL queries!")
print("=" * 55)
