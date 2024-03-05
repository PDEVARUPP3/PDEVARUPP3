-- Query to calculate total sales revenue by product category

-- Create a temporary table to store order details with product category information
CREATE TEMPORARY TABLE TempOrderDetails AS
SELECT
    o.order_id,
    p.product_category,
    oi.quantity,
    oi.unit_price
FROM
    orders o
JOIN
    order_items oi ON o.order_id = oi.order_id
JOIN
    products p ON oi.product_id = p.product_id;

-- Query to calculate total sales revenue by product category
SELECT
    product_category,
    SUM(quantity * unit_price) AS total_revenue
FROM
    TempOrderDetails
GROUP BY
    product_category
ORDER BY
    total_revenue DESC;
