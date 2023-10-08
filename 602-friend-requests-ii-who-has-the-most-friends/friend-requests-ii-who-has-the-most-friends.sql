# Write your MySQL query statement below
WITH Combined AS (
  SELECT requester_id AS id FROM RequestAccepted
  UNION ALL
  SELECT accepter_id AS id FROM RequestAccepted
),
FriendCounts AS (
  SELECT id, COUNT(*) AS num
  FROM Combined
  GROUP BY id
)
SELECT id, num
FROM FriendCounts
ORDER BY num DESC, id ASC
LIMIT 1;
