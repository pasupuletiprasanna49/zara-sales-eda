-- ============================================================
--  ZARA SQL QUERIES - FINAL VERSION
--  Table name: zara_products  (NOT zara1!)
--  
--  HOW TO USE:
--  1. Run create_zara_database.py on your PC first
--  2. Upload zara_database.db to sqliteonline.com
--  3. Copy ONE query block at a time and click Run
-- ============================================================


-- ============================================================
-- STEP 0: Always run this first to verify data loaded
-- ============================================================
SELECT * FROM zara_products LIMIT 5;


-- ============================================================
-- QUERY 1: Top 5 Products by Revenue
-- Business Question: Which products make the most money?
-- ============================================================
SELECT
    name,
    terms           AS category,
    section,
    price,
    "Sales Volume"  AS sales_volume,
    Revenue
FROM zara_products
ORDER BY Revenue DESC
LIMIT 5;


-- ============================================================
-- QUERY 2: Revenue by Product Category
-- Business Question: Which category drives the most revenue?
-- ============================================================
SELECT
    terms                           AS category,
    COUNT(*)                        AS product_count,
    ROUND(SUM(Revenue), 2)          AS total_revenue,
    ROUND(AVG(Revenue), 2)          AS avg_revenue,
    ROUND(AVG(price), 2)            AS avg_price,
    ROUND(AVG("Sales Volume"), 0)   AS avg_sales_volume
FROM zara_products
GROUP BY terms
ORDER BY total_revenue DESC;


-- ============================================================
-- QUERY 3: Promotion Impact Analysis
-- Business Question: Do promotions increase sales?
-- ============================================================
SELECT
    Promotion,
    COUNT(*)                        AS product_count,
    ROUND(AVG(price), 2)            AS avg_price,
    ROUND(AVG("Sales Volume"), 0)   AS avg_sales_volume,
    ROUND(AVG(Revenue), 2)          AS avg_revenue,
    ROUND(SUM(Revenue), 2)          AS total_revenue
FROM zara_products
GROUP BY Promotion;


-- ============================================================
-- QUERY 4: MAN vs WOMAN Section Comparison
-- Business Question: Which section performs better?
-- ============================================================
SELECT
    section,
    COUNT(*)                        AS product_count,
    ROUND(SUM(Revenue), 2)          AS total_revenue,
    ROUND(AVG(Revenue), 2)          AS avg_revenue_per_product,
    ROUND(AVG(price), 2)            AS avg_price,
    MIN(price)                      AS min_price,
    MAX(price)                      AS max_price
FROM zara_products
GROUP BY section
ORDER BY total_revenue DESC;


-- ============================================================
-- QUERY 5: Product Placement Performance
-- Business Question: Does shelf position affect sales?
-- ============================================================
SELECT
    "Product Position"              AS placement,
    COUNT(*)                        AS product_count,
    ROUND(AVG("Sales Volume"), 0)   AS avg_units_sold,
    ROUND(AVG(Revenue), 2)          AS avg_revenue,
    MIN("Sales Volume")             AS min_units,
    MAX("Sales Volume")             AS max_units
FROM zara_products
GROUP BY "Product Position"
ORDER BY avg_units_sold DESC;


-- ============================================================
-- QUERY 6: Price Tier Segmentation
-- Business Question: Which price range generates most revenue?
-- ============================================================
SELECT
    CASE
        WHEN price < 30                  THEN '1. Under $30'
        WHEN price BETWEEN 30 AND 59.99  THEN '2. $30 to $60'
        WHEN price BETWEEN 60 AND 99.99  THEN '3. $60 to $100'
        WHEN price BETWEEN 100 AND 149.99 THEN '4. $100 to $150'
        ELSE                                  '5. $150 and above'
    END                             AS price_tier,
    COUNT(*)                        AS product_count,
    ROUND(AVG("Sales Volume"), 0)   AS avg_units_sold,
    ROUND(SUM(Revenue), 2)          AS total_revenue,
    ROUND(AVG(Revenue), 2)          AS avg_revenue
FROM zara_products
GROUP BY price_tier
ORDER BY price_tier;


-- ============================================================
-- QUERY 7: Seasonal vs Non-Seasonal
-- Business Question: Does seasonality impact performance?
-- ============================================================
SELECT
    Seasonal,
    COUNT(*)                        AS product_count,
    ROUND(AVG(price), 2)            AS avg_price,
    ROUND(AVG("Sales Volume"), 0)   AS avg_units_sold,
    ROUND(AVG(Revenue), 2)          AS avg_revenue,
    ROUND(SUM(Revenue), 2)          AS total_revenue
FROM zara_products
GROUP BY Seasonal;


-- ============================================================
-- QUERY 8: Best of Both Worlds (High Price AND High Volume)
-- Business Question: Which products have best price AND volume?
-- ============================================================
SELECT
    name,
    terms           AS category,
    section,
    price,
    "Sales Volume"  AS sales_volume,
    Revenue
FROM zara_products
WHERE
    price > (SELECT AVG(price) FROM zara_products)
    AND
    "Sales Volume" > (SELECT AVG("Sales Volume") FROM zara_products)
ORDER BY Revenue DESC
LIMIT 10;


-- ============================================================
-- QUERY 9: Rank Products Within Each Category (Window Function)
-- Business Question: Who is #1 in each category?
-- ============================================================
SELECT
    name,
    terms           AS category,
    price,
    "Sales Volume"  AS sales_volume,
    Revenue,
    RANK() OVER (
        PARTITION BY terms
        ORDER BY Revenue DESC
    )               AS rank_in_category
FROM zara_products
ORDER BY terms, rank_in_category
LIMIT 25;


-- ============================================================
-- QUERY 10: Bottom 15 Low Performers
-- Business Question: Which products need attention?
-- ============================================================
SELECT
    name,
    terms           AS category,
    section,
    price,
    "Sales Volume"  AS sales_volume,
    Revenue,
    'REVIEW NEEDED' AS action_flag
FROM zara_products
ORDER BY Revenue ASC
LIMIT 15;


-- ============================================================
-- BONUS QUERY: Full Summary Dashboard in one query
-- ============================================================
SELECT
    COUNT(*)                        AS total_products,
    ROUND(SUM(Revenue), 2)          AS total_revenue,
    ROUND(AVG(Revenue), 2)          AS avg_revenue_per_product,
    ROUND(AVG(price), 2)            AS avg_price,
    MIN(price)                      AS min_price,
    MAX(price)                      AS max_price,
    SUM("Sales Volume")             AS total_units_sold,
    ROUND(AVG("Sales Volume"), 0)   AS avg_units_per_product,
    MAX(Revenue)                    AS highest_product_revenue
FROM zara_products;

-- ============================================================
-- END OF ALL QUERIES
-- ============================================================
