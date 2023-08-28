# Write your MySQL query statement below
WITH FirstOrders AS (
    SELECT customer_id, MIN(order_date) AS first_order_date
    FROM Delivery
    GROUP BY customer_id
),

ImmediateFirstOrders AS (
    SELECT d.customer_id
    FROM Delivery d
    JOIN FirstOrders fo ON d.customer_id = fo.customer_id AND d.order_date = fo.first_order_date
    WHERE d.order_date = d.customer_pref_delivery_date
)

SELECT ROUND(100 * COUNT(DISTINCT customer_id) / (SELECT COUNT(DISTINCT customer_id) FROM FirstOrders), 2) AS immediate_percentage
FROM ImmediateFirstOrders;
