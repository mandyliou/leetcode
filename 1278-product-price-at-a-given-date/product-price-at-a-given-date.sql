SELECT all_products.product_id,
       COALESCE(Products.new_price, 10) AS price
FROM (SELECT DISTINCT product_id FROM Products
      UNION SELECT DISTINCT product_id FROM Products WHERE change_date <= '2019-08-16') AS all_products
LEFT JOIN Products
ON all_products.product_id = Products.product_id
AND Products.change_date = (SELECT MAX(change_date)
                            FROM Products
                            WHERE Products.product_id = all_products.product_id
                            AND change_date <= '2019-08-16');
