# LeetCode 238: Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

        The problem can be solved in O(n) time and O(1) space complexity (excluding the output array).
        """
        n = len(nums)
        answer = [1] * n

        # Calculate prefix products
        prefix_product = 1
        for i in range(n):
            answer[i] = prefix_product
            prefix_product *= nums[i]

        # Calculate suffix products and multiply with prefix products
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix_product
            suffix_product *= nums[i]

        return answer
