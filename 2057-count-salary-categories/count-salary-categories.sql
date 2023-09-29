# Write your MySQL query statement below
-- Count accounts in each category
WITH SalaryCategories AS (
    SELECT CASE
               WHEN income < 20000 THEN 'Low Salary'
               WHEN income BETWEEN 20000 AND 50000 THEN 'Average Salary'
               ELSE 'High Salary'
           END AS category
    FROM Accounts
)
SELECT category,
       COUNT(*) AS accounts_count
FROM SalaryCategories
GROUP BY category

-- Ensure all categories are represented
UNION ALL

SELECT 'Low Salary', 0 WHERE NOT EXISTS (SELECT 1 FROM SalaryCategories WHERE category = 'Low Salary')
UNION ALL
SELECT 'Average Salary', 0 WHERE NOT EXISTS (SELECT 1 FROM SalaryCategories WHERE category = 'Average Salary')
UNION ALL
SELECT 'High Salary', 0 WHERE NOT EXISTS (SELECT 1 FROM SalaryCategories WHERE category = 'High Salary');
