# Write your MySQL query statement below
SELECT name
FROM Customer
#need to select customers not referred by anyone & not by id = 2
WHERE referee_id != 2 OR referee_id IS NULL;