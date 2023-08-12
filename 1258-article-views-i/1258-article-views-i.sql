# Write your MySQL query statement below

SELECT DISTINCT author_id AS id #distinct will get only unique author_id in output
FROM Views
WHERE author_id = viewer_id #must compare author_id and viewer_id from Views table; if they're the same, they viewed own article
ORDER BY author_id; #sorts result by author_id in ascending order
