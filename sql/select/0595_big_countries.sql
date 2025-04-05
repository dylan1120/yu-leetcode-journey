-- LeetCode 595: Big Countries
-- https://leetcode.com/problems/big-countries

-- Your SQL here
Select name, population, area
From World
Where population > 25000000 or area > 3000000;
