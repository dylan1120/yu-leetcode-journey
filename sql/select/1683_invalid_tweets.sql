-- LeetCode 1683: Invalid Tweets
-- https://leetcode.com/problems/invalid-tweets

-- Your SQL here
Select
    tweet_id
From
    Tweets
Where
    Length(content) > 15
    and content not like '%[^a-zA-Z0-9 ]%'