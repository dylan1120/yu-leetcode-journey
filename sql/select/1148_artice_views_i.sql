-- LeetCode 1148: Artice Views I
-- https://leetcode.com/problems/artice-views-i

-- Your SQL here
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id;
