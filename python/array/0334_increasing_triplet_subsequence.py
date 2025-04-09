# LeetCode 334: Increasing Triplet Subsequence
# https://leetcode.com/problems/increasing-triplet-subsequence

class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        """
        Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].
        If no such indices exist, return false.
        """
        first = second = float('inf')
        
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        
        return False