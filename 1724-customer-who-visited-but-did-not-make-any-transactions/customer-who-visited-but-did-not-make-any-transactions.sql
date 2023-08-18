# Write your MySQL query statement below
SELECT v.customer_id, 
  COUNT(v.visit_id) AS count_no_trans #count num of times e/ customer visited without transaction
FROM Visits v #primary table 
LEFT JOIN Transactions t ON t.visit_id = v.visit_id #combines all visits to transaction
WHERE t.transaction_id is NULL #filters out where only the visits without transactions.
GROUP BY v.customer_id; #breakdown of num of times each customer visited w/o making a transaction.

#without group by, it'd just be a single num
