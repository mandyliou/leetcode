# Write your MySQL query statement below

SELECT p.product_name, s.year, s.price
FROM Sales AS s
JOIN Product AS p ON s.product_id = p.product_id 
#want to join Product and Sales table; uses inner join
#ON will match product_id in Sales to product_id in Product
