# leetcode 75: 643. Maximum Average Subarray I
# You are given an integer array nums consisting of n elements, and an integer k.
#
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        current_sum = sum(nums[:k])
        max_sum = current_sum
        for i in range(k,n):
            current_sum += nums[i] - nums[i-k]
            if  current_sum > max_sum:
                max_sum = current_sum
        return max_sum/k


if __name__ == '__main__':
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    solution = Solution()
    solution.isSubsequence(nums, k)