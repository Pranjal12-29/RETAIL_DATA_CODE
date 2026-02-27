--Top Selling Products
SELECT p.product_name, SUM(f.quantity) AS total_quantity
FROM fact_sales f
JOIN dim_products p ON f.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_quantity DESC;

-- Revenue by Category
SELECT p.category, SUM(f.sales_amount) AS total_revenue
FROM fact_sales f
JOIN dim_products p ON f.product_id = p.product_id
GROUP BY p.category;

-- Low Stock Products
SELECT p.product_name, i.stock_qty
FROM dim_inventory i
JOIN dim_products p ON i.product_id = p.product_id
WHERE i.stock_qty < 10;
